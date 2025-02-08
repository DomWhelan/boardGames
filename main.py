# from PyQt6.QtWidgets import QApplication, QWidget
#
# # Only needed for access to command line arguments
# import sys
#
# # You need one (and only one) QApplication instance per application.
# # Pass in sys.argv to allow command line arguments for your app.
# # If you know you won't use command line arguments QApplication([]) works too.
# app = QApplication(sys.argv)
#
# # Create a Qt widget, which will be our window.
# window = QWidget()
# window.show()  # IMPORTANT!!!!! Windows are hidden by default.
#
# # Start the event loop.
# app.exec()
#
#
# # Your application won't reach here until you exit and the event
# # loop has stopped.


import tkinter as tk
import multiprocessing

from babel.messages.checkers import checkers

import games.checkers_v2 as Checkers

root = tk.Tk()
Label = tk.Label
Button = tk.Button

def start_checkers():
    game_process = multiprocessing.Process(target=Checkers.run_game())
    game_process.start()

# CREATING A LABEL WIDGET
top_whitespace = Label(root, text=" ")
heading_1 = Label(root, text="Classic Board Games", font="20px")
my_label2 = Label(root, text="My Name is Dominic")
my_label3 = Label(root, text=" ")                   # TO CREATE WHITESPACE
test_button = Button(root,
                     text="Checkers",
                     command=start_checkers,
                     activebackground="blue",
                     activeforeground="white",
                     anchor="center",
                     bd=3,
                     bg="lightgray",
                     cursor="hand2",
                     disabledforeground="gray",
                     fg="black",
                     font=("Arial", 12),
                     height=2,
                     highlightbackground="black",
                     highlightcolor="green",
                     highlightthickness=2,
                     justify="center",
                     overrelief="raised",
                     padx=10,
                     pady=5,
                     width=15,
                     wraplength=100
                     )

# PLACING THE WIDGETS ON THE SCREEN
top_whitespace.grid(row=0)
heading_1.grid(row=1)
my_label2.grid(row=2, column=0)
my_label3.grid(row=3, column=0)
test_button.grid(row=4)


root.mainloop()
