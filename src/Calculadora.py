from tkinter import *

root = Tk()
root.title("Calculdara Simples")
root.geometry("400x355")
root.maxsize(width=400, height=355)
root.minsize(width=400, height=355)

numero1 = ''
divisao = FALSE
multiplicacao = FALSE
soma = FALSE
subtracao = FALSE

root.configure(bg="#282828")

e = Entry(root, width=15, font=("futura", 20, "bold"), borderwidth=4, bg="#a7a28f", fg="#FFFFFF", relief=FLAT, justify=CENTER)
e.grid(row=0, column=0, columnspan=4, pady=2)

def botao_click(numero):
    #pega o valor atual do entry e concatena com o numero que foi clicado
    e.insert(END, numero)
def button_divide():
    global numero1 
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_multiplica():
    global numero1
    global multiplicacao
    multiplicacao = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_adiciona():
    global numero1
    global soma
    soma = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_subtrai():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_igual():
    global divisao
    global multiplicacao
    global soma
    global subtracao
    numero2 = e.get()
    e.delete(0, END)
    if soma == TRUE:
        e.insert(0, round(float(numero1) + float(numero2), 2))
        soma = FALSE
    if subtracao == TRUE:
        e.insert(0, round(float(numero1) - float(numero2), 2))
        subtracao = FALSE
    if multiplicacao == TRUE:
        e.insert(0, round(float(numero1) * float(numero2), 2))
        multiplicacao = FALSE
    if divisao == TRUE:
        e.insert(0, round(float(numero1) / float(numero2), 2))
        divisao = FALSE
def botao_limpa():
    e.delete(0, END)
def botao_virgula():
    #pega o valor atual do entry e concatena com o numero que foi clicado
    e.insert(END, '.')

divide = Button(root, text="÷", padx=40, pady=20, font=("futura", 12, "bold"), bg="#320064", activebackground='#240046', activeforeground='#FFFFFF', fg="#FFFFFF", relief=FLAT, command=button_divide)
divide.grid(row=0, column=4)

#primeira fileira

um = Button(root, text='1', padx='40', pady='20', command=lambda: botao_click(1),
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
um.grid(row=1, column=1)

dois = Button(root, text='2', padx='40', pady='20', command=lambda: botao_click(2),
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
dois.grid(row=1, column=2)

tres = Button(root, text='3', padx='40', pady='20', command=lambda: botao_click(3),
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
tres.grid(row=1, column=3)

multiplica = Button(root, text='x', padx='40', pady='20', command=botao_multiplica,
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
multiplica.grid(row=1, column=4)

#segunda fileira

quatro = Button(root, text='4', padx='40', pady='20', command=lambda: botao_click(4),
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
quatro.grid(row=2, column=1)
cinco = Button(root, text='5', padx='40', pady='20', command=lambda: botao_click(5),
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
cinco.grid(row=2, column=2)
seis = Button(root, text='6', padx='40', pady='20', command=lambda: botao_click(6),
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
seis.grid(row=2, column=3)
subtrai = Button(root, text='–', padx='40', pady='20', command=botao_subtrai,
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
subtrai.grid(row=2, column=4)

#terceira fileira

sete = Button(root, text='7', padx='40', pady='20', command=lambda: botao_click(7),
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
sete.grid(row=3, column=1)
oito = Button(root, text='8', padx='40', pady='20', command=lambda: botao_click(8),
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
oito.grid(row=3, column=2)
nove = Button(root, text='9', padx='40', pady='20', command=lambda: botao_click(9),
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
nove.grid(row=3, column=3)
adiciona = Button(root, text='+', padx='40', pady='20', command=botao_adiciona,
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
adiciona.grid(row=3, column=4)

#quarta fileira

zero = Button(root, text='0', padx='40', pady='20', command=lambda: botao_click(0),
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
zero.grid(row=4, column=2)
limpa = Button(root, text='c', padx='40', pady='20', command=botao_limpa,
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
limpa.grid(row=4, column=3)
igual = Button(root, text='=', padx='40', pady='20', command=botao_igual,
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 12, 'bold'))
igual.grid(row=4, column=4)
virgula = Button(root, text='.', padx='42', pady='20', command=botao_virgula,
            fg='#FFFFFF', activeforeground='#FFFFFF', bg='#320064',
            activebackground='#240046', relief=FLAT, font=('futura', 13, 'bold'))
virgula.grid(row=4, column=1)

root.mainloop()
