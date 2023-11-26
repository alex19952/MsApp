import tkinter as tk
import chat_window

def register():
    username = entry_username.get()
    password = entry_password.get()
    name = entry_name.get()

    # Добавьте свой код обработки регистрации здесь
    # Например, вы можете вывести значения или отправить их на сервер

    print("Username:", username)
    print("Password:", password)
    print("Name:", name)

    if username and password and name:
        tk.messagebox.showinfo("Успех", "Регистрация успешна!")
        
        # Создаем новое окно чата
        chat_window.start()

        # Скрываем окно регистрации
        root.withdraw()
    else:
        tk.messagebox.showerror("Ошибка", "Заполните все поля!")

# Создаем главное окно
root = tk.Tk()
root.title("Регистрация")

# Устанавливаем размеры окна
root.geometry("700x600")

# Создаем метку и поле для ввода логина
label_username = tk.Label(root, text="Логин:")
label_username.pack(pady=10)
entry_username = tk.Entry(root)
entry_username.pack(pady=10)

# Создаем метку и поле для ввода пароля
label_password = tk.Label(root, text="Пароль:")
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=10)

# Создаем метку и поле для ввода имени
label_name = tk.Label(root, text="Имя:")
label_name.pack(pady=10)
entry_name = tk.Entry(root)
entry_name.pack(pady=10)

# Создаем кнопку "Зарегистрироваться" и привязываем к ней функцию register
button_register = tk.Button(root, text="Зарегистрироваться", command=register)
button_register.pack(pady=20)

# Запускаем главный цикл обработки событий
root.mainloop()
