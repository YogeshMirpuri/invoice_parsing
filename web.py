# -*- coding: utf-8 -*-

import datetime
import streamlit as st  #Web App
import requests
import os
# import basic
import basic
import aspose.words as aw

st.title("INVOICE PARSER")

#subtitle
#st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

#st.markdown("")

#image uploader
#image = st.file_uploader(label = "Upload your image invoice here",type=['png','jpg','jpeg'])
input_file=st.file_uploader(label='UPLOAD PDF FILE HERE:',type=['pdf','doc','docx'])


if input_file is not None:
    if input_file.type == "application/pdf":
        #filename = "./temp_pdfs/"+datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '_invoice.pdf'
        with open(os.path.join("temp_pdfs", input_file.name),"wb") as f:
                f.write((input_file).getbuffer())
        pdf_file = os.path.join("./temp_pdfs/", input_file.name)
        print('------->hello')
        basic.result_data(pdf_file)
    #     with open(filename,"wb") as f:
    #         f.write(pdf.getbuffer())
    #     print(f"saving pdf in server as  {filename}")
    #     st.success("Uploaded Successfully")
    # with st.spinner("🤖 AI is at Work! "):
    #     # call the API to get the invoice data
    #     url = "http://localhost:9090/getInvoiceDataStreamlit"

    #     # send the request to the API
    #     response = requests.get(url, json={"pdfPath": filename})
    #     # get the response from the API
    #     data = response.json()

        # display the response in the web app
        st.success("Invoice Data Extracted Successfully")
        # st.write(data)
        
    #st.success("Here you go!")
    #st.balloons()
    else:
        doc = aw.Document(input_file)
        doc.save("./temp_pdfs/temp.pdf")
        # basic.result_data('./temp_pdfs/temp.pdf')
        basic.result_data('./temp_pdfs/temp.pdf')

else:
    st.write("Upload a pdf")
