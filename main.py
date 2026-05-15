from data_module import  (
  display_dataset_preview_GSW,
  display_dataset_preview_bulls,
  display_dataset_averages_GSW,
  display_dataset_averages_Bulls,
  add_data

)

def main_menu():
    while True:
        print("==============================================================================")
        print("=                            --DATA INTERFACE--                              =")
        print("=             --1996 CHICAGO BULLS VS 2016 GOLDEN STATE WARRIORS--           =")
        print("==============================================================================")
        print("=    OPTIONS:                                                                =")
        print("=    1. view dataset for 2016 Golden State Warriors                          =")
        print("=    2. View dataset for 1996 Chicago Bulls                                  =")
        print("=    3. view averages for 2016 Golden State Warriors                         =")
        print("=    4. View averages for 1996 Chicago Bulls                                 =")
        print("=    5. Add data to dataset                                                  =")
        print("=    6. Exit                                                                 =")
        print("==============================================================================")
        choice = input("select an option from 1-6: ")
        if choice == "1":
            display_dataset_preview_GSW()
        elif choice == "2":
            display_dataset_preview_bulls()
        elif choice == "3":
            display_dataset_averages_GSW()
        elif choice == "4":
            display_dataset_averages_Bulls()
        elif choice == "5":
            add_data()
            print("Data successfully added.")
        elif choice == "6":
            print("Exiting Data Interface")
            break
        else:
            print("Invalid selection. Please choose an option 1-6")
if __name__ == "__main__":
    main_menu()
