# ==============================================================================
# SAKTHI AI - EDIT DETAILS CONFIGURATION FILE
# ==============================================================================
# Edit this file to customize the information displayed on your portfolio website
# and used by Sakthi AI.
# ==============================================================================

# Google Gemini API Key (Configure locally via environment variables or .streamlit/secrets.toml)
API_KEY = ""

# Personal Info
NAME = "Sakthikrishna G"
PHONE = "+91 9360138590"
EMAIL = "sakthikrishna.g.work@gmail.com"
LINKEDIN = "linkedin.com/in/sakthikrishna-g"
GITHUB = "github.com/Sakthi-hash"
TAGLINE = "Embedded Systems Engineer | ECE Graduate | C Programming Specialist"

# Short introduction about yourself (focused on ECE, Embedded Systems, and Fresher looking to build expertise)
ABOUT_ME = """
I am an Electronics and Communication Engineering student and a highly motivated
fresher seeking an Embedded Systems Engineer role. I specialize in writing clean,
optimized C/Embedded C code and integrating microcontrollers with sensors and peripherals.
I am a firm believer in "groundwork first"—getting hands-on in the field, analyzing every
physical possibility, mapping legacy constraints, and executing on-site installations like a pro.
Having completed 4 hands-on ECE internships (spanning air traffic surveillance, electronic circuit
testing, and quality control at Coimbatore Airport, Vasantha Advanced Systems, and Brigade LED),
I am fully prepared to lead physical deployments and build robust automated hardware systems.
"""

# Your primary career aspiration
CAREER_GOAL = """
To kickstart my career as an Embedded Systems Engineer in an innovative environment
where I can write high-efficiency firmware, integrate hardware peripherals, and design
robust circuit boards while constantly elevating my expertise.
"""

# Education background
EDUCATION = "B.E. Electronics & Communication Engineering (Sri Krishna College of Technology) - Lateral Entry"

# List of skills (rendered as chips in the UI - focused heavily on C and Embedded)
SKILLS = [
    "C Programming",
    "Embedded C",
    "Microcontrollers (Arduino, 8051)",
    "Sensors & Actuators",
    "Hardware Integration",
    "Circuit Design & Simulation",
    "EasyEDA",
    "Tinkercad",
    "ThingSpeak (IoT)",
    "Oscilloscope & Test Tools",
    "Soldering & Assembly",
    "Quality Control & Inspection",
    "Java",
    "Technical Troubleshooting",
]

# Details of your featured projects (Academic Projects from Resume - ECE focused)
PROJECT_DETAILS = [
    {
        "name": "Resilient Street-Level Smart Distribution & Autonomous Fault Isolation System",
        "icon": "⚡",
        "desc": "Lead Developer. Built an autonomous power network with ESP32/LoRa. Programmed adaptive theft thresholds, sequence analysis fault detection, and self-healing ring topology in Embedded C.",
        "tags": ["Embedded C", "LoRa", "ESP32", "Fault Isolation", "SQLite"],
    },
    {
        "name": "Solar-Powered IoT Precision Irrigation System (IIT-D Sponsored Capstone)",
        "icon": "☀️",
        "desc": "Site & Hardware Lead. Deployed an automated solar irrigation network — **UBA Funded** (Unnat Bharat Abhiyan 2.0, ₹99,500). Managed on-site groundwork, mapped legacy buried pipes, and coordinated beneficiary farmer allotment.",
        "tags": ["ESP32", "Firebase", "ThingSpeak", "Flutter", "Solar Power"],
    },
    {
        "name": "Smart Crop Yield Predictor (Early ML Project)",
        "icon": "🌾",
        "desc": "Developer. Researched agricultural modeling. Built data preprocessing and feature scaling pipelines to train a Random Forest model, deploying the predictions on a Streamlit interface.",
        "tags": ["Python", "Scikit-learn", "Pandas", "Streamlit"],
    },
    {
        "name": "Ultrasonic Radar System",
        "icon": "📡",
        "desc": "Developer. Designed and constructed an ultrasonic radar system using Arduino. Wrote C algorithms for sweep control, sensor signal processing, and real-time obstacle distance calculations.",
        "tags": ["Embedded C", "Ultrasonic Sensors", "Servo Control", "Arduino"],
    },
    {
        "name": "Li-Fi Communication Model",
        "icon": "💡",
        "desc": "Developer. Developed a working Light Fidelity (Li-Fi) setup for wireless audio and data transmission. Programmed receiver/transmitter logic for light modulation and photodetection hardware.",
        "tags": ["C Programming", "Hardware Integration", "Li-Fi", "LEDs"],
    },
]

