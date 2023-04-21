from tkinter import *
from tkinter import ttk
import datetime
import threading
import time

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
        self.limpar_tela()
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

    def limpar_tela(self):
        """
            Função para limpar todos os elementos da tela
        """
        widgets = self.__janela.grid_slaves()
        for widget in widgets:
            widget.destroy()
    
    def confirmarRacao(self, hora, minuto):
        with open('Configurações.txt', 'r') as configuracoes_leitura:
            atual = configuracoes_leitura.readlines()
        with open('Configurações.txt', 'w') as configuracoes_escrever:
            atual[0] = hora + '\n'
            atual[1] = minuto + '\n'
            for valor in atual:
                configuracoes_escrever.write(valor)
        self.telaPrincipal()

    def confirmarAgua(self, hora, minuto):
        with open('Configurações.txt', 'r') as configuracoes_leitura:
            atual = configuracoes_leitura.readlines()
        with open('Configurações.txt', 'w') as configuracoes_escrever:
            atual[3] = hora + '\n'
            atual[4] = minuto + '\n'
            for valor in atual:
                configuracoes_escrever.write(valor)
        self.telaPrincipal()

    def programarRacao(self):

        self.limpar_tela()

        with open("Configurações.txt", "r") as configuracoes:
            horarios = configuracoes.readlines()
            horaAtual = horarios[0]
            minAtual = horarios[1]

        # Criando os frames para dividir a tela em dois
        programarRacao1 = ttk.Frame(self.__janela)
        programarRacao2 = ttk.Frame(self.__janela)

        atual = ttk.Label(programarRacao1, text= "Horário atual:")
        hora_atual = ttk.Label(programarRacao1, text= horaAtual)
        min_atual = ttk.Label(programarRacao1, text= minAtual)
        comboboxTexto = ttk.Label(programarRacao2, text= "Novo Horário")
        horaCombo = ttk.Combobox(programarRacao2)
        horaCombo['values'] = [i for i in range(00,24)]
        horaCombo.state(['readonly'])
        horaCombo.set("00")
        minutoCombo = ttk.Combobox(programarRacao2)
        minutoCombo['values'] = [i for i in range(00, 60)]
        minutoCombo.state(['readonly'])
        minutoCombo.set("00")
        botao = ttk.Button(programarRacao1, text= "Confirmar", command= lambda: self.confirmarRacao(horaCombo.get(), minutoCombo.get()))

        atual.grid(row= 0, column= 1, columnspan= 2, pady= (182, 0))
        hora_atual.grid(row= 1, column= 1)
        min_atual.grid(row= 1, column= 2)
        comboboxTexto.grid(row= 0, column= 0, columnspan= 2, pady= (182, 0))
        horaCombo.grid(row= 1, column= 0)
        minutoCombo.grid(row= 1, column= 1)
        botao.grid(row= 2, column= 3, columnspan= 2)
        
        # Configurando tamanho das colunas para melhor posicionamento
        programarRacao1.columnconfigure(0, minsize= 80)
        programarRacao1.columnconfigure(1, minsize= 80)
        programarRacao1.columnconfigure(2, minsize= 80)
        programarRacao1.columnconfigure(3, minsize= 80)

        programarRacao2.columnconfigure(0, minsize= 80)
        programarRacao2.columnconfigure(1, minsize= 80)
        programarRacao2.columnconfigure(2, minsize= 80)
        programarRacao2.columnconfigure(3, minsize= 80)

        programarRacao1.grid(column= 0, row= 0, sticky=(W, N))
        programarRacao2.grid(column= 1, row= 0, sticky=(E, N))
    
    def liberarRacao(self):
        pass

    def programarAgua(self):

        self.limpar_tela()

        with open("Configurações.txt", "r") as configuracoes:
            horarios = configuracoes.readlines()
            horaAtual = horarios[0]
            minAtual = horarios[1]

        # Criando os frames para dividir a tela em dois
        programarAgua1 = ttk.Frame(self.__janela)
        programarAgua2 = ttk.Frame(self.__janela)

        atual = ttk.Label(programarAgua1, text= "Horário atual:")
        hora_atual = ttk.Label(programarAgua1, text= horaAtual)
        min_atual = ttk.Label(programarAgua1, text= minAtual)
        comboboxTexto = ttk.Label(programarAgua2, text= "Novo Horário")
        horaCombo = ttk.Combobox(programarAgua2)
        horaCombo['values'] = [i for i in range(00,24)]
        horaCombo.state(['readonly'])
        horaCombo.set("00")
        minutoCombo = ttk.Combobox(programarAgua2)
        minutoCombo['values'] = [i for i in range(00, 60)]
        minutoCombo.state(['readonly'])
        minutoCombo.set("00")
        botao = ttk.Button(programarAgua1, text= "Confirmar", command= lambda: self.confirmarAgua(horaCombo.get(), minutoCombo.get()))

        atual.grid(row= 0, column= 1, columnspan= 2, pady= (182, 0))
        hora_atual.grid(row= 1, column= 1)
        min_atual.grid(row= 1, column= 2)
        comboboxTexto.grid(row= 0, column= 0, columnspan= 2, pady= (182, 0))
        horaCombo.grid(row= 1, column= 0)
        minutoCombo.grid(row= 1, column= 1)
        botao.grid(row= 2, column= 3, columnspan= 2)
        
        # Configurando tamanho das colunas para melhor posicionamento
        programarAgua1.columnconfigure(0, minsize= 80)
        programarAgua1.columnconfigure(1, minsize= 80)
        programarAgua1.columnconfigure(2, minsize= 80)
        programarAgua1.columnconfigure(3, minsize= 80)

        programarAgua2.columnconfigure(0, minsize= 80)
        programarAgua2.columnconfigure(1, minsize= 80)
        programarAgua2.columnconfigure(2, minsize= 80)
        programarAgua2.columnconfigure(3, minsize= 80)

        programarAgua1.grid(column= 0, row= 0, sticky=(W, N))
        programarAgua2.grid(column= 1, row= 0, sticky=(E, N))
        pass
    
    def liberarAgua(self):
        pass

    def iniciar(self):
        self.__janela.mainloop()

global executando
executando = 1

def verificacao_horario():
        while executando == 1:
            agora = datetime.datetime.now()
            horario_especifico = datetime.time(13, 32) # define o horário específico
            agora = datetime.time(int(agora.hour), int(agora.minute))
            if agora == horario_especifico: # verifica se o horário atual é igual ao horário específico
                # realiza ação desejada
                print("Horário específico alcançado!")
            time.sleep(10) # espera 60 segundos antes de verificar novamente
    
# inicia a thread de verificação de horário
thread_verificacao = threading.Thread(target=verificacao_horario)
thread_verificacao.start()


janela = Janela(Tk())
janela.telaPrincipal()
janela.iniciar()

executando = 0