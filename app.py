import json
import random
import string
from pathlib import Path

import streamlit as st

DATABASE = "data.json"

# ----------------------------- Data helpers -----------------------------

def load_data():
    if Path(DATABASE).exists():
        try:
            with open(DATABASE, "r") as fs:
                return json.load(fs)
        except Exception:
            return []
    else:
        with open(DATABASE, "w") as fs:
            json.dump([], fs)
        return []


def save_data(data):
    with open(DATABASE, "w") as fs:
        json.dump(data, fs, indent=4)


def generate_account_number(existing):
    while True:
        acc = "".join(random.choices(string.digits, k=10))
        if not any(u["AccountNo."] == acc for u in existing):
            return acc


def find_user(data, accnumber, pin):
    matches = [u for u in data if u["AccountNo."] == accnumber and u["Pin"] == pin]
    return matches[0] if matches else None


if "data" not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data

st.set_page_config(page_title="Bank Management System", page_icon="🏦", layout="centered")
st.title("🏦 Bank Management System")

menu = st.sidebar.radio(
    "Menu",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account",
    ],
)

# ----------------------------- Create Account -----------------------------
if menu == "Create Account":
    st.header("Create Account")

    with st.form("create_account_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        email = st.text_input("Email")
        pin = st.text_input("4-digit PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Create Account")

    if submitted:
        if not name or not email:
            st.error("Name and Email are required.")
        elif age < 18:
            st.error("Sorry! Age must be at least 18.")
        elif not (pin.isdigit() and len(pin) == 4):
            st.error("PIN must be exactly 4 digits.")
        else:
            info = {
                "Name": name,
                "Age": int(age),
                "Email": email,
                "Pin": int(pin),
                "AccountNo.": generate_account_number(data),
                "Balance": 0,
            }
            data.append(info)
            save_data(data)
            st.success("Account created successfully!")
            st.json(info)
            st.info("Please save your Account Number.")

# ----------------------------- Deposit Money -----------------------------
elif menu == "Deposit Money":
    st.header("Deposit Money")

    with st.form("deposit_form"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount to deposit", min_value=0, step=1)
        submitted = st.form_submit_button("Deposit")

    if submitted:
        pin_val = int(pin) if pin.isdigit() else None
        user = find_user(data, accnumber, pin_val)
        if not user:
            st.error("Invalid Account Number or PIN.")
        elif amount <= 0:
            st.error("Invalid amount.")
        elif amount > 10000:
            st.error("Maximum deposit limit is 10000.")
        else:
            user["Balance"] += amount
            save_data(data)
            st.success("Amount deposited successfully.")
            st.metric("Current Balance", user["Balance"])

# ----------------------------- Withdraw Money -----------------------------
elif menu == "Withdraw Money":
    st.header("Withdraw Money")

    with st.form("withdraw_form"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount to withdraw", min_value=0, step=1)
        submitted = st.form_submit_button("Withdraw")

    if submitted:
        pin_val = int(pin) if pin.isdigit() else None
        user = find_user(data, accnumber, pin_val)
        if not user:
            st.error("Invalid Account Number or PIN.")
        elif amount <= 0:
            st.error("Invalid amount.")
        elif user["Balance"] < amount:
            st.error("Insufficient Balance.")
        else:
            user["Balance"] -= amount
            save_data(data)
            st.success("Withdrawal successful.")
            st.metric("Remaining Balance", user["Balance"])

# ----------------------------- Show Details -----------------------------
elif menu == "Show Details":
    st.header("Show Account Details")

    with st.form("show_form"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Show Details")

    if submitted:
        pin_val = int(pin) if pin.isdigit() else None
        user = find_user(data, accnumber, pin_val)
        if not user:
            st.error("No user found.")
        else:
            st.subheader("Account Details")
            st.json(user)

# ----------------------------- Update Details -----------------------------
elif menu == "Update Details":
    st.header("Update Account Details")

    accnumber = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password", max_chars=4, key="update_pin")

    if accnumber and pin.isdigit() and len(pin) == 4:
        user = find_user(data, accnumber, int(pin))
        if not user:
            st.error("No such user found.")
        else:
            st.caption("Leave a field blank if you don't want to change it.")
            with st.form("update_form"):
                new_name = st.text_input("New Name")
                new_email = st.text_input("New Email")
                new_pin = st.text_input("New PIN", type="password", max_chars=4)
                submitted = st.form_submit_button("Update Details")

            if submitted:
                if new_pin and (len(new_pin) != 4 or not new_pin.isdigit()):
                    st.error("PIN must be exactly 4 digits.")
                else:
                    if new_name:
                        user["Name"] = new_name
                    if new_email:
                        user["Email"] = new_email
                    if new_pin:
                        user["Pin"] = int(new_pin)
                    save_data(data)
                    st.success("Details updated successfully.")
                    st.json(user)

# ----------------------------- Delete Account -----------------------------
elif menu == "Delete Account":
    st.header("Delete Account")

    with st.form("delete_form"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        confirm = st.checkbox("I am sure I want to delete this account.")
        submitted = st.form_submit_button("Delete Account")

    if submitted:
        pin_val = int(pin) if pin.isdigit() else None
        user = find_user(data, accnumber, pin_val)
        if not user:
            st.error("No such account found.")
        elif not confirm:
            st.warning("Please check the confirmation box to delete the account.")
        else:
            data.remove(user)
            save_data(data)
            st.success("Account deleted successfully.")
