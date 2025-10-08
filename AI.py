import words, tts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(list(words.DATA_SET.keys()))

clf = LogisticRegression()
clf.fit(vectors, list(words.DATA_SET.values()))

del words.DATA_SET

def recognize(data):
    trg = words.TRIGGERS.intersection(data.split())
    stp = words.STOP_TRIGGERS.intersection(data.split())
    if not trg:return

    data.replace(list(trg)[0], '')
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    return answer