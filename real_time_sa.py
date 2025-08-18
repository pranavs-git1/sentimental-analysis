import time
import tweepy
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

nltk.download('punkt')

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAANcp0AEAAAAA9kd84MzHxgIIT1Y1%2FZ86bze0mg4%3DJ49RTwo8ufkkfPvXZ2uRYaYVMQJMN7sFTHMjgir2dB1JswU1k9"

client = tweepy.Client(bearer_token=BEARER_TOKEN)

analyzer = SentimentIntensityAnalyzer()


def get_sentiment(text):
    sentiment_score = analyzer.polarity_scores(text)
    if sentiment_score["compound"] >= 0.05:
        return "Positive"
    elif sentiment_score["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"


def fetch_tweets(keyword, max_results=10):
    attempt = 0
    while attempt < 3:
        try:
            response = client.search_recent_tweets(
                query=keyword,
                max_results=max_results,
                tweet_fields=["text", "created_at"]
            )
            if response.data:
                tweet_list = [{"Tweet": tweet.text} for tweet in response.data]
                return pd.DataFrame(tweet_list)
            else:
                print("No tweets found for the given keyword.")
                return pd.DataFrame()

        except tweepy.errors.TooManyRequests:
            attempt += 1
            wait_time = 2 ** attempt
            print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

        except tweepy.errors.Forbidden:
            print("API Access Forbidden! Upgrade your Twitter API plan.")
            return pd.DataFrame()

        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()

    print("Max retries reached. Exiting.")
    return pd.DataFrame()


keyword = input("Enter a keyword or hashtag to search for: ")

df = fetch_tweets(keyword, max_results=10)

if not df.empty:
    df["Sentiment"] = df["Tweet"].apply(get_sentiment)

    print(df)

    sentiment_counts = df["Sentiment"].value_counts()

    plt.figure(figsize=(7, 5))
    sentiment_counts.plot(kind="bar", color=["green", "red", "blue"])
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title(f"Sentiment Analysis of '{keyword}' Tweets")
    plt.xticks(rotation=0)
    plt.show()
else:
    print("No tweets found.")
