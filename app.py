import streamlit as st
from openai import OpenAI

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="AI-Powered Student Knowledge Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🎓 AI-Powered Student Knowledge Assistant")
st.write("Your AI-powered study companion for notes, learning and planning.")

# ---------------- OPENAI API ----------------
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception:
    client = None

# ---------------- SIDEBAR ----------------
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

# ---------------- HOME ----------------
if menu == "🏠 Home":

    st.header("Welcome! 👋")

    st.write("""
    AI-Powered Student Knowledge Assistant is a simple educational
    application designed to help students with learning, notes,
    study planning and quizzes.
    """)

    st.subheader("✨ Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🤖 AI Chatbot\n\nAsk educational questions and get simple answers.")

        st.info("📄 Study Notes\n\nCreate and organize your study notes.")

        st.info("📚 Study Planner\n\nCreate a simple study plan.")

    with col2:
        st.info("❓ Quiz Generator\n\nGenerate educational quiz questions.")

        st.success("🎓 Student Friendly\n\nSimple interface for students.")

        st.success("💡 Easy to Use\n\nDesigned for quick learning support.")


# ---------------- AI CHATBOT ----------------
elif menu == "🤖 AI Chatbot":

    st.header("🤖 AI Student Chatbot")

    question = st.text_area(
        "Ask your study question:",
        placeholder="Example: What is Artificial Intelligence?"
    )

    if st.button("Get Answer", key="chat_button"):

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
Use examples when useful.
Avoid unnecessary complicated language.

Student Question:
{question}
"""
                    )

                st.success("🤖 AI Answer")
                st.write(response.output_text)

            except Exception as e:
                st.error("AI response could not be generated.")
                st.write(str(e))


# ---------------- STUDY NOTES ----------------
elif menu == "📄 Study Notes":

    st.header("📄 Study Notes")

    title = st.text_input(
        "Note Title",
        placeholder="Example: Python Functions"
    )

    notes = st.text_area(
        "Write your notes:",
        height=200,
        placeholder="Write your study notes here..."
    )

    if st.button("Save Note", key="notes_button"):

        if title and notes:

            st.success("✅ Note saved successfully!")

            st.subheader("📝 Your Note")

            st.write("**Title:**", title)
            st.write(notes)

            st.download_button(
                label="⬇️ Download Note",
                data=f"Title: {title}\n\n{notes}",
                file_name=f"{title}.txt",
                mime="text/plain"
            )

        else:
            st.warning("Please enter title and notes.")


# ---------------- STUDY PLANNER ----------------
elif menu == "📚 Study Planner":

    st.header("📚 Study Planner")

    subject = st.text_input(
        "Subject",
        placeholder="Example: Python"
    )

    topic = st.text_input(
        "Topic",
        placeholder="Example: Functions"
    )

    hours = st.number_input(
        "Study Hours",
        min_value=1,
        max_value=12,
        value=2
    )

    if st.button("Create Study Plan", key="planner_button"):

        if subject and topic:

            st.success("✅ Study plan created!")

            st.subheader("📅 Your Study Plan")

            st.write("📖 **Subject:**", subject)
            st.write("📌 **Topic:**", topic)
            st.write("⏰ **Study Hours:**", hours)

            st.write("### Suggested Schedule")

            first_half = hours / 2

            st.write(f"1️⃣ Learn concepts — {first_half:.1f} hours")
            st.write(f"2️⃣ Practice questions — {first_half:.1f} hours")
            st.write("3️⃣ Revise important points")
            st.write("4️⃣ Take a short quiz")

        else:
            st.warning("Please enter subject and topic.")


# ---------------- QUIZ GENERATOR ----------------
elif menu == "❓ Quiz Generator":

    st.header("❓ AI Quiz Generator")

    topic = st.text_input(
        "Enter quiz topic:",
        placeholder="Example: Python, AI, DBMS, Computer Networks"
    )

    number = st.slider(
        "Number of Questions",
        min_value=3,
        max_value=10,
        value=5
    )

    if st.button("Generate Quiz", key="quiz_button"):

        if not topic:
            st.warning("Please enter a quiz topic.")

        elif client is None:
            st.error("OpenAI API key is not configured.")

        else:
            try:

                with st.spinner("Generating quiz..."):

                    response = client.responses.create(
                        model="gpt-4.1-mini",
                        input=f"""
Create {number} multiple-choice questions for students.

Topic: {topic}

For every question:
- Give 4 options: A, B, C and D.
- Clearly mention the correct answer.
- Keep questions educational and easy to understand.
- Do not add unnecessary information.
"""
                    )

                st.success("✅ Quiz Generated!")

                st.write(response.output_text)

            except Exception as e:
                st.error("Quiz could not be generated.")
                st.write(str(e))
