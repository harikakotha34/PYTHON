# Expense Tracker Project

expensesList = []  # list of expenses as dictionaries
print("Welcome to Expense Tracker")

while True:
    print("\n=== MENU ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice: "))

    # 1. ADD EXPENSE
    if choice == 1:
        date = input("Enter the date: ")
        category = input("Enter category (Food, Travel, Shopping, Books): ")
        description = input("Enter description: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("✅ Expense added successfully!")

    # 2. VIEW ALL EXPENSES
    elif choice == 2:
        if len(expensesList) == 0:
            print("❌ No expenses added yet.")
        else:
            print("\n=== ALL EXPENSES ===")
            count = 1
            for eachexpense in expensesList:
                print(f"{count}. Date: {eachexpense['date']}, "
                      f"Category: {eachexpense['category']}, "
                      f"Description: {eachexpense['description']}, "
                      f"Amount: ₹{eachexpense['amount']}")
                count += 1

    # 3. VIEW TOTAL EXPENSE
    elif choice == 3:
        total = 0
        for eachexpense in expensesList:
            total += eachexpense["amount"]

        print("💰 TOTAL EXPENSE =", total)

    # 4. EXIT
    elif choice == 4:
        print("🙏 THANK YOU FOR USING EXPENSE TRACKER")
        break

    else:
        print("❌ INVALID CHOICE. TRY AGAIN")
