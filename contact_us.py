import streamlit as st
import base64

def app():
    st.markdown("<h4 style='font-weight: bold; font-style: italic; font-family: Optima; color: #8BE8E5'>Contact Us</h4>", unsafe_allow_html=True)

    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    
    add_bg_from_local('the2.jpeg') 

    custom_css = """
        <style>
            .st-af {
                color: black !important;
            }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    st.header(":mailbox: Get In Touch With Me!")

    contact_form = """
    <style>
        form {
            background-color: rgba(0, 0, 0, 0.9);
            padding: 20px;
            border-radius: 10px;
            text-align: center; /* Center align the form content */
        }
        .centered-button {
            display: block;
            margin: 0 auto; /* Center the button horizontally */
        }
    </style>
    <form action="https://formsubmit.co/olasehindetaiwo925@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <input type="hidden" name="_autoresponse" value="Thank you for your message, Please hold on while our team gets in contact with you :)">
        <button class="centered-button" type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

if __name__ == '__main__':
    app()

