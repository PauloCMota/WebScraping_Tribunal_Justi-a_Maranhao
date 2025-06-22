import PySimpleGUI as sg
from tribunais import pje

def main():
    sg.theme('DefaultNoMoreNagging')
    layout = [
        [sg.Text('Data para consulta (YYYY-MM-DD):'), sg.Input(key='-DATA-', size=(15,1)), sg.Button('Hoje')],
        [sg.Button('Consultar'), sg.Button('Sair')],
        [sg.Output(size=(80, 20), key='-OUTPUT-')]
    ]
    window = sg.Window('Monitor de Prazos Processuais', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break
        if event == 'Hoje':
            from datetime import date
            window['-DATA-'].update(value=date.today().strftime('%Y-%m-%d'))
        if event == 'Consultar':
            data_consulta = values['-DATA-']
            if not data_consulta:
                sg.popup('Digite ou selecione uma data!')
                continue
            print(f'Buscando prazos para {data_consulta}...')
            prazos = pje.acessar_expediente("PJE_TJMA", data_consulta)
            if not prazos:
                print("Nenhum prazo encontrado.")
            else:
                for p in prazos:
                    print(f"Processo: {p['processo']}, Prazo: {p['prazo']}, Descrição: {p['descricao']}")

    window.close()

if __name__ == "__main__":
    main()