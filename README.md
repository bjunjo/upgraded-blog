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

## Lessons
1. Review relative path vs absolute path: `../static/assets/img/post-bg.jpg`
2. Keep coding. Learning things one day at a time. Come back and learn. Just don't give up.
