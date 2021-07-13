import streamlit as st


def navigation():
    query_params = st.experimental_get_query_params()['p'][0]
    return query_params


if navigation() == "home":
    st.title('Home')
    st.write('This is the home page.')

elif navigation() == "results":
    st.title('Results List')
    for item in range(9):
        st.write(f'Results {item}')

elif navigation() == "analysis":
    st.title('Analysis')
    x, y = st.number_input('Input X'), st.number_input('Input Y')
    st.write('Result: ' + str(x+y))

elif navigation() == "examples":
    st.title('Examples Menu')
    st.write('Select an example.')


elif navigation() == "logs":
    st.title('View all of the logs')
    st.write('Here you may view all of the logs.')


elif navigation() == "verify":
    st.title('Data verification is started...')
    st.write('Please stand by....')


elif navigation() == "config":
    st.title('Configuration of the app.')
    st.write('Here you can configure the application')