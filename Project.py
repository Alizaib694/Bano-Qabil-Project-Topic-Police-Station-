# Police Station Management System
print("======== Sindh Police Station ========")   # Title at the start

cases = []   # Empty list to store all case details
case_id = 1  # Unique ID for every case (starts from 1)

while True:   # Infinite loop until user chooses Exit
    print("\n==== How Can I Help You ====")   # Main Menu
    print("1. Traffic Department: ")
    print("2. Crime Department: ")
    print("3. Cybercrime Department: ")
    print("4. Register a New Case: ")
    print("5. View All Cases: ")
    print("6. Search Case by ID: ")
    print("7. Update Case Status: ")
    print("8. Delete a Case: ")
    print("9. Exit: ")

    # Taking input for menu choice safely
    try:
        choice = int(input("Enter Your Option Please Choose Serial no (1-9): "))
    except ValueError:
        print("❌ Invalid input! Please enter a number (1-9).")
        continue   # Goes back to menu

    # OPTION 1 → Traffic Department Information
    if choice == 1:
        print("🚦 Traffic Department (Services): Handle Traffic Violation & Accidents.")

    # OPTION 2 → Crime Department Information
    elif choice == 2:
        print("🚔 Crime Department (Services): Handles Robbery, Theft, & Assaults.")

    # OPTION 3 → Cybercrime Department Information
    elif choice == 3:
        print("💻 Cybercrime Department (Services): Handles Online Scams, Frauds & Hacking.")  

    # OPTION 4 → Register a New Case
    elif choice == 4:
        print("📝 Register a New Case")

        officer = input("Enter Officer Name You Want to Give Your Case: ")
        complainant = input("Enter The Name Who is Complaining: ")
        case_type = input("Enter Case Type (Traffic/Crime/Cyber): ")
        details = input("Enter Case Details: ")

        # Dictionary to store case details
        case = {
            "ID": case_id,
            "Officer": officer,
            "Complainant": complainant,
            "Type": case_type,
            "Details": details,
            "Status": "Open"   # New cases are open by default
        }

        cases.append(case)   # Store case in the list
        print("✅ Case registered & Your Id is:", case_id)
        case_id += 1   # Increase ID for next case

    # OPTION 5 → View All Cases
    elif choice == 5:
        print("📂 All Registered Cases:")
        if len(cases) == 0:   # If no case is registered
            print("No Cases yet.")
        else:
            for case in cases:
                print("ID:", case["ID"], 
                      "| Officer:", case["Officer"], 
                      "| Complainant:", case["Complainant"], 
                      "| Type:", case["Type"], 
                      "| Details:", case["Details"], 
                      "| Status:", case["Status"])

    # OPTION 6 → Search Case by ID
    elif choice == 6:
        try:
            search_id = int(input("Enter Case ID to Search: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        found = False
        for case in cases:
            if case["ID"] == search_id:   # Case Found
                print("🔎 Case Found:")
                print("ID:", case["ID"], 
                      "| Officer:", case["Officer"], 
                      "| Complainant:", case["Complainant"], 
                      "| Type:", case["Type"], 
                      "| Details:", case["Details"], 
                      "| Status:", case["Status"])
                found = True
        if not found:   # If loop completes and case not found
            print("❌ Case not found.")

    # OPTION 7 → Update Case Status
    elif choice == 7:
        try:
            update_id = int(input("Enter Your Case ID to Update: "))
        except ValueError:
            print("❌ Invalid input! Enter a number.")
            continue

        for case in cases:
            if case["ID"] == update_id:   # Case matched
                print("Current Status:", case["Status"])
                new_status = input("Enter new status (Open/Closed): ")
                case["Status"] = new_status   # Update status
                print("✅ Case status updated.")
                break
        else:
            print("❌ Case not found.")

    # OPTION 8 → Delete a Case
    elif choice == 8:
        try:
            delete_id = int(input("Enter Case ID to Delete: "))
        except ValueError:
            print("❌ Invalid input! Enter a number.")
            continue

        for case in cases:
            if case["ID"] == delete_id:
                cases.remove(case)   # Remove case from list
                print("🗑️ Case deleted successfully.")
                break
        else:
            print("❌ Case not found.")

    # OPTION 9 → Exit System
    elif choice == 9:
        print("👮 Exiting Police Station System. Goodbye!")
        break   # Ends while loop

    # If user enters wrong number
    else:
        print("❌ Invalid choice. Please choose 1-9.")
