import requests
import tkinter as tk
from tkinter import messagebox


def get_post_by_id(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        post_data = response.json()
        return post_data
    else:
        messagebox.showerror("Ошибка", f"Не удалось получить данные для поста с id {post_id}.")
        return None

def show_post_info():
    post_id = entry.get()
    post_data = get_post_by_id(post_id)
    if post_data:
        info_text.config(state=tk.NORMAL)
        info_text.delete(1.0, tk.END)
        info_text.insert(tk.END, f"ID: {post_data['id']}\n")
        info_text.insert(tk.END, f"Пользователь ID: {post_data['userId']}\n")
        info_text.insert(tk.END, f"Заголовок: {post_data['title']}\n")
        info_text.insert(tk.END, f"Текст: {post_data['body']}")
        info_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Получение информации о посте")

label = tk.Label(root, text="Введите ID поста:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Получить информацию", command=show_post_info)
button.pack(pady=10)

info_text = tk.Text(root, height=10, width=50)
info_text.pack(pady=10)
info_text.config(state=tk.DISABLED)

root.mainloop()