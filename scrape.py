from footballwebscraper import fbref

league = "Premier League"
season = "2025-2026"

stat_types = ["standard", "shooting", "passing", "possession", "defense", "gk", "misc"]

# Team stats
for stat in stat_types:
    df_team = fbref.get_season_team_stats(league, season, stat_type=stat)
    df_team.to_csv(f"team_{stat}.csv", index=False)

# Player stats
for stat in stat_types:
    df_player = fbref.get_season_player_stats(league, season, stat_type=stat)
    df_player.to_csv(f"player_{stat}.csv", index=False)
