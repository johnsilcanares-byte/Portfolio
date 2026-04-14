import streamlit as st

st.set_page_config(page_title="Skills | Johnsil's Portfolio", page_icon="🛠️", layout="wide")

st.title("🛠️ Technical Toolkit")

st.subheader("Programming Proficiency")
skills = {"Python": 85, "JavaScript": 70, "PHP": 75, "SQL": 65, "C++": 70, "Data Analytics": 80, "Java": 60, "HTML/CSS": 80}

col_p1, col_p2 = st.columns(2)
for i, (skill, level) in enumerate(skills.items()):
    target = col_p1 if i % 2 == 0 else col_p2
    with target:
        st.write(f"**{skill}**")
        st.progress(level)

st.divider()

col_d1, col_d2 = st.columns(2)
with col_d1:
    st.subheader("🎨 Design")
    st.write("- Figma / UI Design")
    st.write("- Canva")
    st.write("- CSS Frameworks (Bootstrap/Tailwind)")

with col_d2:
    st.subheader("🔧 Tools")
    st.write("- GitHub & Git Version Control")
    st.write("- VS Code")
    st.write("- Streamlit & Flask")

st.divider()

st.subheader("📜 Certifications")

certs = [
    {"title": "Agile Scrum Master", "issuer": "SimpliLearn | SkillUp", "img": "cert/Agile_Scrum_Master_SkillUp.png"},
    {"title": "Advance C++ Course", "issuer": "SimpliLearn | SkillUp", "img": "cert/C++_Course_Online.png"},
    {"title": "Ethical Hacking", "issuer": "SimpliLearn | SkillUp", "img": "cert/Ethical_hacking.png"},
    {"title": "Full Stack Java", "issuer": "SimpliLearn | SkillUp", "img": "cert/Full_Stack_Java.png"},
    {"title": "Introduction to SAFe", "issuer": "SimpliLearn | SkillUp", "img": "cert/Introduction_to_SAFe.png"},
    {"title": "SQL Analytics", "issuer": "SimpliLearn | SkillUp | Databricks", "img": "cert/SQL_Analytics.png"},
    {"title": "HTML Essentials", "issuer": "Cisco Networking Academy", "img": "cert/html_essentials.png"},
    {"title": "CSS Essentials", "issuer": "Cisco Networking Academy", "img": "cert/css_essentials.png"}
]

c1, c2 = st.columns(2)

for i, cert in enumerate(certs):
    target_col = c1 if i % 2 == 0 else c2
    
    with target_col:
        with st.container(border=True):
            try:
                st.image(cert["img"], use_container_width=True)
            except:
                st.warning(f"Image for {cert['title']} not found in /cert folder.")
                
            st.markdown(f"#### {cert['title']}")
            st.caption(f"🏆 Issued by: {cert['issuer']}")
            st.write("")