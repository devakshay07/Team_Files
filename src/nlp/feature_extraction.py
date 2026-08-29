import json
import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.data.contracts import StandardizedReportObject, NLPFeatureObject

class NLPFeatureExtractor:
    def __init__(self, vocab_path: str = None):
        if vocab_path is None:
            vocab_path = os.path.join(os.path.dirname(__file__), "language_variations.json")
        with open(vocab_path, 'r') as f:
            data = json.load(f)
            self.concepts = data.get("concepts", [])
            
        # Define phrases that explicitly imply safety/control success rather than failure
        self.safe_contexts = [
            r"safely",
            r"correctly applied",
            r"passed",
            r"successful",
            r"properly used",
            r"did not fail"
        ]
        
    def _is_negated(self, text: str, match_start: int) -> bool:
        """Check if a matched hazard is actually in a safe/negated context."""
        # Look at the 50 characters before the match for safety keywords
        context = text[max(0, match_start - 50):match_start]
        for safe_word in self.safe_contexts:
            if re.search(safe_word, context):
                return True
        return False
        
    def extract_features(self, report: StandardizedReportObject) -> NLPFeatureObject:
        text = report.cleaned_text.lower()
        
        extracted_entities = {}
        hazard_features = []
        
        # We rewrite the text to help TF-IDF understand safe contexts
        modified_text = text
        
        for safe_word in self.safe_contexts:
            modified_text = re.sub(safe_word, f"SAFE_CONTEXT", modified_text)
        
        for concept in self.concepts:
            concept_name = concept["concept"]
            variations = concept.get("variations", [])
            
            matched_variations = []
            for var in variations:
                for match in re.finditer(r'\b' + re.escape(var.lower()) + r'\b', text):
                    if not self._is_negated(text, match.start()):
                        matched_variations.append(var)
                    else:
                        # It was negated, so replace it in the modified text so TF-IDF doesn't trigger on it
                        modified_text = modified_text.replace(var, f"NEGATED_{var.replace(' ', '_')}")
                        
            if matched_variations:
                # Deduplicate
                matched_variations = list(set(matched_variations))
                extracted_entities[concept_name] = matched_variations
                hazard_features.append(concept_name)
                
        return NLPFeatureObject(
            extracted_entities=extracted_entities,
            hazard_features=list(set(hazard_features)),
            exposure_features=["Worker"] if "worker" in text else [],
            feature_metadata={
                "cleaned_text": modified_text, # Give TF-IDF the negated-aware text!
                "original_text": report.cleaned_text,
                "report_id": report.report_id
            }
        )

if __name__ == "__main__":
    extractor = NLPFeatureExtractor()
    dummy_report = StandardizedReportObject(
        report_id="123",
        report_type="Unsafe Act",
        raw_text="Worker safely descended using full fall protection. LOTO was correctly applied.",
        cleaned_text="worker safely descended using full fall protection. loto was correctly applied."
    )
    features = extractor.extract_features(dummy_report)
    print("Features extracted:", features.model_dump_json(indent=2))
