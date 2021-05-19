import streamlit as st
import base64
from PIL import Image
import webbrowser

def write():
    st.title("Our project :car:")
    st.markdown(
           """## About the project

            Run for your life is a startup tech company. Our goal is to develop a fitness software that is able to be used plug and play style into most apps and smart watches, in a Google Fit style.
One of the main ideas behind the project is to facilitate the calorie counting and make it more precise. In order to do this you will need to build a model that use the different measurements of your phone to classify the activity the athletes are taking part on accurately.
Even though the initial focus is to get it working in as smartphone for Google Fit. We would like for it to work also in less powerful devices like smart watches.

Since the software is meant to complement other apps the easier it is to attach to a fitness software the easier it would be to sell. Same applies to devices, the more devices is works on the easier it will be to sell.

            """
    )

    st.markdown(
        """## Team Huawei Watch 

We are Huaiwei Watch Team from Strive School, and AI engineering students.
        """
    )
    st.write("![Your Awsome GIF](https://media.giphy.com/media/vLOVgH5FABgt2/giphy.gif)")



#Give the details of the team
def dummy_fun():
    st.markdown("## Members:")
    if st.button('Lakshmipathi rao Devalla'):
        webbrowser.open_new_tab('https://www.linkedin.com/in/devalla-lakshmipathirao/')
    elif st.button('Olatunde Salami'):
        webbrowser.open_new_tab('https://www.linkedin.com/in/olatunde-salami/')
    elif st.button('Thanh Nguyen'):
        webbrowser.open_new_tab('https://www.linkedin.com/in/nguyenphuocxuanthanh/')
    elif st.button('Nurlan Sarkhanov'):
        webbrowser.open_new_tab('https://www.linkedin.com/in/nurlan-sarkhanov-8749a698/?originalSubdomain=deithub.com/nsarkhanov')
    elif st.button('Agathiya Raja'):
        webbrowser.open_new_tab('https://www.linkedin.com/in/agathiya-raja-62877213b/')

write()
dummy_fun()