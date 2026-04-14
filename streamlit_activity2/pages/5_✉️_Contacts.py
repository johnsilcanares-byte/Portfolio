import streamlit as st
import pandas as pd

st.set_page_config(page_title="Contacts | Johnsil's Portfolio", page_icon="✉️", layout="wide")

st.title("✉️ Get In Touch")
st.markdown("###### Let's collaborate on your next project!👋")

col_space1, col_form, col_space2 = st.columns([1, 12, 1])

with col_form:
    with st.container(border=True):
        st.subheader("Send me a message")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Name", placeholder="Your Full Name")
            email = st.text_input("Email", placeholder="yourname@example.com")
            message = st.text_area("Message", placeholder="Tell me about your project or inquiry...")
            
            submit = st.form_submit_button("🚀Submit Message")

        if submit:
            if name and email and message:
                st.success(f"Thank you, {name}! Your message has been sent successfully. ✅")
                st.balloons()
            else:
                st.warning("Please ensure all fields are filled before submitting.")

st.divider()

col_info, col_map = st.columns([1, 1.5], gap="large")

with col_info:
    st.markdown("### 📍 Contact Information")
    st.write("**Address:**")
    st.write("Poblacion, Batuan, Masbate, Philippines")
    
    st.write("**Phone:**")
    st.write("+63 9480829996") 
    
    st.write("**Work Hours:**")
    st.write("Monday - Friday: 9:00 AM - 6:00 PM")
    
    st.info("Available for remote work and local projects.")

with col_map:
    st.markdown("### 🗺️ Our Location")
    map_data = pd.DataFrame({
        'lat': [12.42090], 
        'lon': [123.78020]
    })
    st.map(map_data, zoom=11)

st.divider()

st.markdown("### 🌍 Let's Connect")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.link_button("📂 GitHub", "https://github.com/johnsilcanares-byte", use_container_width=True)
    st.caption("View my repositories")

with col2:
    st.link_button("📸 Instagram", "https://instagram.com/jhnsil.cnrs", use_container_width=True)
    st.caption("Follow my journey")

with col3:
    st.link_button("👥 Facebook", "https://web.facebook.com/johnsil.canares.3", use_container_width=True)
    st.caption("Message me directly")

with col4:
    st.link_button("✉️ Email", "mailto:johnsilcanares@gmail.com", use_container_width=True)
    st.caption("Send a formal inquiry")

st.divider()
st.caption("© 2026 Johnsil Cañares | Built with Streamlit")