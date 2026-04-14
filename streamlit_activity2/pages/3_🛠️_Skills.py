import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Skills | Johnsil's Portfolio", page_icon="🛠️", layout="wide")

root_path = Path(__file__).parent.parent

st.title("🛠️ Technical Toolkit")

st.subheader("Programming Proficiency")
skills = {
    "Python": 85, "HTML/CSS": 80, "Data Analytics": 80, "PHP": 75, 
    "JavaScript": 70, "C++": 70, "SQL": 65, "Java": 60
}

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
    with st.container(border=True):
        st.write("- Figma / UI Design")
        st.write("- Canva")
        st.write("- CSS Frameworks (Bootstrap/Tailwind)")

with col_d2:
    st.subheader("🔧 Tools")
    with st.container(border=True):
        st.write("- GitHub & Git Version Control")
        st.write("- VS Code")
        st.write("- Streamlit & Flask")

st.divider()

st.subheader("📜 Certifications")

certs = [
    {"title": "Agile Scrum Master", "issuer": "SimpliLearn | SkillUp", "img_name": "Agile_Scrum_Master_SkillUp.png"},
    {"title": "Advance C++ Course", "issuer": "SimpliLearn | SkillUp", "img_name": "C++_Course_Online.png"},
    {"title": "Ethical Hacking", "issuer": "SimpliLearn | SkillUp", "img_name": "Ethical_hacking.png"},
    {"title": "Full Stack Java", "issuer": "SimpliLearn | SkillUp", "img_name": "Full_Stack_Java.png"},
    {"title": "Introduction to SAFe", "issuer": "SimpliLearn | SkillUp", "img_name": "Introduction_to_SAFe.png"},
    {"title": "SQL Analytics", "issuer": "SimpliLearn | SkillUp | Databricks", "img_name": "SQL_Analytics.png"},
    {"title": "HTML Essentials", "issuer": "Cisco Networking Academy", "img_name": "html_essentials.png"},
    {"title": "CSS Essentials", "issuer": "Cisco Networking Academy", "img_name": "css_essentials.png"}
]

c1, c2 = st.columns(2)

for i, cert in enumerate(certs):
    target_col = c1 if i % 2 == 0 else c2
    
    # Construct the full path to each certificate image
    cert_path = root_path / "cert" / cert["img_name"]
    
    with target_col:
        with st.container(border=True):
            if cert_path.exists():
                st.image(str(cert_path), use_container_width=True)
            else:
                st.warning(f"Certificate image not found.")
                st.caption(f"App is looking in: `{cert_path}`")
                
            st.markdown(f"#### {cert['title']}")
            st.caption(f"🏆 Issued by: {cert['issuer']}")