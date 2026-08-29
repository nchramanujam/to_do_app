import streamlit as st
import json

st.markdown("""
<style>
div[data-baseweb="segmented-control"] button[aria-pressed="true"] {
    background-color: #28a745 !important;
    color: white !important;
    border-color: #28a745 !important;
}
</style>
""", unsafe_allow_html=True)

@st.dialog("🎯 Quiz Results")
def show_dialog(correct_answer, incorrect_answer, multiple_choice):
    if correct_answer > 8:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, #00b09b, #96c93d);
                padding: 20px;
                border-radius: 15px;
                color: white;
                text-align: center;
            ">
                <h1>🎉 PASSED!</h1>
                <h2>Score: {correct_answer}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, #ff416c, #ff4b2b);
                padding: 20px;
                border-radius: 15px;
                color: white;
                text-align: center;
            ">
                <h1>😔 FAILED</h1>
                <h2>Score: {correct_answer}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write(f"❌ Incorrect Answers: {incorrect_answer}")

    for choice in multiple_choice:
        st.markdown(
            f"""
            <div style="
                background: #f0f8ff;
                padding: 12px;
                margin: 8px 0;
                border-radius: 10px;
            ">
                <b>❓ {choice["question"]}</b><br>
                <span style="color: green;">
                    ✅ {choice["answer"]}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )



correct_answer = 0
incorrect_answer = 0


st.set_page_config(layout="wide")
st.title("Test General Knowledge")

with open('files/question.json', "r") as file:
    content = file.read()

multiple_choice = json.loads(content)
print(multiple_choice)

for choice in multiple_choice:
    st.text_input(
        label=choice["question"],
        value=choice["question"],
        key=choice["question"]
    )
    answer = st.segmented_control(
        "Choose an answer",
        choice["options"]
    )
    if answer:
        if answer == choice["answer"]:
            correct_answer += 1
        else:
            incorrect_answer += 1


if st.button("Submit Quiz"):
    show_dialog(correct_answer, incorrect_answer, multiple_choice)


