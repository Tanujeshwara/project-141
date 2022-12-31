from flask import Flask,jsonify
import csv
all_articles=[]
with open('articles.csv',encoding='utf-8') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

liked_articles=[]
not_liked_articles=[]
app=Flask(__name__)
@app.route("/get-article")
def get_article():
    return jsonify({
        'data':all_articles[0],
    })

@app.route("/liked-article",methods=["POST"])
def liked_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/disliked-article",methods=["POST"])
def dislike_article():
    article=all_articles[0]
    all_articles=all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run()