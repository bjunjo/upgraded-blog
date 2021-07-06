from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    get_post = requests.get('https://api.npoint.io/e42b353ee387383898c7')
    post_contents = get_post.json()
    return render_template("index.html", contents=post_contents)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def get_post(id):
    get_post = requests.get('https://api.npoint.io/e42b353ee387383898c7')
    post_contents = get_post.json()
    if post_contents[id - 1]:
        post = post_contents[id - 1]
        post_title = post['title']
        post_subtitle = post['subtitle']
        post_author = post['author']
        post_body = post['body']
        post_date = post['date']
        post_image = post['image']
    return render_template("post.html", title=post_title, subtitle=post_subtitle, author=post_author, body=post_body, date=post_date, image=post_image)

if __name__ == "__main__":
    app.run(debug=True)