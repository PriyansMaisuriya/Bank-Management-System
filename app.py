import json
import random
import string
from database import supabase

import streamlit as st



# ----------------------------- Data helpers -----------------------------




def generate_account_number():
    while True:
        acc = "".join(random.choices(string.digits, k=10))

        response = (
            supabase.table("accounts")
            .select("account_number")
            .eq("account_number", acc)
            .execute()
        )

        if len(response.data) == 0:
            return acc


def find_user(accnumber, pin):
    response = (
        supabase.table("accounts")
        .select("*")
        .eq("account_number", accnumber)
        .eq("pin", pin)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None


response = supabase.table("accounts").select("*").execute()
data = response.data
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
            # Check if email already exists
            existing = (
                supabase.table("accounts")
                .select("email")
                .eq("email", email)
                .execute()
            )

            if existing.data:
                st.error("Email already exists.")

            else:
                account_number = generate_account_number()

                supabase.table("accounts").insert(
                    {
                        "name": name,
                        "age": int(age),
                        "email": email,
                        "pin": int(pin),
                        "account_number": account_number,
                        "balance": 0,
                    }
                ).execute()

                st.success("🎉 Account Created Successfully!")

                st.info(f"Your Account Number is: **{account_number}**")

                st.write("### Account Details")
                st.write(f"**Name:** {name}")
                st.write(f"**Age:** {age}")
                st.write(f"**Email:** {email}")
                st.write("**Balance:** ₹0")

# ----------------------------- Deposit Money -----------------------------
elif menu == "Deposit Money":
    st.header("Deposit Money")

    with st.form("deposit_form"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount to Deposit", min_value=1, step=1)
        submitted = st.form_submit_button("Deposit")

    if submitted:

        if not pin.isdigit():
            st.error("PIN must be numeric.")

        else:
            user = find_user(accnumber, int(pin))

            if not user:
                st.error("Invalid Account Number or PIN.")

            elif amount > 10000:
                st.error("Maximum deposit limit is ₹10,000.")

            else:
                new_balance = user["balance"] + amount

                (
                    supabase.table("accounts")
                    .update({"balance": new_balance})
                    .eq("account_number", accnumber)
                    .execute()
                )

                st.success("✅ Amount Deposited Successfully!")

                st.metric("Current Balance", f"₹{new_balance}")
# ----------------------------- Withdraw Money -----------------------------
elif menu == "Withdraw Money":
    st.header("Withdraw Money")

    with st.form("withdraw_form"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount to Withdraw", min_value=1, step=1)
        submitted = st.form_submit_button("Withdraw")

    if submitted:

        if not pin.isdigit():
            st.error("PIN must be numeric.")

        else:
            user = find_user(accnumber, int(pin))

            if not user:
                st.error("Invalid Account Number or PIN.")

            elif amount > user["balance"]:
                st.error("Insufficient Balance.")

            else:
                new_balance = user["balance"] - amount

                (
                    supabase.table("accounts")
                    .update({"balance": new_balance})
                    .eq("account_number", accnumber)
                    .execute()
                )

                st.success("✅ Withdrawal Successful!")

                st.metric("Remaining Balance", f"₹{new_balance}")
# ----------------------------- Show Details -----------------------------
elif menu == "Show Details":
    st.header("Show Account Details")

    with st.form("show_form"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Show Details")

    if submitted:

        if not pin.isdigit():
            st.error("PIN must be numeric.")

        else:
            user = find_user(accnumber, int(pin))

            if not user:
                st.error("No user found.")

            else:
                st.success("Account Found!")

                st.write("## Account Details")

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Name:** {user['name']}")
                    st.write(f"**Age:** {user['age']}")
                    st.write(f"**Email:** {user['email']}")

                with col2:
                    st.write(f"**Account Number:** {user['account_number']}")
                    st.write(f"**Balance:** ₹{user['balance']}")


# ----------------------------- Update Details -----------------------------
elif menu == "Update Details":
    st.header("Update Account Details")

    accnumber = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password", max_chars=4)

    if accnumber and pin.isdigit():

        user = find_user(accnumber, int(pin))

        if not user:
            st.error("Invalid Account Number or PIN.")

        else:

            with st.form("update_form"):

                new_name = st.text_input("New Name", value=user["name"])
                new_email = st.text_input("New Email", value=user["email"])
                new_pin = st.text_input(
                    "New PIN",
                    value=str(user["pin"]),
                    max_chars=4,
                    type="password"
                )

                submitted = st.form_submit_button("Update")

            if submitted:

                if len(new_pin) != 4 or not new_pin.isdigit():
                    st.error("PIN must be exactly 4 digits.")

                else:

                    (
                        supabase.table("accounts")
                        .update(
                            {
                                "name": new_name,
                                "email": new_email,
                                "pin": int(new_pin)
                            }
                        )
                        .eq("account_number", accnumber)
                        .execute()
                    )

                    st.success("✅ Account Updated Successfully!")


# ----------------------------- Delete Account -----------------------------
elif menu == "Delete Account":
    st.header("Delete Account")

    with st.form("delete_form"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        confirm = st.checkbox("I understand this action cannot be undone.")
        submitted = st.form_submit_button("Delete Account")

    if submitted:

        if not pin.isdigit():
            st.error("PIN must be numeric.")

        else:
            user = find_user(accnumber, int(pin))

            if not user:
                st.error("Invalid Account Number or PIN.")

            elif not confirm:
                st.warning("Please confirm account deletion.")

            else:
                (
                    supabase.table("accounts")
                    .delete()
                    .eq("account_number", accnumber)
                    .execute()
                )

                st.success("✅ Account Deleted Successfully!")
            
