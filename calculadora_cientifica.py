import tkinter as tk;
import math;

# Configurações de visual
FONTE=("monospace", 12)
FONTE_TITULO=("monospace", 20, "bold")
FONTE_SUBTITULO=("monospace", 14, "bold")

COR_BOTAO="#d3d6ed"
COR_BOTAO_ATIVO="#a0a6d4"

COR_TEXTO_ENTRADA="#ffffff"
COR_ENTRADA="#94959c"

# Criar janela
janela = tk.Tk()
janela.title("Prova N1")
janela.config(padx=16, pady=16)

operacoesBasicas = True
resultado = 0

# v funcoes ---------------------------------
# Definir aqui todas as funcionaliedades que ele tem, cada um em sua função
# Lembre de colocar o "command=" para chamar a função aqui definida

# * Operações gerais
def resultadoNoPrimeiroCampo():
  try:
    # Apaga o campo input inteiro
    numero1Input.delete(0, tk.END)
    # Muda o valor para o resultado
    numero1Input.insert(0, str(resultado))

  except ValueError:
    resultadoLabel.config(text="Erro: Não foi possível mudar o valor do campo 1 para o resultado")

def calcular_soma():
  global operacoesBasicas
  operacoesBasicas = True
  global resultado

  try:
    # Pega o valor dos inputs e muda para float 
    num1 = float(numero1Input.get())
    num2 = float(numero2Input.get())
    resultado = num1 + num2

    #Coloca o valor do resultado 
    resultadoLabel.config(text=f"{num1} + {num2} = {resultado}")

  except ValueError:
    resultadoLabel.config(text="Erro: Digite apenas números válidos! Lembre-se de digitar numeros nos 2 campos")

def calcular_subtracao():
  global operacoesBasicas
  operacoesBasicas = True
  global resultado

  try:
    num1 = float(numero1Input.get())
    num2 = float(numero2Input.get())
    resultado = num1 - num2
    resultadoLabel.config(text=f"{num1} - {num2} = {resultado}")

  except ValueError:
    resultadoLabel.config(text="Erro: Digite apenas números válidos! Lembre-se de digitar numeros nos 2 campos")

#Função para deixar o numero inteiro sem a virgula
def formatar(valor):
  if valor == int(valor):
    return str(int(valor))
  return str(round(valor, 4))

def calcularDivisao():
  global operacoesBasicas
  operacoesBasicas = True
  global resultado

  #Pega os 2 numeros e troca a virgula por um ponto
  try:
    n1 = float(numero1Input.get().replace(",", "."))
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

def calcularRadiciacao():
  global operacoesBasicas
  operacoesBasicas = True
  global resultado
  #O n1 é o radicando (número dentro da raiz) e o n2 é o indice (número pequeno fora da raiz)

  #Igual o de cima ele pega os 2 numeros e troca a virgula por um ponto
  try:
    n1 = float(numero1Input.get().replace(",", "."))
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

def fatorial():
  global operacoesBasicas
  operacoesBasicas = True
  global resultado

  try:
    #recebe qual o numero que deve ser feito o fatorial
    numero_fatorial = int(numero1Input.get())

    #obs: não existe nuemro fatorial negativo
    if numero_fatorial < 0:
      resultadoLabel.config(text="Erro: Fatorial não existe para números negativos!")
      resultadoLabel.pack(padx=8, pady=4)

    else:
      # math.factorial é um atalho da bibliotteca math para calcular o expoente 
      #exemplo math.factorial(numero que o usuaario quer descobrir o fatorial)
      resultado = math.factorial(numero_fatorial)
      resultadoLabel.config(text=f" {numero_fatorial}! = {resultado}")
      resultadoLabel.pack(padx=8, pady=4)

  except:
    # se o usuario digitar um caractere que não seja um numero o except avisa o erro 
    resultadoLabel.config(text="Erro: Digite apenas números válidos! No primeiro campo")
    resultadoLabel.pack(padx=8, pady=4)

