import streamlit as st

# Streamlit is imported so the app can be made using Python.
st.set_page_config(page_title="My Portfolio", page_icon="🙂")

# Sidebar menu to switch between pages.
page = st.sidebar.radio("Menu", ["Home", "About Me", "Projects", "Skills", "Contact"])


# =================== HOME PAGE ===================
# Using IF to show the home page when "Home" is selected.
if page == "Home":
    st.title("Welcome to my portfolio!")
    st.write("This is a simple portfolio created while learning Python.")

    # Showing an image from the internet.
    st.image(
        "https://images.unsplash.com/photo-1542831371-29b0f74f9713?q=80&w=1000&auto=format&fit=crop",
        caption="Learning, studying, and building step by step."
    )


# =================== ABOUT ME PAGE ===================
# Showing basic information about background and education.
elif page == "About Me":
    st.title("About Me")

    # Short description about current focus and interests.
    st.write("""
    I am Sayyorakhon Raimjonova
    """)

    st.subheader("Education")
    st.write("**National Louis University**")
    st.write("Bachelor of Science, Computer Science and Information Systems")
    st.write("Expected Graduation: **June 2026** – Chicago, IL")
    st.write("• GPA: **3.7/4.0**, Undergraduate Honors Program")
    st.write("• Board Member – Computer Science Club (News & Communications)")
    st.write("• Member – 3D Printing Club")


# =================== PROJECTS PAGE ===================
# Listing coursework projects with short explanations.
elif page == "Projects":
    st.title("Projects")

    st.subheader("VLAN Network Configuration Project")
    st.caption("Cisco Networking Trainee – National Louis University (June 2024)")
    st.write("""
    • Developed a small business network using Cisco Packet Tracer and a physical Cisco switch.  
    • Implemented VLANs for departmental segmentation and configured inter-VLAN routing (router-on-a-stick).  
    • Managed IP subnet assignments and confirmed network connectivity using ping and show commands.  
    • Enhanced device security by enabling SSH and establishing login authentication.
    """)

    st.subheader("User Management Bash Script Project")
    st.caption("Linux Administration Trainee – National Louis University (April 2025)")
    st.write("""
    • Created and tested an automated Bash script to perform system-wide user management tasks.  
    • Designed logic to create and validate user groups, usernames, and directories while enforcing secure permissions.  
    • Implemented conditional checks and wildcard testing to verify command success, ensuring accurate execution.  
    • Applied Linux administration concepts such as ownership, file permissions, and automation scripting.
    """)


# =================== SKILLS PAGE ===================
# Listing certifications in progress, technologies, skills, and interests.
elif page == "Skills":
    st.title("Certifications, Skills & Interests")

    st.subheader("Certifications (In Progress)")
    st.write("""
    • Cisco CCNA (Introduction to Networks)  
    • Linux Essentials Certification Path
    """)

    st.subheader("Technologies")
    st.write("""
    • Linux: OS administration, file permissions, user management, Bash scripting  
    • Cisco Packet Tracer: networking labs (VLANs, subnetting, routing)  
    • Windows  
    • GitHub  
    • MySQL  
    • Troubleshooting
    """)

    st.subheader("Skills")
    st.write("""
    • Collaboration  
    • Analytical Thinking  
    • Adaptability  
    • Time Management
    """)

    st.subheader("Interests")
    st.write("""
    • Teaching (STEM experiments)  
    • Sewing and Embroidery  
    • Yoga  
    • Kickboxing  
    • Walking
    """)


# =================== CONTACT PAGE ===================
# Simple section to show contact details.
elif page == "Contact":
    st.title("Contact")

    # These values can be updated with real contact info.
    st.write("Email: sraimjonova@my.nl.edu")
    st.write("LinkedIn: www.linkedin.com/in/sayyorakhon-raimjonova")
    st.write("Telegram: @kawkabiyy")
