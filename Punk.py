import nltk

# Check if 'punkt' is already downloaded
try:
    nltk.data.find('tokenizers/punkt')
    print("Punkt is already installed.")
except LookupError:
    print("Punkt is not installed. Downloading now...")
    nltk.download('punkt')