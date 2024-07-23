import tkinter as tk

from PIL import Image, ImageTk  # Usar Pillow para formatos adicionais

# Dicionário com características dos personagens
characters = {
    "Guerreiro": {
        "nome": "Aragorn",
        "idade": 87,
        "classe": "Guerreiro",
        "terra natal": "Gondor",
        "imagem": "projeto/imagens/Aragorn.jpg",  # Caminho da imagem
    },
    "Arqueiro": {
        "nome": "Legolas",
        "idade": 2931,
        "classe": "Arqueiro",
        "terra natal": "Floresta das Trevas",
        "imagem": "projeto/imagens/legolas.jpg",  # Caminho da imagem
    },
    "Mago": {
        "nome": "Gandalf",
        "idade": "Desconhecida",
        "classe": "Mago",
        "terra natal": "Valinor",
        "imagem": "projeto/imagens/gandalf.png",  # Caminho da imagem
    },
}


def mostrar_personagem(personagem):
    # Esconder todos os frames e a tela de apresentação
    tela_apresentacao.pack_forget()
    for frame in frames.values():
        frame.pack_forget()

    if personagem:
        # Mostrar o frame do personagem selecionado
        frames[personagem].pack(fill="both", expand=True)
    else:
        # Mostrar a tela de apresentação novamente
        tela_apresentacao.pack(fill="both", expand=True)


def selecionar_personagem(personagem):
    # Esconder todos os frames e mostrar a tela final
    for frame in frames.values():
        frame.pack_forget()
    tela_final.pack(fill="both", expand=True)

    # Atualizar a mensagem da tela final
    label_final.config(
        text=f"O personagem escolhido foi {characters[personagem]['classe']}"
    )


def encerrar_programa():
    window.quit()


# Criar a janela principal
window = tk.Tk()
window.title("Jogo de Seleção de Personagem")
window.geometry("400x700")
window.config(bg="#EEE8AA")

# Criar Frame da tela de apresentação
tela_apresentacao = tk.Frame(window, bg="#EEE8AA")

# Adicionar imagem na tela de apresentação
imagem_boas_vindas = Image.open(
    "projeto/imagens/teste.jpg"
)  # Substitua pelo caminho da sua imagem
imagem_boas_vindas = imagem_boas_vindas.resize(
    (300, 200), Image.LANCZOS
)  # Ajustar o tamanho conforme necessário
imagem_boas_vindas_tk = ImageTk.PhotoImage(imagem_boas_vindas)
label_imagem_boas_vindas = tk.Label(
    tela_apresentacao, image=imagem_boas_vindas_tk, bg="#EEE8AA"
)
label_imagem_boas_vindas.pack(pady=10)

# Adicionar texto de boas-vindas
label_hello = tk.Label(
    tela_apresentacao,
    text="""Olá, seja bem-vindo ao
    SELECIONADOR DE PERSONAGEM V2
    Na próxima tela você terá 3 opções de personagens
    para sua escolha.""",
    font=("Arial", 12),
    bg="#EEE8AA",
)
label_hello.pack(pady=20)

# Botão para iniciar seleção
botao_proxima_tela = tk.Button(
    tela_apresentacao,
    text="Iniciar Seleção",
    command=lambda: mostrar_personagem("Guerreiro"),
    font=("Arial", 12),
)
botao_proxima_tela.pack(pady=20)


# Função para criar o layout dos frames de cada personagem
def criar_frame_personagem(personagem):
    frame = tk.Frame(window, bg="#EEE8AA")

    # Carregar imagem do personagem usando Pillow
    imagem = Image.open(characters[personagem]["imagem"])
    imagem = imagem.resize(
        (300, 300), Image.LANCZOS
    )  # Usar Image.LANCZOS para redimensionar
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem = tk.Label(frame, image=imagem_tk, bg="#EEE8AA")
    label_imagem.image = imagem_tk  # Manter uma referência para evitar a coleta de lixo
    label_imagem.pack(pady=10)

    # Adicionar informações do personagem
    label_nome = tk.Label(
        frame,
        text=f"Nome: {characters[personagem]['nome']}",
        font=("Arial", 16),
        bg="#EEE8AA",
    )
    label_nome.pack(pady=10)
    label_idade = tk.Label(
        frame,
        text=f"Idade: {characters[personagem]['idade']}",
        font=("Arial", 16),
        bg="#EEE8AA",
    )
    label_idade.pack(pady=10)
    label_classe = tk.Label(
        frame,
        text=f"Classe: {characters[personagem]['classe']}",
        font=("Arial", 16),
        bg="#EEE8AA",
    )
    label_classe.pack(pady=10)
    label_terra_natal = tk.Label(
        frame,
        text=f"Terra Natal: {characters[personagem]['terra natal']}",
        font=("Arial", 16),
        bg="#EEE8AA",
    )
    label_terra_natal.pack(pady=10)

    # Botões para selecionar outros personagens e voltar
    botao_frame = tk.Frame(frame, bg="#EEE8AA")
    botao_guerreiro = tk.Button(
        botao_frame,
        text="Guerreiro",
        command=lambda: mostrar_personagem("Guerreiro"),
        font=("Arial", 12),
    )
    botao_guerreiro.pack(side="left", padx=10)
    botao_arqueiro = tk.Button(
        botao_frame,
        text="Arqueiro",
        command=lambda: mostrar_personagem("Arqueiro"),
        font=("Arial", 12),
    )
    botao_arqueiro.pack(side="left", padx=10)
    botao_mago = tk.Button(
        botao_frame,
        text="Mago",
        command=lambda: mostrar_personagem("Mago"),
        font=("Arial", 12),
    )
    botao_mago.pack(side="left", padx=10)
    botao_frame.pack(pady=10)

    # Botão para selecionar o personagem
    botao_selecionar = tk.Button(
        frame,
        text="Selecionar",
        command=lambda: selecionar_personagem(personagem),
        font=("Arial", 12),
    )
    botao_selecionar.pack(pady=10)

    botao_voltar = tk.Button(
        frame, text="Voltar", command=lambda: mostrar_personagem(""), font=("Arial", 12)
    )
    botao_voltar.pack(pady=10)

    return frame


# Criar e armazenar frames para cada personagem
frames = {}
for char in characters.keys():
    frames[char] = criar_frame_personagem(char)

# Criar Tela Final
tela_final = tk.Frame(window, bg="#EEE8AA")
label_final = tk.Label(tela_final, text="", font=("Arial", 16), bg="#EEE8AA")
label_final.pack(pady=20)
botao_encerrar = tk.Button(
    tela_final, text="Encerrar", command=encerrar_programa, font=("Arial", 12)
)
botao_encerrar.pack(pady=20)

# Mostrar a tela de apresentação inicialmente
tela_apresentacao.pack(fill="both", expand=True)

# Iniciar o loop principal da aplicação
window.mainloop()
