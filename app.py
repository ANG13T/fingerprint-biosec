import streamlit as st

ft = """
<style>
a:link , a:visited{
color: #4fbaf0;
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3;
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: center;
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/> by <a style='display: inline; text-align: left;' href="https://github.com/ANG13T" target="_blank"> Angelina Tsuboi</a></p>
</div>

</div>
"""

st.image("https://github.com/ANG13T/fingerprint-biosec/blob/main/assets/biometrics_logo.png?raw=true", width=700)
st.markdown("<h3 style='text-align: center; color: #494848;'>Fingerprint Analysis Biometrics Suite for Forensics</h3>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🔎 Pattern Recognition", "💾 Database Search", "🧪 Comparison Score", "📈 Image Enhancement"])

with tab1:
   st.header("Pattern Recognition")
   with st.expander("See explanation"):
      st.write("Testing text for this explaination.")

with tab2:
   st.header("Database Search")
   with st.expander("See explanation"):
      st.write("Testing text for this explaination.")

with tab3:
   st.header("Comparison Score")
   with st.expander("See explanation"):
      st.write("Testing text for this explaination.")

with tab4:
   st.header("Image Enhancement")
   with st.expander("See explanation"):
      st.write("Testing text for this explaination.")

st.write(ft, unsafe_allow_html=True)