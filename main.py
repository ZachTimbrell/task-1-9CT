from data_module import  (
  display_dataset_preview_GSW,
  display_dataset_preview_bulls,
  display_dataset_averages_GSW,
  display_dataset_averages_Bulls,
  average_GSW_graph,
  average_chicago_graph,

)

def main_menu():
    while True:
        print("==============================================================================")
        print("=                            --DATA INTERFACE--                              =")
        print("=             --1996 CHICAGO BULLS VS 2016 GOLDEN STATE WARRIORS--           =")
        print("==============================================================================")
        print("=    OPTIONS:                                                                =")
        print("=    1. View hypothesis                                                      =")
        print("=    2. View dataset for 1996 Chicago Bulls                                  =")
        print("=    3. view dataset for 2016 Golden State Warriors                          =")
        print("=    4. View averages for 1996 Chicago Bulls                                 =")
        print("=    5. View averages for 2016 Golden State Warriors                         =")
        print("=    6. Create graph for 2016 Golden State Warriors averages                 =")
        print("=    7. Create graph for 1996 Chicago Bulls averages                         =")
        print("=    8. Exit                     ")                                                               
        print("==============================================================================")
        choice = input("select an option from 1-8: ")
        if choice == "1":
            print('The 2016 Golden state Warriors are better than 1996 Chicago Bulls in the Regular season')
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
            print("Exiting Data Interface")
            break
        else:
            print("Invalid selection. Please choose an option 1-8")
if __name__ == "__main__":
    main_menu()
