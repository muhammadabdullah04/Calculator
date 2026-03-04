import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")
st.title("🧮 Calculator")

# Session state
if "exp" not in st.session_state:
    st.session_state.exp = ""

# Functions
def update_from_keyboard():
    st.session_state.exp = st.session_state.input_box

def press(value):
    st.session_state.exp += value
    st.session_state.input_box = st.session_state.exp

def clear():
    st.session_state.exp = ""
    st.session_state.input_box = ""

def calculate():
    try:
        expression = st.session_state.exp
        expression = expression.replace("➕","+").replace("➖","-").replace("✖","*").replace("➗","/")
        st.session_state.exp = str(eval(expression))
        st.session_state.input_box = st.session_state.exp
    except:
        st.session_state.exp = "Error"
        st.session_state.input_box = "Error"

# Keyboard input
st.text_input(
    "Type with keyboard or use buttons:",
    key="input_box",
    value=st.session_state.exp,
    on_change=update_from_keyboard
)

st.divider()

# Buttons
rows = [
    ["7","8","9","➗"],
    ["4","5","6","✖"],
    ["1","2","3","➖"],
    ["C","0","=","➕"]
]

operators = ["➕","➖","✖","➗"]

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