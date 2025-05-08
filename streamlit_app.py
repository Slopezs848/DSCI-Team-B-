#creating the app 
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from PIL import Image
st.set_page_config(page_title="Autism Prediction App", page_icon=":guardsman:", layout="wide")

model_filename = 'xgboost_model.pkl'
with open(model_filename, 'rb') as file:
    lm2 = pickle.load(file)

#load feature importance
def load_feature_importance():
    try:
        importance_df = pd.read_csv('Data/feature_importance.csv')
        return importance_df
    except FileNotFoundError:
        st.error("Feature importance file not found.")
        return None
    
#sidebar 
image_sidebar = Image.open('UI_Photos/autism.jpg')
st.sidebar.image(image_sidebar, use_container_width =True)
st.sidebar.header("Autism Prediction, Please fill the form below")

#feature selection on sidebar

def get_user_input():
    st.title("Autism Prediction App")
    age = st.sidebar.number_input("Age", min_value=0, max_value=20, value=10)
    Notices_Sounds_A1 = st.sidebar.selectbox("Does He/She Notices small sounds that others do not? ", options=["no", "yes"])
    Whole_Picture_A2 = st.sidebar.selectbox("Does He/She concentrate on the whole picture than small details ?", options=["no", "yes"])
    Tracks_Conversations_A3 = st.sidebar.selectbox("Can he/she easily keep track of several peoples conversations?", options=["no", "yes"])
    Switch_Activities_A4 = st.sidebar.selectbox("Can He/She can easily switch activities ?", options=["no", "yes"])
    Conversation_Struggle_A5 = st.sidebar.selectbox("He/she doesnt know how to keep a conversation going?", options=["no", "yes"])
    Social_ChitChat_A6 = st.sidebar.selectbox("Does He/She have a good social chitchat?", options=["no", "yes"])
    Understands_Intentions_A7 = st.sidebar.selectbox("Do they find it dificult to understand the intent of characters in stories?", options=["no", "yes"])
    Pretend_Play_A8 = st.sidebar.selectbox("While they were in school they used to enjoy playing games involving pretending with other childrens?", options=["no", "yes"])
    Understands_Emotions_A9 = st.sidebar.selectbox("They find it easy to understand the emotions of characters in stories", options=["no", "yes"])  
    Makes_Friends_Easily_A10 = st.sidebar.selectbox("They find it hard to make new friends", options=["no", "yes"])
    jaundice = st.sidebar.selectbox("Did they have jaundice?", options=["no", "yes"])
    autism = st.sidebar.selectbox("Did their parents have autism?", options=["no", "yes"])
    used_app_before = st.sidebar.selectbox("Have you used the app before?", options=["no", "yes"])
    total_autism_score = sum([
    Notices_Sounds_A1 == "yes",
    Whole_Picture_A2 == "yes",
    Tracks_Conversations_A3 == "yes",
    Switch_Activities_A4 == "yes",
    Conversation_Struggle_A5 == "yes",
    Social_ChitChat_A6 == "yes",
    Understands_Intentions_A7 == "yes",
    Pretend_Play_A8 == "yes",
    Understands_Emotions_A9 == "yes",
    Makes_Friends_Easily_A10 == "yes"
    ])
    age_autism_interaction = age * total_autism_score / 2
    gender = st.sidebar.selectbox("Gender ?", options=["Male", "Female"])
    ethnicity = st.sidebar.selectbox("Ethnicity ?", options=["White", "Asian", "Black", "Hispanic","Latino",'Middle Eastern',"South Asian","Turkish","White-European","Pasifika","Others","Unknown"])
    country_options = sorted([
    "Afghanistan", "Argentina", "Armenia", "Australia", "Austria", "Bahrain", "Bangladesh", "Bhutan",
    "Brazil", "Bulgaria", "Canada", "China", "Costa Rica", "Egypt", "Europe", "Georgia", "Germany",
    "Ghana", "India", "Iraq", "Ireland", "'Isle of Man'", "Italy", "Japan", "Jordan", "Kuwait", "Latvia",
    "Lebanon", "Libya", "Malaysia", "Malta", "Mexico", "Nepal", "Netherlands", "'New Zealand'", "Nigeria",
    "Oman", "Pakistan", "Philippines", "Qatar", "Romania", "Russia", "'Saudi Arabia'", "'South Africa'",
    "'South Korea'", "Sweden", "Syria", "Turkey", "'U.S. Outlying Islands'", "'United Arab Emirates'",
    "'United Kingdom'", "'United States'"
    ])
    country_of_resi = st.sidebar.selectbox("Country of Residence", options=country_options)
    relation = st.sidebar.selectbox("Relation to the subject", options=["Parent", "Self", "Relative","self", "unknown"])
    user_data = {
        'age': age,
        'Notices_Sounds_A1': 1 if Notices_Sounds_A1=='yes' else 0,
        'Whole_Picture_A2': 1 if Whole_Picture_A2=='yes' else 0,
        'Tracks_Conversations_A3': 1 if Tracks_Conversations_A3=='yes' else 0,
        'Switch_Activities_A4': 1 if Switch_Activities_A4=='yes' else 0,
        'Conversation_Struggle_A5': 1 if Conversation_Struggle_A5=='yes' else 0,
        'Social_ChitChat_A6': 1 if Social_ChitChat_A6=='yes' else 0,
        'Understands_Intentions_A7': 1 if Understands_Intentions_A7=='yes' else 0,
        'Pretend_Play_A8': 1 if Pretend_Play_A8=='yes' else 0,
        'Understands_Emotions_A9': 1 if Understands_Emotions_A9=='yes' else 0,
        'Makes_Friends_Easily_A10': 1 if Makes_Friends_Easily_A10 =='yes' else 0,
        'jaundice': 1 if jaundice == "yes" else 0,
        'autism': 1 if autism == "yes" else 0,
        'used_app_before': 1 if used_app_before == "yes" else 0,
        'total_autism_score': total_autism_score,
        'age_autism_interaction': age_autism_interaction,
        'gender':1 if gender == "M" else 0,
        f'country_of_res_{country_of_resi}':1,
        f'ethnicity_{ethnicity}':1,
        f'relation_{relation}':1,
    }
    return user_data