# List of certifications (from Awards & Accomplishments)
CERTIFICATIONS = [
    "NPTEL Certification – Sustainable Development",
    "NPTEL Certification – Effective Learning for Professional Development",
]

# Custom selling points / reasons to hire (Emoji, Reason text - highly persuasive ECE profile)
WHY_HIRE_ME = [
    ("💻", "Strong command of C & Embedded C, with verified academic projects running microcontroller firmware"),
    ("⚙️", "4 Hands-on industry internships proving readiness for testing, production, and quality control roles"),
    ("⚡", "Full-cycle hardware builder: experienced in circuit simulation, physical breadboarding, and soldering"),
    ("🎯", "Cross-domain exposure: applied embedded skills across aerospace (CNS/ATC), manufacturing (LED), and agriculture (IoT irrigation) — adapts fast to new problem spaces"),
    ("📊", "Strong academics: Distinction in Diploma (8.1 CGPA) & lateral entry B.E. (7.18 CGPA) with no arrears"),
    ("🤝", "Proven leadership & crisis management: Coordinated the first post-pandemic 3-day ECE Industrial Visit from scratch, successfully resolving tough on-road situations"),
]

# Recommended questions for visitors to ask Sakthi AI (refocused on hireability)
SUGGESTED_QUESTIONS = [
    "Why is Sakthikrishna a strong candidate for an Embedded Software Engineer role?",
    "Tell me about his ECE internships, including his diploma work at Brigade LED.",
    "Explain his C programming and microcontroller debugging skills.",
    "What did he build for his Resilient Fault Isolation and Li-Fi projects?",
    "How does he handle circuit design and hardware testing?",
    "What are his academic and leadership credentials?",
]

# ==============================================================================
# LANDING PAGE METRICS AND HEADERS CONFIGURATION
# ==============================================================================

# Metrics displayed on the landing page (Label, Value)
METRICS = [
    ("Projects Completed", str(len(PROJECT_DETAILS))),
    ("Internships Done", "4"),
    ("B.E. CGPA (No History of Arrears)", "7.18"),
    ("Diploma CGPA (Distinction)", "8.1"),
]

# Section Titles & Subtitles
SKILLS_TITLE = "Technical & Core Competencies"
SKILLS_SUBTITLE = "Key ECE tools, languages, and hardware capabilities I leverage to build embedded solutions"

PROJECTS_TITLE = "Featured ECE & Embedded Projects"
PROJECTS_SUBTITLE = "Working systems designed, coded in C, and integrated with physical sensors and microcontrollers"

WHY_HIRE_TITLE = "Why Hire Me"
WHY_HIRE_SUBTITLE = "Key reasons why my ECE background, C proficiency, and hands-on internship experience add value to your team"

CERTIFICATIONS_TITLE = "Certifications & Student Leadership"

