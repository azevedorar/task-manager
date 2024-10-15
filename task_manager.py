import tkinter as tk
from tkinter import ttk
import json
import os

# Função para carregar tarefas
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

# Função para salvar tarefas
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Função para adicionar uma tarefa
def add_task():
    if task := entry.get():
        tasks.append({"task": task, "completed": False})
        update_task_list()
        save_tasks(tasks)
        entry.delete(0, tk.END)

# Função para remover uma tarefa
def remove_task():
    if selected_task := task_listbox.curselection():
        tasks.pop(selected_task[0])
        update_task_list()
        save_tasks(tasks)

# Função para marcar tarefa como concluída
def complete_task():
    if selected_task := task_listbox.curselection():
        tasks[selected_task[0]]["completed"] = True
        update_task_list()
        save_tasks(tasks)

# Função para atualizar a lista de tarefas
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

# Criação da janela principal
window = tk.Tk()  # Corrigido: tk.Tk() ao invés de tk.tk()
window.title("Gerenciador de Tarefas by Lucas")

# Estilizando a interface com ttk
style = ttk.Style()
style.configure("TButton", font=("Roboto-Black", 12), padding=5, background="red",foreground="black")
style.configure("TEntry", font=("Roboto-Black", 12), padding=15, background="green", foreground="black")

# Carregando tarefas
tasks = load_tasks()  # Corrigido: era 'task', agora é 'tasks'

# Interface gráfica
entry = ttk.Entry(window, width=40)
entry.pack(pady=10)

add_button = ttk.Button(window, text="Adicionar Tarefa", command=add_task)
add_button.pack(pady=5)

remove_button = ttk.Button(window, text="Remover Tarefa", command=remove_task)
remove_button.pack(pady=5)

complete_button = ttk.Button(window, text="Marcar como Concluída", command=complete_task)
complete_button.pack(pady=5)

task_listbox = tk.Listbox(window, width=50, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

update_task_list()

window.mainloop()
