import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from PIL import Image

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Initialize PorterStemmer
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)

# Load the TF-IDF vectorizer and the model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Set page config
st.set_page_config(page_title="Spam Classifier", page_icon="🚫", layout="centered")

# Custom CSS to improve the appearance
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        caret-color: #4CAF50;
    }
    .stButton > button {
        color: #fff;
        background-color: #4CAF50;
        border-radius: 5px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Main app
st.title("📧 Email/SMS Spam Classifier")

# Add a brief description
st.write("This application uses machine learning to classify whether a given message is spam or not.")

# Create a text area for input
input_sms = st.text_area("Enter the message you want to classify:", height=100)

# Add a predict button
if st.button('Classify Message'):
    if input_sms.strip() == "":
        st.warning("Please enter a message to classify.")
    else:
        # Show a spinner while processing
        with st.spinner("Classifying..."):
            # Preprocess
            transformed_sms = transform_text(input_sms)
            # Vectorize
            vector_input = tfidf.transform([transformed_sms])
            # Predict
            result = model.predict(vector_input)[0]
        
        # Display result
        if result == 1:
            st.error("🚨 This message is classified as SPAM.")
        else:
            st.success("✅ This message is classified as NOT SPAM.")
      