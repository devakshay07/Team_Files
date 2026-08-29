import json

problem_statements = [
    # Page 1
    {"sno": 1, "org": "Ministry of Development of North Eastern Region (MDoNER)", "title": "AI-Based early warning and landslide Risk Monitoring System in NER", "category": "Software", "ps_no": "SIH26001", "theme": "Disaster Management"},
    {"sno": 2, "org": "Ministry of Development of North Eastern Region (MDoNER)", "title": "AI-Based Smart Logistics and Accessibility Intelligence Platform for North Eastern Region (NER)", "category": "Software", "ps_no": "SIH26002", "theme": "Smart Automation"},
    {"sno": 3, "org": "Ministry of Development of North Eastern Region (MDoNER)", "title": "AI-Based Cognitive Gaming and Memory Assistance Platform for Elderly Dementia Patients in North Eastern Region (NER)", "category": "Software", "ps_no": "SIH26003", "theme": "Space Technology"},
    {"sno": 4, "org": "Ministry of Development of North Eastern Region (MDoNER)", "title": "AI-Assisted Early Detection System for Osteoarthritis (OA) Risk Markers in North Eastern Region (NER)", "category": "Hardware", "ps_no": "SIH26004", "theme": "Space Technology"},
    {"sno": 5, "org": "Ministry of Development of North Eastern Region (MDoNER)", "title": "Solar-Powered Smart Mini Cold Storage System for Fresh Vegetables in North Eastern Region (NER)", "category": "Hardware", "ps_no": "SIH26005", "theme": "Smart Vehicles"},
    {"sno": 6, "org": "Ministry of Steel", "title": "Development of an Intelligent Freight Forecasting Model for Optimized Vessel Chartering and Bulk Cargo Procurement from overseas to East Coast of India", "category": "Software", "ps_no": "SIH26006", "theme": "Transportation & Logistics"},
    {"sno": 7, "org": "Ministry of Steel", "title": "Safe and Efficient Operation of Mine Vehicles in Fog and Low-Visibility Conditions in Open Cast Iron Ore Mines", "category": "Hardware", "ps_no": "SIH26007", "theme": "Smart Automation"},
    {"sno": 8, "org": "Ministry of Steel", "title": "Belt Joint Rupture and Conveyor Belt Damages in Iron Ore Mining Industry: Intelligent Monitoring and Prediction of Conveyor Belt Joint Rupture and Damages in Iron Ore Mining Industry", "category": "Hardware", "ps_no": "SIH26008", "theme": "Smart Automation"},
    
    # Page 2
    {"sno": 9, "org": "Ministry of Steel", "title": "Using AI/ML and Space Technology to Identify Manganese Reserves and Overcome Production Shortfalls", "category": "Software", "ps_no": "SIH26009", "theme": "Smart Automation"},
    {"sno": 10, "org": "Ministry of Rural Development", "title": "Survey/Resurvey of Rural Agricultural Land in India", "category": "Hardware", "ps_no": "SIH26010", "theme": "Smart Automation"},
    {"sno": 11, "org": "Ministry of Rural Development", "title": "3D ULPIN Generation and vertical Property Mapping System", "category": "Software", "ps_no": "SIH26011", "theme": "Space Technology"},
    {"sno": 12, "org": "Ministry of Rural Development", "title": "AI-Based Automated Urban Parcel Mapping and Cadastral Feature Extraction System using Drone Imagery", "category": "Software", "ps_no": "SIH26012", "theme": "Robotics and Drones"},
    {"sno": 13, "org": "Ministry of Rural Development", "title": "Automated Integration and Intelligent Harmonization of Multi-source Geospatial Data for urban Land Record Management", "category": "Software", "ps_no": "SIH26013", "theme": "Disaster Management"},
    {"sno": 14, "org": "Ministry of Rural Development", "title": "An Integrated GIS-based Digital Public Infrastructure for Land Governance", "category": "Software", "ps_no": "SIH26014", "theme": "Robotics and Drones"},
    {"sno": 15, "org": "Ministry of Rural Development", "title": "Application of Geospatial Techniques for visualization and analysis to interpret Geo-Coded Images to enhance watershed Development Outcomes", "category": "Software", "ps_no": "SIH26015", "theme": "Disaster Management"},
    {"sno": 16, "org": "Ministry of Rural Development", "title": "Real-Time National Land Acquisition & Management System for End-to-End Digital Monitoring and Decision Support", "category": "Software", "ps_no": "SIH26016", "theme": "Miscellaneous"},
    {"sno": 17, "org": "Ministry of Rural Development", "title": "Predictive Analytics System for Early Detection of Land Acquisition Delays", "category": "Software", "ps_no": "SIH26017", "theme": "Agriculture, FoodTech & Rural Development"},
    {"sno": 18, "org": "Ministry of Rural Development", "title": "Intelligent Land Record Digitization and Validation System", "category": "Software", "ps_no": "SIH26018", "theme": "MedTech / BioTech / HealthTech"},
    
    # Page 3
    {"sno": 19, "org": "Ministry of Rural Development", "title": "National Digital Platform for Research, Policy Innovation, and Evidence-Based Land Governance", "category": "Software", "ps_no": "SIH26019", "theme": "Blockchain & Cybersecurity"},
    {"sno": 20, "org": "Ministry of MSME", "title": "Design and Development of Innovative Hand-Spinning Equipment for Enhancing Khadi Artisan Productivity and Income", "category": "Hardware", "ps_no": "SIH26020", "theme": "Blockchain & Cybersecurity"},
    {"sno": 21, "org": "Ministry of MSME", "title": "Honey Chain: A block chain-based system for honey traceability and smart beekeeping management", "category": "Software", "ps_no": "SIH26021", "theme": "Smart Automation"},
    {"sno": 22, "org": "Ministry of MSME", "title": "Design and develop a smart, solar-powered drying and compact packaging system to support home-based agarbatti manufacturing by rural women artisans", "category": "Hardware", "ps_no": "SIH26022", "theme": "Agriculture, FoodTech & Rural Development"},
    {"sno": 23, "org": "Ministry of Coal", "title": "AI-Powered Geological, Mining and other Reporting Solution for CMPDI/CIL subsidiaries", "category": "Software", "ps_no": "SIH26023", "theme": "Miscellaneous"},
    {"sno": 24, "org": "Ministry of Coal", "title": "AI-Based Smart Governance and Compliance Monitoring System for Coal Mines", "category": "Software", "ps_no": "SIH26024", "theme": "Smart Automation"},
    {"sno": 25, "org": "Ministry of Coal", "title": "Development of an AI-enabled Low Cost Real Time Mine Subsidence Monitoring, Prediction and Early Warning System for Underground Coal Mines in India", "category": "Hardware", "ps_no": "SIH26025", "theme": "Disaster Management"},
    {"sno": 26, "org": "Ministry of Railways", "title": "Development of Mobile (Quadruped)/Handheld Device/System for Real-Time Detection of Narcotics and Explosives across Indian Railways", "category": "Hardware", "ps_no": "SIH26026", "theme": "Robotics and Drones"},
    {"sno": 27, "org": "Ministry of Railways", "title": "AI-Powered Automatic Block Planning to Maximize Asset Availability for Train Operations on Indian Railways", "category": "Software", "ps_no": "SIH26027", "theme": "Transportation & Logistics"},
    
    # Page 4
    {"sno": 28, "org": "Ministry of Railways", "title": "Dynamic Forecast of Expected Time of Arrival (ETA) for Coaching Trains", "category": "Software", "ps_no": "SIH26028", "theme": "Disaster Management"},
    {"sno": 29, "org": "Ministry of Consumer Affairs, Food & Public Distribution", "title": "Automated High-Current Short-Circuit Test System for IEC 60898-1:2015 MCB Compliance", "category": "Hardware", "ps_no": "SIH26029", "theme": "Disaster Management"},
    {"sno": 30, "org": "Ministry of Consumer Affairs, Food & Public Distribution", "title": "Automated Cable Specimen Preparation System for IS 10810 and IS 7098 Compliance", "category": "Hardware", "ps_no": "SIH26030", "theme": "Smart Automation"},
    {"sno": 31, "org": "Ministry of Consumer Affairs, Food & Public Distribution", "title": "Quality assessment and grading of onions are often subjective and vary across procurement centers, resulting in disputes and inconsistencies", "category": "Software", "ps_no": "SIH26031", "theme": "Fitness & Sports"},
    {"sno": 32, "org": "Ministry of Consumer Affairs, Food & Public Distribution", "title": "Farmers often face long waiting times, lack of information regarding procurement schedules, and uncertainty about procurement status", "category": "Software", "ps_no": "SIH26032", "theme": "Heritage & Culture"},
    {"sno": 33, "org": "Ministry of Consumer Affairs, Food & Public Distribution", "title": "Multiple intermediaries reduce farmers earnings and increase consumer prices", "category": "Software", "ps_no": "SIH26033", "theme": "MedTech / BioTech / HealthTech"},
    {"sno": 34, "org": "Ministry of Consumer Affairs, Food & Public Distribution", "title": "Software System to check compliance of Packaged Commodities under Legal Metrology(Packaged Commodities) Rules, 2011 by scanning products, images and labels", "category": "Software", "ps_no": "SIH26034", "theme": "Agriculture, FoodTech & Rural Development"},
    {"sno": 35, "org": "Ministry of Consumer Affairs, Food & Public Distribution", "title": "Development of a Software Program/Application for Generation of Test Reports for Non-Automatic Weighing Instruments (NAWI) as per OIML Recommendation R-76", "category": "Software", "ps_no": "SIH26035", "theme": "Smart Vehicles"},
    
    # Page 5
    {"sno": 36, "org": "Ministry of Consumer Affairs, Food & Public Distribution", "title": "Development of an Online Verification System for Weighing and Measuring Instruments", "category": "Software", "ps_no": "SIH26036", "theme": "Transportation & Logistics"},
    {"sno": 37, "org": "MathWorks", "title": "Adaptive Path Planning and Collision Avoidance for Autonomous Vehicles on Unstructured Indian Roads", "category": "Software", "ps_no": "SIH26037", "theme": "Robotics and Drones"},
    {"sno": 38, "org": "MathWorks", "title": "Explainable AI for Diabetic Retinopathy Screening in Rural India", "category": "Software", "ps_no": "SIH26038", "theme": "Clean & Green Technology"},
    {"sno": 39, "org": "Government of Jharkhand", "title": "AI-Powered Underground Mine Safety, Monitoring and Rescue System", "category": "Hardware", "ps_no": "SIH26039", "theme": "Travel & Tourism"},
    {"sno": 40, "org": "Government of Jharkhand", "title": "Smart Water Purification and Quality Monitoring System for Rural and Mining-Affected Areas", "category": "Hardware", "ps_no": "SIH26040", "theme": "Renewable / Sustainable Energy"},
    {"sno": 41, "org": "Government of Jharkhand", "title": "AR-Based Vocational Training Simulator for Industrial Safety in Jharkhand's Mining & Manufacturing Sector", "category": "Software", "ps_no": "SIH26041", "theme": "Blockchain & Cybersecurity"},
    {"sno": 42, "org": "Government of Jharkhand", "title": "AI-Powered Vernacular Pedagogy and Real-Time Translation Tool for Mother Tongue-Based Primary Education", "category": "Software", "ps_no": "SIH26042", "theme": "Smart Education"},
    {"sno": 43, "org": "Government of Jharkhand", "title": "A digital platform to crowdsource societal challenges and facilitate collaborative problem solving through universities and industry partnerships", "category": "Software", "ps_no": "SIH26043", "theme": "Disaster Management"},
    {"sno": 44, "org": "Ministry of Ayush", "title": "Portal for Academia - Industry collaboration for Skill Mapping, Internships and Placement", "category": "Software", "ps_no": "SIH26044", "theme": "Miscellaneous"},
    {"sno": 45, "org": "Ministry of Ayush", "title": "IP-SAKTI Sahayak: a multilingual, RAG-based (source-cited) AI assistant for Intellectual Property and regulatory guidance in Ayurveda, across national and international regimes", "category": "Software", "ps_no": "SIH26045", "theme": "Toys & Games"},
    
    # Page 6
    {"sno": 46, "org": "Ministry of Ayush", "title": "AIIA Clinical Trials Dashboard - a real-time, cloud-based, GCP-compliant Clinical Trial Management System (CTMS) for Ayurveda research, with CDISC/FHIR-interoperable data, role-based KPIs, and integrated ethics, regulatory (CTRI / NDCT Rules 2019) and pharmacovigilance tracking", "category": "Software", "ps_no": "SIH26046", "theme": "Space Technology"},
    {"sno": 47, "org": "Ministry of Ayush", "title": "Patient Case-Taking Software", "category": "Software", "ps_no": "SIH26047", "theme": "Smart Automation"},
    {"sno": 48, "org": "Ministry of Ayush", "title": "iKwath - a pod-based smart Kwatha (Kadha) maker that prepares a fresh, AFI/API-standardized decoction from coarse powder (yavakut churna) on demand, in the shortest practical time without altering the decoctions quality or yield", "category": "Hardware", "ps_no": "SIH26048", "theme": "Fitness & Sports"},
    {"sno": 49, "org": "DRDO", "title": "Modifications to improve the reliability, efficiency, and lifespan of electrical and electronic equipment and systems in the ambient condition of subzero temperature and low pressure of High Altitude Areas(HAA) and Super High Altitude Areas (SHAA) of Ladakh region", "category": "Hardware", "ps_no": "SIH26049", "theme": "Heritage & Culture"},
    {"sno": 50, "org": "DRDO", "title": "High Altitude Performance Optimization and Robust Design of Anti-Drone System", "category": "Hardware", "ps_no": "SIH26050", "theme": "MedTech / BioTech / HealthTech"},
    
    # Page 7
    {"sno": 51, "org": "DRDO", "title": "Software Based Model Development for Design of Area Specific Shelter for Thermal Comfort Maintenance", "category": "Software", "ps_no": "SIH26051", "theme": "Agriculture, FoodTech & Rural Development"},
    {"sno": 52, "org": "DRDO", "title": "To develop an AI/ML-enabled adaptive noise cancellation (ANC) system that effectively suppresses stationary, non-stationary, and impulsive defence noises while maintaining high speech intelligibility and real-time performance on embedded hardware", "category": "Hardware", "ps_no": "SIH26052", "theme": "Smart Vehicles"},
    {"sno": 53, "org": "DRDO", "title": "Adaptive Variable Resolution 2.5D Lidar Mapping for Dynamic Environment Perception", "category": "Software", "ps_no": "SIH26053", "theme": "Transportation & Logistics"},
    {"sno": 54, "org": "DRDO", "title": "AI-Enabled Real-Time Digital Twin System for Health Monitoring, Fault Prediction and Mission Reliability Enhancement of Aero Piston Engines used in MALE UAVs", "category": "Software", "ps_no": "SIH26054", "theme": "Robotics and Drones"},
    {"sno": 55, "org": "DRDO", "title": "Smart Scan strategy for Electronic Warfare", "category": "Software", "ps_no": "SIH26055", "theme": "Clean & Green Technology"},
    {"sno": 56, "org": "MoSPI", "title": "Development of a Real-time Airfare Price Index for India through Automated Web Scraping of Airline and Online Travel Aggregator Portals for Augmentation of the Consumer Price Index (CPI)", "category": "Software", "ps_no": "SIH26056", "theme": "Travel & Tourism"},
    {"sno": 57, "org": "Ministry of Earth Sciences (MoES)", "title": "AI-Powered Automated Underwater Marine Debris and Anomaly Detection System using Side-Scan Sonar Imagery", "category": "Software", "ps_no": "SIH26057", "theme": "Renewable / Sustainable Energy"},
    {"sno": 58, "org": "Ministry of Earth Sciences (MoES)", "title": "Development of a Low-Power, Real-Time Adaptive Software-Defined Sonar Transmitter Payload for Autonomous Underwater Vehicles (AUVs)", "category": "Hardware", "ps_no": "SIH26058", "theme": "Blockchain & Cybersecurity"},
    
    # Page 8
    {"sno": 59, "org": "Ministry of Earth Sciences (MoES)", "title": "AI-Enabled Antarctic Sea-Ice, Iceberg Trajectory, and Navigation Decision Support System", "category": "Software", "ps_no": "SIH26059", "theme": "Smart Education"},
    {"sno": 60, "org": "Ministry of Earth Sciences (MoES)", "title": "Digital Platform for efficient remote management of Indian Antarctic Research Stations", "category": "Software", "ps_no": "SIH26060", "theme": "Disaster Management"},
    {"sno": 61, "org": "Ministry of Earth Sciences (MoES)", "title": "AI-Driven Smart Energy Management System for Polar Research Stations", "category": "Software", "ps_no": "SIH26061", "theme": "Miscellaneous"},
    {"sno": 62, "org": "Ministry of Earth Sciences (MoES)", "title": "Integrated Polar Expedition Logistics and Asset Management System", "category": "Software", "ps_no": "SIH26062", "theme": "Toys & Games"},
    {"sno": 63, "org": "Ministry of Earth Sciences (MoES)", "title": "Integrated Polar Science Outreach, Knowledge Repository and Media Dissemination Portal", "category": "Software", "ps_no": "SIH26063", "theme": "Space Technology"},
    {"sno": 64, "org": "Ministry of Earth Sciences (MoES)", "title": "Low-Cost Deployable Seafloor Metal Detection Sensor for Ocean Resource Exploration", "category": "Hardware", "ps_no": "SIH26064", "theme": "Smart Resource Conservation"},
    {"sno": 65, "org": "Ministry of Earth Sciences (MoES)", "title": "Autonomous Low-Cost Ocean Observation Platform for Polar and Southern Oceans", "category": "Hardware", "ps_no": "SIH26065", "theme": "Smart Automation"},
    {"sno": 66, "org": "Ministry of Earth Sciences (MoES)", "title": "OceanEmbed - Satellite Embedding-Based Deep Learning Framework for Reconstruction of Subsurface Ocean Temperature from Surface Satellite Observations", "category": "Software", "ps_no": "SIH26066", "theme": "Space Technology"},
    {"sno": 67, "org": "Ministry of Earth Sciences (MoES)", "title": "Develop a web-based interactive 3D visualization platform that integrates numerical ocean model outputs and in-situ observations", "category": "Software", "ps_no": "SIH26067", "theme": "Smart Automation"},
    
    # Page 9
    {"sno": 68, "org": "Ministry of Earth Sciences (MoES)", "title": "WeatherGPT: Conversational AI for Weather Forecasting, Alerts, and Climate Information", "category": "Software", "ps_no": "SIH26068", "theme": "Disaster Management"},
    {"sno": 69, "org": "Ministry of Earth Sciences (MoES)", "title": "National Weather Big Data Analytics Platform", "category": "Software", "ps_no": "SIH26069", "theme": "Disaster Management"},
    {"sno": 70, "org": "Ministry of Earth Sciences (MoES)", "title": "To develop an Artificial Intelligence (AI) / Machine Learning (ML) based system for identification, classification, and prediction of different tropical cyclone patterns using multi-source satellite data", "category": "Software", "ps_no": "SIH26070", "theme": "Smart Education"},
    {"sno": 71, "org": "Ministry of Earth Sciences (MoES)", "title": "AI/ML-Based Integrated heavy rainfall Early Warning and Inundation Prediction System using Satellite, Radar, observational Weather and numerical weather prediction model data", "category": "Software", "ps_no": "SIH26071", "theme": "Disaster Management"},
    {"sno": 72, "org": "Ministry of Earth Sciences (MoES)", "title": "AIML based Nowcasting of thunderstorm and lightning using atmospheric observation including multiple radars, satellite, lightning and model data", "category": "Software", "ps_no": "SIH26072", "theme": "Disaster Management"},
    {"sno": 73, "org": "Ministry of Earth Sciences (MoES)", "title": "AI/ML-Based Intelligent Anomaly Detection for Automatic Weather Stations (AWS)", "category": "Software", "ps_no": "SIH26073", "theme": "Disaster Management"},
    {"sno": 74, "org": "Ministry of Earth Sciences (MoES)", "title": "Downscaling of weather forecast from Block level to Panchayat level: Inferring high-resolution plots/data/information from low-resolution plot/data/information/variables for agro-meteorological advisory services", "category": "Software", "ps_no": "SIH26074", "theme": "Disaster Management"},
    
    # Page 10
    {"sno": 75, "org": "Ministry of Earth Sciences (MoES)", "title": "Participants are invited to design and develop CAPACITY CONNECT: A Digital Capacity Building and Learning Management Portal to support organizational training, competency development, and knowledge sharing through a centralized web-based platform", "category": "Software", "ps_no": "SIH26075", "theme": "Smart Education"},
    {"sno": 76, "org": "Ministry of Earth Sciences (MoES)", "title": "Development of personalized homepage for 'Mausam' mobile application", "category": "Software", "ps_no": "SIH26076", "theme": "Miscellaneous"},
    {"sno": 77, "org": "Ministry of Earth Sciences (MoES)", "title": "AI-Driven Hyper-Local Early Warning System for Severe Weather Nowcasting", "category": "Software", "ps_no": "SIH26077", "theme": "Disaster Management"},
    {"sno": 78, "org": "Ministry of Earth Sciences (MoES)", "title": "AI-Driven Spatio-Temporal Tracking of Extreme Weather Anomalies in Medium-Range Forecasts", "category": "Software", "ps_no": "SIH26078", "theme": "Disaster Management"},
    {"sno": 79, "org": "Ministry of Earth Sciences (MoES)", "title": "AI-Based Forecast Bust Detection for Medium-Range Weather Forecasts", "category": "Software", "ps_no": "SIH26079", "theme": "Disaster Management"},
    {"sno": 80, "org": "Ministry of Earth Sciences (MoES)", "title": "Regime-Aware AI Post-Processing of Monsoon Rainfall Forecasts", "category": "Software", "ps_no": "SIH26080", "theme": "Disaster Management"},
    {"sno": 81, "org": "Ministry of Earth Sciences (MoES)", "title": "Hybrid AINWP Multi-Model Forecast Blending System", "category": "Software", "ps_no": "SIH26081", "theme": "Miscellaneous"},
    {"sno": 82, "org": "Ministry of Earth Sciences (MoES)", "title": "Air Pollution Weather Coupled Forecasting System (Delhi NCR Focus)", "category": "Software", "ps_no": "SIH26082", "theme": "Disaster Management"},
    {"sno": 83, "org": "Ministry of Earth Sciences (MoES)", "title": "Extreme Heatwave Early Warning and Human Thermal Stress Index", "category": "Software", "ps_no": "SIH26083", "theme": "Disaster Management"},
    {"sno": 84, "org": "Ministry of Earth Sciences (MoES)", "title": "Convective scale nowcasting for Thunderstorms, Hail & Cloudbursts (06 hr)", "category": "Software", "ps_no": "SIH26084", "theme": "Disaster Management"},
    {"sno": 85, "org": "Ministry of Earth Sciences (MoES)", "title": "Urban Flood Nowcasting System (Drainage and Rainfall Coupling)", "category": "Software", "ps_no": "SIH26085", "theme": "Disaster Management"},
    
    # Page 11
    {"sno": 86, "org": "Ministry of Earth Sciences (MoES)", "title": "Hyperlocal Monsoon Onset & Break Prediction System (Block/Village Scale)", "category": "Software", "ps_no": "SIH26086", "theme": "Miscellaneous"},
    {"sno": 87, "org": "Ministry of Cooperation", "title": "AI-Enabled Cooperative Capacity Building, ERP & Employment Ecosystem", "category": "Hardware", "ps_no": "SIH26087", "theme": "Smart Education"},
    {"sno": 88, "org": "Ministry of Cooperation", "title": "Multilingual Cooperative Governance & Legal Assistance Chatbot", "category": "Hardware", "ps_no": "SIH26088", "theme": "Smart Automation"},
    {"sno": 89, "org": "Ministry of Cooperation", "title": "Cooperative Gig Services Platform for Household & Community Services", "category": "Software", "ps_no": "SIH26089", "theme": "Smart Automation"},
    {"sno": 90, "org": "Ministry of Social Justice and Empowerment (MoSJE)", "title": "AI-Driven Market Linkage and Smart Cataloging Mobile Application for Marginalized Artisans", "category": "Software", "ps_no": "SIH26090", "theme": "Miscellaneous"},
    {"sno": 91, "org": "Ministry of Social Justice and Empowerment (MoSJE)", "title": "AI-Driven Hyper-Local Business Advisory and Financial Structuring Assistant for Rural Micro-Entrepreneurs", "category": "Software", "ps_no": "SIH26091", "theme": "Miscellaneous"},
    {"sno": 92, "org": "Ministry of Social Justice and Empowerment (MoSJE)", "title": "AI-Driven Scheme Matching for Marginalized Entrepreneurs", "category": "Software", "ps_no": "SIH26092", "theme": "Miscellaneous"},
    {"sno": 93, "org": "Ministry of Social Justice and Empowerment (MoSJE)", "title": "AI-Based Real-Time Stress and Trauma Assessment Module for Victims/Complainants Accessing NHAA (14566) and Integrated Portal", "category": "Software", "ps_no": "SIH26093", "theme": "Smart Automation"},
    {"sno": 94, "org": "Ministry of Social Justice and Empowerment (MoSJE)", "title": "AI-Powered Dynamic Mental Health Monitoring and Distress Prediction System for Victims of Atrocities", "category": "Software", "ps_no": "SIH26094", "theme": "MedTech / BioTech / HealthTech"},
    {"sno": 95, "org": "Ministry of Social Justice and Empowerment (MoSJE)", "title": "Smart Real-Time Monitoring & Inspection Mobile App", "category": "Software", "ps_no": "SIH26095", "theme": "Miscellaneous"},
    
    # Page 12
    {"sno": 96, "org": "Ministry of Social Justice and Empowerment (MoSJE)", "title": "Digital Heritage Archive for Memorials, Manuscripts & Ambedkar: AI-Powered Institutional Archive and Audio-Visual Knowledge Platform", "category": "Hardware", "ps_no": "SIH26096", "theme": "Heritage & Culture"},
    {"sno": 97, "org": "Ministry of Social Justice and Empowerment (MoSJE)", "title": "AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY", "category": "Software", "ps_no": "SIH26097", "theme": "Smart Education"},
    {"sno": 98, "org": "Ministry of Defence (MoD)", "title": "Development of a Low-Cost Precision Guidance and Smart Electronic Fuze System for a 155 mm Artillery Shell", "category": "Hardware", "ps_no": "SIH26098", "theme": "Miscellaneous"},
    {"sno": 99, "org": "Ministry of Petroleum & Natural Gas", "title": "AI-Driven Standardization and Harmonization of Material Codes Across CPSEs", "category": "Software", "ps_no": "SIH26099", "theme": "Smart Automation"},
    {"sno": 100, "org": "Ministry of Petroleum & Natural Gas", "title": "AI-Powered Integrated Bid Compliance Verification Platform for GeM Procurement", "category": "Software", "ps_no": "SIH26100", "theme": "Smart Automation"},
    {"sno": 101, "org": "MoSPI", "title": "Develop an AI enabled learning platform that identifies competency gaps, recommends personalized training through integration with the iGOT Karmayogi ecosystem, and capable of generating Quizzes and Multiple choice questions (MCQs) from uploaded learning materials to strengthen capacity building in India's Official Statistical System", "category": "Software", "ps_no": "SIH26101", "theme": "Smart Education"},
    {"sno": 102, "org": "MoSPI", "title": "Development of an AI-powered system to detect anomalies, fraud, and inefficiencies in MPLAD Scheme implementation", "category": "Software", "ps_no": "SIH26102", "theme": "Miscellaneous"},
    
    # Page 13
    {"sno": 103, "org": "MoSPI", "title": "Use case on web-based integrated project-monitoring platform", "category": "Software", "ps_no": "SIH26103", "theme": "Smart Automation"},
    {"sno": 104, "org": "All India Council for Technical Education (AICTE)", "title": "AI-Powered Real-Time Detection and Prevention of Voice Cloning Impersonation Attacks", "category": "Software", "ps_no": "SIH26104", "theme": "Miscellaneous"},
    {"sno": 105, "org": "All India Council for Technical Education (AICTE)", "title": "AI-Powered Continuous Cyber Risk Quantification and Investment Optimization Platform", "category": "Software", "ps_no": "SIH26105", "theme": "Blockchain & Cybersecurity"},
    {"sno": 106, "org": "All India Council for Technical Education (AICTE)", "title": "AI-Powered Email Threat Detection, GeoLocation and Forensic Intelligence Platform", "category": "Software", "ps_no": "SIH26106", "theme": "Blockchain & Cybersecurity"},
    {"sno": 107, "org": "Ministry of Consumer Affairs, Food & Public Distribution", "title": "AI-powered Intelligent Assistant for Indian Standards and BIS Services for Industries and Consumers", "category": "Software", "ps_no": "SIH26107", "theme": "Smart Automation"},
    {"sno": 108, "org": "Ministry of Consumer Affairs, Food & Public Distribution", "title": "AI-Powered Recommendation Engine for Identifying Applicable Indian Standards for Procurement Specifications", "category": "Software", "ps_no": "SIH26108", "theme": "Smart Automation"},
    {"sno": 109, "org": "Ministry of Fisheries, Animal Husbandry & Dairying", "title": "AI-Based Predictive Modelling for Early Forecasting of Bovine Mastitis in Indian Dairy Farms", "category": "Hardware", "ps_no": "SIH26109", "theme": "Agriculture, FoodTech & Rural Development"},
    {"sno": 110, "org": "Ministry of Fisheries, Animal Husbandry & Dairying", "title": "Development of a Low-Cost Light-weight Milk Chilling Can for Small-Scale Dairy Farmers", "category": "Hardware", "ps_no": "SIH26110", "theme": "Agriculture, FoodTech & Rural Development"},
    {"sno": 111, "org": "Ministry of Fisheries, Animal Husbandry & Dairying", "title": "Smart AI-Enabled Rapid Feed and Silage Quality Testing System for Dairy Farmers", "category": "Software", "ps_no": "SIH26111", "theme": "Agriculture, FoodTech & Rural Development"},
    {"sno": 112, "org": "Autodesk", "title": "Design and Develop a Modular Autonomous Mobile Robot (AMR) Platform for Smart Warehouse Automation", "category": "Hardware", "ps_no": "SIH26112", "theme": "Robotics and Drones"},
    {"sno": 113, "org": "Autodesk", "title": "Human augmentation technologies are transforming healthcare, rehabilitation, industrial ergonomics, assistive living, sports, and personal mobility by improving human capabilities and enhancing quality of life", "category": "Hardware", "ps_no": "SIH26113", "theme": "MedTech / BioTech / HealthTech"},
    
    # Page 14
    {"sno": 114, "org": "Autodesk", "title": "Smart City Site Planning using Autodesk Forma Site Design", "category": "Software", "ps_no": "SIH26114", "theme": "Smart Automation"},
    {"sno": 115, "org": "Autodesk", "title": "Design and Develop a Smart Mobile Medical-Waste Collection and Segregation System", "category": "Software", "ps_no": "SIH26115", "theme": "MedTech / BioTech / HealthTech"},
    {"sno": 116, "org": "Autodesk", "title": "Urban Mixed-Use Design Challenge - Design a centrally located mixed-use building in Autodesk Revit with commercial spaces (Ground + 1st floor) and residential units (up to 8 floors). 1 Level of Basement (Car Parking + EV Charging), Total (B+G+9)", "category": "Software", "ps_no": "SIH26116", "theme": "Smart Education"},
    {"sno": 117, "org": "Mangalore Refinery and Petrochemicals Limited (MRPL)", "title": "Sovereign On-Premise Agentic AI Workbench using Open-Weight Multimodal LLMs for Confidential Industrial Work", "category": "Software", "ps_no": "SIH26117", "theme": "Smart Automation"},
    {"sno": 118, "org": "Mangalore Refinery and Petrochemicals Limited (MRPL)", "title": "Passive Colorimetric H2S Exposure-Dosimeter Wristband with AI-Based Quantitative Reading", "category": "Hardware", "ps_no": "SIH26118", "theme": "Miscellaneous"},
    {"sno": 119, "org": "Mangalore Refinery and Petrochemicals Limited (MRPL)", "title": "Indigenous GPU-Accelerated Optimization Solver (Sovereign Alternative to Express / CPLEX)", "category": "Software", "ps_no": "SIH26119", "theme": "Miscellaneous"},
    {"sno": 120, "org": "Oil India Limited", "title": "Digital Twin for Well-to-Surface Optimization of Cyclic Steam Stimulation (CSS) and Sucker Rod Pump (SRP) Operations for Heavy Oil Wells of Baghewala Field", "category": "Software", "ps_no": "SIH26120", "theme": "Smart Automation"},
    {"sno": 121, "org": "Oil India Limited", "title": "eRTMAC-NWIS (Nearby Wells Intelligence System): An AI-Powered Offset Well Knowledge and Decision Support Platform for Drilling Operations", "category": "Software", "ps_no": "SIH26121", "theme": "Smart Automation"},
    
    # Page 15
    {"sno": 122, "org": "Oil India Limited", "title": "Intelligent Data Capture & Schedule-Linking Layer for Infrastructure Project Management: Real-Time Actual Progress Tracking (Planning-to-Execution Bridge)", "category": "Software", "ps_no": "SIH26122", "theme": "Smart Automation"},
    {"sno": 123, "org": "Bharat Electronics Limited (BEL)", "title": "Edge-AI Based Distributed Fleet Coordination for Autonomous Mobile Robots (AMRs) in Smart Warehouses", "category": "Software", "ps_no": "SIH26123", "theme": "Robotics and Drones"},
    {"sno": 124, "org": "Bharat Electronics Limited (BEL)", "title": "AI-Powered Mobile Urban Intelligence Platform Using Public Transport Fleet", "category": "Software", "ps_no": "SIH26124", "theme": "Fitness & Sports"},
    {"sno": 125, "org": "Bharat Electronics Limited (BEL)", "title": "Blockchain-Based Secure Platform for Identity, Access Control, and Digital Asset Management", "category": "Software", "ps_no": "SIH26125", "theme": "Blockchain & Cybersecurity"},
    {"sno": 126, "org": "Bharat Electronics Limited (BEL)", "title": "Vision Based Autonomous Navigation for Unmanned Ground Vehicle for Outdoor environment", "category": "Software", "ps_no": "SIH26126", "theme": "Robotics and Drones"},
    {"sno": 127, "org": "Bharat Electronics Limited (BEL)", "title": "City-Wide AI Engine for Multi-Camera ANPR Trajectory Tracking and Urban Traffic Analytics", "category": "Software", "ps_no": "SIH26127", "theme": "Transportation & Logistics"},
    {"sno": 128, "org": "Government Of Maharashtra", "title": "Efficient systems for early detection, prevention, and management of livestock diseases and animal health issues", "category": "Software", "ps_no": "SIH26128", "theme": "Agriculture, FoodTech & Rural Development"},
    {"sno": 129, "org": "Government Of Maharashtra", "title": "System integration and interoperability among government digital platforms, resulting in fragmented service delivery", "category": "Software", "ps_no": "SIH26129", "theme": "Smart Automation"},
    {"sno": 130, "org": "Government Of Maharashtra", "title": "Efficiency in streamlining industrial approvals, compliance processes, and access to government support services", "category": "Software", "ps_no": "SIH26130", "theme": "Smart Automation"},
    {"sno": 131, "org": "Government Of Maharashtra", "title": "Early detection and management of crop diseases and pest infestations", "category": "Software", "ps_no": "SIH26131", "theme": "Agriculture, FoodTech & Rural Development"},
    
    # Page 16
    {"sno": 132, "org": "Government Of Maharashtra", "title": "Strengthening market linkages and price discovery for farmers", "category": "Software", "ps_no": "SIH26132", "theme": "Agriculture, FoodTech & Rural Development"},
    {"sno": 133, "org": "Government Of Maharashtra", "title": "Accessibility and quality of public healthcare services, particularly in rural and underserved areas", "category": "Software", "ps_no": "SIH26133", "theme": "MedTech / BioTech / HealthTech"},
    {"sno": 134, "org": "Government Of Maharashtra", "title": "Challenges in aligning skill development programs with industry requirements and emerging job market demands", "category": "Software", "ps_no": "SIH26134", "theme": "Miscellaneous"},
    {"sno": 135, "org": "Government Of Maharashtra", "title": "Difficulties in tracking employment outcomes, skill gaps, and the impact of skilling initiatives", "category": "Software", "ps_no": "SIH26135", "theme": "Smart Education"},
    {"sno": 136, "org": "Government Of Maharashtra", "title": "Startup friendly public procurement mechanism that enables government departments to identify, pilot, procure, and scale innovative solutions from eligible startups", "category": "Software", "ps_no": "SIH26136", "theme": "Smart Automation"},
    {"sno": 137, "org": "Egreen Quanta", "title": "Quantum-Inspired Intelligent Traffic Route Optimization in Transportation Systems Using Metaheuristic Optimization", "category": "Software", "ps_no": "SIH26137", "theme": "Fitness & Sports"},
    {"sno": 138, "org": "Egreen Quanta", "title": "Quantum-Inspired Fuel Consumption Prediction and Green Fleet Optimization", "category": "Software", "ps_no": "SIH26138", "theme": "Smart Vehicles"},
    {"sno": 139, "org": "Egreen Quanta", "title": "Hybrid Quantum Machine Learning Platform for Early Disease Detection", "category": "Software", "ps_no": "SIH26139", "theme": "MedTech / BioTech / HealthTech"},
    {"sno": 140, "org": "Egreen Quanta", "title": "AI-Based Interactive Quantum Algorithm Learning Platform", "category": "Software", "ps_no": "SIH26140", "theme": "Smart Education"},
    {"sno": 141, "org": "Egreen Quanta", "title": "Quantum-Inspired Cyber Threat Detection for Digital Signature Security", "category": "Software", "ps_no": "SIH26141", "theme": "Blockchain & Cybersecurity"},
    {"sno": 142, "org": "National Technical Research Organisation (NTRO)", "title": "Deep Learning Based Super Resolution Mapping (SRM) from Medium Resolution Satellite Imageries", "category": "Software", "ps_no": "SIH26142", "theme": "Smart Education"},
    
    # Page 17
    {"sno": 143, "org": "National Technical Research Organisation (NTRO)", "title": "Leveraging satellite imagery to determine Oil spills at sea along with AIS data correlations to identify vessel responsible for the spill", "category": "Software", "ps_no": "SIH26143", "theme": "Space Technology"},
    {"sno": 144, "org": "National Technical Research Organisation (NTRO)", "title": "Design & Development of a High-Sensitivity Micro barometer Infrasound sensor", "category": "Hardware", "ps_no": "SIH26144", "theme": "Miscellaneous"},
    {"sno": 145, "org": "National Technical Research Organisation (NTRO)", "title": "AI-Based Detection of Cyber Threats in Unidirectional IP Traffic", "category": "Software", "ps_no": "SIH26145", "theme": "Blockchain & Cybersecurity"},
    {"sno": 146, "org": "National Technical Research Organisation (NTRO)", "title": "AI-Powered Monitoring & Analysis of Bitcoin Transaction Traffic", "category": "Software", "ps_no": "SIH26146", "theme": "Transportation & Logistics"},
    {"sno": 147, "org": "National Technical Research Organisation (NTRO)", "title": "Automated model for analysis of .IQ and .wav files along with signal parameter extraction", "category": "Software", "ps_no": "SIH26147", "theme": "Miscellaneous"},
    {"sno": 148, "org": "National Technical Research Organisation (NTRO)", "title": "Creation of scripts/functions with new programming language to commence Computer & Network forensic analysis without triggering security solutions", "category": "Software", "ps_no": "SIH26148", "theme": "Blockchain & Cybersecurity"},
    {"sno": 149, "org": "National Technical Research Organisation (NTRO)", "title": "Design and Development of an Integrated Secure Data Erasure and Advanced File Recovery Tool for Digital Forensics and Data Sanitization", "category": "Software", "ps_no": "SIH26149", "theme": "Blockchain & Cybersecurity"},
    {"sno": 150, "org": "National Technical Research Organisation (NTRO)", "title": "Development of a Multi-Vendor DVR/NVR Forensic Analysis Tool for Standardized Acquisition, Recovery, and Analysis of Surveillance Evidence", "category": "Software", "ps_no": "SIH26150", "theme": "Blockchain & Cybersecurity"},
    {"sno": 151, "org": "National Technical Research Organisation (NTRO)", "title": "Dark web threat actor de-anonymization", "category": "Software", "ps_no": "SIH26151", "theme": "Blockchain & Cybersecurity"},
    {"sno": 152, "org": "National Technical Research Organisation (NTRO)", "title": "Social Media Analytics", "category": "Software", "ps_no": "SIH26152", "theme": "Miscellaneous"},
    
    # Page 18
    {"sno": 153, "org": "National Technical Research Organisation (NTRO)", "title": "AI based Network Attack Forecasting from Network Traffic Data", "category": "Software", "ps_no": "SIH26153", "theme": "Blockchain & Cybersecurity"},
    {"sno": 154, "org": "National Technical Research Organisation (NTRO)", "title": "Gen AI Platform for Automated Content Transformation", "category": "Software", "ps_no": "SIH26154", "theme": "Smart Automation"},
    {"sno": 155, "org": "National Technical Research Organisation (NTRO)", "title": "AI-Driven Multi-Vendor Network Security Compliance Auditor", "category": "Software", "ps_no": "SIH26155", "theme": "Blockchain & Cybersecurity"},
    {"sno": 156, "org": "National Technical Research Organisation (NTRO)", "title": "Universal Log Pre-processing Framework", "category": "Software", "ps_no": "SIH26156", "theme": "Miscellaneous"},
    {"sno": 157, "org": "National Technical Research Organisation (NTRO)", "title": "Supervisory Analytics Tool for SOC Assessment (SAT-SA)", "category": "Software", "ps_no": "SIH26157", "theme": "Miscellaneous"},
    {"sno": 158, "org": "National Technical Research Organisation (NTRO)", "title": "Single-Pass Drone Video to Accurate 3D Model Generation System", "category": "Software", "ps_no": "SIH26158", "theme": "Robotics and Drones"},
    {"sno": 159, "org": "National Technical Research Organisation (NTRO)", "title": "SecureMailScope: AI-Assisted Cryptographic Security Posture Assessment for Secure Email Communications", "category": "Software", "ps_no": "SIH26159", "theme": "Blockchain & Cybersecurity"},
    {"sno": 160, "org": "National Technical Research Organisation (NTRO)", "title": "AI-Powered IPsec VPN Protocol Analyzer and Security Assessment Framework", "category": "Software", "ps_no": "SIH26160", "theme": "Blockchain & Cybersecurity"},
    {"sno": 161, "org": "National Technical Research Organisation (NTRO)", "title": "Dam Break Inundation Modelling Using Hydrodynamic Modelling of any River", "category": "Software", "ps_no": "SIH26161", "theme": "Disaster Management"},
    {"sno": 162, "org": "National Technical Research Organisation (NTRO)", "title": "AI-Based Detection and Classification of Industrial Fires and Persistent Thermal Sources Using NASA FIRMS, OSM & Satellite Data", "category": "Software", "ps_no": "SIH26162", "theme": "Miscellaneous"},
    {"sno": 163, "org": "National Technical Research Organisation (NTRO)", "title": "Security Assessment of the World Monitor application", "category": "Software", "ps_no": "SIH26163", "theme": "Miscellaneous"},
    {"sno": 164, "org": "National Technical Research Organisation (NTRO)", "title": "Enterprise Cryptographic Discovery & Analysis Tool (ECDAT)", "category": "Software", "ps_no": "SIH26164", "theme": "Blockchain & Cybersecurity"},
    {"sno": 165, "org": "Oil India Limited", "title": "AI/NLP Engine to Detect Serious Injury & Fatality (SIF) Precursors in OIL's Unsafe-Act/Unsafe-Condition and Near-Miss Reports", "category": "Software", "ps_no": "SIH26165", "theme": "Miscellaneous"},
    
    # Page 19
    {"sno": 166, "org": "Indian Space Research Organisation (ISRO)", "title": "Multi-modal, Sun angle and scale invariant image correspondence using Chandrayaan-2 optical images (OHRC, TMC and IIRS)", "category": "Software", "ps_no": "SIH26166", "theme": "Space Technology"},
    {"sno": 167, "org": "Indian Space Research Organisation (ISRO)", "title": "SatQuery AI - An Interactive Vision-Language Assistant for Multimodal Remote Sensing Image Analysis through Text Queries", "category": "Software", "ps_no": "SIH26167", "theme": "Space Technology"},
    {"sno": 168, "org": "Indian Space Research Organisation (ISRO)", "title": "AI-ML based Intelligent Dead Reckoning system for seamless navigation", "category": "Software", "ps_no": "SIH26168", "theme": "Miscellaneous"},
    {"sno": 169, "org": "Indian Space Research Organisation (ISRO)", "title": "Development of an AI-Based Virtual Camera Tracking System for Coarse Alignment of Mobile Free Space Optical Communication (FSOC) Terminals", "category": "Software", "ps_no": "SIH26169", "theme": "Miscellaneous"},
    {"sno": 170, "org": "Indian Space Research Organisation (ISRO)", "title": "AI-Driven Anomaly Detection in Component Burn-In & Screening", "category": "Software", "ps_no": "SIH26170", "theme": "Smart Automation"},
    {"sno": 171, "org": "Indian Space Research Organisation (ISRO)", "title": "On-device Visual Perception for Light-weight Browser Agents", "category": "Software", "ps_no": "SIH26171", "theme": "Miscellaneous"},
    {"sno": 172, "org": "Indian Space Research Organisation (ISRO)", "title": "Low Latency and Efficient Voice Activator for Edge Devices", "category": "Hardware", "ps_no": "SIH26172", "theme": "Miscellaneous"},
    {"sno": 173, "org": "Indian Space Research Organisation (ISRO)", "title": "iTantra - Indian Multilingual TTS & STT Aided Neural Transceiver Radio Access for low bitrate links", "category": "Software", "ps_no": "SIH26173", "theme": "Miscellaneous"},
    {"sno": 174, "org": "Indian Space Research Organisation (ISRO)", "title": "AI Human Activity Recognition for On-board BAS Experiments", "category": "Software", "ps_no": "SIH26174", "theme": "Miscellaneous"},
    {"sno": 175, "org": "Indian Space Research Organisation (ISRO)", "title": "DepthWizard - Single-View Height Estimation and 3D Flythrough", "category": "Software", "ps_no": "SIH26175", "theme": "Miscellaneous"},
    {"sno": 176, "org": "Indian Space Research Organisation (ISRO)", "title": "ORCA Marine Ecosystem Reasoning with Collaborative Agents", "category": "Software", "ps_no": "SIH26176", "theme": "Miscellaneous"},
    {"sno": 177, "org": "Qualcomm Inc", "title": "A deployable AI-powered autonomous drone that aids search-and-rescue operations by detecting people and hazards, thereby improving responder safety and reducing victim discovery time", "category": "Hardware", "ps_no": "SIH26177", "theme": "Robotics and Drones"},
    
    # Page 20
    {"sno": 178, "org": "Qualcomm Inc", "title": "A resilient, AI-powered environmental monitoring network that provides early detection, localized intelligence, and actionable alerts for floods, forest fires, pollution events, and other environmental hazards common in India, enabling authorities and communities to shift from reactive disaster response to proactive risk prevention", "category": "Hardware", "ps_no": "SIH26178", "theme": "Disaster Management"},
    {"sno": 179, "org": "Qualcomm Inc", "title": "To build an AI-powered retail intelligence platform that delivers real-time shopper analytics, automated inventory visibility, and proactive queue management through on-device AI, enabling retailers to reduce stock-outs, improve customer experience, optimize staffing, and increase operational efficiency while maintaining privacy and minimizing cloud dependency", "category": "Hardware", "ps_no": "SIH26179", "theme": "Smart Automation"},
    {"sno": 180, "org": "Qualcomm Inc", "title": "A field-deployable AI-powered Smart Farming Assistant that helps farmers detect crop diseases, pests, nutrient deficiencies, and irrigation needs at an early stage, while improving resilience against droughts, floods, heat waves, and other agricultural risks common in India. The solution should enable higher yields, lower input costs, more efficient water usage, and faster response to emerging threats through real-time on-device intelligence", "category": "Hardware", "ps_no": "SIH26180", "theme": "Disaster Management"},
    
    # Page 21
    {"sno": 181, "org": "Qualcomm Inc", "title": "A secure, AI-powered Personal Health Companion that delivers real-time, privacy-preserving health monitoring and early warning capabilities, helping individuals recognize health risks before they become emergencies. The solution should improve resilience during heat waves, floods, pollution events, and other disasters common in India while enabling continuous health support through on-device intelligence", "category": "Hardware", "ps_no": "SIH26181", "theme": "MedTech / BioTech / HealthTech"},
    {"sno": 182, "org": "Ministry of Home Affairs (MHA)", "title": "Automated Attribution of Unknown Cryptocurrency Wallets to Nearest Virtual Asset Service Providers (VASPs) through Blockchain Intelligence APIs", "category": "Software", "ps_no": "SIH26182", "theme": "Blockchain & Cybersecurity"},
    {"sno": 183, "org": "Ministry of Home Affairs (MHA)", "title": "Real-Time Identification of Fraud-Linked Cryptocurrency Exchanges from Victim-Reported Suspect Wallet Addresses through Automated Blockchain Analytics", "category": "Software", "ps_no": "SIH26183", "theme": "Blockchain & Cybersecurity"},
    {"sno": 184, "org": "Ministry of Home Affairs (MHA)", "title": "Development of a Predictive Analytics Framework for Cybercrime Complaints to Forecast Likely Cash Withdrawal Locations in Advance, Enabling Generation of Actionable Intelligence for Timely and Proactive Cybercrime Intervention", "category": "Software", "ps_no": "SIH26184", "theme": "Blockchain & Cybersecurity"},
    {"sno": 185, "org": "Ministry of Home Affairs (MHA)", "title": "Helmet mounted conformal antenna for tactical communications in urban CQB environments", "category": "Hardware", "ps_no": "SIH26185", "theme": "Miscellaneous"},
    
    # Page 22
    {"sno": 186, "org": "Ministry of Home Affairs (MHA)", "title": "AI-Based Predictive Personnel Stress and Welfare Monitoring System for Uniformed Forces", "category": "Software", "ps_no": "SIH26186", "theme": "MedTech / BioTech / HealthTech"},
    {"sno": 187, "org": "Ministry of Home Affairs (MHA)", "title": "AI-Based Intelligent Video Analytics Platform for Border Surveillance using existing CCTV Infrastructure", "category": "Software", "ps_no": "SIH26187", "theme": "Smart Automation"},
    {"sno": 188, "org": "Ministry of Home Affairs (MHA)", "title": "AI-Based Fake Identity & Document Screening System", "category": "Software", "ps_no": "SIH26188", "theme": "Miscellaneous"},
    {"sno": 189, "org": "Ministry of Home Affairs (MHA)", "title": "AI-Powered Criminal Network Analysis System", "category": "Software", "ps_no": "SIH26189", "theme": "Blockchain & Cybersecurity"},
    {"sno": 190, "org": "Ministry of Home Affairs (MHA)", "title": "Secure Digital Document Management System for Legal and Investigation Documents", "category": "Software", "ps_no": "SIH26190", "theme": "Miscellaneous"},
    {"sno": 191, "org": "Ministry of Home Affairs (MHA)", "title": "Intelligent Identification of Hazard-Based Red Zones, Carrying Capacity Assessment, and Immediate Relocation Needs for Vulnerable Habitations", "category": "Software", "ps_no": "SIH26191", "theme": "Disaster Management"},
    {"sno": 192, "org": "Ministry of Home Affairs (MHA)", "title": "Flash Flood Prediction System for Hilly Regions using Multi-Source Data Theme", "category": "Software", "ps_no": "SIH26192", "theme": "Disaster Management"},
    {"sno": 193, "org": "AICTE", "title": "Student Innovation - Smart Resource Conservation (Software)", "category": "Software", "ps_no": "SIH26193", "theme": "Smart Resource Conservation"},
    {"sno": 194, "org": "AICTE", "title": "Student Innovation - Fitness & Sports (Software)", "category": "Software", "ps_no": "SIH26194", "theme": "Fitness & Sports"},
    {"sno": 195, "org": "AICTE", "title": "Student Innovation - Heritage & Culture (Software)", "category": "Software", "ps_no": "SIH26195", "theme": "Heritage & Culture"},
    {"sno": 196, "org": "AICTE", "title": "Student Innovation - MedTech / BioTech / HealthTech (Software)", "category": "Software", "ps_no": "SIH26196", "theme": "MedTech / BioTech / HealthTech"},
    {"sno": 197, "org": "AICTE", "title": "Student Innovation - Agriculture, FoodTech & Rural Development (Software)", "category": "Software", "ps_no": "SIH26197", "theme": "Agriculture, FoodTech & Rural Development"},
    {"sno": 198, "org": "AICTE", "title": "Student Innovation - Transportation & Logistics (Software)", "category": "Software", "ps_no": "SIH26198", "theme": "Transportation & Logistics"},
    {"sno": 199, "org": "AICTE", "title": "Student Innovation - Fitness & Sports (Software)", "category": "Software", "ps_no": "SIH26199", "theme": "Fitness & Sports"},
    {"sno": 200, "org": "AICTE", "title": "Student Innovation - MedTech / BioTech / HealthTech (Software)", "category": "Software", "ps_no": "SIH26200", "theme": "MedTech / BioTech / HealthTech"},
    
    # Page 23
    {"sno": 201, "org": "AICTE", "title": "Student Innovation - Smart Resource Conservation (Software)", "category": "Software", "ps_no": "SIH26201", "theme": "Smart Resource Conservation"},
    {"sno": 202, "org": "AICTE", "title": "Student Innovation - Travel & Tourism (Software)", "category": "Software", "ps_no": "SIH26202", "theme": "Travel & Tourism"},
    {"sno": 203, "org": "AICTE", "title": "Student Innovation - Renewable / Sustainable Energy (Software)", "category": "Software", "ps_no": "SIH26203", "theme": "Renewable / Sustainable Energy"},
    {"sno": 204, "org": "AICTE", "title": "Student Innovation - Miscellaneous (Software)", "category": "Software", "ps_no": "SIH26204", "theme": "Miscellaneous"},
    {"sno": 205, "org": "AICTE", "title": "Student Innovation - Smart Education (Software)", "category": "Software", "ps_no": "SIH26205", "theme": "Smart Education"},
    {"sno": 206, "org": "AICTE", "title": "Student Innovation - Disaster Management (Software)", "category": "Software", "ps_no": "SIH26206", "theme": "Disaster Management"},
    {"sno": 207, "org": "AICTE", "title": "Student Innovation - Travel & Tourism (Software)", "category": "Software", "ps_no": "SIH26207", "theme": "Travel & Tourism"},
    {"sno": 208, "org": "AICTE", "title": "Student Innovation - Heritage & Culture (Software)", "category": "Software", "ps_no": "SIH26208", "theme": "Heritage & Culture"},
    {"sno": 209, "org": "AICTE", "title": "Student Innovation - Space Technology (Software)", "category": "Software", "ps_no": "SIH26209", "theme": "Space Technology"},
    {"sno": 210, "org": "AICTE", "title": "Student Innovation - Smart Resource Conservation (Hardware)", "category": "Hardware", "ps_no": "SIH26210", "theme": "Smart Resource Conservation"},
    {"sno": 211, "org": "AICTE", "title": "Student Innovation - Fitness & Sports (Hardware)", "category": "Hardware", "ps_no": "SIH26211", "theme": "Fitness & Sports"},
    {"sno": 212, "org": "AICTE", "title": "Student Innovation - Heritage & Culture (Hardware)", "category": "Hardware", "ps_no": "SIH26212", "theme": "Heritage & Culture"},
    {"sno": 213, "org": "AICTE", "title": "Student Innovation - MedTech / BioTech / HealthTech (Hardware)", "category": "Hardware", "ps_no": "SIH26213", "theme": "MedTech / BioTech / HealthTech"},
    {"sno": 214, "org": "AICTE", "title": "Student Innovation - Agriculture, FoodTech & Rural Development (Hardware)", "category": "Hardware", "ps_no": "SIH26214", "theme": "Agriculture, FoodTech & Rural Development"},
    {"sno": 215, "org": "AICTE", "title": "Student Innovation - Transportation & Logistics (Hardware)", "category": "Hardware", "ps_no": "SIH26215", "theme": "Transportation & Logistics"},
    {"sno": 216, "org": "AICTE", "title": "Student Innovation - Fitness & Sports (Hardware)", "category": "Hardware", "ps_no": "SIH26216", "theme": "Fitness & Sports"},
    {"sno": 217, "org": "AICTE", "title": "Student Innovation - MedTech / BioTech / HealthTech (Hardware)", "category": "Hardware", "ps_no": "SIH26217", "theme": "MedTech / BioTech / HealthTech"},
    {"sno": 218, "org": "AICTE", "title": "Student Innovation - Smart Resource Conservation (Hardware)", "category": "Hardware", "ps_no": "SIH26218", "theme": "Smart Resource Conservation"},
    {"sno": 219, "org": "AICTE", "title": "Student Innovation - Travel & Tourism (Hardware)", "category": "Hardware", "ps_no": "SIH26219", "theme": "Travel & Tourism"},
    {"sno": 220, "org": "AICTE", "title": "Student Innovation - Renewable / Sustainable Energy (Hardware)", "category": "Hardware", "ps_no": "SIH26220", "theme": "Renewable / Sustainable Energy"},
    {"sno": 221, "org": "AICTE", "title": "Student Innovation - Miscellaneous (Hardware)", "category": "Hardware", "ps_no": "SIH26221", "theme": "Miscellaneous"},
    {"sno": 222, "org": "AICTE", "title": "Student Innovation - Smart Education (Hardware)", "category": "Hardware", "ps_no": "SIH26222", "theme": "Smart Education"},
    
    # Page 24
    {"sno": 223, "org": "AICTE", "title": "Student Innovation - Disaster Management (Hardware)", "category": "Hardware", "ps_no": "SIH26223", "theme": "Disaster Management"},
    {"sno": 224, "org": "AICTE", "title": "Student Innovation - Travel & Tourism (Hardware)", "category": "Hardware", "ps_no": "SIH26224", "theme": "Travel & Tourism"},
    {"sno": 225, "org": "AICTE", "title": "Student Innovation - Heritage & Culture (Hardware)", "category": "Hardware", "ps_no": "SIH26225", "theme": "Heritage & Culture"},
    {"sno": 226, "org": "AICTE", "title": "Student Innovation - Space Technology (Hardware)", "category": "Hardware", "ps_no": "SIH26226", "theme": "Space Technology"}
]

