# scrape.py
import pandas as pd
from footballwebscraper import fbref

league = "Premier League"
season = "2025-2026"
stat_types = ["standard", "shooting", "passing", "possession", "defense", "gk", "misc"]

def scrape_team_stats():
    for stat in stat_types:
        try:
            df_team = fbref.get_season_team_stats(league, season, stat_type=stat)
            if df_team.empty:
                print(f"Team stat '{stat}' returned empty dataframe.")
            else:
                df_team.to_csv(f"team_{stat}.csv", index=False)
                print(f"Team stat '{stat}' saved successfully.")
        except Exception as e:
            print(f"Error scraping team stat '{stat}': {e}")

def scrape_player_stats():
    for stat in stat_types:
        try:
            df_player = fbref.get_season_player_stats(league, season, stat_type=stat)
            if df_player.empty:
                print(f"Player stat '{stat}' returned empty dataframe.")
            else:
                df_player.to_csv(f"player_{stat}.csv", index=False)
                print(f"Player stat '{stat}' saved successfully.")
        except Exception as e:
            print(f"Error scraping player stat '{stat}': {e}")

if __name__ == "__main__":
    print("Starting FBref 2025/26 scraper...")
    scrape_team_stats()
    scrape_player_stats()
    print("Scraper finished.")
