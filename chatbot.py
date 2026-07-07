import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
faq_questions = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What is Deep Learning?",
    "What is Python?",
    "What is NLP?"
]

faq_answers = [
    "Artificial Intelligence is the simulation of human intelligence by machines.",
    "Machine Learning is a subset of AI that enables systems to learn from data.",
    "Deep Learning is a branch of ML that uses neural networks.",
    "Python is a popular programming language used in AI and web development.",
    "NLP stands for Natural Language Processing, which helps computers understand human language."
]

vectorizer = TfidfVectorizer()

while True:
    user_input = input("\nYou: ")

    
    if user_input.lower() in ["hello", "hai", "hi"]:
        print("Bot: Hello! How can I help you today?")
        continue
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break


    texts = faq_questions + [user_input]
    tfidf_matrix = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(
        tfidf_matrix[-1],
        tfidf_matrix[:-1]
    )

    best_match = similarity.argmax()

    print("Bot:", faq_answers[best_match])