from tkinter import *
from tkinter import ttk

def main():
    ### Configuração básica ###
    background_color = "#3D4543"
    btn_bg = '#313131'
    valores = []
    janela = Tk()
    janela.resizable(False, False)
    janela.configure(bg=background_color)
    janela.title('Calculadora Python')

    ### FRAME ###
    frame = Frame(janela, bd = 1, bg=background_color)
    frame.pack(fill = 'both', expand = True, padx = 10, pady = 10)

    ### Display ###
    display = ttk.Label(frame, text='insira os valores', padding=(150, 20, 150, 20),borderwidth=2, relief="solid")
    display.grid(column=0, row=0, columnspan=4, pady=(10))

    ### BOTÕES NUMERICOS ###
    botao_7 = Button(frame, text='7',bg=btn_bg,fg='white')
    botao_7.grid(column=0, row=1)

    botao_8 = Button(frame, text='8',bg=btn_bg,fg='white')
    botao_8.grid(column=1, row=1)

    botao_9 = Button(frame, text='9',bg=btn_bg,fg='white')
    botao_9.grid(column=2, row=1)
    
    botao_4 = Button(frame, text='4',bg=btn_bg,fg='white')
    botao_4.grid(column=0, row=2)

    botao_5 = Button(frame, text='5',bg=btn_bg,fg='white')
    botao_5.grid(column=1, row=2)

    botao_6 = Button(frame, text='6',bg=btn_bg,fg='white')
    botao_6.grid(column=2, row=2)

    botao_1 = Button(frame, text='1',bg=btn_bg,fg='white')
    botao_1.grid(column=0, row=3)

    botao_2 = Button(frame, text='2',bg=btn_bg,fg='white')
    botao_2.grid(column=1, row=3)

    botao_3 = Button(frame, text='3',bg=btn_bg,fg='white')
    botao_3.grid(column=2, row=3)

    botao_0 = Button(frame, text='0',bg=btn_bg,fg='white')
    botao_0.grid(column=0, row=4, columnspan=2)

    ### BOTOES OPERADORES ###
    botao_ponto = Button(frame, text='.',bg=btn_bg,fg='white')
    botao_ponto.grid(column=2, row=4)

    botao_soma = Button(frame, text='+',bg=btn_bg,fg='white')
    botao_soma.grid(column=3, row=1)

    botao_subtracao = Button(frame, text='-',bg=btn_bg,fg='white')
    botao_subtracao.grid(column=3, row=2)

    botao_soma = Button(frame, text='*',bg=btn_bg,fg='white')
    botao_soma.grid(column=3, row=3)

    botao_soma = Button(frame, text='/',bg=btn_bg,fg='white')
    botao_soma.grid(column=3, row=4)

    janela.mainloop()

if __name__ == "__main__":
    main()