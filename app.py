import streamlit as st


# Page title and background image
st.set_page_config(page_title='Broadrange AI - Petro Business - Gen AI', page_icon='📑')
page_bg_img = '''
<style>
body {
background-image: url("bgiot.png");
background-size: cover;
}
</style>
'''


uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])
operation_list = ['Mathematical operation']
query_text = st.selectbox('Select the type of query:', operation_list, disabled=not uploaded_file)

st.write("Success")
