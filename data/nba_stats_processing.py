import pandas as pd

# load csv file nba_stats_1996-2022_raw.csv
df = pd.read_csv('nba_stats_1996-2022_raw.csv')
    
# for each player id, combine all seasons into one row with the season as a multiindex, drop the original index
df = df.set_index(['PLAYER_ID', 'PLAYER_NAME', 'SEASON']).unstack(level=2)

# drop the Unnamed: 0 column
df = df.drop('Unnamed: 0', axis=1, level=0)

# switch multiindex levels for season and stats
df = df.swaplevel(0, 1, axis=1)
# resort columns so all seasons are grouped together and in ascending order
df = df.sort_index(axis=1, level=0)

print(df.head())

# print row for PLAYER_NAME = Jayson Tatum
print(df.loc[df.index.get_level_values(1) == 'Jayson Tatum'])

# save dataframe to csv file
df.to_csv('nba_stats_1996-2022_processed.csv', mode='w', header=True)
    
    
# add column headers to csv file
#if season == '1996-97':
#df.to_csv('nba_stats_1996-2022.csv', mode='w', header=True)
# append data to csv file
#df.to_csv('nba_stats_1996-2022.csv', mode='a', header=False)
#print(season + ' done')