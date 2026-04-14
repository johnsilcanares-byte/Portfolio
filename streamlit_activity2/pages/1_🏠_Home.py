import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Home | Johnsil's Portfolio", page_icon="🏠", layout="wide")

root_path = Path(__file__).parent.parent
image_path = root_path / "image" / "image.jpg"

col1, col2 = st.columns([1.2, 1], gap="medium")

with col1:
    st.title("🚀 Welcome to My Portfolio")
    st.header("Hi, I'm Johnsil!")
    st.subheader("Aspiring Developer | Designer | Tech Enthusiast")
    st.write("""
    I am a passionate developer dedicated to leveraging technology to create 
    impactful, scalable, and accessible software solutions. 
    """)

with col2:
    if image_path.exists():
        st.image(str(image_path), use_container_width=True)
    else:
        st.warning("⚠️ Image file not found.")
        st.caption(f"Looking in: `{image_path}`")
        st.image("https://via.placeholder.com/600x400.png?text=Profile+Not+Found")

st.divider()

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### 🎯 My Mission")
    st.write("To transform complex problems into elegant, functional, and user-centric designs.")
    
with col_b:
    st.markdown("### 🎓 Quick Stats")
    st.write("📍 **Location:** Poblacion, Batuan, Masbate")
    st.write("🎓 **Degree:** BS Information Systems")

st.divider()
st.success("Simple Portfolio Multipage App using Streamlit")