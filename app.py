from flask import Flask, render_template, request

app = Flask(__name__)
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        try:
            year = int(request.form["year"])
            if is_leap_year(year):
                result = f"{year} is a leap year."
            else:
                result = f"{year} is not a leap year."
        except ValueError:
            result = "Please enter a valid year."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)