import streamlit as st

st.title("Hackathon Pumpkin 🎃")

click = st.button("push me")
if click:
    st.balloons()

select = st.sidebar.radio("classify pumpkin",["Squash","Gourd"])
st.sidebar.write("You chose",select)

check = st.checkbox("Have a happy holiday",["I will"])
if check:
    st.write("I will, thanks")

with st.expander("Learn more about this project"):
    st.write("This is an experimental practice project to get familiar with simple Streamlit widgets")