def expoencial():
  global operacoesBasicas
  operacoesBasicas = True
  global resultado

  try:
    # recebe os valores das entradas e substitui a vírgula por ponto
    numero_Base = numero1Input.get()
    base_corrigido = float(numero_Base.replace(",",".", 1))

    numero_Expoente = numero2Input.get()
    expoente_corrigido = float(numero_Expoente.replace(",",".", 1))

    # math.pow é um aatalho da bibliotteca math para calcular o expoente 
    #exemplo math.pow(base, expoente)
    resultado = math.pow( base_corrigido, expoente_corrigido)

    # Atualiza o texto do Label existente 
    resultadoLabel.config(text=f"{base_corrigido}^{expoente_corrigido} = {resultado:.2f}")
    resultadoLabel.pack(padx=8, pady=4)

  except:
    # se o usuario digitar um caractere que não seja um numero o except avisa o erro 
    resultadoLabel.config(text="Erro: Digite apenas números válidos! Lembre-se de digitar numeros nos 2 campos")
    resultadoLabel.pack(padx=8, pady=4)

def multiplicacao():
  global operacoesBasicas
  operacoesBasicas = True
  global resultado

  try:
    # recebe os valores das entradas e substitui a vírgula por ponto
    numero1_Multiplicacao = numero1Input.get()
    numero1_corrigido = float(numero1_Multiplicacao.replace(",", ".", 1))

    numero2_Multiplicacao = numero2Input.get()
    numero2_corrigido = float(numero2_Multiplicacao.replace(",", ".", 1))

    # Calcula o resultado
    resultado = numero1_corrigido * numero2_corrigido

    # Atualiza o texto do Label existente 
    resultadoLabel.config(text=f"{numero1_corrigido} x {numero2_corrigido} = {resultado:.2f}")
    resultadoLabel.pack(padx=8, pady=4)

  except:
    # se o usuario digitar um caractere que não seja um numero o except avisa o erro 
    resultadoLabel.config(text="Erro: Digite apenas números válidos! Lembre-se de digitar numeros nos 2 campos")
    resultadoLabel.pack(padx=8, pady=4)

# * Operações extras
def polegadas():
  global operacoesBasicas
  operacoesBasicas = True

  numero_polegadas = numero1Input.get()
  #try para evitar que o usuário digite um caractere que não seja um número.
  try:
    #o eval le o numero da polegada como se fosse uma linha de codigo
    #então ele le o numero_polegadas que normalmente é representado em frações 
    # e as calculas em valores decimais e depois multiplica por 25,4 para descovrir a medida delas em milimimetros
    resultado_numero_polegadas = eval(numero_polegadas)
    milimetros =  resultado_numero_polegadas*25.4
    centimetros = resultado_numero_polegadas*2.54

    #coloquei o print paara paraar na terceira casa decimal.
    resultadoLabel.config(text=f"{numero_polegadas} = {milimetros: .3f} milimetros = {centimetros: .3f} centimetros")
    resultadoLabel.pack(padx=8, pady=4)

  except:
    # se o usuario digitar um caractere que não seja um numero o except avisa o erro 
    resultadoLabel.config(text="Erro:Lembre-se de digitar apenas números em polegadas. Ex: ¼, ⅜ , ½  e etc.")
    resultadoLabel.pack(padx=8, pady=4)

def fahrenheit():
  global operacoesBasicas
  operacoesBasicas = True

  #try para evitar que o usuário digite um caractere que não seja um número.
  try:
    numero_fahrenheit = numero1Input.get()
    # recebe os valores das entradas e substitui a vírgula por ponto
    fahrenheit_corrigido = float(numero_fahrenheit.replace(",",".", 1))

    #a formula para converter a temperatura de fahrenheit para graus celsius
    resulatado_fahrenheit = float(fahrenheit_corrigido * 9/5) + 32
    # Atualiza o texto do Label existente
    resultadoLabel.config(text=f" {numero_fahrenheit} °F  = {resulatado_fahrenheit: .1f} °C")
    resultadoLabel.pack(padx=8, pady=4)
  except:
    # se o usuario digitar um caractere que não seja um numero o except avisa o erro 
    resultadoLabel.config(text="Erro: Digite apenas números válidos! No primeiro campo")
    resultadoLabel.pack(padx=8, pady=4)

# ^ funcoes ---------------------------------

