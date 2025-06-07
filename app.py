from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/apartments')
def apartments():
    return render_template("apartments.html")

@app.route('/restaurant')
def restaurant():
    return render_template("restaurant.html")

@app.route('/children')
def children():
    return render_template("children.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)