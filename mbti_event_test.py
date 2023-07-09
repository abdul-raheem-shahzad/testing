#making streamlit app with pickle model
import streamlit as st
import pickle
# Load the dt pickled model
rf_model = pickle.load(open('rf_model.pkl', 'rb'))
st.write('ENFJ: The Giver')
st.write('ENFP: The Champion')
st.write('ENTJ: The Commander')
st.write('ENTP: The Debater')
st.write('ESFJ: The Caregiver')
st.write('ESFP: The Performer')
st.write('ESTJ: The Supervisor')
st.write('ESTP: The Entrepreneur')
st.write('INFJ: The Advocate')
st.write('INFP: The Mediator')
st.write('INTJ: The Architect')
st.write('INTP: The Logician')
st.write('ISFJ: The Defender')
st.write('ISFP: The Composer')
st.write('ISTJ: The Logistician')
st.write('ISTP: The Virtuoso')
st.write('The app also predicts the risk of pain in the future for each personality type')
st.write('Description of each parameter is given below')
st.image(["types.png"])
st.subheader('FIND YOUR TYPE')
#silder for the user to select between 0 to 25
E = st.slider('Select the level of Extroversion', 0, 25)
I = st.slider('Select the level of Introversion', 0, 25)
S = st.slider('Select the level of Sensing', 0, 25)
N = st.slider('Select the level of Intuition', 0, 25)
T = st.slider('Select the level of Thinking', 0, 25)
F = st.slider('Select the level of Feeling', 0, 25)
J = st.slider('Select the level of Judging', 0, 25)
P = st.slider('Select the level of Perceiving', 0, 25)

#use the following code to predict the output
# Predict the output
prediction = rf_model.predict([[E,I,N,S,T,F,J,P]])
# Display the prediction
# Display the prediction by pressing button
if st.button('Predict'):
    if prediction == 'ENFJ':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ENFJ')
        st.write("You have more prevelance of pain in other body part as compare to other personality type but the good news is your body is less prone to back and neck pain")
    elif prediction == 'ENFP':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ENFP')
        st.write("You have more prevelance of pain in neck part as compare to other personality type but the good news is your body is less prone to in thoracic and lumbar spine")
    elif prediction == 'ENTJ':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ENTJ')
        st.write("You have more prevelance of pain in thoracic as compare to other personality type but the good news is your body is less prone to neck pain")
    elif prediction == 'ENTP':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ENTP')
        st.write("You have more prevelance of pain in other body part and thoracic type but the good news is your body is less prone to neck pain and least in Lumbar pain")
    elif prediction == 'ESFJ':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ESFJ')
        st.write("You have more prevelance of pain in other body part and neck but the good news is your body is less prone to lumbar pain")
    elif prediction == 'ESFP':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ESFP')
        st.write("You have more prevelance of pain in thoracic but the good news is your body is less prone to lumbar pain")
    elif prediction == 'ESTJ':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ESTJ')
        st.write("You have more prevelance of pain in other body parts but the good news is your body is less prone to neck pain")
    elif prediction == 'ESTP':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ESTP')
        st.write("You have more prevelance of pain in other body parts and thoracic but the good news is your body is less prone to neck and lumbar pain")
    elif prediction == 'INFJ':
        st.write('The predicted output is: ', prediction)
        st.write('You are a INFJ')
        st.write("You are at risk at spinal cord as well as other body parts so take of your health")
    elif prediction == 'INFP':
        st.write('The predicted output is: ', prediction)
        st.write('You are a INFP')
        st.write("You are at risk at spinal cord as well as other body parts so take of your health")
    elif prediction == 'INTJ':
        st.write('The predicted output is: ', prediction)
        st.write('You are a INTJ')
        st.write("You are at risk of Thoracic and neck pain so take of your health")
    elif prediction == 'INTP':
        st.write('The predicted output is: ', prediction)
        st.write('You are a INTP')
        st.write("Sorry the dataset about this type was not avaible")
    elif prediction == 'ISFJ':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ISFJ')
        st.write("You are at risk of thoracic and neck pain but hte good news is your body is less prone to lumbar pain")
    elif prediction == 'ISFP':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ISFP')
        st.write("You are at the highest risk of thoracic pain take care of your health")
    elif prediction == 'ISTJ':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ISTJ')
        st.write("You are at the high risk of neck and thoracic pain take care of your health but the good news is your body is less prone to pain in other body parts")
    elif prediction == 'ISTP':
        st.write('The predicted output is: ', prediction)
        st.write('You are a ISTP')
        st.write("You are at the high risk of all sorts of pain take care of your self")
    
