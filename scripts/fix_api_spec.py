import json

with open('api/frontend_api_spec.json', 'r') as f:
    spec = json.load(f)

props = spec['components']['schemas']['ModelPrediction']['properties']
props['immediate_action'] = {"type": "string", "nullable": True}
props['intervention'] = {"type": "string", "nullable": True}
props['corrective_action'] = {"type": "string", "nullable": True}
props['preventive_action'] = {"type": "string", "nullable": True}
props['work_stopped'] = {"type": "boolean", "nullable": True}

with open('api/frontend_api_spec.json', 'w') as f:
    json.dump(spec, f, indent=2)
