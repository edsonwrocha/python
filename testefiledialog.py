import tkinter as tk
from tkinter import filedialog

# Função para selecionar arquivos
def selecionar_arquivos():
    root = tk.Tk()
    root.withdraw()
    # Mostrar janela para selecionar arquivos
    file_path = filedialog.askopenfilenames()
    print(file_path)

# Criar janela
janela = tk.Tk()
janela.title("Selecionar Arquivos")

# Criar botão para selecionar arquivos
botao = tk.Button(janela, text="Selecionar Arquivos", command=selecionar_arquivos)
botao.pack()

# Iniciar loop principal da janela
janela.mainloop()