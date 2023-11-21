from mwrogue.esports_client import EsportsClient
from tqdm import tqdm
site = EsportsClient("lol")

liga = ['CBLOL']
for nome in tqdm(liga):
    response = site.cargo_client.query(

            tables="ScoreboardGames=SG, Tournaments=T",
            join_on="SG.OverviewPage=T.OverviewPage",
            fields="T.Name, SG.DateTime_UTC, SG.Team1, SG.Team2"
    )

print(response)
