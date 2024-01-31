from deep_translator import GoogleTranslator as Gt
import streamlit as st
from docx import Document
import pdfplumber


# Page configuration
st.set_page_config(
    page_title="File upload",
    page_icon="📂",
)


# Function to read document files (.doc | .docx)
def read_docs(docs_upload):
    doc = Document(docs_upload)
    text_docs = ""
    for i in doc.paragraphs:
        text_docs += i.text + "\n"
    return text_docs


# Function to read PDF files
def read_pdf(pdf_upload):
    with pdfplumber.open(pdf_upload) as pdf:
        text_pdf = " "
        for page in pdf.pages:
            text_pdf += page.extract_text()
    return text_pdf


# Function to read TXT files
def read_txt(txt_upload):
    translated_txt = ''
    for line in txt_upload.readlines():
        decode_txt = line.strip().decode() + "\n"
        translated_txt += decode_txt
    return translated_txt


# Function to translate and download translations as a text file
def translate_file():
    translated = Gt(source=lang_file, target=lang_user).translate(content_pdf)
    st.divider()
    st.header("Translated PDF")
    st.text(translated)
    if st.download_button(label="Download file", data=translated, file_name='File_translation.txt'):
        st.success("Thank you for downloading the translation")


st.header("UPLOAD FILE FOR TRANSLATION")

# A list of all the languages supported
lang_list = Gt().get_supported_languages()

# Selection boxes (File language | Preferred language)
col1, col2 = st.columns(2)

with col1:
    lang_file = st.selectbox("What language is your file written in?", lang_list,
                             index=27)
    st.write(f"Your selected translation is : **{lang_file.upper()}**")

with col2:
    lang_user = st.selectbox("Translate your file to:", lang_list,
                             index=None)
    if not lang_user:
        pass
    else:
        st.write(f"Your selected translation is : **{lang_user.upper()}**")

# File type
file_opt = st.selectbox("What is your file type?", ['.pdf', '.doc', '.docx', '.txt'],
                        index=0)
st.write(f"Your selected translation is : **{file_opt}**")

# Usage of the file uploader function
# uploaded_file = st.file_uploader("Choose a file", type="pdf")

# PDF files
if file_opt == ".pdf":
    try:
        uploaded_file = st.file_uploader("Choose a file", type="pdf")
        content_pdf = read_pdf(uploaded_file)
        st.header("Original PDF")
        st.text(content_pdf)
        # Translation takes place here
        if not lang_user:
            st.warning("Select a desired translation for your file")
        else:
            translate_file()

    except AttributeError:
        st.warning("No file uploaded")
    except Exception:
        st.warning("Please upload a .pdf file")

# docs file
elif file_opt in [".doc", ".docx"]:
    try:
        uploaded_file = st.file_uploader("Choose a file", type=['doc', 'docx'])
        contentdoc = read_docs(uploaded_file)
        st.header("Original Document")
        st.text(contentdoc)
        # Translation takes place here

        if not lang_user:
            st.warning("Select a desired translation for your file")
        else:
            translate_file()    # Translate file function defined to translate and download files.
    except AttributeError:
        st.warning("An error occurred please attempt selecting the preferred translation before the file type.")

elif file_opt == ".txt":
    try:
        uploaded_file = st.file_uploader("Choose a file", type="txt")
        contenttxt = read_txt(uploaded_file)
        st.text(contenttxt)
        # Translation takes place here

        if not lang_user:
            st.warning("Select a desired translation for your file")
        else:
            translate_file()

    except AttributeError:
        st.warning("No file uploaded")


