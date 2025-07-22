from flask import Flask, render_template

app = Flask(__name__, static_folder="static")

# ---- single route for now ----
@app.route("/")
def index():
    return render_template("index.html", page_title="Home")

@app.route("/about/")
def about():
    return render_template(
        "about.html",
        page_title="About"
)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
