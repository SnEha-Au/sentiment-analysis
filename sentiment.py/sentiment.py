import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from textblob import TextBlob

def test_audio_file(file_path):
    recognizer = sr.Recognizer()

    # Convert MP3 to WAV using pydub in memory
    audio_mp3 = AudioSegment.from_mp3(file_path)
    audio_wav = BytesIO()
    audio_mp3.export(audio_wav, format="wav")
    audio_wav.seek(0)

    # Load the WAV audio into speech recognition
    with sr.AudioFile(audio_wav) as source:
        audio = recognizer.record(source)

    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        print("Converted Text:", text)
        
        # Perform sentiment analysis using TextBlob
        sentiment = TextBlob(text).sentiment.polarity
        
        # Check if the sentence is positive, negative, or neutral
        if sentiment > 0:
            print("Sentiment: Positive")
        elif sentiment < 0:
            print("Sentiment: Negative")
        else:
            print("Sentiment: Neutral")
    
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Could not request results from service")

# Call the function using MP3 file path
test_audio_file(r"C:\Users\USER\Desktop\sentiment.py\audio.mp3")