# Academic Deliverables (UG)
UG_DELIVERABLES = [
    {
        "title": "Smart Traffic System (Task Management)",
        "type": "B.E. UG Seminar",
        "desc": "Designed and presented an Autonomous Vehicle Task Management Simulator, handling control flow logic and real-time task scheduling simulations.",
    },

    {
        "title": "Smart Fabrics for Soldier Health Monitoring",
        "type": "Research Study",
        "desc": "Authored a comprehensive technical review evaluating bio-sensor placements, network transceivers, and conductive textile materials for real-time monitoring.",
    },
    {
        "title": "Optical Fiber Modes",
        "type": "Physics & ECE Seminar",
        "desc": "Presented mathematical derivations of propagation modes in optical wave-guides, illustrating single-mode vs. multi-mode boundaries.",
    },
    {
        "title": "Software Defined Networking (SDN)",
        "type": "Technical Question Bank",
        "desc": "Compiled an exhaustive reference guide and exam question bank detailing OpenFlow, SDN controller architectures, and virtualization layers.",
    },
    {
        "title": "Wireless Communication Paper Comparison",
        "type": "Research Comparative Review",
        "desc": "Conducted a critical analysis of multiple research papers comparing MIMO channel capacities, spatial multiplexing, and path loss models.",
    },
    {
        "title": "Entrepreneurship & Business Feasibility Study",
        "type": "Academic Report",
        "desc": "Prepared a project cost-benefit feasibility analysis, covering cash flows, market entry barriers, and scaling blueprints.",
    },
    {
        "title": "Engineering PowerPoint Templates",
        "type": "Presentation Design",
        "desc": "Designed modular technical layout templates for ECE reviews, optimizing graphic block diagrams and signal flowcharts.",
    }
]

# Academic Deliverables (Diploma)
DIPLOMA_DELIVERABLES = [
    {
        "title": "Temperature-Sensor Based Fan Cooling System",
        "type": "Diploma Final Project & Demo",
        "desc": "Designed and demonstrated a thermistor-driven automatic cooling circuit prototype to the diploma project review panel.",
    },
    {
        "title": "Industrial Visit & Event Coordination Reports",
        "type": "Leadership Briefings",
        "desc": "Authored and presented comprehensive scheduling, budgeting, and execution reports as the appointed IV Coordinator at Sankara Polytechnic.",
    },
    {
        "title": "Student Committee & Anti-Ragging Policies",
        "type": "Committee Coordination",
        "desc": "Coordinated campus safety briefings and student welfare initiatives as an active student representative.",
    }
]

# Hands-on Industry Internships
INTERNSHIPS = [
    {
        "role": "Student Intern (CNS)",
        "company": "Coimbatore International Airport (Airports Authority of India)",
        "duration": "June 2026 (10 Days)",
        "desc": "Observed and analyzed Communication, Navigation, and Surveillance (CNS) hardware infrastructure and Air Traffic Control (ATC) operational systems.",
        "achievements": "<strong>Company & Industry News:</strong> Coimbatore International Airport is in the final stages of a major expansion, including land acquisition to modernize cargo links and CNS automation systems.",
        "icon": "✈️",
        "image": "airport.jpg"
    },
    {
        "role": "Production Engineer Intern",
        "company": "Vasantha Advanced Systems Pvt Ltd",
        "duration": "May–June 2026 (30 Days)",
        "desc": "Executed quality testing, multi-meter inspections, PCB assembly diagnostics, and production floor checks for high-reliability ECE systems.",
        "achievements": "<strong>Company Profile & News:</strong> Vasantha Advanced Systems is an AS9100D certified aerospace and defense electronics supplier, manufacturing high-reliability ECE modules under national 'Make in India' initiatives.",
        "icon": "🏭",
        "image": "vasantha.jpg"
    },
    {
        "role": "Production Engineer Intern",
        "company": "Brigade LED Pvt Ltd",
        "duration": "May–June 2025 (30 Days)",
        "desc": "Assisted in production assembly line management, LED commercial lighting system checks, and circuit integrity assurance.",
        "achievements": "<strong>Company Milestone:</strong> Brigade LED is a leading regional manufacturer fulfilling large smart city energy-efficient streetlighting contracts and green-energy lighting transformations.",
        "icon": "💡",
        "image": "brigade.jpg"
    },
    {
        "role": "Diploma Intern",
        "company": "Brigade LED Pvt Ltd",
        "duration": "May–June 2023 (30 Days)",
        "desc": "Conducted hand-soldering, LED driver circuit board debugging, and quality inspection during Diploma studies at Sankara Polytechnic.",
        "achievements": "<strong>Company Details:</strong> Brigade LED manufactures specialized optoelectronics and commercial driver boards, maintaining rigorous factory quality control protocols.",
        "icon": "🔌"
    }
]

# Creativity level of Hulk AI (0.0 to 2.0. Higher means more creative, expressive, and engaging)
AI_TEMPERATURE = 0.95
