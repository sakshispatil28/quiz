import streamlit as st

# Define the quiz questions, options, and correct answers
questions = [
    "What is the largest ocean on Earth?",
    "Who is known as the 'Father of Computer Science'?",
    "Which element has the chemical symbol 'O'?",
    "What is the capital of Japan?",
]

options = [
    ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
    ["Alan Turing", "Bill Gates", "Steve Jobs", "Mark Zuckerberg"],
    ["Oxygen", "Gold", "Silver", "Iron"],
    ["Beijing", "Seoul", "Tokyo", "Bangkok"],
]

correct_answers = [0, 0, 0, 2]  # Index of correct options for each question

# Initialize variables for keeping track of user responses and final score
user_responses = []
score = 0

# Streamlit app
st.title("Quiz App")

# Display each question and options for user selection
for i, question in enumerate(questions):
    st.subheader(f"Q{i + 1}: {question}")
    selected_option = st.radio("Choose an option", options[i])
    user_responses.append(selected_option)

# Submit button to calculate score and display correct answers
if st.button("Submit Quiz"):
    # Calculate the score based on user responses
    for i in range(len(questions)):
        if options[i].index(user_responses[i]) == correct_answers[i]:
            score += 1

    # Display correct answers
    st.subheader("Correct Answers:")
    for i, question in enumerate(questions):
        st.write(f"Q{i + 1}: {question}")
        st.write(f"Correct Answer: {options[i][correct_answers[i]]}")
        st.write("")

    # Display final score
    st.subheader("Your Final Score:")
    st.write(f"You scored {score} out of {len(questions)}")
