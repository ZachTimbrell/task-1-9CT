# **Hypothesis**:The 2016 Golden State Warriors are better than the 1996 Chicago Bulls

## Assessment task 1  Zach Timbrell

### Functional Requirements
 **Data Loading**: 
- The system must be able to load the csv files using pandas library
- Allow users to efficiently choose file locations
- detect errors such as missing files, corrupted data or incorrect input


**Data Cleaning**:
- Handle missing files by exchanging them for usable variables
- Remove duplicate files and data used in the amking of my task


**Data Analysis**:
- Calculate statistical values such as mean, median, and mode.
- Compare datasets to identify trends, patterns, or outliers in the data

**Data Visualisation**: 
- Display data clearly using Pandas DataFrames and tables.
- Create graphs such as bar charts, line graphs, and pie charts using Matplotlib.
- Use labelled axes, titles, and legends to improve readability of charts.

**Data Reporting**: 
- Export final datasets and results into formats such as .csv or .txt files.
- Generate summary reports containing key findings and visualisations.


### Non-Functional Requirements
 **Usability**: 
- My Read Me file will effectively indicate what each option will do
- My User interface will be clean and show each options clearly
- Each option will work accordingly

**Reliability**: What is required from the system when providing information to the user on errors and ensuring data integrity?
- The system will clearly indicate a display error when there is invalid test
- The porgram will continue to run until user decides to exit

### Use-Case
**Actor**: User

**Goal**: To access and interact with existing data through the program’s user interface.

**Preconditions**:

- The dataset has already been preloaded into the system by an administrator / programmer.

- The user has access to the system interface.

**Main Flow**:

 - User opens the program and is presented with a text-based menu.

- User selects one of the following options:
1. View Hypothesis
2. View dataset for GSW
3. view dataset for 2016 Golden State Warriors                 
5. View averages for 2016 Golden State Warriors                         
6. View graph for 2016 Golden State Warriors averages             
7. View graph for 1996 Chicago Bulls averages                           
8. View team average graph for 2016 Golden State Warriors           
9. View team average graph for 1996 Chicago Bulls                       
10. View regular season record for 2016 Golden State Warriors          
11. View regular season record for 1996 Chicago Bulls                   
12. Exit                                 

- System performs the requested action and outputs to user.

**Postconditions**:

- User has viewed and/or interacted with the data.

- Data remains available for further queries or analysis.Actor: User



### Data Dictionary
| Field         | datatype | Format For Display | Description                        | Example          | Validation                                             |   |
|---------------|----------|--------------------|------------------------------------|------------------|--------------------------------------------------------|---|
| Player        | str      | XX..XX             | The name of the player             | Stephen Curry    | Can be any amount of letters, must not include numbers |   |
| Jersey Number | int      | XX                 | the jersey number the player wears |               30 | Must be 1-2 integers long                              |   |
| Pos           | str      | XX                 | The position they play             | PG               | 1-2 Letters                                            |   |
| Height        | int      | X-X                | Their height                       |              6-2 | Must be 2 integers long with a - between               |   |
| Weight        | int      | XXX                | Their weight                       |              185 | Must be 3 integers long                                |   |
| DOB           | str      | XX..XX             | Their date of birth                | Feburary 1, 1996 | can be numbers and letters                             |   |


## Conclusion:
According to my dataset, The 2016 Golden State Warriors played better in the regular season with a final track record of 73-9 wins while the 1996 Chicago Bulls mearly lost with a track record of 72-10 wins. The Golden State warriors were more efficient in point scoring and field goal percentage. Overall the 2016 Golden State Warriors were a better team offensively, compared to the 1996 chicago bulls in terms of stats.


** Biblyography:
- https://www.basketball-reference.com/teams/GSW/2016.html
- https://www.landofbasketball.com/stats_by_team/2015_2016_warriors_rs.htm
- https://www.basketball-reference.com/teams/GSW/2016_games.html
- https://www.basketball-reference.com/teams/CHI/1996.html
- https://www.landofbasketball.com/stats_by_team/1995_1996_bulls_rs.htm
- https://www.basketball-reference.com/teams/CHI/1996_games.html



STATEMENT EXPLANATION EXAMPLE CONSION
