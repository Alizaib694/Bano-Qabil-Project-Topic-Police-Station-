print("==== WELCOME TO POLICE STATION ====")

cases = []
case_id = 1   

while True:
    print("\n----- MAIN MENU -----")
    print("1. Traffic Office")
    print("2. Crime Office")
    print("3. Cybercrime Office")
    print("4. Register a New Case")
    print("5. View All Cases")
    print("6. Search Case by ID")
    print("7. Update Case Status")
    print("8. Delete a Case")
    print("9. Exit")

    choice = int(input("Enter your choice (1-9): "))

    if choice == 1:
        print("Traffic Office: Handles traffic violations and accidents.")

    elif choice == 2:
        print("Crime Office: Handles robbery, theft, and assaults.")

    elif choice == 3:
        print("Cybercrime Office: Handles online fraud and hacking.")

    elif choice == 4:
        print("Register a New Case")
        officer = input("Enter Officer Name: ")
        complainant = input("Enter Complainant Name: ")
        case_type = input("Enter Case Type (Traffic/Crime/Cyber): ")
        details = input("Enter Case Details: ")

        case = {
            "ID": case_id,
            "Officer": officer,
            "Complainant": complainant,
            "Type": case_type,
            "Details": details,
            "Status": "Open"
        }

        cases.append(case)
        print("Case registered with ID:", case_id)
        case_id += 1

    elif choice == 5:
        print("All Registered Cases:")
        if len(cases) == 0:
            print("No cases yet.")
        else:
            for case in cases:
                print("ID:", case["ID"], 
                      "| Officer:", case["Officer"], 
                      "| Complainant:", case["Complainant"], 
                      "| Type:", case["Type"], 
                      "| Details:", case["Details"], 
                      "| Status:", case["Status"])

    elif choice == 6:
        search_id = int(input("Enter Case ID to Search: "))
        found = False
        for case in cases:
            if case["ID"] == search_id:
                print("Case Found:")
                print("ID:", case["ID"], 
                      "| Officer:", case["Officer"], 
                      "| Complainant:", case["Complainant"], 
                      "| Type:", case["Type"], 
                      "| Details:", case["Details"], 
                      "| Status:", case["Status"])
                found = True
        if not found:
            print("Case not found.")

    elif choice == 7:
        update_id = int(input("Enter Case ID to Update: "))
        for case in cases:
            if case["ID"] == update_id:
                print("Current Status:", case["Status"])
                new_status = input("Enter new status (Open/Closed): ")
                case["Status"] = new_status
                print("Case status updated.")
                break
        else:
            print("Case not found.")

    elif choice == 8:
        delete_id = int(input("Enter Case ID to Delete: "))
        for case in cases:
            if case["ID"] == delete_id:
                cases.remove(case)
                print("Case deleted successfully.")
                break
        else:
            print("Case not found.")

    elif choice == 9:
        print("Exiting Police Station System. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
