import sqlite3
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nlp = spacy.load("ru_core_news_sm")


#database
def get_info(user_message):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    cursor.execute("SELECT question FROM Questions")
    questions_db_tuple = cursor.fetchall()

    questions_db = [i[0] for i in questions_db_tuple]
    processed_questions = [preprocess_question(q) for q in questions_db]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(processed_questions)

    def find_best_match(user_question):
        processed_user_question = preprocess_question(user_question)
        user_tfidf = vectorizer.transform([processed_user_question])
        
        similarities = cosine_similarity(user_tfidf, tfidf_matrix)
        best_match_index = similarities.argmax()
        
        best_similarity = similarities[0][best_match_index]

        # Установите порог для определения "достаточно похожего"
        threshold = 0.5  # Настройте это значение по необходимости
        
        if best_similarity < threshold:
            return None
        return questions_db[best_match_index]
    
    question_for_answer = (find_best_match(user_message), )

    if question_for_answer is None:
        return None
    
    cursor.execute("SELECT answer FROM Questions WHERE question = ?", question_for_answer)
    answer = cursor.fetchall()

    return answer


def preprocess_question(question):
    doc = nlp(question)
    return " ".join([token.lemma_ for token in doc if not token.is_stop])