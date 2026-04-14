import streamlit as st
from pathlib import Path

# 1. Page Configuration
st.set_page_config(page_title="Projects | Johnsil's Portfolio", page_icon="📁", layout="wide")

# --- DYNAMIC PATH HANDLING ---
root_path = Path(__file__).parent.parent

st.title("📁 My Projects")
st.markdown("### Showcase of my latest development work")

projects = [
    {
        "name": "CyberSurfer CTF+",
        "desc": "A comprehensive cybersecurity training platform designed for university students to learn through hands-on, real-time competitions.",
        "image_name": "project1.png", 
        "tech": ["Web Security", "CTF Challenges", "Interactive Learning"]
    },
    {
        "name": "AR Solar System Explorer",
        "desc": "An educational tool featuring gesture control to explore planetary orbits and scientific data in an augmented reality environment.",
        "image_name": "project2.png",
        "tech": ["Python", "AR Technology", "Scientific Modeling"]
    },
    {
        "name": "Smart Attendance Monitoring System",
        "desc": "A face-recognition based system for Panique National High School to enhance classroom and event attendance security.",
        "image_name": "project3.png",
        "tech": ["Face Recognition", "Automation", "Security"]
    },
    {
        "name": "Cafe'Han Ordering Platform",
        "desc": "A clean, aesthetic web interface for a coffee shop focusing on user-centric design and a fresh ordering experience.",
        "image_name": "project4.jpg",
        "tech": ["Frontend Dev", "UI/UX Design", "E-commerce"]
    },
    {
        "name": "SmartCal",
        "desc": "A utility application providing a Binary Converter, BMI Calculator, and Unit Converter in one interface.",
        "image_name": "project5.png",
        "tech": ["Streamlit", "Python", "Mathematical Logic"]
    },
    {
        "name": "Student Attendance Tracker",
        "desc": "A management dashboard that tracks student attendance percentages and status with full administrative controls.",
        "image_name": "project6.png",
        "tech": ["Data Analytics", "Management Systems", "Dashboard Design"]
    }
]

# --- RENDER PROJECTS ---
for project in projects:
    img_path = root_path / "image" / project["image_name"]
    
    with st.container(border=True):
        col1, col2 = st.columns([1.2, 1], gap="large")
        
        with col1:
            if img_path.exists():
                st.image(str(img_path), use_container_width=True)
            else:
                st.warning(f"Image for {project['name']} not found.")
                st.image("https://via.placeholder.com/600x300?text=Project+Preview", use_container_width=True)
                
        with col2:
            st.subheader(project["name"])
            st.write(project["desc"])
            
            # --- FIXED ALIGNMENT SECTION ---
            st.markdown("**Tech Stack:**")
            
            # Combine tags into a single line with professional formatting
            # This prevents the "staircase" or uneven alignment of multiple columns
            tech_tags = "".join([f" `{t}` " for t in project["tech"]])
            st.markdown(tech_tags)
            
            st.write("") # Spacer

st.divider()
st.info("💡 These projects demonstrate my proficiency in Full Stack development and Data Systems.")