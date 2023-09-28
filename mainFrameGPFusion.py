import sqlite3
import tkinter
from customtkinter import *
from PIL import Image
from tkcalendar import DateEntry
from tkinter import messagebox
from backend import Banco


class AppGPCadastro(CTk, Banco):
    def __init__(self):
        super().__init__()
        self.initial_window()

    def initial_window(self):
        self.geometry('1100x600')
        self.title('Sistema GP Fusiontec - Cadastro')
        self.resizable(False, False)

        self.main_frame_menu = CTkFrame(self, fg_color="#2b2b2b", width=180, height=580)
        self.main_frame_menu.grid(row=0, column=0, padx=10, pady=10)

        self.main_frame_bots = CTkFrame(self, fg_color="#2b2b2b", width=790, height=580)
        self.main_frame_bots.grid(row=0, column=1, pady=10)

        self.main_frame_cadastro = CTkFrame(self, fg_color="#2b2b2b", width=790, height=580)
        self.main_frame_cadastro.grid(row=0, column=1, pady=10, sticky="nsew")

        self.main_frame_editar = CTkFrame(self, fg_color="#2b2b2b", width=790, height=580)
        self.main_frame_editar.grid(row=0, column=1, pady=10, sticky="nsew")

        self.main_frame_atividades = CTkFrame(self, fg_color="#2b2b2b", width=790, height=580)
        self.main_frame_atividades.grid(row=0, column=1, pady=10, sticky="nsew")

        self.main_frame_view = CTkFrame(self, fg_color="#2b2b2b", width=790, height=580)
        self.main_frame_view.grid(row=0, column=1, pady=10)

        # widgets frame menu
        logo_image = CTkImage(dark_image=Image.open("LogoFusiontecNovo.png"), size=(280, 180))
        lb_image = CTkLabel(master=self.main_frame_menu, image=logo_image, text="")
        lb_image.grid(row=0, column=0, pady=72)

        self.btn_view = CTkButton(master=self.main_frame_menu, width=270, height=30, text='Visualizar Pedidos', command=self.active_frame_view)
        self.btn_view.grid(row=1, column=0, pady=10)

        self.btn_cadastro = CTkButton(master=self.main_frame_menu, width=270, height=30, text='Cadastrar Pedidos', command=self.active_frame_cadastro)
        self.btn_cadastro.grid(row=2, column=0, pady=10)

        self.btn_editar = CTkButton(master=self.main_frame_menu, width=270, height=30, text='Editar Pedidos', command=self.active_frame_editar)
        self.btn_editar.grid(row=3, column=0, pady=10)

        self.btn_atividades = CTkButton(master=self.main_frame_menu, width=270, height=30, text='Cadastrar Atividades', command=self.active_frame_atividades)
        self.btn_atividades.grid(row=4, column=0, pady=10)

        self.btn_bots = CTkButton(master=self.main_frame_menu, width=270, height=30, text='Executar Robôs', command=self.active_frame_bots)
        self.btn_bots.grid(row=5, column=0, pady=10)

        # widgets frame view

        # widgets frame cadastro
        self.lb_projeto = CTkLabel(master=self.main_frame_cadastro, text='Nome do Projeto(*):')
        self.lb_projeto.place(relx=0.1, rely=0.06, anchor=tkinter.CENTER)

        self.entry_projeto = CTkEntry(master=self.main_frame_cadastro, width=620)
        self.entry_projeto.place(relx=0.57, rely=0.06, anchor=tkinter.CENTER)

        self.lb_cliente = CTkLabel(master=self.main_frame_cadastro, text='Nome do cliente:')
        self.lb_cliente.place(relx=0.1, rely=0.12, anchor=tkinter.CENTER)

        self.entry_cliente = CTkEntry(master=self.main_frame_cadastro, width=620)
        self.entry_cliente.place(relx=0.57, rely=0.12, anchor=tkinter.CENTER)

        self.lb_email = CTkLabel(master=self.main_frame_cadastro, text='Email do cliente:')
        self.lb_email.place(relx=0.1, rely=0.18, anchor=tkinter.CENTER)

        self.entry_email = CTkEntry(master=self.main_frame_cadastro, width=620)
        self.entry_email.place(relx=0.57, rely=0.18, anchor=tkinter.CENTER)

        self.lb_inicio = CTkLabel(master=self.main_frame_cadastro, text='Inicio(*):')
        self.lb_inicio.place(relx=0.1, rely=0.24, anchor=tkinter.CENTER)

        self.entry_calendar_inicio = DateEntry(master=self.main_frame_cadastro, date_pattern='dd/mm/yyyy', font="Arial 14")
        self.entry_calendar_inicio.place(relx=0.26, rely=0.24, anchor=tkinter.CENTER)

        self.lb_prazo = CTkLabel(master=self.main_frame_cadastro, text='Prazo:')
        self.lb_prazo.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)

        self.entry_calendar_prazo = DateEntry(master=self.main_frame_cadastro, date_pattern='dd/mm/yyyy', font="Arial 14")
        self.entry_calendar_prazo.place(relx=0.26, rely=0.3, anchor=tkinter.CENTER)

        self.lb_status = CTkLabel(master=self.main_frame_cadastro, text='Status(*):')
        self.lb_status.place(relx=0.1, rely=0.36, anchor=tkinter.CENTER)

        self.opt_status = CTkOptionMenu(master=self.main_frame_cadastro, values=["OK", "EM PRODUÇÃO", "FALTA INFORMAÇÃO", "AGUARDANDO FINALIZAR", "ETAPA ROBO", "FINALIZADO"], width=300)
        self.opt_status.place(relx=0.37, rely=0.36, anchor=tkinter.CENTER)

        self.btn_cadastrar = CTkButton(master=self.main_frame_cadastro, text="Cadastrar", fg_color="green", width=300, height=60, font=("Arial", 20), command=self.input_banco)
        self.btn_cadastrar.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # widgets frame editar

        self.lb_status_editar = CTkLabel(master=self.main_frame_editar, font=("Arial", 18), text='selecione o projeto que deseja editar:')
        self.lb_status_editar.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        ############################ Conectando no banco para atualizar a lista editar ##############################
        '''conn = sqlite3.connect("sistema_gp_fusiontec.db")
        self.r_set = conn.execute("SELECT distinct(Projeto) as class FROM Pedidos")
        self.lista_editar = [r for r, in self.r_set]'''
        self.opt_lista_editar()
        ####################################################################################################################

        self.opt_atividades_editar = CTkOptionMenu(master=self.main_frame_editar, width=700, values=self.lista_editar)
        self.opt_atividades_editar.place(relx=0.5, rely=0.12, anchor=tkinter.CENTER)

        self.btn_dados = CTkButton(master=self.main_frame_editar, text="Carregar dados", fg_color="gray", width=300, command=self.load_dados, font=("Arial", 20))
        self.btn_dados.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.lb_projeto_editar = CTkLabel(master=self.main_frame_editar, text='Nome do Projeto:')
        self.lb_projeto_editar.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)

        self.entry_projeto_editar = CTkEntry(master=self.main_frame_editar, width=620)
        self.entry_projeto_editar.place(relx=0.57, rely=0.3, anchor=tkinter.CENTER)

        self.lb_cliente_editar = CTkLabel(master=self.main_frame_editar, text='Nome do cliente:')
        self.lb_cliente_editar.place(relx=0.1, rely=0.36, anchor=tkinter.CENTER)

        self.entry_cliente_editar = CTkEntry(master=self.main_frame_editar, width=620)
        self.entry_cliente_editar.place(relx=0.57, rely=0.36, anchor=tkinter.CENTER)

        self.lb_email_editar = CTkLabel(master=self.main_frame_editar, text='Email do cliente:')
        self.lb_email_editar.place(relx=0.1, rely=0.42, anchor=tkinter.CENTER)

        self.entry_email_editar = CTkEntry(master=self.main_frame_editar, width=620)
        self.entry_email_editar.place(relx=0.57, rely=0.42, anchor=tkinter.CENTER)

        self.lb_inicio_editar = CTkLabel(master=self.main_frame_editar, text='Inicio:')
        self.lb_inicio_editar.place(relx=0.1, rely=0.48, anchor=tkinter.CENTER)

        self.entry_calendar_editar = DateEntry(master=self.main_frame_editar, date_pattern='dd/mm/yyyy', font="Arial 14")
        self.entry_calendar_editar.place(relx=0.26, rely=0.48, anchor=tkinter.CENTER)

        self.lb_prazo_editar = CTkLabel(master=self.main_frame_editar, text='Prazo:')
        self.lb_prazo_editar.place(relx=0.1, rely=0.54, anchor=tkinter.CENTER)

        self.entry_calendar_prazo_editar = DateEntry(master=self.main_frame_editar, date_pattern='dd/mm/yyyy', font="Arial 14")
        self.entry_calendar_prazo_editar.place(relx=0.26, rely=0.54, anchor=tkinter.CENTER)

        self.lb_status_editar = CTkLabel(master=self.main_frame_editar, text='Status:')
        self.lb_status_editar.place(relx=0.1, rely=0.6, anchor=tkinter.CENTER)

        self.opt_status_editar = CTkOptionMenu(master=self.main_frame_editar, values=["OK", "EM PRODUÇÃO", "FALTA INFORMAÇÃO", "AGUARDANDO FINALIZAR", "ETAPA ROBO", "FINALIZADO"], width=300)
        self.opt_status_editar.place(relx=0.37, rely=0.6, anchor=tkinter.CENTER)

        self.btn_editar = CTkButton(master=self.main_frame_editar, text="Editar", fg_color="blue", width=300, font=("Arial", 20), command=self.btn_function_editar)
        self.btn_editar.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        self.btn_excluir = CTkButton(master=self.main_frame_editar, text="Excluir", fg_color="red", width=300, font=("Arial", 20), command=self.btn_function_excluir)
        self.btn_excluir.place(relx=0.5, rely=0.86, anchor=tkinter.CENTER)

        # widgets frame atividades

        ############################ Conectando no banco para atualizar a lista de atividades ##############################
        '''conn = sqlite3.connect("sistema_gp_fusiontec.db")
        self.r_set = conn.execute("SELECT distinct(Projeto) as class FROM Pedidos")
        self.lista_atividades = [r for r, in self.r_set]'''
        self.opt_lista_atividades()
        ####################################################################################################################

        self.lb_atividades = CTkLabel(master=self.main_frame_atividades, font=("Arial", 18), text='selecione o projeto que deseja adicionar tarefas:')
        self.lb_atividades.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        self.opt_atividades = CTkOptionMenu(master=self.main_frame_atividades, width=700, values=self.lista_atividades)
        self.opt_atividades.place(relx=0.5, rely=0.12, anchor=tkinter.CENTER)

        self.lb_data_atividade = CTkLabel(master=self.main_frame_atividades, text='Data da Tarefa:', font=("Arial", 14))
        self.lb_data_atividade.place(relx=0.1, rely=0.24, anchor=tkinter.CENTER)

        self.entry_data_atividade = DateEntry(master=self.main_frame_atividades, date_pattern='dd/mm/yyyy', font="Arial 14")
        self.entry_data_atividade.place(relx=0.26, rely=0.24, anchor=tkinter.CENTER)

        self.lb_tarefa = CTkLabel(master=self.main_frame_atividades, text='Tarefa:', font=("Arial", 14))
        self.lb_tarefa.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)

        self.entry_tarefa = CTkEntry(master=self.main_frame_atividades, width=620)
        self.entry_tarefa.place(relx=0.57, rely=0.3, anchor=tkinter.CENTER)

        self.btn_adicionar = CTkButton(master=self.main_frame_atividades, text="Adicionar", fg_color="green", width=200, font=("Arial", 16), command=self.add_task)
        self.btn_adicionar.place(relx=0.18, rely=0.4, anchor=tkinter.CENTER)

        self.btn_excluir = CTkButton(master=self.main_frame_atividades, text="Remover", fg_color="red", width=200, font=("Arial", 16), command=self.remove_task)
        self.btn_excluir.place(relx=0.50, rely=0.4, anchor=tkinter.CENTER)

        self.btn_atualizar = CTkButton(master=self.main_frame_atividades, text="Atualizar", fg_color="blue", width=200, font=("Arial", 16), command=self.atualiza_lista_pedidos)
        self.btn_atualizar.place(relx=0.82, rely=0.4, anchor=tkinter.CENTER)

        self.tasks_list = tkinter.Listbox(master=self.main_frame_atividades, width=75, height=13, font="Arial, 16")
        self.tasks_list.place(x=40, y=350)

