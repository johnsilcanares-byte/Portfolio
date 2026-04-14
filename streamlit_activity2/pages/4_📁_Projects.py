import streamlit as st
import os

st.set_page_config(page_title="Projects | Johnsil's Portfolio", page_icon="📁", layout="wide")

st.title("📁 My Projects")
st.markdown("### Showcase of my latest development work")

projects = [
    {
        "name": "CyberSurfer CTF+",
        "desc": "A comprehensive cybersecurity training platform designed for university students to learn through hands-on, real-time competitions.",
        "image": "image/project1.png", 
        "tech": ["Web Security", "CTF Challenges", "Interactive Learning"]
    },
    {
        "name": "AR Solar System Explorer",
        "desc": "An educational tool featuring gesture control to explore planetary orbits and scientific data in an augmented reality environment.",
        "image": "image/project2.png",
        "tech": ["Python", "AR Technology", "Scientific Modeling"]
    },
    {
        "name": "Smart Attendance Monitoring System",
        "desc": "A face-recognition based system for Panique National High School to enhance classroom and event attendance security.",
        "image": "image/project3.png",
        "tech": ["Face Recognition", "Automation", "Security"]
    },
    {
        "name": "Cafe'Han Ordering Platform",
        "desc": "A clean, aesthetic web interface for a coffee shop focusing on user-centric design and a fresh ordering experience.",
        "image": "image/project4.jpg",
        "tech": ["Frontend Dev", "UI/UX Design", "E-commerce"]
    },
    {
        "name": "SmartCal",
        "desc": "A utility application providing a Binary Converter, BMI Calculator, and Unit Converter in one interface.",
        "image": "image/project5.png",
        "tech": ["Streamlit", "Python", "Mathematical Logic"]
    },
    {
        "name": "Student Attendance Tracker",
        "desc": "A management dashboard that tracks student attendance percentages and status with full administrative controls.",
        "image": "image/project6.png",
        "tech": ["Data Analytics", "Management Systems", "Dashboard Design"]
    }
]

for project in projects:
    with st.container(border=True):
        col1, col2 = st.columns([1.2, 1])
        
        with col1:
            if os.path.exists(project["image"]):
                st.image(project["image"], use_container_width=True)
            else:
                st.warning(f"Image '{project['image']}' not found. Please verify the file path.")
                st.image("https://via.placeholder.com/600x300?text=Image+Coming+Soon")
            
        with col2:
            st.subheader(project["name"])
            st.write(project["desc"])
            
            st.markdown("**Tech Stack:**")
            st.caption(" | ".join(project["tech"]))
            
            st.write("") 

st.divider()
st.info("💡 These projects utilize a variety of stacks including Python, Streamlit, and PHP.")