from customtkinter import *
import customtkinter
from PIL import Image
from backend import Banco
from tkinter import messagebox


class AppGPLogin(CTk, Banco):
    def __init__(self):
        super().__init__()
        self.initial_window()

    def initial_window(self):
        self.geometry("700x300")
        self.title("Tela de Login - Sistema GP Fusiontec")
        self.resizable(False, False)
        main_frame = CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.grid(row=0, column=0, padx=30, pady=30)

        # Login Window title

        lb_title = CTkLabel(master=main_frame, text="Digite suas credenciais para acessar o sistema!\n Qualquer dúvida,\n por gentileza contate o Administrador!", font=("Century Gothic Bold", 14))
        lb_title.grid(row=0, column=0, pady=10, padx=10)

        my_image = customtkinter.CTkImage(dark_image=Image.open("LogoFusiontecNovo.png"), size=(300, 150))
        image_label = customtkinter.CTkLabel(master=main_frame, image=my_image, text="")
        image_label.grid(row=1, column=0, padx=10)

        # Username label and entry box
        main_frame2 = CTkFrame(self, fg_color=self.cget("bg"))
        main_frame2.grid(row=0, column=2, padx=30, pady=30)

        user_label = CTkLabel(master=main_frame2, text="FAÇA SEU LOGIN", font=("Century Gothic bold", 22))
        user_label.grid(row=0, column=2, padx=10, pady=10)

        self.user_entry = CTkEntry(master=main_frame2, width=230)
        self.user_entry.grid(row=1, column=2, pady=10, padx=10)

        # Password label and entry box
        self.pass_entry = CTkEntry(master=main_frame2, width=230, show="*")
        self.pass_entry.grid(row=2, column=2, pady=10, padx=10)

        # Login button
        login_button = CTkButton(master=main_frame2, width=230, text="Login", command=self.button_login_function)
        login_button.grid(row=3, column=2, pady=10, padx=10, sticky="e")

        # Exit button
        exit_button = CTkButton(master=main_frame2, width=230, text="Sair", command=self.button_exit_function)
        exit_button.grid(row=4, column=2, pady=10, padx=10, sticky="e")

    def valida_login(self):
        self.username_login = self.user_entry.get()
        self.password_login = self.pass_entry.get()
        self.connect_db()
        self.cursor.execute("""SELECT Username, Password FROM Usuarios WHERE Username = ? AND Password = ?""", (self.username_login, self.password_login))
        verify_data = self.cursor.fetchone()

        try:
            if self.username_login == "" or self.password_login == "":
                messagebox.showwarning(title="Sistema GP Fusiontec - Login", message="Por favor, preencha todos os campos!")
                self.disconnect_db()

            elif self.username_login in verify_data and self.password_login in verify_data:
                messagebox.showinfo(title='Sistema GP Fusiontec - Login', message='Login realizado com sucesso!')
                self.disconnect_db()
                app.destroy()

        except:
            messagebox.showerror(title='Sistema GP Fusiontec - Login', message='ERRO! Dados não encontrados no sistema!')
            self.disconnect_db()

    def button_login_function(self):
        self.valida_login()

    def button_exit_function(self):
        app.destroy()
        print('Exit Success')


if __name__ == "__main__":
    app = AppGPLogin()
    app.mainloop()
