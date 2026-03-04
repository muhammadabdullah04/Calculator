import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

st.title("🧮 Calculator")

if "exp" not in st.session_state:
    st.session_state.exp = ""

def press(v):
    st.session_state.exp += v

def clear():
    st.session_state.exp = ""

def backspace():
    st.session_state.exp = st.session_state.exp[:-1]

def calculate():
    try:
        st.session_state.exp = str(eval(st.session_state.exp))
    except:
        st.session_state.exp = "Error"

colA, colB, colC = st.columns([6,1,1])

with colA:
    st.text_input("", key="exp")

with colB:
    st.button("⌫", use_container_width=True, on_click=backspace)

with colC:
    st.button("C", use_container_width=True, on_click=clear)

st.divider()


rows = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    [".","0","=","+"]
]

for row in rows:
    cols = st.columns(4)

    for i, key in enumerate(row):

        if key == "=":
            cols[i].button(
                "=",
                use_container_width=True,
                on_click=calculate,
                type="primary"
            )

        else:
            cols[i].button(
                key,
                use_container_width=True,
                on_click=press,
                args=(key,)
            )