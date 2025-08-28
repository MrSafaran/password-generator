import streamlit as st
from password_generator import RandomPassword,PinCode,MemorablePassword

st.image("src/image/download.png", width = 600)
st.title(":lock: Password Generator")


option = st.radio(
    "Select your password generator:",
    ("Random Password", "Memorable Password", "Pin Code")
)

if option == "Pin Code" :
    length = st.slider("Select the length of Pin Code", 4, 32)

    generator = PinCode(length)

elif option == "Random Password":
    length = st.slider("Select the length of random password:", 8, 100)
    include_number = st.toggle("Include Numbers")
    include_punctuation = st.toggle("Include Punctuations")
 
    generator = RandomPassword(length, include_number,include_punctuation)

elif option == "Memorable Password" :
    length = st.slider("Select the Memorable password length: ", 8, 64)
    seprator = st.text_input("Enter a separator (e.g., '---' or '====')", "---")
    capitalized = st.toggle("Include Capitalization")

    generator = MemorablePassword(length, seprator, capitalized)


password = generator.generate()
st.write(fr"Your password is: ```{password}``` ")