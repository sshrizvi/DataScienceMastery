# <picture><source srcset="https://docs.streamlit.io/logo.svg" type="image/webp"><img src="https://docs.streamlit.io/logo.svg" width="50" height="50"></picture> Streamlit for Data Science

> [!TIP]  
> Link to Previous Article  
> 🡸 [Merging, Joining & Concatenating](./117_merging.md)

## Streamlit - A Handy Way to Build Data Science Dashboards
 
1. Streamlit is a library of Python that allows a data professional to build data apps and websites easily and in very less time, without the knowledge of core Web development.
2. Streamlit allows us to build websites all purely with Python.
3. Streamlit is built on ReactJS, which is a famous framework in the web development domain.

Let's start with the basics of Streamlit, so that we can also build data dashboards easily.

> [!NOTE]  
> Make sure to first install Streamlit on your system by running `pip install streamlit` in the command prompt.


### Text Based Utilities

1. **title**
    - It allows to add a title on a webpage.
    - **Code**

      ```python
        import streamlit as st
        st.title('_Streamlit_ is :blue[cool] :sunglasses:')
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\title.py
        ```
        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

2. **header**
    - It allows to add a heading on a webpage.
    - **Code**

      ```python
        import streamlit as st
        st.header('I am a Heading!')
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\header.py
        ```
        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

3. **subheader**
    - It allows to add a sub-heading on a webpage.
    - **Code**

      ```python
        import streamlit as st
        st.header('I am a _Sub-Heading_!')
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\subheader.py
        ```
        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

4. **markdown**
    - It allows to display rendered markdown code on a webpage.
    - **Code**

      ```python
        import streamlit as st
        st.markdown('''
        # This is Markdown Heading 1
        ## This is Markdown Heading 2

        1. Ordered List Item 1
        2. Ordered List Item 2

        - Unordered List Item 1
        - Unordered List Item 2
        ''')
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\markdown.py
        ```
        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

5. **code**
    - It allows to display a code block on a webpage.
    - **Code**

      ```python
        import streamlit as st
        st.code(
            body = '''
                a = 3
                b = 5
                c = a + b
                print(c)
            ''',
            language = 'python',
            line_numbers = True
        )
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\code.py
        ```
        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

6. **LaTex**
    - It allows to display beautifully formatted mathematical equations on a webpage.
    - **Code**

      ```python
        import streamlit as st
        st.latex(
            body = r'x^2 + y^2 = 0'
        )
        ```
    - **Output**  
        $$
        x^2 + y^2 = 0
        $$
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\latex.py
        ```
        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

### Data Based Utilities

1. **dataframe**
    - It allows to add a Pandas DataFrame on a webpage.
    - **Code**

      ```python
        import pandas as pd
        import streamlit as st

        df = pd.DataFrame(
            data = {
                'Name': ['Alice', 'Bob', 'Charlie'],
                'Age': [25, 30, 28],
                'City': ['New York', 'London', 'Paris']
            }
        )

        st.dataframe(
            data = df
        )
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\dataframe.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

2. **metric**
    - It allows to add a Metric on a webpage.
    - **Code**

      ```python
        import streamlit as st

        st.metric(
            label = "Temperature",
            value = "70 °F",
            delta = "1.2 °F"
        )
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\metric.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

3. **json**
    - It allows to add beautifully formatted JSON object on a webpage.
    - **Code**

      ```python
        import streamlit as st

        st.json(
            {
                "foo": "bar",
                "stuff": [
                    "stuff 1",
                    "stuff 2",
                    "stuff 3",
                ],
                "level1": {"level2": {"level3": {"a": "b"}}},
            }
        )
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\json.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.


### Media Elements

1. **image**
    - It allows to add a image on a webpage.
    - **Code**

      ```python
        import streamlit as st

        st.image(
            image = 'https://docs.streamlit.io/logo.svg',
            width = 300,
            caption = 'Streamlit Logo'
        )
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\image.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

2. **video**
    - It allows to add a video on a webpage.
    - **Code**

      ```python
        import streamlit as st

        st.video(
            data = 'https://youtu.be/Jv5JEZpPdzg?feature=shared'
        )
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\video.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

### Layouts & Containers

