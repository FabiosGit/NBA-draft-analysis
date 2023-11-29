# nba-draft-analysis
 NBA draft analysis - Which NBA team selects the best players relative to the average player at their respective draft position?


To run the analysis, please complete the following steps:
- Install docker
- Navigate to the directory where you want to clone this repository and run the following command: "git clone https://github.com/FabiosGit/NBA-draft-analysis.git"
- Navigate to the root of this repository ("cd NBA-draft-analysis") and run the following command to build the docker image: "docker build -t my-jupyter-container ."
- Run the following command to run the docker container: "docker run -p 8888:8888 my-jupyter-container"
- Open the created URL to access the jupyter server
- Open "analysis.ipynb" in jupyter lab (otherwise the interactive widgets will not work)
- Run all cells in the notebook sequentially
