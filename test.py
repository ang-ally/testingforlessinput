import streamlit as st

fl = st.text_input("fl")
fh = st.text_input("fh")
bw = list()
bw = float(fh) - float(fl)

st.write(bw)