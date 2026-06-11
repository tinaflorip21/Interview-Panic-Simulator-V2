from email.mime import message

from questions import *
import random
import winsound
import tkinter as tk

score = 0
try:

    with open("highscore.txt", "r") as file:
        high_score = int(file.read())

except:

    high_score = 0
current_question = 0
selected_questions = []
user_answers = []

correct_answers = 0
wrong_answers = 0

question_points = 10

time_left = 15
question_time = 15
timer_id = None
root = tk.Tk()

root.title("Interview Panic Simulator V2")
root.geometry("1000x850")
root.configure(bg="black")


# =====================
# FUNCTIONS
# =====================

def show_question():

    global time_left
    global timer_id

    time_left = question_time

    if timer_id:
        root.after_cancel(timer_id)

    question = selected_questions[current_question]

    counter_label.config(
        text=f"Question {current_question + 1}/{len(selected_questions)}"
    )

    percent = int(
    ((current_question + 1) /
     len(selected_questions)) * 100
)

    progress_label.config(
    text=f"Progress: {percent}%"
)

    score_label.config(
    text=f"Score: {score}"
)

    question_label.config(
        text=question["question"]
    )

    radio1.config(
        text=question["options"][0],
        value=question["options"][0]
    )

    radio2.config(
        text=question["options"][1],
        value=question["options"][1]
    )

    radio3.config(
        text=question["options"][2],
        value=question["options"][2]
    )

    radio4.config(
        text=question["options"][3],
        value=question["options"][3]
    )

    option_var.set("")

    countdown()

def countdown():

    global time_left
    global timer_id

    timer_label.config(
        text=f"Time Left: {time_left}"
    )

    if time_left <= 0:

        next_question()
        return

    time_left -= 1

    timer_id = root.after(
        1000,
        countdown
    )


def next_question():

    global score
    global current_question
    global correct_answers
    global wrong_answers

    selected = option_var.get()

    user_answers.append(selected)

    correct_answer = selected_questions[current_question]["answer"]

    if selected == correct_answer:

        score += question_points
        correct_answers += 1

        winsound.Beep(
            1000,
            200
        )

    else:

        wrong_answers += 1

        winsound.Beep(
            400,
            300
        )

    score_label.config(
        text=f"Score: {score}"
    )

    current_question += 1

    if current_question < len(selected_questions):
        show_question()

    else:
        show_result()


def show_result():

    global timer_id
    global high_score
    global question_label
    global restart_btn

    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None

    radio1.pack_forget()
    radio2.pack_forget()
    radio3.pack_forget()
    radio4.pack_forget()

    next_button.pack_forget()

    timer_label.config(text="")
    counter_label.config(text="")

    max_score = len(selected_questions) * 10
    if score > high_score:

        high_score = score

        with open("highscore.txt", "w") as file:
            file.write(str(high_score))

    percentage = int(
        (score / max_score) * 100
    )


    if percentage >= 80:
        message = "Excellent!\nYou're Interview Ready 🚀"

    elif percentage >= 50:
         message = "Good Job!\nKeep Practicing 👍"

    else:
        message = "PANIC DETECTED!\nPractice More 😅"
    if percentage >= 80:
        rank = "Interview Master 🏆"

    elif percentage >= 60:
        rank = "Advanced 🔥"

    elif percentage >= 40:
        rank = "Intermediate 📚"

    else:
        rank = "Beginner 🌱"

    result_text = f"""
Quiz Finished!

Score = {score}
High Score = {high_score}

Rank = {rank}

{message}
"""

    question_label.config(
    text=result_text,
    justify="center"
)

    review_text = f"""
Correct = {correct_answers}
Wrong = {wrong_answers}
"""

    review_label.config(
        text=review_text
    )

    review_label.place(
        relx=0.78,
        rely=0.45,
        anchor="center"
    )

    restart_btn.place(
        relx=0.78,
        rely=0.60,
        anchor="center"
    )


def restart_quiz():

    global timer_id

    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None

    global score
    global current_question
    global correct_answers
    global wrong_answers
    global user_answers

    score = 0
    current_question = 0
    user_answers = []

    correct_answers = 0
    wrong_answers = 0
    score_label.config(
    text="Score: 0"
)

    timer_label.config(text="")
    counter_label.config(text="")
    progress_label.config(text="")
    score_label.config(text="")
    question_label.config(text="Choose Difficulty")
    review_label.config(text="")
    review_label.place_forget()

    restart_btn.place_forget()

    radio1.pack_forget()
    radio2.pack_forget()
    radio3.pack_forget()
    radio4.pack_forget()

    next_button.pack_forget()

    easy_btn.pack(pady=10)
    medium_btn.pack(pady=10)
    hard_btn.pack(pady=10)