####################### FUNÇÕES FRAME MENU ########################
    def active_frame_view(self):
        self.main_frame_view.tkraise()

    def active_frame_cadastro(self):
        self.main_frame_cadastro.tkraise()

    def active_frame_editar(self):
        self.main_frame_editar.tkraise()

        self.connect_db()
        r_set = self.conn.execute("SELECT distinct(Projeto) as class FROM Pedidos")
        lista_editar2 = [r for r, in r_set]
        self.opt_atividades_editar.configure(values=lista_editar2)

    def active_frame_atividades(self):
        self.main_frame_atividades.tkraise()

        self.connect_db()
        r_set = self.conn.execute("SELECT distinct(Projeto) as class FROM Pedidos")
        lista_editar2 = [r for r, in r_set]
        self.opt_atividades.configure(values=lista_editar2)

    def active_frame_bots(self):
        self.main_frame_bots.tkraise()

####################### FUNÇÕES FRAME VIEW ########################
    def btn_filtro_desempenho(self):
        pass

####################### FUNÇÕES FRAME CADASTRO ########################
    def input_banco(self):
        projeto = self.entry_projeto.get()
        cliente = self.entry_cliente.get()
        email = self.entry_email.get()
        inicio = self.entry_calendar_inicio.get()
        prazo = self.entry_calendar_prazo.get()
        status = self.opt_status.get()
        print(projeto, cliente, email, inicio, prazo, status)
        if projeto and inicio and status:
            self.connect_db()
            self.cursor.execute("""INSERT INTO Pedidos (
                        Status,
                        Prazo,
                        Inicio,
                        Email,
                        Cliente,
                        Projeto
                    )
                    VALUES (
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?
                    );""", (status, prazo, inicio, email, cliente, projeto))
            self.conn.commit()
            self.disconnect_db()
            messagebox.showinfo('Commit', 'Pedido cadastrado!')
        else:
            messagebox.showerror('Error', 'Preencha os campos obrigatórios (*)!')

