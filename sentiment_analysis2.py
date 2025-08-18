import matplotlib.pyplot as plt
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

df = pd.read_csv("twitter_dataset.csv")

def get_sentiment(text):
    sentiment_score = analyzer.polarity_scores(str(text))
    if sentiment_score["compound"] >= 0.05:
        return "Positive"
    elif sentiment_score["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["sentiment"].apply(get_sentiment)

print(df)

sentiment_counts = df["Sentiment"].value_counts()

plt.figure(figsize=(7,5))
sentiment_counts.plot(kind="bar", color=["green", "red", "blue"])
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.title("Sentiment Analysis using VADER on Custom Dataset")
plt.xticks(rotation=0)
plt.show()
