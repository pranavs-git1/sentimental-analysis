# Sentiment Analysis (Backend)

A Python Data Science and analysis backend project for performing sentiment analysis on:

User-provided input text

Real-time tweets from Twitter (X)

The project uses the VADER Sentiment Analyzer to classify text into Positive, Negative, or Neutral, along with sentiment scores.

# Features

-Sentiment analysis of any custom input text

-Real-time Twitter sentiment analysis (fetches recent tweets for a given keyword)

-Sentiment scores: Positive, Negative, Neutral, Compound

-Console-based results

# Tech Stack

Language: Python 3

Libraries:

vaderSentiment (for sentiment analysis)

tweepy or snscrape (for fetching tweets)

matplotlib (optional, for visualization)


# Create virtual environment (recommended)

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux


# Install dependencies

pip install -r requirements.txt


Or install manually:

pip install vaderSentiment tweepy matplotlib

-Usage
-Analyze Custom Input Text

# Run:

python text_sa.py


Enter a sentence when prompted. 
#Example:

Enter your text: I really love Python but hate debugging.


# Output:

Positive: 0.56
Neutral: 0.23
Negative: 0.21
Compound: 0.34
Overall Sentiment: Positive 😀

# Analyze Real-Time Tweets

Run:

python real_time_sa.py


Enter a keyword (e.g., AI, Elections, Movies).
Output will show:

10 recent tweets

Sentiment score of each tweet

Summary of overall sentiment distribution

# Example Output

Keyword: Python

Tweet: "Python is amazing for AI projects!" → Sentiment: Positive 😀  
Tweet: "Debugging in Python is the worst 😠" → Sentiment: Negative 😠  

Summary:  
Positive: 6  
Neutral: 2  
Negative: 2  
Overall: Positive

# Future Improvements

Add database storage for analyzed tweets

Extend to other social media platforms

Upgrade to advanced NLP models (e.g., BERT, RoBERTa)

Add visualization for results

# Author

Developed by Pranav Swarnkar ✨

Data Scientist | IoT Enthusiast | Python Developer

# Some Outputs
<img width="700" height="500" alt="plot_2025-03-20 22-35-03_0" src="https://github.com/user-attachments/assets/5d28f84a-355f-4392-9fa1-226df5ead5d2" />
<img width="700" height="500" alt="plot_2025-03-20 01-12-52_0" src="https://github.com/user-attachments/assets/cfe30b83-1448-43ee-8617-cf2d4423f0cd" />
<img width="700" height="500" alt="myplot" src="https://github.com/user-attachments/assets/df3f4a67-8576-4a4e-bd8b-2015cc493b33" />
<img width="700" height="500" alt="#kunalkamra" src="https://github.com/user-attachments/assets/a1685a69-bbcd-4a86-a36d-dc7cb60422cd" />
<img width="700" height="500" alt="plot_2025-03-23 20-08-16_2" src="https://github.com/user-attachments/assets/ee405ff1-606a-4451-9b69-92402ea7e9e3" />
<img width="700" height="500" alt="plot_2025-03-23 20-08-16_1" src="https://github.com/user-attachments/assets/940e30d9-53aa-4b9b-99ce-bff702dc21ec" />
