import streamlit as st
from PIL import Image


def write():

    st.title("Graphext models")
    st.header("""**Description**: """)
    st.markdown(
            """ 
Graphext is an app used to build data science project fast, collaboratively and without coding. It gives us the comprehensive views with descripsive models, graphs, and insights.
If you would like to try the app by yourself, you can easily do so by
uploading your datasets which you can find [here](https://www.graphext.com/).\n
So without wasting any time, \n
            """
        )
        

    #Make the plots
    st.header("**Insights** :chart:")
    st.markdown("### We take some insights from Graphext and let have a look if these predictions meaningful?")

    #Graphs
    st.write("Clusters")
    st.image("cluster_target.png")

    st.write("Graph colored by errors")
    st.image("Graph colored by error.png")

    st.write("Comparison")
    st.image("Comparasion_Everything.png")

    st.write("Prediction")
    st.image("Prediction.png")

    st.write("How do you think about these insights?")
    
write()