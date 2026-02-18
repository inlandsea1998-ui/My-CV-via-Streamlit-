import streamlit as st

# Page configuration
st.set_page_config(page_title="My CV", layout="wide")

# Title and intro
st.title("📄 My CV Website")
st.write("Welcome to my CV site! Here you can explore my certificates, diplomas, language skills, and achievements.\n Here's my github website: https://github.com/inlandsea1998-ui")

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to:", ["Home", "Diplomas", "Certificates", "Language Skills"])

# Home section
if section == "Home":
    st.header("About Me")
    st.markdown("""
Psychology graduate with a solid foundation in research and statistical analysis, currently completing a second bachelor’s degree in Artificial Intelligence.  
Combining human-centered insight with technical expertise in machine learning to pursue a career in IT and AI-driven solutions.  


**Experience: soft skills + organizational skills (project management, communication, data handling)**  
- **International Trade Coordination**: Managed documentation, supplier communication, and logistics with global partners, demonstrating precision, negotiation, and cross-cultural communication skills.  
- **Pharmacy Operations Management**: Oversaw inventory systems, supported prescription processing, and multitasked in high-pressure environments, building organizational and analytical skills.  
- **Medical Translation & Coordination**: Facilitated communication between patients, medical staff, and insurance providers, showcasing problem-solving, documentation accuracy, and professional English fluency.  
- **Team & Client Management in Psychology Services**: Coordinated schedules for 40+ specialists, matched clients to appropriate services, and ensured smooth operations, proving leadership, data organization, and client-focused service delivery.  
""")

# Certificates section
elif section == "Certificates":
    st.header("🏅 Certificates")
    cert_choice = st.sidebar.selectbox(
        "Choose a certificate:",
        ["무역실무", "Driver's License", "컴퓨터 활용능력"]
    )

    if cert_choice == "컴퓨터 활용능력":
        st.subheader("Spreadsheet & Presentation Practical Certificate (Level 2) – Korea Human Resource Development Institute")
        st.markdown("""
This certification verifies proficiency in spreadsheet applications, including data entry, formatting, formula usage, and practical business functions. 
It demonstrates the ability to manage and analyze data effectively, create structured reports, and apply spreadsheet tools to real-world tasks.
Holders of this certificate are recognized for their competence in computer-based office work, showcasing skills essential for data-driven environments and organizational efficiency
""")
        st.image(["my_cv/스프레드시트실무2급.png", "my_cv/프레젠테이션실무2급.png"])

    elif cert_choice == "Driver's License":
        st.subheader("Valid Driver's License")
        st.write("""
Owns a car and experienced in safe, independent driving  
Flexible mobility for business travel and commuting
""")
        st.image("my_cv/운전면허.png")

    elif cert_choice == "무역실무":
        st.subheader("Trade English Certificate (Level 1) – Korea Chamber of Commerce and Industry")
        st.markdown(""" 
This nationally accredited certification demonstrates advanced proficiency in both English and international trade practices.  
The exam evaluates three key areas:  
- English translation  
- English composition  
- Practical trade knowledge (Incoterms, contracts, trade finance, shipping documentation)  

Achieving Level 1 signifies strong command of trade-related English and the ability to accurately interpret and draft complex business documents used in global commerce.  
""")
        st.image("my_cv/무역영어.png")


# Diplomas section
elif section == "Diplomas":
    st.header("🎓 Diplomas")
    diploma_choice = st.sidebar.selectbox(
        "Choose a diploma:",
        ["인공지능", "심리학"]
    )

    if diploma_choice == "심리학":
        st.subheader("Bachelor’s Degree in Psychology (Sogang University)")
        st.markdown("""
Completed coursework in clinical, social, and cognitive psychology, with strong training in 
- research methods 
- statistical analysis
- experimental design 

Developed analytical thinking, data interpretation, and human-centered problem-solving skills.""")
        st.image(["my_cv/졸업증명서.png", "my_cv/academic_record.png"], caption=["졸업증명서", "Academic Record"])

    elif diploma_choice == "인공지능":
        st.subheader("Second Bachelor’s Degree in Artificial Intelligence (In Progress, 4th Year)")
        st.markdown("""Developing strong technical expertise through coursework in:
- Programming & Data Analysis: Python, R, Data Visualization, Software Development Practice
- Mathematics & Statistics: Probability, Linear Algebra, Optimization, Discrete Mathematics, Regression Analysis
- Core AI & Machine Learning: Artificial Intelligence Systems, Machine Learning, Vision AI, Algorithms & Data Structures
- Applied AI for Business & Research: AI & Big Data for Business, Statistical Computing, Applications of Linear Regression

Academic Performance: Cumulative GPA 3.64/4.5 (≈90/100)
This program has equipped me with a solid foundation in statistical modeling, algorithm design, and practical machine learning applications.

Combined with my background in psychology, I bring a unique perspective that integrates human-centered insights with technical AI expertise—ideal for roles in IT, data science, and machine learning.
""")
        st.image(["my_cv/재학증명서_AI전공.png", "my_cv/성적증명서_AI전공.png"])

# Language Skills section
elif section == "Language Skills":
    st.header("🌐 Language Skills")
    lang_choice = st.sidebar.selectbox(
        "Choose a language:",
        ["English", "French", "Chinese"]
    )

    if lang_choice == "English":
        st.subheader("English")
        st.write("Proficiency: Advanced (C1)")
        st.write("Certificates: TOEIC 930, OPIc IH")
        st.image(["my_cv/토익성적표.png", "my_cv/Opic_Score-1.png", "my_cv/Opic_Score-2.png"])

    elif lang_choice == "French":
        st.subheader("French")
        st.write("Proficiency: Intermediate (A2)")
        st.write("Certificates: DELF A2")
        st.image("my_cv/DELF자격증.png")


    elif lang_choice == "Chinese":
        st.subheader("Chinese")
        st.write("Proficiency: Advanced (Native)")