import os

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


def _create_average_graph(title, df, output_file):
    os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

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
    print(f"\nGraph saved as {output_file}\n")


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


def add_data():
    print("\nAdd data is not connected yet.")
    print("Next step: choose a team, collect player details, then save to CSV.\n")
