import os
import platform
import subprocess
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


GSW_FILE = "data/basketball.csv"
BULLS_FILE = "data/chicago.csv"
GSW_AVERAGES_FILE = "data/averages_gsw.csv"
BULLS_AVERAGES_FILE = "data/averages_Chicago.csv"

GSW_df = pd.read_csv(GSW_FILE)
chicago_df = pd.read_csv(BULLS_FILE)
GSW_averages_df = pd.read_csv(GSW_AVERAGES_FILE, skiprows=1)
chicago_averages_df = pd.read_csv(BULLS_AVERAGES_FILE, skiprows=1)


def _height_to_inches(height):
    feet, inches = height.split("-")
    return int(feet) * 12 + int(inches)


def _inches_to_height(total_inches):
    feet = int(total_inches // 12)
    inches = round(total_inches % 12)
    return f"{feet}-{inches}"


def _display_table(title, df):
    print(f"\n{title}")
    print("-" * len(title))
    print(df.to_string(index=False))
    print()


def _display_averages(title, df):
    average_height = df["Height"].apply(_height_to_inches).mean()
    summary = pd.DataFrame(
        {
            "Stat": ["Players", "Average Jersey Number", "Average Height", "Average Weight"],
            "Value": [
                len(df),
                round(df["Jersey Number"].mean(), 1),
                _inches_to_height(average_height),
                f"{round(df['Weight'].mean(), 1)} lbs",
            ],
        }
    )
    _display_table(title, summary)


def _open_graph_file(graph_path):
    system = platform.system()

    try:
        if system == "Darwin":
            result = subprocess.run(["open", str(graph_path)], capture_output=True, text=True, timeout=5)
            if result.returncode != 0:
                print("Could not open the graph automatically. Open the saved file above to view it.")
        elif system == "Windows":
            os.startfile(graph_path)
        else:
            result = subprocess.run(["xdg-open", str(graph_path)], capture_output=True, text=True, timeout=5)
            if result.returncode != 0:
                print("Could not open the graph automatically. Open the saved file above to view it.")
    except Exception:
        print("Could not open the graph automatically. Open the saved file above to view it.")


def _create_average_graph(title, df, output_file, open_graph=True):
    graph_columns = ["Pts", "Ast", "Stl", "Blk"]
    graph_data = df[["Player"] + graph_columns].set_index("Player")

    graph_data.plot(kind="bar", figsize=(14, 7))
    plt.title(title)
    plt.xlabel("Player")
    plt.ylabel("Average per game")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

    graph_path = Path(output_file).resolve()
    print(f"\nGraph saved as {graph_path}\n")

    if open_graph:
        _open_graph_file(graph_path)


def _create_team_average_graph(title, df, output_file, open_graph=True):
    graph_columns = {
        "Pts": "Points",
        "TRb": "Rebounds",
        "Ast": "Assists",
        "Stl": "Steals",
        "Blk": "Blocks",
    }
    graph_data = df[list(graph_columns.keys())].sum().rename(index=graph_columns)

    graph_data.plot(kind="bar", figsize=(9, 6), color=["#1D428A", "#CE1141", "#FDB927", "#007A33", "#552583"])
    plt.title(title)
    plt.xlabel("Statistic")
    plt.ylabel("Team average per game")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

    graph_path = Path(output_file).resolve()
    print(f"\nGraph saved as {graph_path}\n")

    if open_graph:
        _open_graph_file(graph_path)


def display_dataset_preview_bulls():
    _display_table("1996 Chicago Bulls Roster", chicago_df)


def display_dataset_preview_GSW():
    _display_table("2016 Golden State Warriors Roster", GSW_df)


def display_dataset_averages_Bulls():
    _display_table("1996 Chicago Bulls Regular Season Averages", chicago_averages_df)


def display_dataset_averages_GSW():
    _display_table("2016 Golden State Warriors Regular Season Averages", GSW_averages_df)


def average_chicago_graph():
    _create_average_graph(
        "1996 Chicago Bulls Average Points, Assists, Steals and Blocks",
        chicago_averages_df,
        "data/average_chicago_graph.png",
    )


def average_GSW_graph():
    _create_average_graph(
        "2016 Golden State Warriors Average Points, Assists, Steals and Blocks",
        GSW_averages_df,
        "data/average_GSW_graph.png",
    )


def gsw_team_average():
    _create_team_average_graph(
        "2016 Golden State Warriors Team Averages",
        GSW_averages_df,
        "data/gsw_team_average.png",
    )


def chicago_team_average():
    _create_team_average_graph(
        "1996 Chicago Bulls Team Averages",
        chicago_averages_df,
        "data/chicago_team_average.png",
    )


def add_data():
    print("\nAdd data is not connected yet.")
    print("Next step: choose a team, collect player details, then save to CSV.\n")
