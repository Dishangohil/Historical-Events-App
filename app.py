from flask import Flask, render_template, request
import datetime
import os

app = Flask(__name__)

# Static sample historical events (MM-DD format)
events_data = {
    "06-10": [
        "1940 – Italy declares war on France and the United Kingdom.",
        "1967 – The Six-Day War ends.",
        "1991 – Mount Pinatubo erupts in the Philippines."
    ],
    "07-20": [
        "1969 – Apollo 11 lands on the Moon.",
        "1976 – Viking 1 lands on Mars.",
        "1944 – Failed assassination attempt on Hitler."
    ],
    "01-01": [
        "1993 – Czechoslovakia peacefully splits into the Czech Republic and Slovakia.",
        "2002 – The Euro becomes the official currency of 12 European countries."
    ],
    "12-25": [
        "800 – Charlemagne crowned Holy Roman Emperor.",
        "1991 – Mikhail Gorbachev resigns, marking the end of the Soviet Union."
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    today = datetime.date.today()
    selected_date = today.strftime("%Y-%m-%d")
    date_key = today.strftime("%m-%d")

    if request.method == "POST":
        selected_date = request.form.get("date", selected_date)
        try:
            dt = datetime.datetime.strptime(selected_date, "%Y-%m-%d")
            date_key = dt.strftime("%m-%d")
        except ValueError:
            pass

    events = events_data.get(date_key, ["Sorry, no events found for this date."])
    return render_template("index.html", events=events, selected_date=selected_date)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5006))
    app.run(host='0.0.0.0', port=port)

