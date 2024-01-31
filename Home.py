import streamlit as st
import base64

# Set page title and icon
st.set_page_config(
    page_title="Welcome to Our Language Translator",
    page_icon="🌐",
)

# Create a centered header with a welcoming message
st.title("Welcome to the Global Translator!")

st.subheader("Your Gateway to Communicating Across Languages")

# Adding a GIF for welcome
file_ = open("vedo.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" width="500" height="250">',
    unsafe_allow_html=True,
)

# Providing a brief overview of the site's functionalities
st.write("""
**Explore the world of languages with our easy-to-use translator!**

Here's what you can do:

## Core Functionalities

- **Choose from a variety of languages:** We support a wide range of languages to meet your translation needs.
- **Translation Methods:** Deep Translator library in Python.
- **Translate text:** Accurately translate between multiple languages with a simple click.
- **Translation Quality:** Relies on Deep Translator's capabilities

## Additional Features
- **Document Translation:** Supports PDF, TXT, and DOC file uploads for translation
- **Language Detection:** Automatically identifies the language of input text
- **Detect languages:** Automatically identify the language of any text you provide.
- **Enjoy a seamless experience:** Our user-friendly interface makes translation effortless.
- **Translation Download:** After translating your file, you can download your translation as a text file.

## Limitations
- **File Size:** Although this web app supports PDf, DOC and TXT file types, the sizes of the files will affect the 
speed of upload and reading (If it ever loads completely), the size of the file also affects the translation, the max 
accepted characters for now is 5,000 characters.
- **Accuracy:** The accuracy of the language detection aspect of this web app is not high, there are certain languages
that still can't be detected
 

Ready to start translating? Head over to the **Translation** page to get started!
""")

st.warning("**THIS WEB APP IS STILL UNDERGOING CONTINUOUS DEVELOPMENT!!**")

