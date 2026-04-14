import streamlit as st

st.set_page_config(
    page_title="Johnsil's Portfolio",
    page_icon="🚀",
    layout="wide"
)

st.title("🌟 Welcome to My Professional Portfolio")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Hi! I'm Johnsil.
    I build digital solutions that bridge the gap between complex problems and user-friendly designs. 
    
    **👈 Use the sidebar to navigate** through my journey, skills, and projects.
    """)
    st.info("Currently seeking opportunities as a Full Stack Developer.")

with col2:
    st.image("image/image.jpg", caption="Johnsil T. Cañares | Aspiring Developer")

st.success("Feel free to explore and reach out via the Contact page!")