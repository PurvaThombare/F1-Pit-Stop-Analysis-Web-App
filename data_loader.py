import pandas as pd

def load_data():
    pit_stops = pd.read_csv("pit_stops.csv")
    races = pd.read_csv("races.csv")
    drivers = pd.read_csv("drivers.csv")
    results = pd.read_csv("results.csv")
    constructors = pd.read_csv("constructors.csv")
    return pit_stops, races, drivers, results, constructors
