from flask import Flask, redirect, request, url_for, render_template, flash
from flask import send_from_directory
from model_sqlite3 import model

app = Flask(__name__)


# Route for the welcome page
@app.route("/")
def welcome_page():
    # Check if a success parameter is provided in the URL
    success = request.args.get("success", False)
    # Render the welcome page template with the success parameter
    return render_template("index.html", success=success)


# Route for displaying entries (quotes)
@app.route("/entries")
def entries_page():
    # Create a model instance and retrieve quotes from the database
    db = model()
    quotes = db.select()
    # Render the entries page template with the retrieved quotes
    return render_template("entries.html", quotes=quotes)


# Route for displaying the form to post a new quote
@app.route("/post")
def post_page():
    # Render the post page template
    return render_template("post.html")


# Route for processing the submitted quote form
@app.route("/process_post", methods=["POST"])
def process_post():
    # Create a model instance
    db = model()
    # Insert the submitted quote details into the database
    db.insert(
        request.form["quote"],
        request.form["attributed_person"],
        request.form["date_of_quote"],
        request.form["source_type"],
        request.form["quote_source"],
        request.form["quote_rating"],
    )
    # Redirect to the welcome page with a success parameter
    return redirect(url_for("welcome_page", success=True))


# Run the Flask app if the script is executed
if __name__ == "__main__":
    app.run(debug=True)