1. **sidebar**
    - It allows to add a sidebar on a webpage.
    - **Code**

      ```python
        import streamlit as st
        import time

        with st.sidebar:
            with st.echo():
                st.write("This code will be printed to the sidebar.")

            with st.spinner("Loading..."):
                time.sleep(5)
            st.success("Done!")
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\sidebar.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

2. **columns**
    - Inserts a number of multi-element containers laid out side-by-side and returns a list of container objects.
    - **Code**

      ```python
        import streamlit as st
        import numpy as np

        col1, col2 = st.columns(
            spec = [3, 1], 
            vertical_alignment = "bottom",
            gap = "medium"
        )
        data = np.random.randn(10, 1)

        col1.markdown("#### Chart")
        col1.line_chart(data)

        col2.markdown("#### Values")
        col2.write(data)
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\columns.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

### Status Elements

1. **progress**
    - Display a progress bar.
    - **Code**

      ```python
        import streamlit as st
        import time

        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()

        st.button("Rerun")
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\progress.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

2. **error**
    - Display error message.
    - **Code**

      ```python
        import streamlit as st

        st.error('This is an error', icon="🚨")
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\error.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

3. **success**
    - Display success message.
    - **Code**

      ```python
        import streamlit as st

        st.success('This is a success message!', icon="✅")
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\success.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

4. **info**
    - Display an informational message.
    - **Code**

      ```python
        import streamlit as st

        st.info('This is a purely informational message', icon="ℹ️")
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\info.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

5. **warning**
    - Display a Warning message.
    - **Code**

      ```python
        import streamlit as st

        st.warning('This is a warning', icon="⚠️")
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\warning.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

6. **balloons**
    - Draw celebratory balloons.
    - **Code**

      ```python
        import streamlit as st

        st.balloons()
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\balloons.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

7. **spinner**
    - Display a loading spinner while executing a block of code.
    - **Code**

      ```python
        import streamlit as st
        import time

        with st.spinner("Wait for it...", show_time=True):
            time.sleep(5)
        st.success("Done!")
        st.button("Rerun")
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\spinner.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.


### Input Widgets

1. **text_input**
    - Display a single-line text input widget.
    - **Code**

      ```python
        import streamlit as st

        title = st.text_input("Movie title", "Life of Brian")
        st.write("The current movie title is", title)
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\text_input.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

2. **number_input**
    - Display a numeric input widget.
    - **Code**

      ```python
        import streamlit as st

        number = st.number_input("Insert a number")
        st.write("The current number is ", number)
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\number_input.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.


3. **date_input**
    - Display a date input widget.
    - **Code**

      ```python
        import datetime
        import streamlit as st

        d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
        st.write("Your birthday is:", d)
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\date_input.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

4. **button**
    - Display a button widget..
    - **Code**

      ```python
        import streamlit as st

        st.button("Reset", type="primary")
        if st.button("Say hello"):
            st.write("Why hello there")
        else:
            st.write("Goodbye")

        if st.button("Aloha", type="tertiary"):
            st.write("Ciao")
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\button.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

5. **selectbox**
    - Display a select widget.
    - **Code**

      ```python
        import streamlit as st

        option = st.selectbox(
            "How would you like to be contacted?",
            ("Email", "Home phone", "Mobile phone"),
        )

        st.write("You selected:", option)
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\selectbox.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.

6. **file_uploader**
    - Display a file uploader widget.
    - By default, uploaded files are limited to 200 MB each. You can configure this using the server.maxUploadSize config option.
    - **Code**

      ```python
        import streamlit as st
        import pandas as pd

        uploaded_files = st.file_uploader(
            "Choose a CSV file", accept_multiple_files=True
        )
        for uploaded_file in uploaded_files:
            df = pd.read_csv(uploaded_file)
            st.write("File Name : ", uploaded_file.name)
            st.dataframe(df)
        ```
    - **Output**  
        You must have cloned this repository in your local environment. If *Yes*, then just open the *Console* and run the following command.

        ```bash
        streamlit run .\Streamlit\Code\file_uploader.py
        ```

        If *NO*, then please clone the repository first.  
        If you have exceuted the above bash command you might now be able to see a browser tab with the output.


<!-- > [!TIP]  
> Link to Next Article  
> 🡺 []() -->