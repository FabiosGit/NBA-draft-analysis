# NBA Draft Analysis
In this repository, we attempt to answert the following research question: Which NBA team selects the best players relative to the average player at their respective draft position?

To do so, we use performance metrics of individual NBA players and compare them to other players that were drafted at the same draft position. After conducting an analysis on the individual player-level, we group the players by the team they were drafted by in order to answer the question above. Through a variety of inveractive visualizations and the ability to set certain parameters dynamically, you can vary and validate our analysis to your own needs.


To **run the analysis**, please complete the following steps:
- Install docker
- Navigate to the directory where you want to clone this repository and run the following command: "git clone https://github.com/FabiosGit/NBA-draft-analysis.git"
- Navigate to the root of this repository ("cd NBA-draft-analysis") and run the following command to build the docker image: "docker build -t my-jupyter-container ."
- Run the following command to run the docker container: "docker run -p 8888:8888 my-jupyter-container"
- Open the created URL to access the jupyter server
- Open "analysis.ipynb" in jupyter lab (otherwise the interactive widgets will not work)
- Run all cells in the notebook sequentially


To **extend the analysis** at a later point in time with an update timeframe, please complete the following steps:
- Run the [get_nba_api_stats.py](src/data_processing/get_nba_api_stats.py) script with an updated timeframe to produce an updated version of [nba_stats_1996-2022_raw.csv](data/raw/nba_stats_1996-2022_raw.csv)
- Download all .csv files of the additional draft years from the draft section of [Basketball Reference](https://www.basketball-reference.com) and append them to the bottom of [nba_draft_data_bbref_raw.csv](data/raw/nba_draft_data_bbref_raw.csv)
- Run the [bbref_combine_player_seasons.ipynb](src/data_processing/bbref_combine_player_seasons.ipynb) notebook to combine all seasonal stats of one player from the NBA API into one data entry
- Use Excel formulas to combine the [nba_stats_seasons_stacked.csv](data/interim/nba_stats_seasons_stacked.csv) and [nba_draft_data_bbref_raw.csv](data/raw/nba_draft_data_bbref_raw.csv) files into one. This part requires some manual work because there is no unique ID for the players and their names differ in some cases because the NBA API data doesn't contain any special characters but the Basketball Reference data does. The combined file should be saved as [nba_draft_data_combined.csv](data/interim/nba_draft_data_combined.csv)
- Run the [adjust_teams.ipynb](src/data_processing/adjust_teams.ipynb) notebook. See an explanation why this is required at the beginning of the notebook.
- Run the [season2career_stats.ipynb](src/data_processing/season2career_stats.ipynb) to aggregate all statistics to a career-level and obtain the final processed data file [player_career_avg.csv](data/processed/player_career_avg.csv)
- Now you are ready to re-run the analysis with updated data
