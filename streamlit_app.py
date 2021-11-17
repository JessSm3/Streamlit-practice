import streamlit as st

st.title("Hackathon Pumpkin")

click = st.button("push me")
if click:
    st.balloons()

select = st.radio("classify pumpkin",["Squash","Gourd"])
st.write("You chose",select)

check = st.checkbox("Have a happy holiday",["I will"])
