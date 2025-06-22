from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text.
    
    Returns:
        Polarity score (float): -1 (negative) to 1 (positive)
        Sentiment category (str): 'Positive', 'Neutral', or 'Negative'
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = 'Positive'
    elif polarity < -0.1:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return polarity, sentiment

if __name__ == "__main__":
    text = input("Enter text to analyze sentiment: ")
    polarity, sentiment = analyze_sentiment(text)
    print(f"Sentiment Polarity: {polarity:.2f}")
    print(f"Overall Sentiment: {sentiment}")
