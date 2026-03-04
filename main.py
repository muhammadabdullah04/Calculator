import streamlit as st

st.title("🧮 Calculator")

if "exp" not in st.session_state:
    st.session_state.exp = ""

# keyboard typing
st.session_state.exp = st.text_input("Type calculation", st.session_state.exp)

def press(val):
    st.session_state.exp += val

def clear():
    st.session_state.exp = ""

def calculate():
    try:
        st.session_state.exp = str(eval(st.session_state.exp))
    except:
        st.session_state.exp = "Error"

rows = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["C","0","=","+"]
]

for row in rows:
    cols = st.columns(4)
    for i in range(4):
        if row[i] == "=":
            cols[i].button("=", on_click=calculate)
        elif row[i] == "C":
            cols[i].button("C", on_click=clear)
        else:
            cols[i].button(row[i], on_click=press, args=(row[i],))