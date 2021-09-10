#Mini Project-1
#  English language correction application -
from gingerit.gingerit import GingerIt
import streamlit as st 

st.title("English Language Correction Application-")
text = st.text_area("Enter Your Text:", value=' ', height= None, max_chars= None,key=None )
parser = GingerIt()
if st.button('Correction Your Sentence'):
    if text =='':
        st.write('Enter Your Text For Checking')
    else:
        my_result_dict = parser.parse(text)
        st.markdown('Corrected Sentence is -  ' + str(my_result_dict["result"]))
else:
     pass