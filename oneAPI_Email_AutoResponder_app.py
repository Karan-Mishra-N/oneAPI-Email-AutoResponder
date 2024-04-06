import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import nltk
nltk.download('vader_lexicon')  # Download VADER lexicon for sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import torch

# Define model and tokenizer names (DistilBERT for sentiment analysis)
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
st.success("Model and tokenizer loaded successfully!")

import onemkl as mkl
def clean_email(text):
  text = mkl.tolower(text)  # Convert to lowercase using oneMKL
  return text

# Sentiment analysis using VADER (limited functionality)
def predict_sentiment_vader(email):
  cleaned_email = clean_email(email)
  analyzer = SentimentIntensityAnalyzer()
  sentiment_scores = analyzer.polarity_scores(cleaned_email)
  # Extract sentiment category based on highest compound score
  if sentiment_scores['compound'] >= 0.05:
    return "Positive"
  elif sentiment_scores['compound'] <= -0.05:
    return "Negative"
  else:
    return "Neutral"

# Sentiment analysis using pre-trained model (might be less accurate without fine-tuning)
def predict_sentiment_distilbert(email):
  # Tokenize the email
  tokenized_email = tokenizer(email, padding="max_length", truncation=True)

  # Get input IDs and attention mask from the tokenized email
  input_id = torch.tensor(tokenized_email["input_ids"], dtype=torch.long)  # Assuming input_ids are integers
  attention_mask = torch.tensor(tokenized_email["attention_mask"], dtype=torch.long)  # Assuming attention_mask are integers

  # Forward pass through the model
  outputs = model(input_id, attention_mask=attention_mask)
  # Get the predicted sentiment category (argmax of logits)
  predicted_sentiment = torch.argmax(outputs.logits).detach().item()

  # Define sentiment labels based on the model's output (might need adjustments)
  sentiment_labels = {0: "Negative", 1: "Neutral", 2: "Positive"}

  return sentiment_labels[predicted_sentiment]

# Define reply suggestions based on sentiment
reply_suggestions = {
  "Negative": "I'm sorry to hear about the difficulties that you faced. Is there anything I can do to help resolve this issue?",
  "Neutral": "Thank you for bringing this to my attention.I acknowledge the information you've provided.",
  "Positive": "Thank you for your email and the positive update. I appreciate you keeping me informed."
}

# Streamlit app layout
st.title("Sentiment Analysis and Reply Suggestion App")
email_content = st.text_area("Enter the email content here:", height=200)

# Sentiment analysis options
sentiment_method = st.selectbox("Choose Sentiment Analysis Method:", ["VADER", "DistilBERT"])

if st.button("Analyze Sentiment"):
  if sentiment_method == "VADER":
    predicted_sentiment = predict_sentiment_vader(email_content)
  else:
    predicted_sentiment = predict_sentiment_distilbert(email_content)
  
  st.write(f"\nPredicted Sentiment: {predicted_sentiment}")
  st.write(f"\nSuggested Reply: {reply_suggestions.get(predicted_sentiment)}")
