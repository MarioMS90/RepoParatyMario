from flask import Flask, render_template

app = Flask(__name__)

posts = []


@app.route("/")
def index():
    return render_template("index.html", num_posts=len(posts))


@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)


@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)


numeros = [1, 2, 3, 4, 5]

user = {'id': 1, 'name': 'Mario', 'lastname': 'Muñoz', 'age': 30}

@app.route("/pruebas/")
def pruebas():
    return render_template("pruebas.html", numeros=numeros, user=user)
