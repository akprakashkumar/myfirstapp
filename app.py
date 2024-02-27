"""
Ticker Tracker App

Application to track several tickers (stock)

https://github.com/aswinpkumar
v1.0.0
February 27th, 2024

Author:
    @aswinpkumar : https://github.com/aswinpkumar
"""

import streamlit as st
from pathlib import Path
import base64

# Initial page config

st.set_page_config(
     page_title='Ticker Tracker Application',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    cs_sidebar()
    cs_body()
    return None

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def cs_sidebar():

    # st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.header('Ticker Tracker App')

    st.sidebar.markdown('''
                        <small>Summary of the [docs](https://docs.streamlit.io/), as of [Streamlit v1.25.0](https://www.streamlit.io/).</small>
                        ''', unsafe_allow_html=True)

    st.sidebar.markdown('__Install and import__')

    st.sidebar.code('$ pip install streamlit')

    st.sidebar.code('''
                    # Import convention
                    >>> import streamlit as st ''')

    st.sidebar.markdown('__Add widgets to sidebar__')
    st.sidebar.code(''' 
                    # Just add it after st.sidebar:
                    >>> a = st.sidebar.radio(\'Choose:\',[1,2]) ''')

    st.sidebar.markdown('__Magic commands__')
    st.sidebar.code('''
                    '_This_ is some __Markdown__'
                    a=3
                    'dataframe:', data ''')

    st.sidebar.markdown('__Command line__')
    st.sidebar.code('''$ streamlit --help
                    $ streamlit run your_script.py
                    $ streamlit hello
                    $ streamlit config show
                    $ streamlit cache clear
                    $ streamlit docs
                    $ streamlit --version''')

    st.sidebar.markdown('<small>Learn more about [experimental features](https://docs.streamlit.io/library/advanced-features/prerelease#beta-and-experimental-features)</small>', unsafe_allow_html=True)

    st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<small>[Cheat sheet v1.25.0](https://github.com/daniellewisDL/streamlit-cheat-sheet)  | Aug 2023 | [Daniel Lewis](https://daniellewisdl.github.io/)</small>''', unsafe_allow_html=True)

    return None

def cs_body():

    col1, col2, col3 = st.columns(3)

    #######################################
    # COLUMN 1
    #######################################
    
    # Display text

    col1.subheader('Display text')
    col1.code('''
              st.text('Fixed width text')
              st.markdown('_Markdown_') # see #*
              st.caption('Balloons. Hundreds of them...')
              st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
              st.write('Most objects') # df, err, func, keras!
              st.write(['st', 'is <', 3]) # see *
              st.title('My title')st.header('My header')
              st.subheader('My sub')
              st.code('for i in range(8): foo()')# * optional kwarg unsafe_allow_html = True ''')

    # Display data

    col1.subheader('Display data')
    col1.code('''
              st.dataframe(my_dataframe)
              st.table(data.iloc[0:10])
              st.json({'foo':'bar','fu':'ba'})
              st.metric(label="Temp", value="273 K", delta="1.2 K") ''')


    # Display media

    col1.subheader('Display media')
    col1.code(''' 
              st.image('./header.png')
              st.audio(data)
              st.video(data) ''')


    #######################################
    # COLUMN 2
    #######################################

    # Display interactive widgets

    col2.subheader('Display code')
    col2.code(''' 
              st.echo()
              >>> with st.echo():
              >>>     st.write('Code will be executed and printed') ''')

    # Placeholders, help, and options


    #######################################
    # COLUMN 3
    #######################################


    # Connect to data sources
    
    col3.subheader('Connect to data sources')

    col3.code(''' 
              st.experimental_connection('pets_db', type='sql')
              conn = st.experimental_connection('sql')
              conn = st.experimental_connection('snowpark')
              >>> class MyConnection(ExperimentalBaseConnection[myconn.MyConnection]):
              >>>    def _connect(self, **kwargs) -> MyConnection:
              >>>        return myconn.connect(**self._secrets, **kwargs)
              >>>    def query(self, query):
              >>>       return self._instance.query(query)''')

    return None


if __name__ == '__main__':
    main()

