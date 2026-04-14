import streamlit as st
import os

st.set_page_config(
    page_title="Johnsil's Portfolio",
    page_icon="🚀",
    layout="wide"
)

st.title("🌟 Welcome to My Professional Portfolio")
st.divider()

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("## Hi! I'm Johnsil T. Cañares.")
    st.write("""
    I am an **Computer Science** student and aspiring developer who builds 
    digital solutions that bridge the gap between complex problems and user-friendly designs. 
    """)
    
    with st.container(border=True):
        st.markdown("#### 🚀 Current Status")
        st.write("Seeking opportunities as a **Full Stack Developer** to create impactful software.")
    
    st.markdown("### 👈 Navigation")
    st.info("Use the sidebar to explore my journey, technical skills, and latest projects.")

with col2:
    image_path = "image/image.jpg"
    
    if os.path.exists(image_path):
        st.image(image_path, caption="Johnsil T. Cañares | Aspiring Developer", use_container_width=True)
    else:
        st.warning("⚠️ Profile image not found.")
        st.caption(f"Check if '{image_path}' exists in your project folder.")
        st.image("https://via.placeholder.com/500x500.png?text=Developer+Profile", use_container_width=True)
st.divider()
st.success("Feel free to explore and reach out via the **Contact** page!")