import tkinter as tk
from tkinter import messagebox, ttk

# Estilos globais para harmonizar a aparência
BG_MAIN = "#E8EEF1"
BG_CARD = "#F5F5F5"
BTN_BG = "#2E86AB"
BTN_FG = "white"
FONT_TITLE = ("Segoe UI", 14, "bold")
FONT_NORMAL = ("Segoe UI", 11)
BTN_FONT = ("Segoe UI", 11, "bold")

def setup_style(root=None):
    style = ttk.Style()
    try:
        style.theme_use('clam')
    except Exception:
        pass
    style.configure('TCombobox', font=FONT_NORMAL)
    if root:
        root.option_add('*Font', FONT_NORMAL)

alunos = []
professores = []
disciplina = []



def abrir_cadastro_aluno():
    clear_content()
    tk.Label(content_frame, text="Cadastrar Aluno", bg=BG_CARD, font=FONT_TITLE).pack(pady=8)
    form = tk.Frame(content_frame, bg=BG_CARD)
    form.pack(padx=8, pady=4)

    tk.Label(form, text="Nome do Aluno:", bg=BG_CARD, font=FONT_NORMAL).grid(row=0, column=0, sticky="w", pady=4)
    entry_nome_aluno = tk.Entry(form, width=40, font=FONT_NORMAL)
    entry_nome_aluno.grid(row=0, column=1, pady=4)

    tk.Label(form, text="CPF:", bg=BG_CARD, font=FONT_NORMAL).grid(row=1, column=0, sticky="w", pady=4)
    entry_cpf = tk.Entry(form, width=40, font=FONT_NORMAL)
    entry_cpf.grid(row=1, column=1, pady=4)

    tk.Label(form, text="Data de Nascimento (DD/MM/AAAA):", bg=BG_CARD, font=FONT_NORMAL).grid(row=2, column=0, sticky="w", pady=4)
    entry_dob = tk.Entry(form, width=40, font=FONT_NORMAL)
    entry_dob.grid(row=2, column=1, pady=4)

    tk.Label(form, text="Email:", bg=BG_CARD, font=FONT_NORMAL).grid(row=3, column=0, sticky="w", pady=4)
    entry_email = tk.Entry(form, width=40, font=FONT_NORMAL)
    entry_email.grid(row=3, column=1, pady=4)

    tk.Label(form, text="Matrícula:", bg=BG_CARD, font=FONT_NORMAL).grid(row=4, column=0, sticky="w", pady=4)
    entry_matricula = tk.Entry(form, width=40, font=FONT_NORMAL)
    entry_matricula.grid(row=4, column=1, pady=4)


    def salvar_aluno():
        nome = entry_nome_aluno.get().strip()
        cpf = entry_cpf.get().strip()
        dob = entry_dob.get().strip()
        email = entry_email.get().strip()
        matricula = entry_matricula.get().strip()
        if not nome or not cpf or not dob or not email or not matricula:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return
        # Validação simples de email
        if "@" not in email or "." not in email:
            messagebox.showwarning("Aviso", "Email inválido.")
            return
        alunos.append({"nome": nome, "cpf": cpf, "dob": dob, "email": email})
        messagebox.showinfo("Sucesso", f"Aluno '{nome}' cadastrado com sucesso!")
        clear_content()

    tk.Button(content_frame, text="Salvar Aluno", command=salvar_aluno, bg=BTN_BG, fg=BTN_FG, font=BTN_FONT, width=20).pack(pady=10)

def abrir_cadastro_professor():
    clear_content()
    tk.Label(content_frame, text="Cadastrar Professor", bg=BG_CARD, font=FONT_TITLE).pack(pady=8)
    form = tk.Frame(content_frame, bg=BG_CARD)
    form.pack(padx=8, pady=4)

    tk.Label(form, text="Nome do Professor:", bg=BG_CARD, font=FONT_NORMAL).grid(row=0, column=0, sticky="w", pady=6)
    entry_nome_prof = tk.Entry(form, width=40, font=FONT_NORMAL)
    entry_nome_prof.grid(row=0, column=1, pady=6)

    tk.Label(form, text="CPF:", bg=BG_CARD, font=FONT_NORMAL).grid(row=1, column=0, sticky="w", pady=4)
    entry_cpf = tk.Entry(form, width=40, font=FONT_NORMAL)
    entry_cpf.grid(row=1, column=1, pady=4)

    tk.Label(form, text="Data de Nascimento (DD/MM/AAAA):", bg=BG_CARD, font=FONT_NORMAL).grid(row=2, column=0, sticky="w", pady=4)
    entry_dob = tk.Entry(form, width=40, font=FONT_NORMAL)
    entry_dob.grid(row=2, column=1, pady=4)

    tk.Label(form, text="Email:", bg=BG_CARD, font=FONT_NORMAL).grid(row=3, column=0, sticky="w", pady=4)
    entry_email = tk.Entry(form, width=40, font=FONT_NORMAL)
    entry_email.grid(row=3, column=1, pady=4)

    def salvar_professor():
        nome = entry_nome_prof.get().strip()
        cpf = entry_cpf.get().strip()
        dob = entry_dob.get().strip()
        email = entry_email.get().strip()
        if not nome or not cpf or not dob or not email:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
            return
        if nome != "":
            professores.append(nome)
            messagebox.showinfo("Sucesso", f"Professor '{nome}' cadastrado com sucesso!")
            clear_content()
        else:
            messagebox.showwarning("Aviso", "Por favor, digite um nome.")

    tk.Button(content_frame, text="Salvar Professor", command=salvar_professor, bg=BTN_BG, fg=BTN_FG, font=BTN_FONT, width=20).pack(pady=10)
