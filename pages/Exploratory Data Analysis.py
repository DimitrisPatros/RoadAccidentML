
import streamlit as st
import streamlit.components.v1 as components

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')

st.set_page_config(
     page_title="Data visualization",
     page_icon="🧊",
     #layout="wide",
     initial_sidebar_state ="auto",
 )

st.download_button('https://dionysisk.eu/RSA/report.html', 'report.html')

components.iframe("https://dionysisk.eu/RSA/report.html",height = 700,scrolling =True,width=700)


