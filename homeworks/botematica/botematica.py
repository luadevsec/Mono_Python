from time import sleep
from pyautogui import press, write, PAUSE, hotkey
from pyautogui import prompt, confirm, alert
from pyautogui import screenshot


############# funções #############
def pesquisar(pesquisa):
    press('win')
    write('vivald')
    sleep(1)
    press('enter')
    sleep(1.5)
    write(pesquisa)
    press('enter')

def lembrete(tempo, tipo):
    if tipo == 'segundos':
        sleep(tempo)
    if tipo == 'minutos':
        sleep(tempo*60)
    if tipo == 'horas':
        sleep(tempo*60*60)
    alert(f'seu lembrete de {tempo} {tipo} acabou!')


def contar(entrada):
    hotkey('win', 'r')
    write('calc')
    press('enter')
    sleep(1)
    write(entrada)
    press('enter')
    alert(f'o resultado de {entrada} tá ai kkkk')

def fotinha():
    sleep(3)
    foto = screenshot('foto.png')
    foto.show()
    alert('aqui está sua fotinha kkkkkk')
    


menus = ['pesquisar', 'lembrete', 'fazer conta', 'fotinha', 'agora não']

PAUSE = 0.3

alert('olá, eu sou o botematica, um bot de teste e aprendizado para praticar automação em python, e irei te ajudar com coisas simples por enquanto') 




run = True
wait = 0
while run == True:
    resposta = confirm('precisa de ajuda ? selecione a opção que deseja que eu execute'
                   , buttons=menus)
    if resposta == menus[0]: # pesquisa
        entrada = prompt('digite o que você quer pesquisar aqui')
        pesquisar(entrada)
    if resposta == menus[1]: # lembrete
        tipos = ['segundos', 'minutos', 'horas']
        tipo = confirm('escolha a medida de tempo para o seu lembrete', buttons=tipos)
        entrada = int(prompt(f'digite agora o tempo que você quer que eu espere em {tipo}'))
        lembrete(entrada, tipo)
    if resposta == menus[2]: # conta
        entrada = prompt('digite a conta matematica que eu terei que fazer')
        contar(entrada)
    if resposta == menus[3]: #fotinha
        fotinha()
    if resposta == menus[4]: # sair
        if wait != 5: wait+=1
        if confirm(f'ok, eu volto em {5*wait} minutos então', buttons=['ok', 'não volte'])  == 'não volte':
            run = False
        else:
            sleep((5*60)*wait)

alert('ok, espero ter ajudado, se quiser que eu te ajuda terá que me chamar denovo')











