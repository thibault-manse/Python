import customtkinter as ctk 
from login_guest_ui import LoginGuestUi

if __name__ == "__main__":
    root = ctk.CTk()
    app = LoginGuestUi(root)
    root.mainloop()