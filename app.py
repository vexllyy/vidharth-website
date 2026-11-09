from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    success = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if name and email and message:
            print("NEW MESSAGE RECEIVED")
            print("Name:", name)
            print("Email:", email)
            print("Message:", message)

            success = "Thank you! Your message has been received."

    return render_template("index.html", success=success)


if __name__ == "__main__":
    app.run(debug=True)