####################### FUNÇÕES FRAME EDITAR ########################
    def opt_lista_editar(self):
        conn = sqlite3.connect("sistema_gp_fusiontec.db")
        r_set = conn.execute("SELECT distinct(Projeto) as class FROM Pedidos")
        self.lista_editar = [r for r, in r_set]

    def load_dados(self):
        projeto = self.opt_atividades_editar.get()
        self.connect_db()
        self.cursor.execute("""SELECT Id,
       Projeto, 
       Cliente,
       Email,
       Inicio,
       Prazo,
       Status
  FROM Pedidos
 WHERE Projeto = '{}';""".format(projeto))

        lista = self.cursor.fetchall()

        self.id_consulta_editar = lista[0][0]

        self.projeto_consulta_editar = lista[0][1]

        self.cliente_consulta_editar = lista[0][2]
        if self.cliente_consulta_editar == None:
            self.cliente_consulta_editar = " "

        self.email_consulta_editar = lista[0][3]
        if self.email_consulta_editar == None:
            self.email_consulta_editar = " "

        self.inicio_consulta_editar = lista[0][4]

        self.prazo_consulta_editar = lista[0][5]
        if self.prazo_consulta_editar == None:
            self.prazo_consulta_editar = "01/01/2023"

        self.status_consulta_editar = lista[0][6]

        self.entry_projeto_editar.delete(0, END)
        self.entry_projeto_editar.insert(0, self.projeto_consulta_editar)

        self.entry_cliente_editar.delete(0, END)
        self.entry_cliente_editar.insert(0, self.cliente_consulta_editar)

        self.entry_email_editar.delete(0, END)
        self.entry_email_editar.insert(0, self.email_consulta_editar)

        self.entry_calendar_editar.delete(0, END)
        self.entry_calendar_editar.insert(0, self.inicio_consulta_editar)

        self.entry_calendar_prazo_editar.delete(0, END)
        self.entry_calendar_prazo_editar.insert(0, self.prazo_consulta_editar)

        self.opt_status_editar.set(self.status_consulta_editar)

        self.disconnect_db()

    def btn_function_editar(self):
        projeto = self.entry_projeto_editar.get()
        cliente = self.entry_cliente_editar.get()
        email = self.entry_email_editar.get()
        inicio = self.entry_calendar_editar.get()
        prazo = self.entry_calendar_prazo_editar.get()
        status = self.opt_status_editar.get()

        answer = messagebox.askokcancel(title='Editar Pedido', message='Deseja realmente editar esse pedido?')
        if answer:
            self.connect_db()
            self.cursor.execute(
                """UPDATE Pedidos SET Projeto = ?, Cliente = ?, Email = ?, Inicio = ?, Prazo = ?, Status = ? WHERE Id = ?""",
                (projeto, cliente, email, inicio, prazo, status, self.id_consulta_editar))
            self.conn.commit()
            messagebox.showinfo(title='Editar Pedido', message='Pedido editado com sucesso')

            r_set = self.conn.execute("SELECT distinct(Projeto) as class FROM Pedidos")
            lista_editar2 = [r for r, in r_set]

            self.opt_atividades_editar.configure(values=lista_editar2)

            self.disconnect_db()

    def btn_function_excluir(self):
        projeto = self.entry_projeto_editar.get()
        cliente = self.entry_cliente_editar.get()
        email = self.entry_email_editar.get()
        inicio = self.entry_calendar_editar.get()
        prazo = self.entry_calendar_prazo_editar.get()
        status = self.opt_status_editar.get()

        answer = messagebox.askokcancel(title='Excluir Pedido', message='Deseja realmente excluir esse pedido?')
        if answer:
            self.connect_db()
            self.cursor.execute("DELETE FROM Pedidos WHERE Id = {};".format(self.id_consulta_editar))
            self.conn.commit()
            messagebox.showinfo(title='Excluir Pedido', message='Pedido deletado com sucesso')

            r_set = self.conn.execute("SELECT distinct(Projeto) as class FROM Pedidos")
            lista_editar2 = [r for r, in r_set]

            self.opt_atividades_editar.configure(values=lista_editar2)

            self.disconnect_db()


