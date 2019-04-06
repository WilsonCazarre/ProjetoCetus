"""Design para o aplicativo Cetus PCR.

"Interface" armazena todas as informações sobre os widgets do aplicativo.

A estrutura principal do programa é baseada principalmente nessas duas classes:
class CetusPCR -> Seleciona/Cria um experimento;
class ExperimentPCR -> Edita/Executa o experimento selecionado;

Todas as classes de janelas herdadas da biblioteca tk.Frame.
Isso é feito apenas por propósitos de design,
uma vez que facilita a colocação das bordas e organização dos widgets dentro da
janela.
"""

import tkinter as tk
from tkinter import ttk
import constants as std

import functions

# f = functions.Experiment()


class CetusPCR(tk.Frame):
    """Primeira janela do aplicativo.

    Nessa janela o usuário pode selecionar, deletar ou criar um experimento.
    """
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.master = master
        self.master.geometry('+200+10')
        self.master.title('Cetus PCR')
        self.master.iconbitmap(std.icon)
        self.pack()
        self.pack_propagate(False)
        self.configure(width=1000,
                       height=660,
                       bg=std.bg,
                       bd=0,
                       relief=std.relief,
                       highlightcolor=std.bd,
                       highlightbackground=std.bd,
                       highlightthickness=std.bd_width)
        # self.show_experiments()

    def _widgets(self):
        """Cria os widgets da janela.

        A razão para qual os widgets são colocador em outro método é que essa classe
        será futuramente herdada pela janela ExperimentPCR e não é suposta  para\
        copiar todos os widgets para outra janela, apenas as opções de quadro.
        """
        # Criar os widgets
        self.options_frame = tk.Frame(master=self,
                                      width=250,
                                      height=200,
                                      bg=std.bg,
                                      bd=0,
                                      relief=std.relief,
                                      highlightcolor=std.bd,
                                      highlightbackground=std.bd,
                                      highlightthickness=std.bd_width)

        self.options_box_title = tk.Label(master=self,
                                          text='Opções',
                                          font=(std.font_title, 13, 'bold'),
                                          bg=std.bg,
                                          fg=std.label_color,
                                          width=7)
        self.buttons = {}
        # Criar e posicionar 3 botões dentro do "options_frame"
        for but in ('Abrir', 'Novo', 'Excluir'):
            self.buttons[but] = tk.Button(master=self.options_frame,
                                          font=(std.font_buttons, 13, 'bold'),
                                          text=but,
                                          relief=std.relief,
                                          width=8,
                                          height=0)
            self.buttons[but].pack(pady=14)
        self.buttons['Abrir'].configure(command=self.handle_openbutton)

        self.experiment_combo = ttk.Combobox(master=self,
                                             width=30,
                                             font=(std.font_title, 15),
                                             values=['Experimento 01'])

        self.experiment_combo_title = tk.Label(master=self,
                                               font=(std.font_title, 25, 'bold'),
                                               text='Selecione o experimento:',
                                               fg=std.label_color,
                                               bg=std.bg)

        # Posicionar os widgets(botões não incluídos)
        self.options_frame.place(rely=0.45,
                                 relx=0.75,
                                 anchor='center')
        self.options_frame.pack_propagate(False)

        self.options_box_title.place(in_=self.options_frame,
                                     bordermode='outside',
                                     relx=0.05,
                                     y=-10)

        self.experiment_combo.place(relx=0.35,
                                    rely=0.47,
                                    anchor='center')

        self.experiment_combo_title.place(in_=self.experiment_combo,
                                          relx=0.5,
                                          anchor='s',
                                          bordermode='outside')

    def show_experiments(self):
        self.experiment_combo.configure(values=functions.experiments)

    def handle_openbutton(self):
        print(functions.experiments)
        newroot = tk.Tk()
        new = ExperimentPCR(newroot,
                            functions.experiments[self.experiment_combo.current()])
        new._widgets()
        self.master.destroy()


