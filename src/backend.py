from customtkinter import filedialog
import os

def file_selector() -> str:
    global file
    file = str(filedialog.askopenfilename(initialdir="scripts", title="Select A File", filetypes=(("script files", "*.sh"), ("all files", "*.*"))))
    return file

def run() -> None:
    with open(file, "r") as f:
        os.system(f"./{file}")