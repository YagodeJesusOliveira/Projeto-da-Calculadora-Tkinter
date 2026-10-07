import tkinter as tk;
import math;

# Configurações de visual
FONTE=("monospace", 12)
FONTE_TITULO=("monospace", 20, "bold")

COR_BOTAO="#d3d6ed"
COR_BOTAO_ATIVO="#a0a6d4"

COR_ENTRADA="#94959c"

# Criar janela
janela = tk.Tk()
janela.title("Prova N1")
janela.config(padx=16, pady=16)

# v funcoes ---------------------------------
# Definir aqui todas as funcionaliedades que ele tem, cada um em sua função
# Lembre de colocar o "command=" para chamar a função aqui definida

#Função para deixar o numero inteiro sem a virgula
def formatar(valor):
    if valor == int(valor):
        return str(int(valor))
    return str(round(valor, 4))

#Divisão
def calcularDivisao():
    #Pega os 2 numeros e troca a virgula por um ponto
    try:
        n1 = float(numero1Inpnut.get().replace(",", "."))
        n2 = float(numero2Input.get().replace(",", "."))

    #Mensagem carinhosa quando errarem a digitação
    except ValueError:
        resultadoLabel.config(text="Digita o número direito")
        return

    #Quando a LENDA tentar dividir algum número por 0
    if n2 == 0:
        resultadoLabel.config(text="O número não pode ser dividido por 0")
        return

    #Agora é o calculo
    resultado = n1 / n2
    #O número aqui já sai bunitinho
    resultadoLabel.config(text=f"O resultado foi {formatar(resultado)}")

#Radiciação
def calcularRadiciacao():
    #O n1 é o radicando (número dentro da raiz) e o n2 é o indice (número pequeno fora da raiz)

    #Igual o de cima ele pega os 2 numeros e troca a virgula por um ponto
    try:
        n1 = float(numero1Inpnut.get().replace(",", "."))
        n2 = float(numero2Input.get().replace(",", "."))
    
    #Mensagem carinhosa quando errarem a digitação. Padrão
    except ValueError:
        resultadoLabel.config(text="Digita o número direito")
        return

    #Não existe raiz quadrada quando o indice é 0
    if n2 == 0:
        resultadoLabel.config(text="O indice não pode ser 0")
        return

    #Raiz de negativo só existe quando o indice é inteiro ou ímpar (ex: raiz cúbica de -8)
    if n1 < 0:
        if n2 != int(n2) or int(n2) % 2 == 0:
            resultadoLabel.config(text="A Raiz de número negativo não existe, Gênio!")
            return
        resultado = -math.pow(-n1, 1 / n2)
    else:
        resultado = math.pow(n1, 1 / n2)

    #Aqui sai o resultado
    resultadoLabel.config(text=f"O resultado foi {formatar(resultado)}")


# ^ funcoes ---------------------------------

# Título: "Calculadora"
titulo = tk.Label(janela, text="Calculadora", font=FONTE_TITULO)
titulo.pack(padx=16, pady=8)

# ---------------------------------
# Texto: "Digite o primeiro número"
numero1Label = tk.Label(janela, text="Digite o primeiro número", font=FONTE)
numero1Label.pack(padx=8, pady=4)

# Campo: "Número 1"
numero1Inpnut = tk.Entry(janela, font=FONTE, bg=COR_ENTRADA, relief="flat")
numero1Inpnut.pack(padx=16, pady=8)


# ---------------------------------
# Texto: "Digite o secundo número"
numero2Label = tk.Label(janela, text="Digite o secundo número", font=FONTE)
numero2Label.pack(padx=8, pady=4)

# Campo: "Número 2"
numero2Input = tk.Entry(janela, font=FONTE, bg=COR_ENTRADA, relief="flat")
numero2Input.pack(padx=16, pady=8)


# ---------------------------------
# Opções de conta

botoesFrame = tk.Frame(janela)
botoesFrame.pack(pady=8)

somaButton = tk.Button(botoesFrame, text="+ | soma", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat")

subtrairButton = tk.Button(botoesFrame, text="- | subtraír", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat")

multiplicarButton = tk.Button(botoesFrame, text="× | multiplicar", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat")

dividirButton = tk.Button(botoesFrame, text="÷ | dividir", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=calcularDivisao) 

exponenciacaoButton = tk.Button(botoesFrame, text="xʸ | exponenciação", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat")

radiciacaoButton = tk.Button(botoesFrame, text="ⁿ√x | radiciação", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=calcularRadiciacao) 

fatorialButton = tk.Button(botoesFrame, text="! | fatorial", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat")

# Alinhar
somaButton.grid(row=0, column=0, padx=16, pady=8, sticky="ew")
subtrairButton.grid(row=0, column=1, padx=16, pady=8, sticky="ew")
multiplicarButton.grid(row=0, column=2, padx=16, pady=8, sticky="ew")

dividirButton.grid(row=1, column=0, padx=16, pady=8, sticky="ew")
exponenciacaoButton.grid(row=1, column=1, padx=16, pady=8, sticky="ew")
radiciacaoButton.grid(row=1, column=2, padx=16, pady=8, sticky="ew")

fatorialButton.grid(row=2, column=0, padx=16, pady=8, sticky="ew")

# Texto: "Resultado"
resultadoLabel = tk.Label(janela, text=f"O resultado foi {0}", font=FONTE)
resultadoLabel.pack(padx=8, pady=4)

# Campo: "Calcular"
usarResultadoNoCampo1Button = tk.Button(janela, text="Usar resultado no campo 1", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat")
usarResultadoNoCampo1Button.pack(padx=16, pady=8)

janela.mainloop()