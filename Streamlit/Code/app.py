import streamlit as st
import pandas as pd
import time

# --------------------------- TEXT BASED UTILITIES ----------------------------

st.title(
    body = 'Startup Dashboard'
)

st.header(
    body = 'I am Abbas'
)

st.subheader(
    body = 'I am loving Streamlit'
)

st.markdown(
    body = '''
            ## Numpy - An Introduction

            > **Definition**:  
            > The fundamental package for scientific computing with Python.

            ### Features of Numpy
            - **Powerful N-dimensional arrays** : Fast and versatile, the NumPy vectorization, indexing, and broadcasting concepts are the de-facto standards of array computing today.
            - **Numerical computing tools** : NumPy offers comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more.
            - **Open source** : Distributed under a liberal BSD license, NumPy is developed and maintained publicly on GitHub by a vibrant, responsive, and diverse community.
            - **Interoperable** : NumPy supports a wide range of hardware and computing platforms, and plays well with distributed, GPU, and sparse array libraries.
            - **Performant** : The core of NumPy is well-optimized C code. Enjoy the flexibility of Python with the speed of compiled code.
            - **Easy to use** : NumPy’s high level syntax makes it accessible and productive for programmers from any background or experience level.
            '''
)

st.code(
    body = '''
            import streamlit as st
            st.title(
                body = 'Startup Dashboard'
            )
            '''
)

st.latex(
    body = 'x_1 + x_2 = x_3'
)

# --------------------------- DISPLAY BASED UTILITIES ----------------------------

dict_data = {
    'IQ' : [100, 120, 140, 160, 180],
    'MARKS' : [200, 220, 240, 260, 280],
    'PACKAGE' : [60, 70, 80, 90, 100]
}

df_from_dict = pd.DataFrame(data = dict_data)

st.dataframe(
    data = df_from_dict
)

st.metric(
    label = 'Revenue',
    value = '3 Crore INR',
    delta = '3%'
)

st.json(
    {
    'IQ' : [100, 120, 140, 160, 180],
    'MARKS' : [200, 220, 240, 260, 280],
    'PACKAGE' : [60, 70, 80, 90, 100]
    }
)

# --------------------------- MEDIA UTILITIES ----------------------------

st.image(
    image = 'https://docs.streamlit.io/logo.svg',
    width = 300
)

st.video(
    data = 'https://www.youtube.com/watch?v=Jv5JEZpPdzg&list=PLTDTTold5MrYdNQxu4M8Jt69jieqLY04I'
)

# --------------------------- LAYOUT UTILITIES ----------------------------

st.sidebar.title(
    body = 'Menu'
)

col1, col2 = st.columns(
    spec = 2
)

with col1:
    st.image(
        image = 'https://docs.streamlit.io/logo.svg',
        width = 150
    )
with col2:
    st.image(
        image = 'https://docs.streamlit.io/logo.svg',
        width = 150
    )

# --------------------------- STATUS UTILITIES ----------------------------

bar = st.progress(
    value = 0,
    text = 'Progress'
)

for i in range(1, 101):
    time.sleep(0.01)
    bar.progress(
        value = i
    )

st.error(
    body = 'Login Failed'
)

st.success(
    body = 'Logged In Successfully'
)

st.info(
    body = 'This is info utility.'
)

st.warning(
    body = 'Mobile Number must have exacly 10 digits'
)

# --------------------------- USER INPUT UTILITIES ----------------------------

st.text_input(
    label = 'Enter your name'
)

st.number_input(
    label = 'Enter Mobile Number'
)

st.date_input(
    label = 'Date of Birth'
)

st.button(
    label = 'Sign In'
)

st.balloons()

with st.spinner("Wait for it...", show_time=True):
    time.sleep(5) 
st.success("Done!")
st.button("Rerun")

st.selectbox(
    label = 'Gender',
    options = [
        'Male',
        'Female',
        'Transgender'
    ]
)

st.file_uploader()