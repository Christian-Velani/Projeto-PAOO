from tkinter import *
from tkinter import ttk

class Janela:
    def __init__(self, janela):
        self.__janela = janela
        self.__janela.resizable(0, 0)
        self.__janela.geometry("640x480")
        self.__janela.title("Alimentador PET")
        self.__janela.columnconfigure(0, minsize= 320)
        self.__janela.columnconfigure(1, minsize= 320)
        self.__janela.rowconfigure(0, minsize = 480)


    def telaPrincipal(self):
        # Criando os frames para dividir a tela em dois
        tela_principal_parte1 = ttk.Frame(self.__janela)
        tela_principal_parte2 = ttk.Frame(self.__janela)

        # Criando os widgets do lado que controla a ração
        titulo_racao = ttk.Label(tela_principal_parte1, text= "Controle da Ração")
        botao_area_programar_racao = ttk.Button(tela_principal_parte1, text= "Programar Hora", command= self.programarRacao, padding=(0, 20, 0, 20))
        botao_liberar_racao = ttk.Button(tela_principal_parte1, text= "Liberar Ração", command= self.liberarRacao, padding=(0, 20, 0, 20))

        # Criando os widgets do lado que controla a água
        titulo_agua = ttk.Label(tela_principal_parte2, text= "Controle da Água")
        botao_area_programar_agua = ttk.Button(tela_principal_parte2, text= "Programar Hora", command= self.programarAgua, padding=(0, 20, 0, 20))
        botao_liberar_agua = ttk.Button(tela_principal_parte2, text= "Liberar Água", command= self.liberarAgua, padding=(0, 20, 0, 20))

        # Posicionando os elementos relacionados a ração
        titulo_racao.grid(column= 1, row = 0, columnspan= 2, pady=(182, 0))
        botao_area_programar_racao.grid(column= 1, row= 1)
        botao_liberar_racao.grid(column= 2, row= 1)

        # Posicionando os elementos relacionados a água
        titulo_agua.grid(column= 1, row= 0, columnspan= 2, pady=(182, 0))
        botao_area_programar_agua.grid(column= 1, row= 1)
        botao_liberar_agua.grid(column= 2, row= 1)

        # Configurando tamanho das colunas para melhor posicionamento
        tela_principal_parte1.columnconfigure(0, minsize= 80)
        tela_principal_parte1.columnconfigure(1, minsize= 80)
        tela_principal_parte1.columnconfigure(2, minsize= 80)
        tela_principal_parte1.columnconfigure(3, minsize= 80)

        tela_principal_parte2.columnconfigure(0, minsize= 80)
        tela_principal_parte2.columnconfigure(1, minsize= 80)
        tela_principal_parte2.columnconfigure(2, minsize= 80)
        tela_principal_parte2.columnconfigure(3, minsize= 80)

        # Posicionando os frames
        tela_principal_parte1.grid(column= 0, row= 0, sticky=(W, N))
        tela_principal_parte2.grid(column= 1, row= 0, sticky=(E, N))

    def programarRacao(self):
        pass
    
    def liberarRacao(self):
        pass

    def programarAgua(self):
        pass
    
    def liberarAgua(self):
        pass

    def iniciar(self):
        self.__janela.mainloop()


janela = Janela(Tk())
janela.telaPrincipal()
janela.iniciar()

