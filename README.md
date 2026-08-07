# 🏦 Bank Management System

A modern **Bank Management System** built with **Python**, **Streamlit**, and **Supabase**. This project provides a simple banking interface where users can create accounts, deposit and withdraw money, update account information, and securely store all data in a cloud database.

---

## 🚀 Features

- ✅ Create Bank Account
- 💰 Deposit Money
- 💸 Withdraw Money
- 👤 View Account Details
- ✏️ Update Account Details
- 🗑️ Delete Account
- ☁️ Cloud Database using Supabase
- 🔐 PIN Authentication
- 🎲 Automatic 10-Digit Account Number Generation
- 📱 User-Friendly Streamlit Interface

---

## 🛠️ Technologies Used

- Python 3.13+
- Streamlit
- Supabase
- PostgreSQL (Supabase Database)

---

## 📁 Project Structure

```
BANK/
│
├── .streamlit/
│   └── secrets.toml
│
├── app.py                 # Streamlit Application
├── bank_main.py           # Console Version
├── database.py            # Supabase Connection
├── requirements.txt
├── README.md
├── data.json              # Used by Console Version
│
└── __pycache__/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
https://github.com/PriyansMaisuriya/Bank-Management-System.git```

```bash
cd Bank-Management-System
```

---

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Supabase Configuration

Create the following file:

```
.streamlit/secrets.toml
```

Add:

```toml
SUPABASE_URL = "https://mkmkdytgppdvawlouawn.supabase.co"
SUPABASE_KEY = "sb_publishable_tzW6ZEuekd6fk4GqymUDhQ_zH80oXFZ"
```

---

## 🗄️ Create Database Table

Create a table named:

```
accounts
```

Columns:

| Column | Type |
|----------|---------|
| id | bigint (Primary Key) |
| name | text |
| age | integer |
| email | text |
| pin | integer |
| account_number | text |
| balance | integer |

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

---

## 💻 Console Version

Run:

```bash
python bank_main.py
```

This version stores data locally in `data.json`.

---

## 🌐 Streamlit Deployment

Deploy easily using:

- GitHub
- Streamlit Community Cloud

Remember to add the following secrets in Streamlit Cloud:

```
SUPABASE_URL
SUPABASE_KEY
```

---

## 📸 Screenshots

### Create Account

- Create a new account
- Auto-generated account number

### Deposit Money

- Deposit funds securely

### Withdraw Money

- Balance validation before withdrawal

### Show Details

- Display account information

### Update Details

- Update Name
- Update Email
- Update PIN

### Delete Account

- Delete account with confirmation

---

## 📌 Future Improvements

- 🔐 Login System
- 👨‍💼 Admin Dashboard
- 📊 Analytics Dashboard
- 📜 Transaction History
- 📄 PDF Bank Statement
- 📧 Email Notifications
- 📱 Mobile Responsive UI
- 💳 ATM Card Generation
- 📈 Charts & Reports
- 🔍 Search Accounts

---

## 👨‍💻 Author

**Priyans Maisuriya**

B.Sc. Information Technology Student

Aspiring Data Scientist & Python Developer

GitHub:
https://github.com/PriyansMaisuriya

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.

It motivates me to build more open-source projects.

---

## 📄 License

This project is created for learning and educational purposes.
