# 🏦 Bank Management System

A simple **Bank Management System** developed in **Python** using **JSON** for data storage. This project allows users to create bank accounts, deposit and withdraw money, update account information, and manage accounts through a console-based interface.

---

## 📌 Features

- ✅ Create a New Bank Account
- 💰 Deposit Money
- 💸 Withdraw Money
- 👤 View Account Details
- ✏️ Update Account Information
- 🗑️ Delete Bank Account
- 💾 Store Data in JSON File
- 🔐 PIN Authentication

---

## 🛠️ Technologies Used

- Python 3
- JSON
- pathlib
- random
- string

---

## 📂 Project Structure

```
bank/
│
├── bank_main.py      # Main Python Program
├── data.json         # Stores Account Information
└── README.md         # Project Documentation
```

---

## ⚙️ Requirements

- Python 3.x

No external libraries are required.

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/PriyansMaisuriya/Bank-Management-System.git
```

### 2. Open the Project Folder

```bash
cd bank
```

### 3. Run the Program

```bash
python bank_main.py
```

---

## 📋 Menu

```
====== BANK MANAGEMENT SYSTEM ======

1. Create Account
2. Deposit Money
3. Withdraw Money
4. Show Details
5. Update Details
6. Delete Account
7. Exit
```

---

## 💾 Data Storage

All account information is stored in the **data.json** file.

Example:

```json
[
    {
        "Name": "John",
        "Age": 22,
        "Email": "john@example.com",
        "Pin": 1234,
        "AccountNo.": "1234567890",
        "Balance": 5000
    }
]
```

---

## 🔒 Validation

- Minimum age must be **18 years**
- PIN must contain **exactly 4 digits**
- Deposit amount cannot exceed **₹10,000** per transaction
- Withdrawal is allowed only if sufficient balance is available

---

## 🚀 Future Improvements

- Login System
- Password Encryption
- Transaction History
- Interest Calculation
- Mini Statement
- Streamlit GUI
- SQLite/MySQL Database
- Email Notifications
- Account Search
- Admin Panel

---

## 👨‍💻 Author

**Priyans Maisuriya**

GitHub: https://github.com/PriyansMaisuriya

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.
