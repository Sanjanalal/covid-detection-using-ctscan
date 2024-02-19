import streamlit as st
def main():
    st.title("COVID-19 DETECTION USING CHEST CT SCAN")
    uploaded_file=st.file_uploader("Choose an image",type=["jpg","jpeg","png","webp"])
    if uploaded_file is not None:
        st.image(uploaded_file,caption="Upload Your CTscan Image",use_column_width=True)
    button_clicked=st.button("Continue")
main()        