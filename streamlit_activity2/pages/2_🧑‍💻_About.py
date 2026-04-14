import streamlit as st

st.set_page_config(page_title="About | Johnsil's Portfolio", page_icon="🧑‍💻", layout="wide")

st.title("🧑‍💻 About Me")

col_intro, col_img = st.columns([2, 1], gap="large")

with col_intro:
    st.markdown("### My Story")
    st.write("""
    I am a passionate developer who enjoys creating systems that solve real-world problems. 
    I focus on turning complex technical requirements into simple, intuitive, and 
    user-friendly designs that provide real value to end-users.
    """)
    
    st.markdown("#### 💡 Work Philosophy")
    st.info("""
    "I believe that clean code and thoughtful design are the foundations of 
    impactful technology. My goal is to bridge the gap between human needs 
    and digital solutions."
    """)

with col_img:
    with st.container(border=True):
        st.markdown("**Role:** Aspiring Full Stack Developer")
        st.markdown("**Focus:** System Logic & UI/UX")
        st.markdown("**Location:** Poblacion, Batuan, Masbate")

st.divider()

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.subheader("🎓 Education & Training")
    st.markdown("""
    * **BS Computer Science**
    * **Specialized Training:** Web Development
    * **Design Focus:** UI/UX Design & Prototyping
    """)

with col2:
    st.subheader("🎯 Career Goals")
    st.markdown("""
    * **Mastery:** Full Stack Development
    * **Impact:** Build impactful tech solutions
    * **Community:** Contribute to Open Source projects
    """)

st.divider()

st.caption("“The best way to predict the future is to invent it.”")