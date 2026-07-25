import streamlit as st

st.set_page_config(page_title="Student Study Assistant", page_icon="📚")

st.title("📚 Student Study Assistant")
st.write("Welcome to the Student Study Assistant!")

st.header("Features")

st.write("✅ Upload Notes")
st.write("✅ Ask Questions")
st.write("✅ Summarize Notes")
st.write("✅ Generate Quiz")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")

question = st.text_input("Ask a question about your notes")

if st.button("Ask AI"):
    if question:
        st.info("AI response will appear here.")
    else:
        st.warning("Please enter a question.")
