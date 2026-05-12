import pandas as pd

def display_dataset_preview_bulls():
    display_dataset_preview_bulls = pd.DataFrame([
    ['0', 'PG', '6-2', '190', 'May 22, 1968'],
    ['25', 'PG',	'6-3',	'175',	'September 27, 1965'],
    ['9', 'PG',	'6-6',	'185',	'January 20, 1964'],
    ['23', 'SG',	'6-6',	'198',	'February 17, 1963'],
    ['30', 'SF', '6-6',	'220',	'June 19, 1968'],
    ['7', 'SF',	'6-10',	'192',	'September 18, 1968'],
    ['33', 'SF',	'6-8',	'210',	'September 25, 1965'],
    ['35', 'PF',	'6-8',	'255',	'June 12, 1973'],
    ['91', 'PF',	'6-7',	'210',	'May 13, 1961'],
    ['22', 'PF',	'6-11',	'230',	'May 16, 1964'],
    ['8', 'PF',	'6-9',	'248',	'April 6, 1972'],
    ['53', 'C',	'7-1',	'252',	'November 22, 1955'],
    ['54', 'C',	'6-10',	'240'	'January 27, 1964'],
    ['13', 'C',	'7-2',	'265',	'January 19, 1969'],
    ['34','C','7-0','245','April 26, 1963'],  
    ], columns = ['Randy Brown','Steve Kerr','Ron Haprer','Michael Jordan','Jud Buechler','Toni Kukoč','Scottie Pippen','Jasen Caffey','Dennis Rodman','John Salley','Dickey Simpkins','James Edwards','Jack Haley','luc Longley','Bill Wellington']
    , row = ('name','jersey number','position','height','weight','date of birth')
    )
def display_dataset_previews_GSW():
    display_dataset_previews_GSW = pd.DataFrame([
    ['30', 'PG', '6-2',	'185',	'March 14, 1988'],
    ['34', 'PG',	'6-7',	'192',	'September 11, 1985'],
    ['19', 'SG', '6-3', '194', 'November 28, 1982'],
    ['4', 'SG',	'6-6',	'220',	'July 7, 1985'],
    ['11','SG','6-5','220','February 8, 1990'],
    ['21', 'SG',	'6-3',	'175',	'March 7, 1991'],
    ['40', 'SF',	'6-7',	'225',	'May 30, 1992'],
    ['9', 'SF',	'6-6',	'215',	'January 28, 1984'],
    ['23', 'PF',	'6-6',	'230',	'March 4, 1990'],
    ['36', 'PF',	'6-9',	'222',	'February 6, 1996'],
    ['20', 'PF',	'6-9',	'230',	'January 4, 1993'],
    ['12', 'C',	'7-0',	'260',	'November 28, 1984'],
    ['31', 'C',	'6-11',	'255',	'October 21, 1989'],
    ['5', 'C',	'6-10',	'255'	'August 4, 1987'],
    ['1', 'C',	'6-11',	'250',	'July 21, 1986'],
    ['18','C','6-11','273','September 28, 1982'], 
    ], columns = ['Stephen Curry','Shaun Livingston','Leandro Barbosa','Brandon Rush','Klay Thompson','Ian Clark','Harrison Barnes','Andre Iguodala','Draymond Green','Kevon Looney','James Michael','Andrew Bogut','Festus Ezeli','Marreese Speights','Jason Thompson']

    )

def display_dataset_averages_chicago_bulls():
    display_dataset_averages_chicago_bulls = pd.DataFrame([''
    ])

    print(display_dataset_preview_bulls)