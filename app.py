import streamlit as st
import pandas as pd

# data1 = pd.read_csv('ChildBloodType.csv')
# data2 = pd.read_csv('input_output_data.csv')

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Function to navigate to a different page
def navigate_to(page):
    st.session_state.page = page


# Defining the pages
def home_page():
    st.title("Blood Type Prediction and Matching")
    st.markdown("<br><br>", unsafe_allow_html=True) 
    # st.markdown(
    # """
    # <h1 style='text-align: center;'>🩸Blood Type Prediction & Matching</h1>
    # """,
    # unsafe_allow_html=True
    # )

    col1, col2, col3, col4 = st.columns(4)

    with col2:
        if st.button('Blood Type Prediction'):
            navigate_to('page1')
    with col3:
        if st.button("Find Blood Group Match"):
            navigate_to('page2')



def page1():
    st.title("Blood Type Prediction🤰")
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Father")
    col1, col2 = st.columns(2)
    with col1:
        father_blood = st.selectbox(label="Blood Type", options=["A", "B", "AB", "O"], key="blood_father")
    with col2:
        father_Rh = st.selectbox(label="Rh", options=["+", "-"], key="Rh_father")
    st.subheader("Mother")
    col1, col2 = st.columns(2)
    with col1:
        mother_blood = st.selectbox(label="Blood Type", options=["A", "B", "AB", "O"], key="blood_mother")
    with col2:
        mother_Rh = st.selectbox(label="Rh", options=["+", "-"], key="Rh_mother")
    st.markdown("<br>", unsafe_allow_html=True)

    # Create three columns
    col5, col6, col7, col8 = st.columns([1, 1, 1, 2])

    # Initialize a session state variable for button click
    if 'button_clicked' not in st.session_state:
        st.session_state['button_clicked'] = False

    
    with col7:
        if st.button('Submit'):
            st.session_state['button_clicked'] = True

    if st.session_state['button_clicked']:
            st.write("The child's blood type will be")
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown("<p style='color:red; font-weight:bold;'>Exceptions to the rules:</p>", unsafe_allow_html=True)
            st.write("There are a few ways to break the rules and end up with a child with an unexpected blood type! You can read more about the rule-breaking exceptions here:")
            st.write("- [Chimerism](https://www.thetech.org/ask-a-geneticist/?categories=chimera)")
            st.write("- [Bombay blood group](https://www.thetech.org/ask-a-geneticist/?categories=bombay-blood-group)")
            st.write("- [Cis-AB blood type](https://www.thetech.org/ask-a-geneticist/?categories=cis-ab-blood-type)")
            st.write("- [Mutations](https://www.thetech.org/ask-a-geneticist/ask181)")
        
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Back"):
        navigate_to('home')
    



def page2():
    st.title("Find Blood Group Match 🩸")
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Receiver")
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox(label="Blood Type", options=["A", "B", "AB", "O"], key="blood_receiver")
    with col2:
        st.selectbox(label="Rh", options=["+", "-"], key="Rh_receiver")
    st.subheader("Donor")
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox(label="Blood Type", options=["A", "B", "AB", "O"], key="blood_donor")
    with col2:
        st.selectbox(label="Rh", options=["+", "-"], key="Rh_donor")
    st.markdown("<br>", unsafe_allow_html=True)

    # Create three columns
    col5, col6, col7, col8 = st.columns([1, 1, 1, 2])
    # Place the button in the middle column
    with col7:
        if st.button('Submit'):
            st.write("It is/is not a match.")
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Back"):
        navigate_to('home')




# Display the appropriate page based on session state
if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'page1':
    page1()
elif st.session_state.page == 'page2':
    page2()