def abrir_disciplina():
    clear_content()
    tk.Label(content_frame, text="Cadastrar Disciplina", bg=BG_CARD, font=FONT_TITLE).pack(pady=8)
    form = tk.Frame(content_frame, bg=BG_CARD)
    form.pack(padx=8, pady=4)

    tk.Label(form, text="Nome da Disciplina:", bg=BG_CARD, font=FONT_NORMAL).grid(row=0, column=0, sticky="w", pady=6)
    entry_nome_disc = tk.Entry(form, width=40, font=FONT_NORMAL)
    entry_nome_disc.grid(row=0, column=1, pady=6)

    tk.Label(form, text="Descrição:", bg=BG_CARD, font=FONT_NORMAL).grid(row=1, column=0, sticky="w", pady=6)
    entry_des_disc = tk.Entry(form, width=40, font=FONT_NORMAL)
    entry_des_disc.grid(row=1, column=1, pady=6)

    # Combobox para selecionar professor
    tk.Label(form, text="Professor:", bg=BG_CARD, font=FONT_NORMAL).grid(row=2, column=0, sticky="w", pady=6)
    var_prof = tk.StringVar()
    valores_prof = professores if professores else ["(Nenhum professor cadastrado)"]
    combo_prof_disc = ttk.Combobox(form, textvariable=var_prof, values=valores_prof, width=36, state="readonly")
    combo_prof_disc.grid(row=2, column=1, pady=6)

    def on_prof_selected(event=None):
        sel = var_prof.get()
        match sel:
            case "(Nenhum professor cadastrado)":
                messagebox.showwarning("Aviso", "Nenhum professor disponível para vincular.")
            case "":
                messagebox.showinfo("Info", "Nenhum professor selecionado.")
            case _:
                messagebox.showinfo("Professor Selecionado", f"Professor '{sel}' vinculado à disciplina.")

    combo_prof_disc.bind("<<ComboboxSelected>>", on_prof_selected)

    def salvar_disciplina():
        nome = entry_nome_disc.get().strip()
        desc = entry_des_disc.get().strip()
        prof = var_prof.get()
        if nome == "":
            messagebox.showwarning("Aviso", "Digite o nome da disciplina.")
            return
        if prof == "(Nenhum professor cadastrado)":
            prof = ""
        disciplina.append({"nome": nome, "descricao": desc, "professor": prof})
        messagebox.showinfo("Sucesso", f"Disciplina '{nome}' cadastrada com sucesso.")
        clear_content()

    tk.Button(content_frame, text="Salvar Disciplina", command=salvar_disciplina, bg=BTN_BG, fg=BTN_FG, font=BTN_FONT, width=20).pack(pady=8)

def listar_cadastros():
    clear_content()
    tk.Label(content_frame, text="Lista de Cadastros", bg=BG_CARD, font=FONT_TITLE).pack(pady=8)

    # Alunos
    tk.Label(content_frame, text="Alunos", bg=BG_CARD, font=FONT_NORMAL).pack(anchor="w", padx=8)
    frame_al = tk.Frame(content_frame, bg=BG_CARD)
    frame_al.pack(fill="x", padx=8, pady=4)
    cols_al = ("nome", "cpf", "dob", "email", "matricula")
    tree_al = ttk.Treeview(frame_al, columns=cols_al, show="headings", height=6)
    for col, heading, width in (("nome", "Nome", 200), ("cpf", "CPF", 120), ("dob", "Nasc", 120), ("email", "Email", 220), ("matricula", "Matrícula", 100)):
        tree_al.heading(col, text=heading)
        tree_al.column(col, width=width)
    sb_al = tk.Scrollbar(frame_al, orient="vertical", command=tree_al.yview)
    tree_al.configure(yscrollcommand=sb_al.set)
    tree_al.pack(side="left", fill="x", expand=True)
    sb_al.pack(side="right", fill="y")

    for a in alunos:
        if isinstance(a, str):
            tree_al.insert("", "end", values=(a, "", "", "", ""))
        else:
            tree_al.insert("", "end", values=(a.get("nome", ""), a.get("cpf", ""), a.get("dob", ""), a.get("email", ""), a.get("matricula", "")))

    # Professores
    tk.Label(content_frame, text="Professores", bg=BG_CARD, font=FONT_NORMAL).pack(anchor="w", padx=8, pady=(12,0))
    frame_pr = tk.Frame(content_frame, bg=BG_CARD)
    frame_pr.pack(fill="x", padx=8, pady=4)
    cols_pr = ("nome", "cpf", "dob", "email")
    tree_pr = ttk.Treeview(frame_pr, columns=cols_pr, show="headings", height=6)
    for col, heading, width in (("nome", "Nome", 200), ("cpf", "CPF", 150), ("dob", "Nasc", 120), ("email", "Email", 220)):
        tree_pr.heading(col, text=heading)
        tree_pr.column(col, width=width)
    sb_pr = tk.Scrollbar(frame_pr, orient="vertical", command=tree_pr.yview)
    tree_pr.configure(yscrollcommand=sb_pr.set)
    tree_pr.pack(side="left", fill="x", expand=True)
    sb_pr.pack(side="right", fill="y")

    for p in professores:
        if isinstance(p, str):
            tree_pr.insert("", "end", values=(p, "", "", ""))
        else:
            tree_pr.insert("", "end", values=(p.get("nome", ""), p.get("cpf", ""), p.get("dob", ""), p.get("email", "")))

