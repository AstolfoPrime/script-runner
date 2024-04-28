from customtkinter import filedialog

def file_selector() -> str:
    file = filedialog.askopenfilename(initialdir="scripts", title="Select A File", filetypes=(("script files", "*.sh"), ("all files", "*.*")))
