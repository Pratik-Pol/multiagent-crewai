from flask import Flask, render_template, request
from crew_logic import generate_content

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        topic = request.form.get("topic")

        if topic:
            result = generate_content(topic)
        else:
            result = "Please enter a topic."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)