def listar_disciplinas():
    clear_content()
    tk.Label(content_frame, text="Lista de Disciplinas", bg=BG_CARD, font=FONT_TITLE).pack(pady=8)
    if not disciplina:
        tk.Label(content_frame, text="Nenhuma disciplina cadastrada.", bg=BG_CARD, font=FONT_NORMAL).pack(pady=8)
        return

    # Treeview com colunas: Nome, Descrição, Professor
    cols = ("nome", "descricao", "professor")
    tree = ttk.Treeview(content_frame, columns=cols, show="headings", height=10)
    tree.heading("nome", text="Nome")
    tree.heading("descricao", text="Descrição")
    tree.heading("professor", text="Professor")
    tree.column("nome", width=200)
    tree.column("descricao", width=250)
    tree.column("professor", width=150)

    # Scrollbar
    sb = tk.Scrollbar(content_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=sb.set)
    sb.pack(side="right", fill="y", padx=(0,8), pady=4)
    tree.pack(side="left", fill="both", expand=True, padx=8, pady=4)

    for d in disciplina:
        nome = d.get("nome", "") if isinstance(d, dict) else str(d)
        desc = d.get("descricao", "") if isinstance(d, dict) else ""
        prof = d.get("professor", "") if isinstance(d, dict) else ""
        tree.insert("", "end", values=(nome, desc, prof))

def remover_cliente():
    messagebox.showinfo("Aviso", "A função de remover ainda será implementada!")

def sair():
    janela_principal.destroy()

# --- INTERFACE PRINCIPAL (O MENU) ---

janela_principal = tk.Tk()
janela_principal.title("Sistema de Notas - Menu Principal")
janela_principal.geometry("720x520")
janela_principal.configure(bg=BG_MAIN)

setup_style(janela_principal)

tk.Label(janela_principal, text="Sistema de Notas", font=FONT_TITLE, bg=BG_MAIN).pack(pady=12)

# Área de navegação lateral
nav_frame = tk.Frame(janela_principal, bg=BG_MAIN)
nav_frame.pack(side="left", fill="y", padx=12, pady=12)

content_frame = tk.Frame(janela_principal, bg=BG_CARD)
content_frame.pack(side="right", expand=True, fill="both", padx=12, pady=12)

def clear_content():
    for w in content_frame.winfo_children():
        w.destroy()

# Criando os botões do Menu (estilizados) na barra lateral
tk.Button(nav_frame, text="Cadastrar Aluno", command=abrir_cadastro_aluno, bg=BTN_BG, fg=BTN_FG, font=BTN_FONT, width=20).pack(pady=6)
tk.Button(nav_frame, text="Cadastrar Professor", command=abrir_cadastro_professor, bg=BTN_BG, fg=BTN_FG, font=BTN_FONT, width=20).pack(pady=6)
tk.Button(nav_frame, text="Cadastrar Disciplina", command=abrir_disciplina, bg=BTN_BG, fg=BTN_FG, font=BTN_FONT, width=20).pack(pady=6)
tk.Button(nav_frame, text="Listar Cadastros", command=listar_cadastros, bg=BTN_BG, fg=BTN_FG, font=BTN_FONT, width=20).pack(pady=6)
tk.Button(nav_frame, text="Listar Disciplinas", command=listar_disciplinas, bg=BTN_BG, fg=BTN_FG, font=BTN_FONT, width=20).pack(pady=6)
tk.Button(nav_frame, text="Remover Cliente", command=remover_cliente, bg=BTN_BG, fg=BTN_FG, font=BTN_FONT, width=20).pack(pady=6)
tk.Button(nav_frame, text="Sair", command=sair, bg="#6C757D", fg=BTN_FG, font=BTN_FONT, width=20).pack(pady=18)
tk.Label(content_frame, text="Bem-vindo! Use o menu à esquerda.", bg=BG_CARD, font=FONT_NORMAL).pack(padx=8, pady=8)

janela_principal.mainloop()