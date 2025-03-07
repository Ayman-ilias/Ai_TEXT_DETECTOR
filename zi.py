import streamlit as st
import string, pickle

st.title("🧠 AI Text Detector")
st.subheader("Developed by Ayman")

input_text = st.text_area("✍️ Enter your text below:", height=200)

contractions = {
    "ain't": "am not", "aren't": "are not", "can't": "cannot",
    "could've": "could have", "couldn't": "could not", "didn't": "did not",
    "doesn't": "does not", "don't": "do not", "hadn't": "had not",
    "hasn't": "has not", "haven't": "have not", "he'd": "he had",
    "he'll": "he will", "he's": "he is", "how'd": "how did",
    "how'll": "how will", "how's": "how is", "I'd": "I had",
    "I'll": "I will", "I'm": "I am", "I've": "I have",
    "isn't": "is not", "it'd": "it had", "it'll": "it will",
    "it's": "it is", "let's": "let us", "ma'am": "madam",
    "mightn't": "might not", "might've": "might have",
    "mustn't": "must not", "must've": "must have", "needn't": "need not",
    "shan't": "shall not", "she'd": "she had", "she'll": "she will",
    "she's": "she is", "should've": "should have", "shouldn't": "should not",
    "that'd": "that had", "that's": "that is", "there'd": "there had",
    "there's": "there is", "they'd": "they had", "they'll": "they will",
    "they're": "they are", "they've": "they have", "wasn't": "was not",
    "we'd": "we had", "we'll": "we will", "we're": "we are",
    "we've": "we have", "weren't": "were not", "what'll": "what will",
    "what're": "what are", "what's": "what is", "what've": "what have",
    "where's": "where is", "who'd": "who had", "who'll": "who will",
    "who're": "who are", "who's": "who is", "who've": "who have",
    "won't": "will not", "would've": "would have", "wouldn't": "would not",
    "you'd": "you had", "you'll": "you will", "you're": "you are",
    "you've": "you have"
}

def clean_text(text):
    text = text.lower()

    # Remove specified tags
    tags=['\n','\'']
    for tag in tags:
        text=text.replace(tag,'')

    # Remove punctuation
    text=''.join([char for char in text if char not in string.punctuation])

    # Expand contractions
    for contraction, expanded in contractions.items():
        text=text.replace(contraction,expanded)

    return text

if st.button("Detect"):
    if input_text.strip() != "":
        cleaned_input = clean_text(input_text)

        clf_svm = pickle.load(open('clf.pkl', 'rb'))
        tfidf = pickle.load(open('tfidf.pkl', 'rb'))

        text_vector = tfidf.transform([cleaned_input])
        prediction = clf_svm.predict(text_vector)

        if prediction[0] == 1:
            st.markdown("<h3 style='color:red;'><b>This text appears to be AI-generated.</b></h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='color:green;'><b>This text appears to be human-written.</b></h3>", unsafe_allow_html=True)
