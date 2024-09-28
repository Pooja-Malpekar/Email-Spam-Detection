
### Email Spam Detection Web App

This project is an **Email Spam Detection** web application built using **Streamlit**. The app utilizes Natural Language Processing (NLP) techniques to classify emails as either "Spam" or "Not Spam" based on their content.

#### Key Features:
- **Text Preprocessing**: The app processes the input email text by converting it to lowercase, removing stopwords and punctuation, tokenizing words, and applying stemming.
- **Modeling**: It leverages a machine learning model trained with **TF-IDF vectorization** for feature extraction, and a classifier model (e.g., Logistic Regression or similar) to predict whether the email is spam or not.
- **Streamlit Interface**: Provides an intuitive, user-friendly web interface where users can input email text to classify.
- **Pickle Integration**: The trained model and vectorizer are loaded using Pickle for fast predictions.

#### Dependencies:
- **Streamlit**: For building the web interface.
- **NLTK**: For text preprocessing, including tokenization, stemming, and stopword removal.
- **Pickle**: For loading the pre-trained model and TF-IDF vectorizer.
- **PIL**: For handling image processing.

#### How to Run:
1. Install the required dependencies.
2. Run the Streamlit app locally with `streamlit run app.py`.
3. Enter the email text to get the spam classification.

---

Let me know if you'd like any specific changes!
