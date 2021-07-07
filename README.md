# upgraded-blog
## Problem: Building websites with jinja2 and Flask
## Solution

1. Showing each post
```
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
```

2. Use two different http methods for the contact form
```
@app.route('/contact', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        # Do something
```
4. Email me with the message and contact details of the user using `smtplib`
```
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
```
## Lessons
1. Review relative path vs absolute path: `../static/assets/img/post-bg.jpg`
2. Keep coding. Learning things one day at a time. Come back and learn. Just don't give up.
