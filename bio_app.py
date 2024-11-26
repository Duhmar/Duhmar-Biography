import streamlit as st
import base64 

def main():
    st.title("Write Your Biography")
    
    menu = st.sidebar.selectbox("Menu", ["Add Biography", "View Biography"])

    default_photo_path = "C:/Users/User/Downloads/programmings.jpg"

    if "bio_info" not in st.session_state:
        st.session_state["bio_info"] = {}
    if "photo" not in st.session_state:
        with open(default_photo_path, "rb") as file:
            st.session_state["photo"] = base64.b64encode(file.read()).decode("utf-8")
    
    if menu == "Add Biography":
        st.header("Information")
        
        new_photo = st.file_uploader("Choose a new photo to upload:", type=["png", "jpg", "jpeg"])
        if new_photo:
            st.session_state["photo"] = base64.b64encode(new_photo.read()).decode("utf-8")
            st.success("Photo updated successfully!")
        
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{st.session_state['photo']}" alt="Current Photo" style="width: 400px; height: auto; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Reset to Default Photo"):
            with open(default_photo_path, "rb") as file:
                st.session_state["photo"] = base64.b64encode(file.read()).decode("utf-8")
            st.success("Photo reset to default successfully!")

        with st.form("bio_form"):
            name = st.text_input("Name:", st.session_state["bio_info"].get("Name", ""))
            
            age = st.number_input("Age:", min_value=1, max_value=120, value=st.session_state["bio_info"].get("Age"))
            
            dob = st.date_input("Date of Birth:", st.session_state["bio_info"].get("Date of Birth", None))
            email = st.text_input("Email:", st.session_state["bio_info"].get("Email", ""))
            phone = st.text_input("Phone:", st.session_state["bio_info"].get("Phone", ""))
            
            st.subheader("Bio")
            biography = st.text_area(
                "Write a biography about yourself:",
                st.session_state["bio_info"].get("Biography", "")
            )

            st.subheader("Educational Attainment")
            education = st.text_area(
                "Enter your education (one entry per line, format: Degree - Institution - Year Graduated):",
                "\n".join(st.session_state["bio_info"].get("Education", []))
            )
            
            st.subheader("Certificates and Awards")
            certificates = st.text_area(
                "Enter your certificates/awards (one entry per line, format: Title - Year):",
                "\n".join(st.session_state["bio_info"].get("Certificates", []))
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
            st.write("No photo uploaded.")

        if st.session_state["bio_info"]:
            bio = st.session_state["bio_info"]
            st.write(f"**Name:** {bio.get('Name', 'N/A')}")
            st.write(f"**Age:** {bio.get('Age', 'N/A')}")
            st.write(f"**Date of Birth:** {bio.get('Date of Birth', 'N/A')}")
            st.write(f"**Email:** {bio.get('Email', 'N/A')}")
            st.write(f"**Phone:** {bio.get('Phone', 'N/A')}")
            
            st.subheader("Biography")
            st.write(st.session_state["bio_info"].get("Biography", "No biography provided."))

            st.subheader("Educational Attainment")
            for edu in bio.get("Education", []):
                st.write(f"- {edu}")
            
            st.subheader("Certificates and Awards")
            for cert in bio.get("Certificates", []):
                st.write(f"- {cert}")
        else:
            st.write("No biography information available.")

if __name__ == "__main__":
    main()
