import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")
st.title("🧮 Calculator")

# Store expression
if "exp" not in st.session_state:
    st.session_state.exp = ""

# Functions
def press(value):
    st.session_state.exp += value

def clear():
    st.session_state.exp = ""

def calculate():
    try:
        expression = st.session_state.exp
        expression = expression.replace("➕", "+").replace("➖", "-").replace("✖", "*").replace("➗", "/")
        st.session_state.exp = str(eval(expression))
    except:
        st.session_state.exp = "Error"

# ✅ ONE input box (keyboard typing will show here)
st.text_input("Type with keyboard OR click buttons:", key="exp")

st.divider()

# Buttons
rows = [
    ["7", "8", "9", "➗"],
    ["4", "5", "6", "✖"],
    ["1", "2", "3", "➖"],
    ["C", "0", "=", "➕"]
]

operators = ["➕", "➖", "✖", "➗"]

for row in rows:
    cols = st.columns(4)
    for i in range(4):
        if row[i] == "=":
            cols[i].button("=", use_container_width=True, on_click=calculate, type="primary")
        elif row[i] == "C":
            cols[i].button("C", use_container_width=True, on_click=clear)
        elif row[i] in operators:
            cols[i].button(row[i], use_container_width=True, on_click=press, args=(row[i],), type="primary")
        else:
            cols[i].button(row[i], use_container_width=True, on_click=press, args=(row[i],))