#top banner
image_banner = Image.open('UI_Photos/autism_prediction.jpg')
st.image(image_banner, use_container_width =True)

st.markdown(
    "<h1 style='text-align: center;'>Autism prediction</h1>",
    unsafe_allow_html=True
)
left_column, right_column = st.columns(2)

with left_column:
    st.header("Feature Importance")
    importance_df = load_feature_importance()
    final_fi_sorted = importance_df.sort_values(by='Importance', ascending=True)
    
    fig = px.bar(
        final_fi_sorted,
        x='Feature',
        y='Importance',
        title="Feature Importance; What features do matters most?",
        labels={'Importance': 'Feature Importance Score', 'Feature': 'Variable'},
        text='Importance',  
        color_discrete_sequence=['#48a3b4']
    )
    fig.update_layout(
        xaxis_title="Feature Importance Score",
        yaxis_title="Variable",
        template="plotly_white",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

with right_column:
    st.header("Model Performance")
    user_data = get_user_input()
   
    def prepare_input(data,feature_list):
        input_data = {feature:data.get(feature,0) for feature in feature_list}
        return np.array([list(input_data.values())])
    features = [
    "Notices_Sounds_A1",
    "Whole_Picture_A2",
    "Tracks_Conversations_A3",
    "Switch_Activities_A4",
    "Conversation_Struggle_A5",
    "Social_ChitChat_A6",
    "Understands_Intentions_A7",
    "Pretend_Play_A8",
    "Understands_Emotions_A9",
    "Makes_Friends_Easily_A10",
    "age",
    "jaundice",
    "autism",
    "used_app_before",
    "total_autism_score",
    "age_autism_interaction",
    "gender",
    "ethnicity_'South Asian'",
    "ethnicity_Asian",
    "ethnicity_Black",
    "ethnicity_Hispanic",
    "ethnicity_Latino",
    "ethnicity_Others",
    "ethnicity_Pasifika",
    "ethnicity_Turkish",
    "ethnicity_White-European",
    "ethnicity_unknown",
    "country_of_res_'Isle of Man'",
    "country_of_res_'New Zealand'",
    "country_of_res_'Saudi Arabia'",
    "country_of_res_'South Africa'",
    "country_of_res_'South Korea'",
    "country_of_res_'U.S. Outlying Islands'",
    "country_of_res_'United Arab Emirates'",
    "country_of_res_'United Kingdom'",
    "country_of_res_'United States'",
    "country_of_res_Afghanistan",
    "country_of_res_Argentina",
    "country_of_res_Armenia",
    "country_of_res_Australia",
    "country_of_res_Austria",
    "country_of_res_Bahrain",
    "country_of_res_Bangladesh",
    "country_of_res_Bhutan",
    "country_of_res_Brazil",
    "country_of_res_Bulgaria",
    "country_of_res_Canada",
    "country_of_res_China",
    "country_of_res_Egypt",
    "country_of_res_Europe",
    "country_of_res_Georgia",
    "country_of_res_Germany",
    "country_of_res_Ghana",
    "country_of_res_India",
    "country_of_res_Iraq",
    "country_of_res_Ireland",
    "country_of_res_Italy",
    "country_of_res_Japan",
    "country_of_res_Jordan",
    "country_of_res_Kuwait",
    "country_of_res_Latvia",
    "country_of_res_Lebanon",
    "country_of_res_Libya",
    "country_of_res_Malaysia",
    "country_of_res_Malta",
    "country_of_res_Mexico",
    "country_of_res_Nepal",
    "country_of_res_Netherlands",
    "country_of_res_Nigeria",
    "country_of_res_Oman",
    "country_of_res_Pakistan",
    "country_of_res_Philippines",
    "country_of_res_Qatar",
    "country_of_res_Romania",
    "country_of_res_Russia",
    "country_of_res_Sweden",
    "country_of_res_Syria",
    "country_of_res_Turkey",
    "relation_Parent",
    "relation_Relative",
    "relation_Self",
    "relation_self",
    "relation_unknown"
    ]
    if st.button("Predict"):
        input_data = prepare_input(user_data, features)
        prediction = lm2.predict(input_data)
        prediction_proba = lm2.predict_proba(input_data)

        
        autism_probability = prediction_proba[0][1] * 100  

        non_autism_probability = prediction_proba[0][0] * 100

        if prediction[0] == 1:
            st.write(f"Prediction: Your responses indicate that **your child may be showing traits commonly associated with autism spectrum disorder (ASD)**.")
            st.write(f"Model Confidence: **{autism_probability:.2f}%**")
            st.info("Note: This is not a medical diagnosis, but a preliminary screening result based on patterns identified by our machine learning model. We recommend consulting a licensed healthcare professional.")
        else:
            st.write(f"Prediction: Based on your responses, **your child does not show significant traits commonly associated with autism spectrum disorder (ASD)** according to our prediction tool.")
            st.write(f"Model Confidence: **{non_autism_probability:.2f}%**")
            st.info("Note: However, if you have any concerns, we recommend consulting a healthcare professional. Every child is unique.")




