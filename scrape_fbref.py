import pandas as pd
import requests
from bs4 import BeautifulSoup

# FBref Premier League stats page
league_url = "https://fbref.com/en/comps/9/Premier-League-Stats"  # 2025/26 season

# List of stat types
stat_types = ["standard", "shooting", "passing", "possession", "defense", "gk", "misc"]

# Function to fetch a table by its ID
def get_table(url, table_id):
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        table = soup.find("table", id=table_id)
        if table is None:
            print(f"Table '{table_id}' not found on page")
            return pd.DataFrame()
        df = pd.read_html(str(table))[0]
        print(f"Successfully fetched table '{table_id}' with {len(df)} rows")
        return df
    except Exception as e:
        print(f"Error fetching table '{table_id}': {e}")
        return pd.DataFrame()

# Scrape all team stats
def scrape_team_stats():
    for stat in stat_types:
        try:
            table_id = f"stats_{stat}_teams"  # FBref table ID format
            df = get_table(league_url, table_id)
            if not df.empty:
                print(f"Saving team CSV: team_{stat}.csv")
                df.to_csv(f"team_{stat}.csv", index=False)
            else:
                print(f"Team stat '{stat}' returned empty dataframe")
        except Exception as e:
            print(f"Error scraping team stat '{stat}': {e}")

# Scrape all player stats
def scrape_player_stats():
    for stat in stat_types:
        try:
            table_id = f"stats_{stat}_players"  # FBref table ID format
            df = get_table(league_url, table_id)
            if not df.empty:
                print(f"Saving player CSV: player_{stat}.csv")
                df.to_csv(f"player_{stat}.csv", index=False)
            else:
                print(f"Player stat '{stat}' returned empty dataframe")
        except Exception as e:
            print(f"Error scraping player stat '{stat}': {e}")

# Main execution
if __name__ == "__main__":
    print("Starting FBref 2025/26 Premier League scraper...")
    scrape_team_stats()
    scrape_player_stats()
    print("Scraper finished.")
