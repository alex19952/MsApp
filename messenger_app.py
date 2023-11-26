# from tkinter import Frame, Label, Entry, Button, Listbox, Scrollbar, Text, messagebox

# class MessengerApp(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.master.title("Messenger App")
#         self.pack()

#         # Инициализация компонентов UI
#         self.init_components()

#     def init_components(self):
#         # Реализация компонентов UI здсь
#         pass


from tkinter import Frame, Label, Button, Menu, messagebox
from login_window import LoginWindow
from chat_window import ChatWindow
from contact_search_window import ContactSearchWindow

class MessengerApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Messenger App")
        self.pack()

        # Инициализация компонентов UI
        self.init_menu()
        self.init_chat_window()
        self.init_buttons()

    def init_menu(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.master.destroy)
        menubar.add_cascade(label="File", menu=file_menu)

    def init_chat_window(self):
        self.chat_window = ChatWindow(self)

    def init_buttons(self):
        self.btn_login = Button(self, text="Login", command=self.open_login_window)
        self.btn_login.pack(side="left", padx=5)

        self.btn_search_contact = Button(self, text="Search Contact", command=self.open_contact_search_window)
        self.btn_search_contact.pack(side="left", padx=5)

    def open_login_window(self):
        login_window = LoginWindow(self)

    def open_contact_search_window(self):
        contact_search_window = ContactSearchWindow(self)

if __name__ == "__main__":
    import tkinter
    root = tkinter.Tk()
    app = MessengerApp(root)
    root.mainloop()