# Título: "Calculadora"
titulo = tk.Label(janela, text="Calculadora", font=FONTE_TITULO)
titulo.pack(padx=16, pady=8)

# ---------------------------------
# Texto: "Digite o primeiro número"
numero1Label = tk.Label(janela, text="Digite o primeiro número", font=FONTE)
numero1Label.pack(padx=8, pady=4)

# Campo: "Número 1"
numero1Input = tk.Entry(janela, font=FONTE, bg=COR_ENTRADA, fg=COR_TEXTO_ENTRADA, relief="flat")
numero1Input.pack(ipadx=16, ipady=8)


# ---------------------------------
# Texto: "Digite o secundo número"
numero2Label = tk.Label(janela, text="Digite o segundo número", font=FONTE)
numero2Label.pack(padx=8, pady=4)

# Campo: "Número 2"
numero2Input = tk.Entry(janela, font=FONTE, bg=COR_ENTRADA, fg=COR_TEXTO_ENTRADA, relief="flat")
numero2Input.pack(ipadx=16, ipady=8)


# ---------------------------------
# Operações gerais

operacoesGerais = tk.Label(janela, text="Operações gerais", font=FONTE_SUBTITULO)
operacoesGerais.pack(padx=16, pady=8)

operacoesGeraisFrame = tk.Frame(janela)
operacoesGeraisFrame.pack(pady=8)

somaButton = tk.Button(operacoesGeraisFrame, text="+ | soma", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=calcular_soma)

subtrairButton = tk.Button(operacoesGeraisFrame, text="- | subtraír", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=calcular_subtracao)

multiplicarButton = tk.Button(operacoesGeraisFrame, text="× | multiplicar", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=multiplicacao)

dividirButton = tk.Button(operacoesGeraisFrame, text="÷ | dividir", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=calcularDivisao)

exponenciacaoButton = tk.Button(operacoesGeraisFrame, text="xʸ | exponenciação", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=expoencial)

radiciacaoButton = tk.Button(operacoesGeraisFrame, text="ⁿ√x | radiciação", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=calcularRadiciacao)

fatorialButton = tk.Button(operacoesGeraisFrame, text="! | fatorial", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=fatorial)

# Operações gerais > Alinhar
somaButton.grid(row=0, column=0, padx=16, pady=8, sticky="ew")
subtrairButton.grid(row=0, column=1, padx=16, pady=8, sticky="ew")
multiplicarButton.grid(row=0, column=2, padx=16, pady=8, sticky="ew")

dividirButton.grid(row=1, column=0, padx=16, pady=8, sticky="ew")
exponenciacaoButton.grid(row=1, column=1, padx=16, pady=8, sticky="ew")
radiciacaoButton.grid(row=1, column=2, padx=16, pady=8, sticky="ew")

fatorialButton.grid(row=2, column=1, padx=16, pady=8, sticky="ew")

# ---------------------------------
# Conversor

conversor = tk.Label(janela, text="Conversor", font=FONTE_SUBTITULO)
conversor.pack(padx=16, pady=8)

conversorFrame = tk.Frame(janela)
conversorFrame.pack(pady=8)

polegadaButton = tk.Button(conversorFrame, text="Polegada => Milímetro(mm) e Centímetro(cm)", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=polegadas)

fahrenheitButton = tk.Button(conversorFrame, text="Fahrenheit => Celsius", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=fahrenheit)

# Operações gerais > Alinhar
polegadaButton.grid(row=0, column=0, padx=16, pady=8, sticky="ew")
fahrenheitButton.grid(row=0, column=1, padx=16, pady=8, sticky="ew")

# Texto: "Resultado"
resultadoLabel = tk.Label(janela, text="O resultado aparecerá aqui", font=FONTE)
resultadoLabel.pack(padx=8, pady=4)

# Campo: "Usar resultado no campo 1"
usarResultadoNoCampo1Button = tk.Button(janela, text="Usar resultado no campo 1", font=FONTE, bg=COR_BOTAO, activebackground=COR_BOTAO_ATIVO, relief="flat", command=resultadoNoPrimeiroCampo)
usarResultadoNoCampo1Button.pack(padx=16, pady=8)

janela.mainloop()