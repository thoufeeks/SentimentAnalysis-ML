from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

texts = ["I love this!", "I hate this!", "Fantastic!", "Terrible!", "Very good", "Awful"]
labels = [1, 0, 1, 0, 1, 0]

vec = CountVectorizer()
X = vec.fit_transform(texts)

clf = MultinomialNB()
clf.fit(X, labels)

joblib.dump((vec, clf), "model.pkl")
print("✅ Model trained and saved as model.pkl")
