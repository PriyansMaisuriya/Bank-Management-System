import json
import random
import string
from pathlib import Path
from getpass import getpass


class Bank:
    database = "data.json"
    data = []

    # Load existing data
    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.load(fs)
        else:
            with open(database, "w") as fs:
                json.dump([], fs)
            data = []
    except Exception as err:
        print(f"An exception occurred: {err}")
        data = []

    @staticmethod
    def update():
        with open(Bank.database, "w") as fs:
            json.dump(Bank.data, fs, indent=4)

    @staticmethod
    def accountgenerate():
        
        num = random.choices(string.digits, k=10)
        
        acc =  num 
        random.shuffle(acc)
        return "".join(acc)

    def createaccount(self):
        info = {
            "Name": input("Tell your Name: "),
            "Age": int(input("Enter your Age: ")),
            "Email": input("Tell your Email: "),
            "Pin": int(input("Tell your 4-digit Pin: ")),
            "AccountNo.": Bank.accountgenerate(),
            "Balance": 0
        }

        if info["Age"] < 18:
            print("Sorry! Age must be at least 18.")
            return

        if len(str(info["Pin"])) != 4:
            print("PIN must be exactly 4 digits.")
            return

        Bank.data.append(info)
        Bank.update()

        print("\nAccount created successfully!\n")
        for key, value in info.items():
            print(f"{key}: {value}")

        print("\nPlease save your Account Number.")

    def depositemoney(self):
        accnumber = input("Enter Account Number: ")
        pin = int(input("Enter PIN: "))

        userdata = [
            i for i in Bank.data
            if i["AccountNo."] == accnumber and i["Pin"] == pin
        ]

        if not userdata:
            print("Invalid Account Number or PIN.")
            return

        amount = int(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > 10000:
            print("Maximum deposit limit is 10000.")
            return

        userdata[0]["Balance"] += amount
        Bank.update()

        print("Amount deposited successfully.")
        print("Current Balance:", userdata[0]["Balance"])

    def withdrawmoney(self):
        accnumber = input("Enter Account Number: ")
        pin = int(input("Enter PIN: "))

        userdata = [
            i for i in Bank.data
            if i["AccountNo."] == accnumber and i["Pin"] == pin
        ]

        if not userdata:
            print("Invalid Account Number or PIN.")
            return

        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount.")
            return

        if userdata[0]["Balance"] < amount:
            print("Insufficient Balance.")
            return

        userdata[0]["Balance"] -= amount
        Bank.update()

        print("Withdrawal successful.")
        print("Remaining Balance:", userdata[0]["Balance"])

    def showdetails(self):
        accnumber = input("Enter Account Number: ")
        pin = int(input("Enter PIN: "))

        userdata = [
            i for i in Bank.data
            if i["AccountNo."] == accnumber and i["Pin"] == pin
        ]

        if not userdata:
            print("No user found.")
            return

        print("\n------ Account Details ------")
        for key, value in userdata[0].items():
            print(f"{key}: {value}")

    def updatedetails(self):
        accnumber = input("Enter Account Number: ")
        pin = int(input("Enter PIN: "))

        userdata = [
            i for i in Bank.data
            if i["AccountNo."] == accnumber and i["Pin"] == pin
        ]

        if not userdata:
            print("No such user found.")
            return

        user = userdata[0]

        print("\nLeave blank if you don't want to change.\n")

        name = input("New Name: ")
        email = input("New Email: ")
        newpin = input("New PIN: ")

        if name:
            user["Name"] = name

        if email:
            user["Email"] = email

        if newpin:
            if len(newpin) != 4 or not newpin.isdigit():
                print("PIN must be exactly 4 digits.")
                return
            user["Pin"] = int(newpin)

        Bank.update()

        print("Details updated successfully.")

    def delete(self):
        accnumber = input("Enter Account Number: ")
        pin = int(input("Enter PIN: "))

        userdata = [
            i for i in Bank.data
            if i["AccountNo."] == accnumber and i["Pin"] == pin
        ]

        if not userdata:
            print("No such account found.")
            return

        check = input("Are you sure? (Y/N): ")

        if check.lower() == "y":
            Bank.data.remove(userdata[0])
            Bank.update()
            print("Account deleted successfully.")
        else:
            print("Deletion cancelled.")


user = Bank()

while True:
    print("\n====== BANK MANAGEMENT SYSTEM ======")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Show Details")
    print("5. Update Details")
    print("6. Delete Account")
    print("7. Exit")

    try:
        check = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if check == 1:
        user.createaccount()

    elif check == 2:
        user.depositemoney()

    elif check == 3:
        user.withdrawmoney()

    elif check == 4:
        user.showdetails()

    elif check == 5:
        user.updatedetails()

    elif check == 6:
        user.delete()

    elif check == 7:
        print("Thank you for using the Bank Management System.")
        break

    else:
        print("Invalid Choice.")