class ExperimentPCR(CetusPCR):
    """Lida com o experimento dado pela janela CetusPCR.

    Essa janela é composto por alguns widgets da classe tk.Entry.
    Seu estado é definido pelas instruções dadas pelo usuário
    na janela anterior.

    Abrir -> Widgets de entrada são desabilitados com as opções do experimento
    dentro deles.
    Novo -> Widgets de entrada são habilitados e esvaziados.

    Se o usuário escolher a opção Abrir, ainda é possível
    ativar os widgets de entrada pressionando o botão Editar.

    Herdar do CetusPCR cria automaticamente uma janela
    com as mesmas configurações de quadro.
    Isso é util pois a janela deve ter a mesma aparência, título, ícone e tamanho,
    porém, com widgets e opções diferentes.
    """
    def __init__(self, master: tk.Tk, experiment):
        super().__init__(master)
        self.experiment = experiment

    def _widgets(self):
        self.entry_of_options = {}
        self.gapy = 20
        for stage in ('Desnaturação', 'Anelamento', 'Extensão'):
            self.gapx = 20
            for option in ('Temperatura', 'Tempo'):
                entry = tk.Entry(master=self,
                                 font=(std.font_title, 30),
                                 width=3,
                                 bd=1,
                                 highlightcolor=std.bd,
                                 highlightthickness=std.bd_width)
                key = 'Entry-' + stage + ' ' + option
                self.entry_of_options[key] = entry
                entry.place(relx=0.2,
                            rely=0.2,
                            x=self.gapx,
                            y=self.gapy,
                            anchor='ne')
                self.gapx += 150
                if option == 'Temperatura':
                    text = '°C'
                else:
                    text = 'Seg'
                unit_label = tk.Label(master=self,
                                      text=text,
                                      fg=std.label_color,
                                      bg=std.bg,
                                      font=(std.font_title, 14, 'bold'))
                unit_label.place(in_=entry,
                                 relx=1,
                                 rely=0,
                                 x=10)
            self.gapy += 120
            label = tk.Label(master=self,
                             font=(std.font_title, 20, 'bold'),
                             text=stage+':',
                             bg=std.bg,
                             fg=std.label_color)
            self.entry_of_options['Label-'+stage] = label
            label.place(in_=self.entry_of_options['Entry-'+stage+' Temperatura'],
                        anchor='sw',
                        y=-10,
                        bordermode='outside')

        self.gapy = 20
        for option in ('Nº de ciclos', 'Temperatura Final'):
            key = 'Entry- ' + option
            entry = tk.Entry(master=self,
                             font=(std.font_title, 30),
                             width=3,
                             bd=1,
                             highlightcolor=std.bd,
                             highlightthickness=std.bd_width)
            entry.place(relx=0.7,
                        rely=0.2,
                        y=self.gapy)
            self.gapy += 120
            self.entry_of_options[key] = entry

            key = 'Label- ' + option
            label = tk.Label(master=self,
                             font=(std.font_title, 20, 'bold'),
                             text=option+':',
                             fg=std.label_color,
                             bg=std.bg)
            label.place(in_=entry,
                        anchor='s',
                        relx=0.5,
                        y=-10)
            self.entry_of_options[key] = label
            if option == 'Temperatura Final':
                unit_label = tk.Label(master=self,
                                      font=(std.font_title, 14, 'bold'),
                                      text='°C',
                                      bg=std.bg,
                                      fg=std.label_color)
                unit_label.place(in_=entry,
                                 # anchor='ne',
                                 relx=1,
                                 rely=0,
                                 x=10)

        self.buttons_frame = tk.Frame(master=self,
                                      width=250,
                                      height=100,
                                      bg=std.bg,
                                      bd=0,
                                      relief=std.relief,
                                      highlightcolor=std.bd,
                                      highlightbackground=std.bd,
                                      highlightthickness=std.bd_width)
        self.buttons_frame.place(in_=self.entry_of_options['Entry- Temperatura Final'],
                                 anchor='n',
                                 relx=0.5,
                                 rely=1,
                                 y=50)
        self.buttons_frame_title = tk.Label(master=self,
                                            text='Opções',
                                            font=(std.font_title, 13, 'bold'),
                                            bg=std.bg,
                                            fg=std.label_color,
                                            width=7)
        self.buttons_frame_title.place(in_=self.buttons_frame,
                                       bordermode='outside',
                                       relx=0.05,
                                       y=-10)
        self.buttons_frame.pack_propagate(False)

        self.buttons = {}
        for but in ('Editar', 'Executar'):
            self.buttons[but] = tk.Button(master=self.buttons_frame,
                                          text=but,
                                          width=7,
                                          font=(std.font_buttons, 15))
            self.buttons[but].pack(side='left',
                                   padx=17)
        self.open_experiment(self.experiment)

    def open_experiment(self, experiment: functions.Experiment):
        values = experiment.__dict__.keys()
        done_entry = []
        for value in values:
            if value != 'name':
                for entry in self.entry_of_options:
                    if entry not in done_entry and 'Entry' in entry:
                        self.entry_of_options[entry].insert(0, experiment.__dict__
                                                            [value])
                        done_entry.append(entry)
                        break



