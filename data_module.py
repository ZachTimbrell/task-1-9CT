import pandas as pd


GSW_FILE = "data/basketball.csv"
BULLS_FILE = "data/chicago.csv"

GSW_df = pd.read_csv(GSW_FILE)
chicago_df = pd.read_csv(BULLS_FILE)


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


def display_dataset_preview_bulls():
    _display_table("1996 Chicago Bulls Roster", chicago_df)


def display_dataset_preview_GSW():
    _display_table("2016 Golden State Warriors Roster", GSW_df)


def display_dataset_averages_Bulls():
    _display_averages("1996 Chicago Bulls Averages", chicago_df)


def display_dataset_averages_GSW():
    _display_averages("2016 Golden State Warriors Averages", GSW_df)


def add_data():
    print("\nAdd data is not connected yet.")
    print("Next step: choose a team, collect player details, then save to CSV.\n")
