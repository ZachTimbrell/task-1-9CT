from data_module import  (
 display_dataset_preview_GSW,
 display_dataset_preview_bulls,
 display_dataset_averages_GSW,
 display_dataset_averages_Bulls,
 average_GSW_graph,
 average_chicago_graph,
 gsw_team_average,
 chicago_team_average,
 track_record_chicago,
 track_record_gsw,
 search_data,


)
import time
def typewrite(text):
   for char in text:
       print(char, end="", flush=True)
       time.sleep(0.005)
   print()


def main_menu():
   while True:
       typewrite("==============================================================================")
       typewrite("=                           (  DATA INTERFACE  )                             =")
       typewrite("=             --1996 CHICAGO BULLS VS 2016 GOLDEN STATE WARRIORS--           =")
       typewrite("==============================================================================")
       typewrite("=    OPTIONS:                                                                =")
       typewrite("=    1. View hypothesis                                                      =")
       typewrite("=    2. View dataset for 1996 Chicago Bulls                                  =")
       typewrite("=    3. view dataset for 2016 Golden State Warriors                          =")
       typewrite("=    4. View averages for 1996 Chicago Bulls                                 =")
       typewrite("=    5. View averages for 2016 Golden State Warriors                         =")
       typewrite("=    6. View graph for 2016 Golden State Warriors averages                   =")
       typewrite("=    7. View graph for 1996 Chicago Bulls averages                           =")
       typewrite("=    8. View team average graph for 2016 Golden State Warriors               =")
       typewrite("=    9. View team average graph for 1996 Chicago Bulls                       =")
       typewrite("=    10. View regular season record for 2016 Golden State Warriors           =")
       typewrite("=    11. View regular season record for 1996 Chicago Bulls                   =")
       typewrite("=    12. Exit                                                                =")
       typewrite("==============================================================================")
       choice = input("select an option from 1-12: ")
       typewrite(":----------------------------------------------------------------------------:")
       if choice == "1":
           typewrite('The 2016 Golden state Warriors are better than 1996 Chicago Bulls in the Regular season')
       elif choice == "2":
           display_dataset_preview_bulls()
       elif choice == "3":
           display_dataset_preview_GSW()
       elif choice == "4":
           display_dataset_averages_Bulls()
       elif choice == "5":
           display_dataset_averages_GSW()
       elif choice == "6":
           average_GSW_graph()
       elif choice == "7":
           average_chicago_graph()
       elif choice == "8":
           gsw_team_average()
       elif choice == "9":
           chicago_team_average()
       elif choice == "10":
           track_record_gsw()
       elif choice == "11":
           track_record_chicago()
       elif choice == "12":
           search_data
       elif choice == "13":
           typewrite("Exiting the program. Goodbye!")
           break
       else:
           typewrite("Invalid selection. Please choose an option 1-13")


if __name__ == "__main__":
   main_menu()
