import pandas as pd

def analyze_pit_stops(year, pit_stops, races, drivers, results, constructors):
    races_year = races[races['year'] == year]

    merged = pit_stops.merge(races_year[['raceId']], on='raceId')
    merged = merged.merge(results[['raceId', 'driverId', 'constructorId']], on=['raceId', 'driverId'])
    merged = merged.merge(drivers[['driverId', 'surname']], on='driverId')

    merged['duration'] = pd.to_numeric(merged['duration'], errors='coerce')
    avg_by_driver = merged.groupby(['constructorId', 'surname'])['duration'].mean().reset_index()

    # Merge team names
    avg_named = avg_by_driver.merge(constructors[['constructorId', 'name']], on='constructorId')
    avg_named = avg_named.rename(columns={'name': 'team_name'})

    # Filter teams with exactly 2 drivers
    valid_teams = avg_named['team_name'].value_counts()
    valid_teams = valid_teams[valid_teams == 2].index
    avg_named = avg_named[avg_named['team_name'].isin(valid_teams)]

    return avg_named
