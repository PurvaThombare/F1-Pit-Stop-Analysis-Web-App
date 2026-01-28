from data_loader import load_data
from analyzer import analyze_pit_stops
from plotter import plot_pit_stop_comparison

def main():
    YEAR = 2024

    pit_stops, races, drivers, results, constructors = load_data()
    avg_pitstop_df = analyze_pit_stops(YEAR, pit_stops, races, drivers, results, constructors)
    plot_pit_stop_comparison(avg_pitstop_df, YEAR)

if __name__ == "__main__":
    main()
