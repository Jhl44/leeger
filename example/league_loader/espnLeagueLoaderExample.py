from leeger.league_loader import ESPNLeagueLoader
from leeger.model.league import League

if __name__ == '__main__':
    # PUBLIC LEAGUE
    # Get a League object with years 2019 and 2020 for ESPN league with ID: "12345678".
    espnLeagueLoader = ESPNLeagueLoader("12345678", [2019, 2020])
    league: League = espnLeagueLoader.loadLeague()

    # PRIVATE LEAGUE
    # You will need the ESPN_S2 and SWID parameters to retrieve a private league.
    # To retrieve these, follow these steps:
    # 1. Visit your main league page (i.e. https://fantasy.espn.com/football/team?leagueId=12345678seasonId=2020)
    # 2. Make sure you are logged in.
    # 3. Open Developer Tools (on Chrome/Firefox, right-click anywhere on the page and select Inspect Element)
    # 4. Go to Storage (for Firefox) or Application (for Chrome) and browse the Cookies available for fantasy.espn.com
    # 5. The values you need are called "SWID" and "ESPN_S2". You can right-click and copy the values from here.
    # Get a League object with years 2019 and 2020 for ESPN league with ID: "12345678".
    espnS2 = "AEBlX3XJ7L2w59zF8psAhxg9hR646qNr%2Bf%2FXR%2BgJWVYA%2BrQ%2F%2BSQL%2Br0CZ7WChNOZd09VOSjLtOTtVfXb7jHSVd30yKxi%2Fe09zQE1Kn4OvYmxSu%2FWWiE79ME9jcMuGYNl10iAkpRLlJ7IfrxIsQAHd9jVkDsk1%2FTGMtZrDOQtoAB4eFq9zXANEnjsGDWA965D8X2np6jM8JXPvhgEsJMczIMPcQ82rCyW%2Fj%2FZzmoPyv6wjpynh9TFQgvPpMR4Tyxnk5U%3D"
    swid = "{6E14BB58-E3BC-41B9-94BB-58E3BC31B9B2}"
    espnLeagueLoader = ESPNLeagueLoader("THE Fantasy League", [2021, 2022], espnS2=espnS2, swid=swid)
    league: League = espnLeagueLoader.loadLeague()
