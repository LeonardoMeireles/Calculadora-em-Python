from tkinter import *

root = Tk()
root.title("Calculadora")

#Onde será apresentado os números inseridos e os resultados
e = Entry(root, width=60, borderwidth=5) 
e.grid(row=0, column=0, columnspan=4, padx=6, pady=6)

#Global que aloca o resultado caso o usuário faça diversas operações matematicas antes de apertar o botão "="
global result
result = 0

#Indica se o botão apertado anteriormente foi de uma operação matematica ou não
apos_op = FALSE

#Função para adicionar um numero à sequencia
def apertar_botao(num):
    global apos_op
    if (apos_op == TRUE):
        e.delete(0,END)
    atual = e.get()
    e.delete(0, END)
    e.insert(0, str(atual) + str(num))
    apos_op == FALSE

#Função "Clear"(limpa a aba de numeros) e o result
def clear():
    e.delete(0, END)
    result = 0

#Função para soma
def soma():
    num1 = e.get()
    global p_num
    global acao
    global apos_op
    acao = "soma"
    p_num = int(num1)
    if(apos_op == TRUE):
        igual()
        apos_op = TRUE
    else:
        e.delete(0, END)
    apos_op = TRUE

#Função para subtração
def sub():
    num1 = e.get()
    global p_num
    global acao
    global apos_op
    acao = "sub"
    p_num = int(num1)
    if(apos_op == TRUE):
        igual()
        apos_op = TRUE
    else:
        e.delete(0, END)
    apos_op = TRUE

#Função para soma
def mult():
    num1 = e.get()
    global p_num
    global acao
    global apos_op
    acao = "mult"
    p_num = int(num1)
    if(apos_op == TRUE):
        igual()
        apos_op = TRUE
    else:
        e.delete(0, END)
    apos_op = TRUE

#Função para divisão
def div():
    num1 = e.get()
    global p_num
    global acao
    global apos_op
    acao = "div"
    p_num = int(num1)
    if(apos_op == TRUE):
        igual()
        apos_op = TRUE
    else:
        e.delete(0, END)
    apos_op = TRUE

#Imprime a resposta
def igual():
    global result
    num2 = e.get()
    e.delete(0, END)
    if (acao == "soma"):
        if (result == 0):
            result = p_num + int(num2)
            e.insert(0, result)
        else:
            result += int(num2)
            e.insert(0, result)
    if (acao == "sub"):
        if (result == 0):
            result = p_num + int(num2)
            e.insert(0, result)
        else:
            result -= int(num2)
            e.insert(0, result)
    if (acao == "mult"):
        if (result == 0):
            result = p_num + int(num2)
            e.insert(0, result)
        else:
            result *= int(num2)
            e.insert(0, result)
    if (acao == "div"):
        if (result == 0):
            result = p_num + int(num2)
            e.insert(0, result)
        else:
            result /= int(num2)
            e.insert(0, result)
      


#Definindo os botões
botao_1 = Button(root, text="1", padx=40, pady=20, command=lambda: apertar_botao(1))
botao_2 = Button(root, text="2", padx=40, pady=20, command=lambda: apertar_botao(2))
botao_3 = Button(root, text="3", padx=40, pady=20, command=lambda: apertar_botao(3))
botao_4 = Button(root, text="4", padx=40, pady=20, command=lambda: apertar_botao(4))
botao_5 = Button(root, text="5", padx=40, pady=20, command=lambda: apertar_botao(5))
botao_6 = Button(root, text="6", padx=40, pady=20, command=lambda: apertar_botao(6))
botao_7 = Button(root, text="7", padx=40, pady=20, command=lambda: apertar_botao(7))
botao_8 = Button(root, text="8", padx=40, pady=20, command=lambda: apertar_botao(8))
botao_9 = Button(root, text="9", padx=40, pady=20, command=lambda: apertar_botao(9))
botao_0 = Button(root, text="0", padx=40, pady=20, command=lambda: apertar_botao(0))
botao_soma = Button(root, text="+", padx=37.4, pady=20, command = soma)
botao_sub = Button(root, text="-", padx=39.4, pady=20, command = sub)
botao_vezes = Button(root, text="x", padx=38.5, pady=20, command = mult)
botao_igual = Button(root, text="=", padx=38, pady=20, command = igual)
botao_C = Button(root, text="C", padx=37, pady=20, command = clear)
botao_divisao = Button(root, text="/", padx=40, pady=20, command=div)

#Alocando os botões no grid
botao_1.grid(row=1, column=0)
botao_2.grid(row=1, column=1)
botao_3.grid(row=1, column=2)

botao_4.grid(row=2, column=0)
botao_5.grid(row=2, column=1)
botao_6.grid(row=2, column=2)

botao_7.grid(row=3, column=0)
botao_8.grid(row=3, column=1)
botao_9.grid(row=3, column=2)

botao_0.grid(row=4, column=0)

botao_C.grid(row=1, column=3)
botao_soma.grid(row=2, column=3)
botao_sub.grid(row=3, column=3)
botao_vezes.grid(row=4, column=3)
botao_igual.grid(row=4, column=1)
botao_divisao.grid(row=4, column=2)

root.mainloop()
