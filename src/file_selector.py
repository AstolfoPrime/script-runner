from customtkinter import filedialog

def file_selector() -> str:
    file = str(filedialog.askopenfilename(initialdir="scripts", title="Select A File", filetypes=(("script files", "*.sh"), ("all files", "*.*")))
