import tkinter as tk
from tkinter import *
import webbrowser
import os

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Web Page Generator")
        self.master.resizable(width=False, height=False)
        self.master.config(bg="lightgray")

        # Label at the top
        self.lbl = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5))

        # Entry field for custom text
        self.txt_entry = Entry(self.master, width=75)
        self.txt_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=(5, 10))

        # Buttons
        self.btn_default = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn_default.grid(row=2, column=0, padx=10, pady=10)

        self.btn_custom = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn_custom.grid(row=2, column=1, padx=10, pady=10)

    # Generate page with default text
    def defaultHTML(self):
        self.createHTML("Stay tuned for our amazing summer sale!")

    # Generate page with custom text from entry
    def customHTML(self):
        user_text = self.txt_entry.get().strip()
        if not user_text:
            user_text = "You didn’t enter any text. Showing default message."
        self.createHTML(user_text)

    # Write HTML file and open it in a browser
    def createHTML(self, content):
        html = f"""
        <html>
            <body>
                <h1>{content}</h1>
            </body>
        </html>
        """
        file_path = os.path.join(os.getcwd(), "index.html")
        with open(file_path, "w") as f:
            f.write(html)

        webbrowser.open_new_tab(file_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()
