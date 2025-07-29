app = Flask(__name__)

@app.route("/search", methods=["POST", "GET"])
def home():
    result = ""
    if request.method == "POST":
        search = request.form["search"]

        try:
            result = wikipedia.summary(search, sentences=2)
        except wikipedia.exceptions.DisambiguationError as e:
            result = f"Multiple matches found: {e.options}"
        except wikipedia.exceptions.PageError:
            result = "No page found."

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

