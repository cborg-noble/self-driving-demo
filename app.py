import streamlit as st
import pandas as pd 


def main():
    # Set the title of the web app
    st.title("NobleAI Self-Driving Demo")

    st.markdown("Welcome to NobleReactor. Here, you'll be able to accelerate your work using SBAI models to design novel materials and chemical formulations. In this demonstration, we will guide you through the process of using an SBAI model to guide the formulation of sustainable concrete.")
    st.markdown("Today, the manufacture of concrete is responsible for 8% of global carbon emissions with global demand expected to increase to 6.2bn tons by 2050. To combat global warming, your team (Sustainable Concrete LLC.), is developing a new concrete formulation that produces less CO2 while also maintaining its strength and is cost-effective to produce.")
    st.markdown("A typical concrete formulation contains seven ingredients: cement, fine aggregate, coarse aggregate, blast furnace slag, fly ash, superplasticizer, and water (with relative ratios as shown in the figure below).")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Example concrete formulation')
        st.image('concrete_formulation.png')

    with col2:
        st.subheader('Typical ingredient ranges for concrete mixtures')
        df = pd.read_csv('concrete_ingredients.csv')
        st.write(df)

    st.markdown("Your goal is to use the reactor platform to design a novel concrete formulation that meets the following targets:")

    df = pd.read_csv('targets.csv')
    st.write(df)

    st.subheader('Guiding Questions:')

    user_input = st.text_input("1. How many experiments were used to train the AI model to predict concrete strength? What is the accuracy of the model? ", None)
    user_input = st.text_area("2. Let’s identify a past experiment to compare against our model predictions. Use the table filters on the training data to find any formulations that meet the property targets outlined in table 1. How many past experiments hit these targets? Report one below to use as a benchmark. (or use the provided experiment, formulation-465)", None)
    

    col3, col4 = st.columns(2)

    with col3:
        df = pd.read_csv('run_465.csv')
        st.write(df)

    with col4:
        df = pd.read_csv('run_465_output.csv')
        st.write(df)

    user_input = st.text_area("3. Perform an inverse design, with the targets noted in table 1. Were any formulations generated that meet all the target criteria? Calculate the percent improvement in each property relative to the past experiment you found in the previous question.", None)



if __name__ == "__main__":
    main()