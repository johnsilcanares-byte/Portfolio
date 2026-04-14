import streamlit as st
import os

st.set_page_config(page_title="Home | Johnsil's Portfolio", page_icon="🏠", layout="wide")

col1, col2 = st.columns([1.2, 1], gap="medium")

with col1:
    st.title("🚀 Welcome to My Portfolio")
    st.header("Hi, I'm Johnsil!")
    st.subheader("Aspiring Developer | Designer | Tech Enthusiast")
    st.write("""
    I am a passionate developer dedicated to leveraging technology to create 
    impactful, scalable, and accessible software solutions. 
    Explore my work and technical journey through this interactive app.
    """)
    
    st.info("💡 Currently seeking opportunities to build user-friendly digital experiences.")

with col2:
    image_path = "image/image.jpg"
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.image("https://via.placeholder.com/600x400.png?text=Developer+At+Work", use_container_width=True)

st.divider()

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### 🎯 My Mission")
    st.write("To transform complex problems into elegant, functional, and user-centric designs.")
    
with col_b:
    st.markdown("### 🎓 Quick Stats")
    st.write("📍 **Location:** Poblacion, Batuan, Masbate")
    st.write("🎓 **Degree:** BS Computer Science")

st.divider()
st.success("Simple Portfolio Multipage App using Streamlit")