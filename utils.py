import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize NLTK
nltk.download('vader_lexicon', quiet=True)

class SentimentEngine:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze(self, text):
        if not text: return 0
        scores = self.sia.polarity_scores(text)
        return scores['compound'] # Range -1 to 1