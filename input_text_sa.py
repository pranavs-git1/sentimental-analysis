import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from PIL import Image, ImageDraw, ImageFont

nltk.download('punkt_tab', force=True)

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    sentiment_score = analyzer.polarity_scores(text)
    compound_score = sentiment_score["compound"]

    if compound_score >= 0.05:
        return "Positive", sentiment_score
    elif compound_score <= -0.05:
        return "Negative", sentiment_score
    else:
        return "Neutral", sentiment_score

def extract_positive_words(text):
    """Extracts only positive words from the sentence using VADER's lexicon."""
    words = nltk.word_tokenize(text)
    positive_words = []

    for word in words:
        if word.lower() in analyzer.lexicon and analyzer.lexicon[word.lower()] > 0:
            positive_words.append(word)

    return " ".join(positive_words) if positive_words else "Stay Positive!"

def create_positive_image(positive_text):
    """Creates an image with the extracted positive words displayed."""
    img = Image.new('RGB', (500, 300), color=(255, 255, 153))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()

    text_position = (50, 130)
    draw.text(text_position, positive_text, fill=(0, 128, 0), font=font)  # Green text

    img.show()

text = input("Enter a sentence for sentiment analysis: ")

sentiment, scores = get_sentiment(text)

print("\n🔍 Sentiment Analysis Result:")
print(f"→ Sentiment: {sentiment}")
print(f"→ Scores: {scores}")

if "Positive" in sentiment:
    positive_text = extract_positive_words(text)
    create_positive_image(positive_text)


