### This code is developed to explore the 

import base64
import streamlit as st
from PIL import Image
import urllib
import requests
import urllib.request

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)
image = Image.open('Aayat-as-shifa-6.png')
col1, col2, col3 = st.columns([0.01,1.0,0.01])
with col1:
	st.write("")
with col2:
        #st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="BGR", output_format="auto")

        st.image(image, use_column_width=1)
with col3:	
        st.write("")
#b = st.button("Paracc")
def displayPDF(file):
    # Opening file from file path. this is used to open the file from a website rather than local
    with urllib.request.urlopen(file) as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="950" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

def show_pdf(file_path):
    with open(file_path,"rb") as f:
          base64_pdf = base64.b64encode(f.read()).decode('utf-8')
          pdf_display = F'<embed src="https://drive.google.com/viewerng/viewer?embedded=true&url=http://example.com/the.pdf" width="500" height="375">'

    #pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    st.markdown(pdf_display, unsafe_allow_html=True)
st.sidebar.header("Please Select the Chapter:")
with st.sidebar:
     p1 = st.checkbox('Para1')
     p2 = st.checkbox('Para2')
     #p3 = st.checkbox('Sahi-Bukhari')
     #p4 = st.checkbox('Fazaile-Amal')
if p1:
    displayPDF("Para1.pdf")
    #show_pdf("Para1.pdf")
if p2:
    show_pdf("Para2.pdf")
#if p4:
 #   show_pdf("Fazail.pdf") 
#if p3:
 #   show_pdf('MukhtasarSahiBukhariInHindiLanguageVolume-1www.momeen.blogspot.com.pdf')   

#with st.sidebar:
    
 #   p1=st.button('Para1'),
  #  p2=st.button('Para2')
   # p2=st.button('Para3')
    #p3=st.button('Para4')

