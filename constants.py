import json

# -------------------------------------- Caminhos para arquivos de configuração
EXP_PATH = 'experiments.pcr'
SETTINGS_PATH = 'settings.json'

with open(SETTINGS_PATH, 'r') as infile:
    settings_values = json.load(infile)

# ------------------------------------------------------- Constantes do sistema

COOLING_TEMP_C = settings_values['COOLING_TEMP_C']
KP = settings_values['KP']
KI = settings_values['KI']
KD = settings_values['KD']
TOLERANCE = settings_values['TOLERANCE']

# ---------------------------------------------------------- Constantes Tkinter
BG = '#434343'
BD = '#2ecc71'
BD_WIDTH = 3
RELIEF = 'flat'
TEXTS_COLOR = 'white'
SIDE_BAR_COLOR = '#383838'
TOP_BAR_COLOR = '#529E76'

# --------------------------------------------------------------------- Fontes
FONT_TITLE = 'Courier New'
FONT_BUTTONS = 'Arial'
FONT_HOVER = 'Arial'
FONT_ENTRY_TITLE = 'Courier New'
FONT_ENTRY = 'Courier New'

# --------------------------------- Caminhos de arquivo para imagens dos ícones
HEADER_IMAGE_PATH = 'assets/header_cetus.png'
LOGO_IMAGE_PATH = 'assets/logo.png'
WINDOW_ICON = 'assets/cetus.ico'
side_buttons_path = {'home_icon': 'assets/home_icon.png',
                     'settings_icon': 'assets/settings_icon.png',
                     'reconnect_icon': 'assets/reconnect_icon.png',
                     'cooling_icon': 'assets/cooling_icon.png',
                     'info_icon': 'assets/info_icon.png',
                     'home_highlight': 'assets/home_highlight.png',
                     'settings_highlight': 'assets/settings_highlight.png',
                     'reconnect_highlight': 'assets/reconnect_highlight.png',
                     'cooling_highlight': 'assets/cooling_highlight.png',
                     'info_highlight': 'assets/info_highlight.png'}
cetuspcr_buttons_path = {'add_icon': 'assets/add_icon.png',
                         'delete_icon': 'assets/delete_icon.png',
                         'confirm_icon': 'assets/confirm_icon.png',
                         'add_highlight': 'assets/add_highlight.png',
                         'delete_highlight': 'assets/delete_highlight.png',
                         'confirm_highlight': 'assets/confirm_highlight.png'}
experimentpcr_buttons_path = {'add_icon': 'assets/add_icon.png',
                              'save_icon': 'assets/save_icon.png',
                              'run_icon': 'assets/run_icon.png',
                              'add_highlight': 'assets/add_highlight.png',
                              'save_highlight': 'assets/save_highlight.png',
                              'run_highlight': 'assets/run_highlight.png'}
remove_button_path = 'assets/remove_icon.png'


# ---------------------------------------------------- Textos da barra inferior
hover_texts = {
    'default': 'Feito com ♥ na ETEC PV pelo 3º Mecatrônica(2k19).',
    'home': 'Voltar a tela inicial.',
    'info': 'Exibir informações do programa.',
    'cooling': 'Iniciar processo de resfriamento.',
    'reconnect': 'Iniciar conexão com o Cetus PCR.',
    'settings': 'Exibir configurações dos processos padrões.',
    'add': 'Adicionar um novo experimento.',
    'delete': 'Remove o experimento selecionado.',
    'confirm': 'Exibir as informações do experimento selecionado.',
    'save': 'Salva as informações do experimento atual.',
    'run': 'Iniciar experimento.',
    'cancel': 'Cancelar a execução do experimento atual'
}
