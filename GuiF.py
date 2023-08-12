import tkinter as tk
from Grader import *


def create_gui():
    # creates borders and general look
    window = tk.Tk()
    window.title("Final")
    window.geometry("600x800")
    window.resizable(False, False)
    left = 10

    # different fonts to choose from
    title_font = ("Times", 22, "bold")
    label_font = ("Times", 18)
    # provides spacing for title
    main_frame = tk.Frame(window)
    main_frame.pack(padx=10, pady=10)

    # title for the grader
    title_label = tk.Label(main_frame, text="Grader", font=title_font)
    title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=left, sticky="ew")


# list of functions that will be used to execute the program

    # clears all messages and entry boxes off of the screen to grade a new student

    def clear():
        error.config(text='')
        gradEnter.delete(0, tk.END)
        hme.delete(0, tk.END)
        enter2.config(state=tk.DISABLED)
        gradEnter.config(state=tk.DISABLED)
        final_label.config(text='')
        for label in grade_labels:
            label.destroy()
        grade_labels.clear()

    # determines whether input is valid or not valid
    def save():
        num = hme.get().strip()
        try:
            num = int(num)
            if num <= 0:
                raise ValueError()
        except ValueError:
            error.config(text="Invalid Input, please enter a positive integer.")
        else:
            error.config(text='')
            error.config(text=f'Enter grades for {num} classes:', wraplength=300)
            toggle_enter()

    # determines whether x amount of classes matches x amount of grades given
    # Also prints off list of letter grades and final grade
    def save2():
        # retrieves scores from input and separates them
        scores = gradEnter.get().strip()
        scores_list = scores.split()
        num_classes = int(hme.get().strip())

        # error code used for exceptions
        try:
            scores_list = [float(score) for score in scores_list]
            for score in scores_list:
                if score > 100 or score < 0:
                    errorc = "Please input a positive number between 0 and 100."
                    raise ValueError()
        except ValueError:
            # checks if value of gradEnter entry box is valid for grading, also handles error
            if any(not isinstance(score, (int,float)) for score in scores_list):
                errorc = "Please input a positive number between 0 and 100."
            error.config(text=errorc)

        else:
            error.config(text='')
            if len(scores_list) != num_classes:
                error.config(text=f"Please enter {num_classes} grades for {num_classes} classes.", wraplength=300)
            else:
                error.config(text=f"Enter {num_classes} grades for {num_classes} classes:", wraplength=300)

                letter_grades = grader(scores_list)
                final_grades = letter_grades
                gpa = calculate_gpa(letter_grades)

                for i, grade in enumerate(final_grades):
                    grade_label = tk.Label(main_frame, text=f'Class {i+1} Grade: {grade}', font=label_font)
                    grade_label.grid(row=6 + i, column=0, columnspan=2, padx=left, pady=5)
                    grade_labels.append(grade_label)

            # gpa label
            final_label.config(text=f'Cumulative GPA: {gpa:.2f} ')
            final_label.grid(row=6 + num_classes, column=0, columnspan=2, padx=left, pady=5)
            # grids the restart button
            restart_button.grid(row=7 + num_classes, column=0, columnspan=2, padx=left, pady=10)

    # toggles the state of the enter button
    def toggle_enter():
        if error.cget("text") == "Invalid Input, please enter a positive integer.":
            enter2.config(state=tk.DISABLED)
            gradEnter.config(state=tk.DISABLED)
        else:
            enter2.config(state=tk.ACTIVE)
            gradEnter.config(state=tk.NORMAL)

    # hidden enter button that will be used to begin grading
    enter2 = tk.Button(main_frame, text="Enter", width=26, command=save2)
    enter2.grid(row=5, column=1, padx=left)
    enter2.config(state=tk.DISABLED)

    # hidden entry box for class scores
    gradEnter = tk.Entry(main_frame, width=30)
    gradEnter.grid(row=4, column=1, pady=10)
    gradEnter.config(state=tk.DISABLED)

    # creating labels and entries for gui
    howmany = tk.Label(main_frame, text="Total number of classes:", font=label_font)
    howmany.grid(row=1, column=0, sticky='w', padx=left)
    hme = tk.Entry(main_frame, width=30)
    hme.grid(row=1, column=1, pady=5)

    # first enter button
    enter = tk.Button(main_frame, text="Enter", width=26, command=save)
    enter.grid(row=3, column=1, padx=left)

    # empty error label that will be used for exceptions
    error = tk.Label(main_frame, text='', wraplength=250, font=label_font)
    error.grid(row=4, column=0, pady=5)

    # empty gpa label that will be completed when save2 is executed
    final_label = tk.Label(main_frame, text='', font=label_font)

    # empty grade label list that holds the grade labels until cleared
    grade_labels = []

    restart_button = tk.Button(main_frame, text="Clear", width=26, command=clear)
    # hidden enter button that will be used to begin grading
    enter2 = tk.Button(main_frame, text="Enter", width=26, command=save2)
    enter2.grid(row=5, column=1, padx=left)
    enter2.config(state=tk.DISABLED)

    window.mainloop()


if __name__ == "__main__":
    create_gui()
