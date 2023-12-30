# Importing all the necessary libraries
from flask import Flask, render_template, request
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Creating an instance of the Flask web application framework
app = Flask(__name__)

# Routing the web Flask application
@app.route('/', methods=['GET', 'POST'])
def index(): 
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    # Getting the input text
    text_1 = request.form['review_text_1']
    text_2 = request.form['review_text_2']

    # Getting sentence embedding for both the text
    embeddings = model.encode([text_1, text_2])

    # Calculating the sementic similarity between two sentence
    predict = cosine_similarity(embeddings[0].reshape(1, -1), embeddings[1].reshape(1, -1))[0][0]

    # If cosine similarity is negative it's highlt dissimilar, so making predict value 0 
    if predict < 0:
        predict = 0
    
    return render_template("index.html", prediction = predict)

if __name__ == '__main__':
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2') # Loading Sentence Embedding model
    app.run(host="0.0.0.0", port="8080")