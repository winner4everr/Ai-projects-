#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install nltk


# In[2]:


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(review):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(review)
    
    if sentiment_scores['compound'] >= 0.05:
        return "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Download NLTK resources
nltk.download('vader_lexicon')

# Example usage
review = "I absolutely love this product! It exceeded my expectations."
sentiment = analyze_sentiment(review)
print(f"Review sentiment: {sentiment}")


# In[3]:


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(opinion):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(opinion)
    
    if sentiment_scores['compound'] >= 0.05:
        return "positive"
    elif sentiment_scores['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"

# Download NLTK resources
nltk.download('vader_lexicon')

# Example usage
opinion = input("Enter your opinion (positive/negative): ")
sentiment = analyze_sentiment(opinion)
print(f"Sentiment analysis result: {sentiment}")


# In[ ]:




