import streamlit as st
import os.path
import pathlib
from pdfquery import PDFQuery

# from src.chunking.chunk_token import start

st.write("""
# File Picker
""")
uploaded_file = st.file_uploader("Choose a PDF/CSV file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = uploaded_file.getvalue().decode('latin1').splitlines()  # .decode('utf-8').splitlines()
    st.session_state["preview"] = ''
    for i in range(0, min(5, len(data))):
        st.session_state["preview"] += data[i]
preview = st.text_area("CSV Preview", "", height=150, key="preview")
upload_state = st.text_area("Upload State", "", key="upload_state")


def upload():
    if uploaded_file is None:
        st.session_state["upload_state"] = "Upload a file first!"
    else:
        data = uploaded_file.getvalue().decode('latin1')
        parent_path = pathlib.Path(__file__).parent.parent.resolve()
        save_path = os.path.join(parent_path, "files")
        isExist = os.path.exists(save_path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(save_path)
            print("The new directory is created!")

        complete_name = os.path.join(save_path, uploaded_file.name)
        print("file to store name = ", complete_name)

        destination_file = open(complete_name, "w")
        destination_file.write(data)
        destination_file.close()
        st.session_state["upload_state"] = "Saved " + complete_name + " successfully!"

    return save_path

st.button("Upload file to Sandbox", on_click=upload)


def read_text_from_pdf(filename):
    pdf = PDFQuery(filename)
    pdf.load()

    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq('LTTextLineHorizontal').text()

    return text_elements


def is_csv_file(filename):
    return parse_extension(filename) == "csv"


def is_pdf_file(filename):
    return parse_extension(filename) == "pdf"


def parse_extension(filename):
    return filename.split(".")[1]
