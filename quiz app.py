import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")

        self.questions = [
            {"question": "Which Indian cricketer became the fastest batsman in the world to reach 20,000 international runs mark", "answer": "Virat Kohli"},
            {"question": "Sachin Tendulkar scored his first century after playing", "answer": "78"},
            {"question": "Who hit the longest six in Cricket World Cup 2023", "answer": "Shreyas Iyer"}
        ]

        self.current_question_index = 0

        self.question_label = tk.Label(self.master, text=self.questions[self.current_question_index]["question"])
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.master, width=30)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().title()
        correct_answer = self.questions[self.current_question_index]["answer"]

        if user_answer == correct_answer:
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect!", f"Sorry, the correct answer is: {correct_answer}")

        self.answer_entry.delete(0, tk.END)  # Clear the entry
        self.next_question()

    def next_question(self):
        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question_index]["question"])
        else:
            messagebox.showinfo("Quiz Completed", "You have completed the quiz!")

# Create the main window
root = tk.Tk()
app = QuizApp(root)

# Run the main loop
root.mainloop()