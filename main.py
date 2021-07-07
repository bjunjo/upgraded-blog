from flask import Flask, render_template, request
import requests
import smtplib

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

@app.route('/contact', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']
        user_phone = request.form['phone']
        user_msg = request.form['message']

        my_email = "YOUR-EMAIL"
        password = "YOUR-EMAIL-PASSWORD"

        # Email me what the user has filled out in the form
        with smtplib.SMTP("YOUR-EMAIL-PROVIDER-SMTP. GMAIL:smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            # Write messages
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:New Message\n\nName: {user_name}\nEmail: {user_email}\nPhone: {user_phone}\nMessage: {user_msg}"
            )
        return render_template("form-entry.html")
    else:
        return contact()

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