def start_easy():

    global selected_questions
    global current_question
    global score
    global question_points
    global correct_answers
    global wrong_answers
    global question_time
    global user_answers

    score = 0
    current_question = 0
    user_answers = []

    correct_answers = 0
    wrong_answers = 0

    selected_questions = random.sample(
    easy_questions,
    5
)
    question_points = 10
    question_time = 20

    easy_btn.pack_forget()
    medium_btn.pack_forget()
    hard_btn.pack_forget()

    radio1.pack()
    radio2.pack()
    radio3.pack()
    radio4.pack()

    next_button.pack(pady=20)

    score_label.config(text="Score: 0")

    show_question()


def start_medium():

    global selected_questions
    global current_question
    global score
    global question_points
    global correct_answers
    global wrong_answers
    global question_time
    global user_answers

    score = 0
    current_question = 0
    user_answers = []

    correct_answers = 0
    wrong_answers = 0

    selected_questions = random.sample(
        medium_questions,
        5
    )
    random.shuffle(selected_questions)
    question_points = 20
    question_time = 15

    easy_btn.pack_forget()
    medium_btn.pack_forget()
    hard_btn.pack_forget()

    radio1.pack()
    radio2.pack()
    radio3.pack()
    radio4.pack()

    next_button.pack(pady=20)

    score_label.config(text="Score: 0")

    show_question()


def start_hard():

    global selected_questions
    global current_question
    global score
    global question_points
    global correct_answers
    global wrong_answers
    global question_time
    global user_answers
    score = 0
    current_question = 0
    correct_answers = 0
    wrong_answers = 0
    user_answers = []

    question_points = 30
    question_time = 10

    selected_questions = random.sample(
        hard_questions,
        5
    )
    random.shuffle(selected_questions)

    easy_btn.pack_forget()
    medium_btn.pack_forget()
    hard_btn.pack_forget()

    radio1.pack()
    radio2.pack()
    radio3.pack()
    radio4.pack()

    next_button.pack(pady=20)

    score_label.config(text="Score: 0")

    show_question()


# =====================
# TITLE
# =====================

title = tk.Label(
    root,
    text="INTERVIEW PANIC SIMULATOR",
    fg="pink",
    bg="black",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)


# =====================
# BUTTONS
# =====================

easy_btn = tk.Button(
    root,
    text="Easy",
    width=15,
    command=start_easy
)

easy_btn.pack(pady=10)


medium_btn = tk.Button(
    root,
    text="Medium",
    width=15,
    command=start_medium
)

medium_btn.pack(pady=10)


hard_btn = tk.Button(
    root,
    text="Hard",
    width=15,
    command=start_hard
)

hard_btn.pack(pady=10)


# =====================
# LABELS
# =====================

counter_label = tk.Label(
    root,
    text="",
    fg="pink",
    bg="black",
    font=("Arial", 12, "bold")
)

counter_label.pack()

progress_label = tk.Label(
    root,
    text="",
    fg="cyan",
    bg="black",
    font=("Arial", 12, "bold")
)

progress_label.pack()

score_label = tk.Label(
    root,
    text="Score: 0",
    fg="lightgreen",
    bg="black",
    font=("Arial", 12, "bold")
)

score_label.pack()

timer_label = tk.Label(
    root,
    text="",
    fg="red",
    bg="black",
    font=("Arial", 14, "bold")
)

timer_label.pack()


question_label = tk.Label(
    root,
    text="Choose Difficulty",
    fg="white",
    bg="black",
    font=("Arial", 18)
)

question_label.pack(pady=40)

review_label = tk.Label(
    root,
    text="",
    fg="white",
    bg="black",
    font=("Arial", 10),
    justify="left"
)

review_label.place_forget()



# =====================
# OPTIONS
# =====================

option_var = tk.StringVar()

radio1 = tk.Radiobutton(
    root,
    text="",
    variable=option_var,
    bg="black",
    fg="white",
    selectcolor="black"
)

radio2 = tk.Radiobutton(
    root,
    text="",
    variable=option_var,
    bg="black",
    fg="white",
    selectcolor="black"
)

radio3 = tk.Radiobutton(
    root,
    text="",
    variable=option_var,
    bg="black",
    fg="white",
    selectcolor="black"
)

radio4 = tk.Radiobutton(
    root,
    text="",
    variable=option_var,
    bg="black",
    fg="white",
    selectcolor="black"
)


# Hide initially

radio1.pack_forget()
radio2.pack_forget()
radio3.pack_forget()
radio4.pack_forget()


# =====================
# NEXT BUTTON
# =====================

next_button = tk.Button(
    root,
    text="Next",
    width=15,
    command=next_question
)

next_button.pack_forget()


# =====================
# RESTART BUTTON
# =====================

restart_btn = tk.Button(
    root,
    text="Restart Quiz",
    width=15,
    command=restart_quiz
)

restart_btn.pack_forget()


# =====================
# START APP
# =====================

root.mainloop()