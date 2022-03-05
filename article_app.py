from this import d
from flask import Flask, request, jsonify
import csv
from demographic import something
from content import getRecommendations
import itertools

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
    movieData = {
        'title': all_articles[12]
    }
    return jsonify({
        "data": movieData,
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

@app.route('/recommended-articles')

def recommended_articles():
    all_recommended = []

    for liked_article in liked_articles:
        output = getRecommendations(liked_article[12])

        for data in output:
            all_recommended.append(data)
    
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended, _ in itertools.groupby(all_recommended))

    article_data = []

    for recommended in all_recommended:
        a = {
            'title': recommended[12]
        }

        article_data.append(a)
    
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if __name__ == '__main__':
    app.run(debug = True)