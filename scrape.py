# scrape.py
from footballwebscraper import fbref

# Example: scrape 2025-26 Premier League player stats
league = "Premier League"
season = "2025-2026"

# Fetch squad standard stats
df_squad = fbref.get_season_team_stats(league, season, stat_type="standard")
df_squad.to_csv("squad_standard.csv", index=False)

# Fetch player stats
df_player = fbref.get_season_player_stats(league, season, stat_type="standard")
df_player.to_csv("player_standard.csv", index=False)

# You can repeat with other stat_types:
# shooting, passing, possession, defense, gk, misc
