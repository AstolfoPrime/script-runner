import customtkinter as ctk
from file_selector import file_selector

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()

window.geometry("250x200")
window.title("Script Runner")

label = ctk.CTkLabel(master=window, text="Placeholder Text").pack(padx=10, pady=10)
button = ctk.CTkButton(master=window, text="Run", command=file_selector).pack(padx=10, pady=10)

window.mainloop()
