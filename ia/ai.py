import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib


# Charger les données CSV
data = pd.read_csv("mails_data.csv")
print(data['label'].value_counts())


# Prétraiter le texte pour le modèle
vectorizer = TfidfVectorizer(stop_words="english")
vectorizerf = TfidfVectorizer(stop_words="english")

# Appliquer le vecteur TF-IDF sur le contenu des emails
X = vectorizer.fit_transform(data['body'])
Xf = vectorizerf.fit_transform(data['from'])

# Séparer les features (X) et les labels (y)
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
Xf_train, Xf_test, yf_train, yf_test = train_test_split(Xf, y, test_size=0.2, random_state=42)
# Créer le modèle
model = LogisticRegression(class_weight='balanced', random_state=42)
modelf = LogisticRegression(class_weight='balanced', random_state=42)

# Entraîner le modèle
model.fit(X_train, y_train)
modelf.fit(Xf_train,yf_train)

# Prédire avec le modèle
y_pred = model.predict(X_test)
yf_pred = modelf.predict(Xf_test)

# Évaluer la précision du modèle
accuracy = accuracy_score(y_test, y_pred)
accuracyf = accuracy_score(yf_test, yf_pred)
print(f"Accuracy Body: {accuracy}")
print(f"Accuracy From : {accuracyf}")

data = {
    "from": "account-security-noreply@est",
    "subject": "FWD: REclamez votre Oral-B Series 9 Pro - Gratuit",
    "body": "test" 
}

new_email_body = [data["body"]]  # Mettez la chaîne dans une liste
new_email_from = [data['from']]
new_emailf_transformed = vectorizerf.transform(new_email_from)
new_email_transformed = vectorizer.transform(new_email_body)  # Transformez avec le vectorizer

# Prédire avec le modèle
res = model.predict(new_email_transformed)
resf = modelf.predict(new_emailf_transformed)
print(f"Prediction body: {res}")
print(f"Prediction from : {resf}")


# # Exporter le modèle en local
joblib.dump(model, "model.pkl")
joblib.dump(modelf,"modelf.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(vectorizerf, "vectorizerf.pkl")

