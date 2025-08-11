import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime as dt  # we'll use this to figure out 24 hours ago

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("File Transfer")

        # --- GUI setup ---
        self.sourceDir_btn = Button(self.master, text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        self.source_dir = Entry(self.master, width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

        # run it now and then run it again every day
        self.schedule_transfer()

    def sourceDir(self):
        # ask user to pick a folder and put it in the text box
        folder = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, folder)

    def destDir(self):
        # same idea but for the destination folder
        folder = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, folder)

    def transferFiles(self):
        src = self.source_dir.get()
        dest = self.destination_dir.get()

        # sanity check — need both folders to do anything
        if not src or not dest:
            print("Please pick source and destination first.")
            return

        # figure out what '24 hours ago' means
        now = dt.datetime.now()
        day_ago = dt.timedelta(hours=24)

        # loop over stuff in source folder
        for fname in os.listdir(src):
            full_path = os.path.join(src, fname)

            # skip subfolders
            if os.path.isfile(full_path):
                # last time this file was touched
                last_mod = dt.datetime.fromtimestamp(os.path.getmtime(full_path))

                # if it's within the last 24 hours, copy it over
                if now - last_mod < day_ago:
                    shutil.copy2(full_path, os.path.join(dest, fname))
                    print(f"Transferred: {fname}")
                else:
                    print(f"Skipped: {fname} (too old)")

    def schedule_transfer(self):
        """Run transfer now, then again every 24 hours."""
        self.transferFiles()
        self.master.after(24 * 60 * 60 * 1000, self.schedule_transfer)  # wait a day, then do it again

    def exit_program(self):
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
