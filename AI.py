import words, tts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(list(words.DATA_SET.keys()))

clf = LogisticRegression()
clf.fit(vectors, list(words.DATA_SET.values()))

del words.DATA_SET

import jsonlines

# Читаем данные из JSONL файла
with open('RCB/test.jsonl', mode='r', encoding='utf-8') as reader:
    records = list(jsonlines.Reader(reader))

# Выделяем массивы текстов и меток
texts = [record['premise'] for record in records]
labels = [record['label'] for record in records]

# Преобразуем тексты в числовую форму с помощью CountVectorizer
vectorizer = CountVectorizer()
X_vectors = vectorizer.fit_transform(texts)

# Обучаем классификатор
clf = LogisticRegression(max_iter=1000)
clf.fit(X_vectors, labels)

def recognize(data):
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:return

    data.replace(list(trg)[0], '')
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    tts.speak(answer)