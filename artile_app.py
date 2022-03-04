from flask import Flask, request, jsonify
import csv

from itsdangerous import json

all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
disliked_articles = []
unread_articles = []

app = Flask('__name__')

@app.route('/get-article')

def get_article():
    return jsonify({
        "data": all_articles,
        "status": "success"
    })

# liked articles
@app.route('/liked-article', methods = ['POST'])

def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]

    liked_articles.append(article)

    return jsonify({
        "status": "success"
    }), 201

# disliked articles
@app.route('/disliked-article', methods = ['POST'])

def disliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]

    disliked_articles.append(article)

    return jsonify({
        "status": "success"
    }), 201

# unread articles
@app.route('/unread-article', methods = ['POST'])

def unread_article():
    article = all_articles[0]
    all_articles = all_articles[1:]

    unread_articles.append(article)

    return jsonify({
        "status": "success"
    }), 201

if __name__ == '__main__':
    app.run(debug = True)