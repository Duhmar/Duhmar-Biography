import streamlit as st
import base64
from datetime import date

def main():
    st.title("Write Your Biography")
    
    menu = st.sidebar.selectbox("Menu", ["Add Biography", "View Biography"])

    default_photo_path = "C:/Users/User/Desktop/biography/default photo.jpg"

    if "bio_info" not in st.session_state:
        st.session_state["bio_info"] = {}
    if "photo" not in st.session_state:
        try:
            with open(default_photo_path, "rb") as file:
                st.session_state["photo"] = base64.b64encode(file.read()).decode("utf-8")
        except FileNotFoundError:
            st.session_state["photo"] = None 

    if menu == "Add Biography":
        st.header("Information")
        
        new_photo = st.file_uploader("Choose a new photo to upload:", type=["png", "jpg", "jpeg"])
        if new_photo:
            st.session_state["photo"] = base64.b64encode(new_photo.read()).decode("utf-8")
            st.success("Photo updated successfully!")

        if st.session_state["photo"]:
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{st.session_state['photo']}" alt="Current Photo" style="width: 400px; height: auto; border-radius: 5px;">
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.warning("No photo available. Upload a photo or reset to the default photo.")

        if st.button("Reset to Default Photo"):
            try:
                with open(default_photo_path, "rb") as file:
                    st.session_state["photo"] = base64.b64encode(file.read()).decode("utf-8")
                st.success("Photo reset to default successfully!")
            except FileNotFoundError:
                st.error("Default photo not found. Please upload a new photo.")

        with st.form("bio_form"):
            st.form_submit_button()
            name = st.text_input("Name:", st.session_state["bio_info"].get("Name", "Duhmar M. Duhiling"))
            age = st.number_input(
                "Age:", 
                min_value=1, 
                max_value=120, 
                value=st.session_state["bio_info"].get("Age", 19)  
            )
            dob = st.date_input(
            "Date of Birth:",
            st.session_state["bio_info"].get("Date of Birth", date(2005, 8, 15))  
)
            email = st.text_input("Email:", st.session_state["bio_info"].get("Email", "damplovechannel@gmail.com"))
            phone = st.text_input("Phone:", st.session_state["bio_info"].get("Phone", "09953497684"))
            
            st.subheader("Bio")
            biography = st.text_area(
                "Write a biography about yourself:",
                st.session_state["bio_info"].get("Biography", "I am Duhmar M. Duhiling. I live in purok 2 Luna, San Jose Dinagat Islands. I'm a shy type of person, introvert, and hard to get along. But I like who I am because I can do whatever I want without disturbing someone.")
            )

            st.subheader("Educational Attainment")
            education = st.text_area(
                "Enter your education (one entry per line, format: Degree - Institution - Year Graduated):",
            "\n".join (st.session_state["bio_info"].get("Education", ["College : Bachelor of Science in Computer Engineering - SNSU - Ongoing"]))
            )
            
            st.subheader("Certificates and Awards")
            certificates = st.text_area(
                "Enter your certificates/awards (one entry per line, format: Title - Year):",
                "\n".join(st.session_state["bio_info"].get("Certificates", ["With Honors - Grade 1 to Grade 6", "With Honors - Grade 7 to 10", "With Honors - Grade 11 to 12", "1st Best Picture - 2024"]))
            )
            
            submitted = st.form_submit_button("Save")
            
            if submitted:
                st.session_state["bio_info"] = {
                    "Name": name,
                    "Age": age, 
                    "Date of Birth": dob,
                    "Email": email,
                    "Phone": phone,
                    "Biography": biography,
                    "Education": [line.strip() for line in education.split("\n") if line.strip()],
                    "Certificates": [line.strip() for line in certificates.split("\n") if line.strip()],
                }
                st.success("Biography information saved successfully!")

        if st.button("Clear All Information"):
            st.session_state["bio_info"] = {}
            st.success("Information cleared!")
    
    elif menu == "View Biography":
        st.header("Biography")
        
        if st.session_state["photo"]:
            st.subheader("Photo")
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{st.session_state['photo']}" alt="Current Photo" style="width: 400px; height: auto; border-radius: 5px;">
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.warning("No photo uploaded.")

        if st.session_state["bio_info"]:
            bio = st.session_state["bio_info"]
            st.write(f"**Name:** {bio.get('Name', 'N/A')}")
            st.write(f"**Age:** {bio.get('Age', 'N/A')}")
            st.write(f"**Date of Birth:** {bio.get('Date of Birth', 'N/A')}")
            st.write(f"**Email:** {bio.get('Email', 'N/A')}")
            st.write(f"**Phone:** {bio.get('Phone', 'N/A')}")
            
            st.subheader("Biography")
            st.write(bio.get("Biography", "No biography provided."))

            st.subheader("Educational Attainment")
            for edu in bio.get("Education", []):
                st.write(f"- {edu}")
            
            st.subheader("Certificates and Awards")
            for cert in bio.get("Certificates", []):
                st.write(f"- {cert}")
        else:
            st.warning("No biography information available.")

if __name__ == "__main__":
    main()