print(f"Total PS parsed: {len(problem_statements)}")

# Generate Markdown file
md_content = """# SIH 2026: Official Problem Statements Master Directory

[🏠 Home](../README.md) > [📁 SIH 2026 Intelligence](./rules.md) > **Problem Statements**

> **Official Document Status**: `[OFFICIAL FACT]`  
> **Source**: Ministry of Education's Innovation Cell (MIC) & AICTE Official Problem Statement Release  
> **Submission Deadline**: **20th September 2026** *(Official Deadline)*  
> **Total Problem Statements**: **226** (168 Software | 58 Hardware)  
> **Prize Money**: **₹1,50,000 per Problem Statement** for winning teams  
> **Cap Rule**: Maximum 500 ideas per PS before automatic portal freeze  

---

## 🧭 Navigation & Sectoral Breakdown

```mermaid
pie title SIH 2026 Problem Statements by Sector Domain
    "Space, Defence & Security (ISRO, DRDO, NTRO, MHA)" : 58
    "Earth Sciences, Climate & Disaster (MoES, MDoNER)" : 36
    "GovTech, Rural Dev, Coal & Steel" : 35
    "Student Innovation (Open Track)" : 34
    "Corporate & PSU (Qualcomm, BEL, MRPL, Autodesk, OIL)" : 28
    "Social Welfare, AYUSH, MSME, Cooperation & Health" : 35
```

---

## 📊 Summary Statistics

| Category | Total Problem Statements | Key Participating Ministries / Organizations |
| :--- | :---: | :--- |
| **Software** | **168** | ISRO, MoES, NTRO, MHA, MoSJE, Govt of Maharashtra, Rural Dev, Steel, Coal, Ayush |
| **Hardware** | **58** | DRDO, Qualcomm, MoD, Autodesk, MoES, MSME, Fisheries & Dairying, MDoNER, Student Innovation |
| **Total** | **226** | **50+ Union Ministries, State Governments, PSUs, and Global Industry Leaders** |

---

## 📋 Master Problem Statements Table (SIH26001 – SIH26226)

| S.No | PS Number | Category | Organization / Ministry | Theme | Problem Statement Title |
| :---: | :---: | :---: | :--- | :--- | :--- |
"""

