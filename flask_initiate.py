from flask import Flask, render_template,url_for

app = Flask(__name__)

app.static_folder = 'static'
app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route("/")
def template():
    return render_template("template.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/forum")
def forum():
    return render_template("forum.html")

@app.route("/resource")
def resource():
    return render_template("resource.html")

@app.route("/resource/language")
def language():
    return render_template("language.html")

@app.route("/resource/internship")
def internship():
    return render_template("internship.html")

@app.route("/resource/opportunity")
def opportunity():
    return render_template("opportunity.html")

@app.route("/resource/language/html")
def html():
    return render_template("html.html")

@app.route("/resource/language/python")
def python():
    return render_template("python.html")

@app.route("/resource/language/java")
def java():
    return render_template("java.html")


if __name__ == "__main__":
    app.run(debug=True)