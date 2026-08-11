import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI-Powered Student Knowledge Assistant",
    page_icon="🎓"
)

st.title("🎓 AI-Powered Student Knowledge Assistant")
st.write("Your AI-powered study companion for notes, learning and planning.")

# OpenAI API
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception:
    client = None

st.sidebar.title("📚 Menu")

menu = st.sidebar.selectbox(
    "Choose an option",
    [
        "🏠 Home",
        "🤖 AI Chatbot",
        "📄 Study Notes",
        "📚 Study Planner",
        "❓ Quiz Generator"
    ]
)

if menu == "🏠 Home":
    st.header("Welcome! 👋")
    st.write("Ask questions, organize your study notes and plan your learning.")

elif menu == "🤖 AI Chatbot":
    st.header("🤖 AI Student Chatbot")

    question = st.text_input("Ask your study question:")

    if st.button("Get Answer"):
        if not question:
            st.warning("Please enter a question.")
        elif client is None:
            st.error("OpenAI API key is not configured.")
        else:
            try:
                with st.spinner("AI is thinking..."):
                    response = client.responses.create(
                        model="gpt-4.1-mini",
                        input=f"""
You are an AI Student Assistant.
Give simple, clear and educational answers.

Student Question:
{question}
"""
                    )

                st.success("AI Answer")
                st.write(response.output_text)

            except Exception as e:
                st.error("AI response could not be generated.")
                st.write(str(e))

elif menu == "📄 Study Notes":
    st.header("📄 Study Notes")

    title = st.text_input("Note Title")
    notes = st.text_area("Write your notes:")

    if st.button("Save Note"):
        if title and notes:
            st.success("Note saved successfully!")
        else:
            st.warning("Please enter title and notes.")

elif menu == "📚 Study Planner":
    st.header("📚 Study Planner")

    subject = st.text_input("Subject")
    topic = st.text_input("Topic")
    hours = st.number_input("Study Hours", 1, 12, 2)

    if st.button("Create Study Plan"):
        if subject and topic:
            st.success("Study plan created!")
            st.write("📖 Subject:", subject)
            st.write("📌 Topic:", topic)
            st.write("⏰ Study Hours:", hours)
        else:
            st.warning("Please enter subject and topic.")

elif menu == "❓ Quiz Generator":
    st.header("❓ Quiz Generator")

    topic = st.text_input("Enter quiz topic:")

    if st.button("Generate Quiz"):
        if topic:
            st.info("AI Quiz Generator will be connected next.")
        else:
            st.warning("Please enter a topic.")
