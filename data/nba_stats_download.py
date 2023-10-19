import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats

# create list with all seasons between 1996-97 and 2022-23
seasons = []
for i in range(1996, 2023):
    seasons.append(str(i) + '-' + str(i+1)[2:])

# create empty dataframe
df = pd.DataFrame()

# get data for all seasons
for season in seasons:
    ls = leaguedashplayerstats.LeagueDashPlayerStats(season=season, measure_type_detailed_defense='Advanced')
    df_season = ls.get_data_frames()[0]
    # drop all columns except: PLAYER_ID, PLAYER_NAME, TEAM_ID, TEAM_ABBREVIATION, AGE, GP, MIN, OFF_RATING, DEF_RATING, NET_RATING, PIE
    df_season = df_season[['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'AGE', 'GP', 'MIN', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'PIE']]
    # add season column as first column
    df_season.insert(0, 'SEASON', season)
    # append data to dataframe
    df = df.append(df_season)
    print(season + ' done')

# save dataframe to csv file
df.to_csv('nba_stats_1996-2022_raw.csv', mode='w', header=True)