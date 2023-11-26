import tkinter as tk
from tkinter import scrolledtext

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Чат")

        # Создаем список контактов
        self.contacts_listbox = tk.Listbox(self.root)
        self.contacts_listbox.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky=tk.N+tk.S)

        # Кнопка "Добавить контакт"
        self.add_contact_button = tk.Button(self.root, text="Добавить", command=self.add_contact)
        self.add_contact_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

        # Создаем поле с перепиской
        self.chat_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=20)
        self.chat_text.grid(row=0, column=1, padx=10, pady=10, rowspan=2, sticky=tk.N+tk.S+tk.E+tk.W)

        # Создаем поле ввода сообщения
        self.message_entry = tk.Entry(self.root)
        self.message_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W+tk.E)

        # Кнопка "Отправить"
        self.send_button = tk.Button(self.root, text="Отправить", command=self.send_message)
        self.send_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

    def add_contact(self):
        # Здесь вы можете добавить функционал для добавления контакта
        pass

    def send_message(self):
        message = self.message_entry.get()
        # Здесь вы можете добавить функционал для отправки сообщения
        # В данном примере, просто добавим сообщение в поле с перепиской
        self.chat_text.insert(tk.END, f"You: {message}\n")
        self.message_entry.delete(0, tk.END)

def start():
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
