#Status(study/work/unemployed) i wanna refine this to skip either one of the q if the condition is true.
import streamlit as st
import re
from datetime import datetime

st.set_page_config(page_title="Dating Form")
st.title("💘 Boyfriend / Girlfriend Dating Form")

with st.form("dating_form"):
    name = st.text_input("What is your name?")
    age = st.number_input("How old are you?", min_value=0, step=1)
    gender = st.text_input("Gender")
    height = st.number_input("What is your height (in cm)?", min_value=0, step=1)
    weight = st.number_input("What is your weight (in kg)?", min_value=0, step=1)
    ethnic = st.text_input("What is your ethnicity?")

    status = st.radio("Select your current status:", ["Student", "Working", "Unemployed"])

    fsong = st.text_input("What is your favourite song?")
    fact = st.text_input("Tell me a random fact about you")
    nickname = st.text_input("Would you be okay if I give you a cute nickname?")
    outfit = st.text_input("Do you pay attention to your outfit?")
    clingy = st.text_input("Do you mind if I'm a clingy person?")
    phone = st.text_input("Phone Number")
    ig = st.text_input("Instagram")

    submitted = st.form_submit_button("Submit")

    phone_valid = re.match(r"^(\+\d{1,3})?\d{9,15}$", phone)
    ig_valid = re.match(r"^[A-Za-z0-9._]{1,30}$", ig)

    if submitted:
        if not name or not gender or not ethnic or not fsong or not fact or not nickname or not outfit or not clingy:
            st.error("❗ All text fields must be filled out.")
        elif not phone_valid:
            st.error("❗ Enter a valid phone number (9-15 digits, may start with +).")
        elif not ig_valid:
            st.error("❗ Enter a valid Instagram handle (only letters, numbers, '.', '_').")
        else:
            st.success("✅ Your responses have been submitted!")

            st.markdown("---")
            st.subheader("📋 Summary")
            st.write({
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Height (cm)": height,
                "Weight (kg)": weight,
                "Ethnicity": ethnic,
                "Status": status,
                "Favorite Song": fsong,
                "Random Fact": fact,
                "Nickname Consent": nickname,
                "Fashion Aware": outfit,
                "Clingy OK": clingy,
                "Phone": phone,
                "Instagram": ig,
            })
