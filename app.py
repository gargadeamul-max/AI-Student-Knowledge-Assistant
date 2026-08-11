import streamlit as st

st.set_page_config(
    page_title="AI-Powered Student Knowledge Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Powered Student Knowledge Assistant")
st.write("Your AI-powered study companion for notes, learning and planning.")

menu = st.sidebar.selectbox(
    "Choose an option",
    ["🏠 Home", "🤖 AI Chatbot", "📄 Study Notes", "📚 Study Planner", "❓ Quiz Generator"]
)

if menu == "🏠 Home":
    st.header("Welcome! 👋")
    st.write("Ask questions, organize your study notes and plan your learning.")
    st.info("Select an option from the menu to get started.")

elif menu == "🤖 AI Chatbot":
    st.header("🤖 AI Student Chatbot")
    question = st.text_input("Ask your study question:")

    if st.button("Get Answer"):
        if question.strip():
            st.success("Your question was received!")
            st.write("AI response will be connected in the next version.")
        else:
            st.warning("Please enter a question.")

elif menu == "📄 Study Notes":
    st.header("📄 Study Notes")
    title = st.text_input("Note Title")
    notes = st.text_area("Write your notes here:")

    if st.button("Save Note"):
        if title and notes:
            st.success("Note saved successfully!")
            st.write("###", title)
            st.write(notes)
        else:
            st.warning("Please enter both title and notes.")

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
            st.success(f"Quiz generation for '{topic}' will be connected to AI.")
        else:
            st.warning("Please enter a topic.")
