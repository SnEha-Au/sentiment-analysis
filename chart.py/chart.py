import matplotlib.pyplot as plt
from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment of the given text and return sentiment polarity.
    Positive > 0, Negative < 0, Neutral = 0
    """
    sentiment = TextBlob(text).sentiment.polarity
    return sentiment

def plot_pie_chart(positive_count, negative_count, neutral_count):
    """
    Plot sentiment distribution as a pie chart.
    """
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [positive_count, negative_count, neutral_count]
    colors = ['lightgreen', 'lightcoral', 'lightskyblue']

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
    plt.title("Sentiment Analysis Distribution (Pie Chart)")
    plt.show()

# Example text samples
texts = [
    "I love this product! It's absolutely fantastic.",
    "This is the worst experience I've ever had.",
    "I feel indifferent about this service.",
    "What an amazing day! Everything went perfectly.",
    "I don't like this at all. It's terrible."
]

# Initialize sentiment counts
positive_count = 0
negative_count = 0
neutral_count = 0

# Analyze sentiment for each text sample
for text in texts:
    sentiment = analyze_sentiment(text)
    if sentiment > 0:
        positive_count += 1
    elif sentiment < 0:
        negative_count += 1
    else:
        neutral_count += 1

# Plot sentiment distribution as a pie chart
plot_pie_chart(positive_count, negative_count, neutral_count)
