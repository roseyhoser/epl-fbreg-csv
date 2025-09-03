# scrape_fbref.py
import pandas as pd
import requests
from bs4 import BeautifulSoup

league_url = "https://fbref.com/en/comps/9/Premier-League-Stats"  # 2025/26 stats page
stat_types = ["standard", "shooting", "passing", "possession", "defense", "gk", "misc"]

def get_table(url, table_id):
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        table = soup.find("table", id=table_id)
        if table is None:
            print(f"Table {table_id} not found")
            return pd.DataFrame()
        df = pd.read_html(str(table))[0]
        return df
    except Exception as e:
        print(f"Error fetching table {table_id}: {e}")
        return pd.DataFrame()

def scrape_team_stats():
    for stat in stat_types:
        table_id = f"stats_{stat}_teams"  # FBref convention: check actual HTML id
        df = get_table(league_url, table_id)
        if not df.empty:
            df.to_csv(f"team_{stat}.csv", index=False)
            print(f"Team stat {stat} saved")
        else:
            print(f"Team stat {stat} empty")

def scrape_player_stats():
    for stat in stat_types:
        table_id = f"stats_{stat}_players"  # FBref convention: check actual HTML id
        df = get_table(league_url, table_id)
        if not df.empty:
            df.to_csv(f"player_{stat}.csv", index=False)
            print(f"Player stat {stat} saved")
        else:
            print(f"Player stat {stat} empty")

if __name__ == "__main__":
    print("Scraping 2025/26 Premier League FBref stats...")
    scrape_team_stats()
    scrape_player_stats()
    print("Scraping finished.")
