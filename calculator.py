import streamlit as st

st.title("Simple Calculator")    #It is used for the heading
st.subheader("All operations are there")   #It is used for the subheading
st.markdown("This is s simple calculator app using Streamlit.")   #It is used for the main content

c1,c2 = st.columns(2)
fnum= c1.number_input("First Number",value=0)     #It is used to for the input field
snum= c2.number_input("Second Number",value = 0)

options = ["Add","Substract","Multiply","Divide"]
choice= st.checkbox("Select Operation",options)       #radio Keyword is used for the select operation symbol.....you can use the other alternatives like checkbox

button = st.button("Calculate")

result= 0
if button:
    if choice == 'Add':
        result = fnum+ snum
    if choice == 'Substract':
        result= fnum-snum
    if choice == 'Multiply':
        result = fnum*snum
    if choice == 'Divide':
        result = fnum/snum
st.success(f'Result : {result}')  #success keyword is used for the green color
                                  #warning keyword is used for the yellow color
#st.balloons()
st.snow()
#streamlit run filename , if a file is saved in the root directory                                 