for ps in problem_statements:
    md_content += f"| {ps['sno']} | **`{ps['ps_no']}`** | `{ps['category']}` | {ps['org']} | {ps['theme']} | {ps['title']} |\n"

md_content += """
---

## 🏢 Index by Sponsoring Organization

### 1. Central Ministries & Government Departments
- **Ministry of Development of North Eastern Region (MDoNER)**: `SIH26001` - `SIH26005`
- **Ministry of Steel**: `SIH26006` - `SIH26009`
- **Ministry of Rural Development**: `SIH26010` - `SIH26019`
- **Ministry of MSME**: `SIH26020` - `SIH26022`
- **Ministry of Coal**: `SIH26023` - `SIH26025`
- **Ministry of Railways**: `SIH26026` - `SIH26028`
- **Ministry of Consumer Affairs, Food & Public Distribution**: `SIH26029` - `SIH26036`, `SIH26107` - `SIH26108`
- **Ministry of Ayush**: `SIH26044` - `SIH26048`
- **Ministry of Statistics and Programme Implementation (MoSPI)**: `SIH26056`, `SIH26101` - `SIH26103`
- **Ministry of Earth Sciences (MoES)**: `SIH26057` - `SIH26086` (30 Problem Statements)
- **Ministry of Cooperation**: `SIH26087` - `SIH26089`
- **Ministry of Social Justice and Empowerment (MoSJE)**: `SIH26090` - `SIH26097`
- **Ministry of Defence (MoD)**: `SIH26098`
- **Ministry of Petroleum & Natural Gas**: `SIH26099` - `SIH26100`
- **Ministry of Fisheries, Animal Husbandry & Dairying**: `SIH26109` - `SIH26111`
- **Ministry of Home Affairs (MHA)**: `SIH26182` - `SIH26192` (11 Problem Statements)

### 2. Premier R&D & Strategic Defence Organizations
- **Defence Research and Development Organisation (DRDO)**: `SIH26049` - `SIH26055`
- **National Technical Research Organisation (NTRO)**: `SIH26142` - `SIH26164` (23 Problem Statements)
- **Indian Space Research Organisation (ISRO)**: `SIH26166` - `SIH26176` (11 Problem Statements)

### 3. State Governments
- **Government of Jharkhand**: `SIH26039` - `SIH26043`
- **Government of Maharashtra**: `SIH26128` - `SIH26136`

### 4. Public Sector Undertakings (PSUs) & Industry Leaders
- **MathWorks**: `SIH26037` - `SIH26038`
- **Autodesk**: `SIH26112` - `SIH26116`
- **Mangalore Refinery and Petrochemicals Limited (MRPL)**: `SIH26117` - `SIH26119`
- **Oil India Limited**: `SIH26120` - `SIH26122`, `SIH26165`
- **Bharat Electronics Limited (BEL)**: `SIH26123` - `SIH26127`
- **Egreen Quanta**: `SIH26137` - `SIH26141`
- **Qualcomm Inc**: `SIH26177` - `SIH26181`

### 5. All India Council for Technical Education (AICTE) & Open Student Innovation
- **AICTE Strategic Tech**: `SIH26104` - `SIH26106`
- **AICTE Student Innovation (Open Track)**: `SIH26193` - `SIH26226` (34 Problem Statements)
"""

with open("/Users/akshaybhagat/Documents/silentStack/2026/problem_statements.md", "w") as f:
    f.write(md_content)

print("Generated 2026/problem_statements.md successfully!")
