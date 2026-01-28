from flask import Flask, render_template, request, send_file
from data_loader import load_data
from analyzer import analyze_pit_stops
from plotter import plot_pit_stop_comparison
import os

app = Flask(__name__)
data = load_data()

@app.route("/", methods=["GET", "POST"])
def index():
    years = sorted(data[1]["year"].unique(), reverse=True)
    selected_year = None
    plot_path = None
    driver_list = []  # ✅ Add this line to prevent UnboundLocalError

    if request.method == "POST":
        selected_year = int(request.form["year"])
        df = analyze_pit_stops(selected_year, *data)
        plot_path, driver_list = plot_pit_stop_comparison(df, selected_year)

    return render_template("index.html", years=years, selected_year=selected_year,
                           plot_path=plot_path, driver_list=driver_list)
"""
@app.route("/", methods=["GET", "POST"])
def index():
    years = sorted(data[1]["year"].unique(), reverse=True)
    selected_year = None
    plot_path = None

    if request.method == "POST":
        selected_year = int(request.form["year"])
        df = analyze_pit_stops(selected_year, *data)
        plot_path, driver_list = plot_pit_stop_comparison(df, selected_year)

    return render_template("index.html", years=years, selected_year=selected_year, plot_path=plot_path, driver_list=driver_list)
"""
@app.route("/plot/<filename>")
def plot(filename):
    return send_file(f"plots/{filename}", mimetype="image/png")

if __name__ == "__main__":
    if not os.path.exists("plots"):
        os.makedirs("plots")
    app.run(debug=True)