####################### FUNÇÕES FRAME ATIVIDADES ########################
    def opt_lista_atividades(self):
        conn = sqlite3.connect("sistema_gp_fusiontec.db")
        r_set = conn.execute("SELECT distinct(Projeto) as class FROM Pedidos")
        self.lista_atividades = [r for r, in r_set]

    def atualiza_lista_pedidos(self):
        projeto = self.opt_atividades.get()
        self.connect_db()
        lista = self.cursor.execute("SELECT Data, Tarefa FROM Atividades WHERE Projeto = '{}'".format(projeto))
        self.tasks_list.delete(0, END)
        for row in lista:
            texto = ' '.join(row)
            self.tasks_list.insert(0, str(texto))

    def add_task(self):
        projeto = self.opt_atividades.get()
        task1 = self.entry_data_atividade.get()
        task2 = self.entry_tarefa.get()
        if task1 and task2 and projeto:
            self.connect_db()
            self.cursor.execute("INSERT INTO Atividades (Projeto, Data, Tarefa) VALUES (?,?,?)", (projeto, task1, task2))
            self.conn.commit()
            self.disconnect_db()
            self.entry_data_atividade.delete(0, END)
            self.entry_tarefa.delete(0, END)
            self.atualiza_lista_pedidos()
        else:
            messagebox.showerror('Error', 'Adicione a data e a tarefa!')

    def remove_task(self):
        selected = self.tasks_list.selection_get()
        selectedList = selected.split(None, 1)
        projeto = self.opt_atividades.get()
        data = selectedList[0]
        tarefa = selectedList[1]
        if selected:
           self.connect_db()
           self.cursor.execute("DELETE FROM Atividades WHERE Tarefa = ? AND Projeto = ? AND Data = ?;", (tarefa, projeto, data))
           self.conn.commit()
           self.atualiza_lista_pedidos()
        else:
            messagebox.showerror('Error', 'Selecione uma tarefa para deleta-la!')


if __name__ == "__main__":
    app = AppGPCadastro()
    app.mainloop()
