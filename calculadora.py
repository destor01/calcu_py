import math
def expre(operacion):
  #Pasa la operacion a una lista, donde elimina los espacios que hay y separa por parte cada numero, parentesis y operacion. Luego lo envia a otra subrutina ordenar.
  bor = ""
  num = ""
  lista = []
  for x in operacion:
    if x == "(" or x == ")" or x ==" ":
      bor += x
      if num != "":
        lista.append(num)
        num = ""
      if x == "(" or x == ")":
        lista.append(x)
    else:
      num += x
  r = ordenar(lista)
  return r

def ordenar(lista):
  #subrutina recursiva, la base recibe una lista ya sin parentesis para mandarla a operaciones y que regrese unicamente el resultado. 
  if lista[0] != "(":
    r = operacion(lista)
    return r
  else:
    #ordena la lista y se vuelve a enviar unicamente del primer parentesis abierto hasta el ultimo parentesis, luego la ordena y se vuelve a enviar esa operacion hasta que la lista unicamente tenga el resultado sin los parentesis
    p = bp(lista)
    aux = lista[p+1:]
    p2 = aux.index(")")
    aux2 = aux[:p2]
    r = ordenar(aux2)
    aux3 = lista[:p] + r + lista[p+p2+2:]
    r2 = ordenar(aux3)
    if len(r2) == 1:
      return r2
      
def bp(lista):
  #busca el ultimo parentesis abierto que se encuentra en la lista
  p = 0
  c = 0
  for co in lista:
    if co == "(":
      p = c
    c += 1
  return p

def operacion(lista):
  #las operaciones. En x que lee la lista operando y pasa uno por uno, luego con c lee la lista que le mandamos y hace el arreglos de las operaciones para volver a hacer los procedimientos si es que hay mas de una operacion 
  operandos = ["factorial!", "cos", "sin", "tan", "sqr", "sqroot", "div", "%", "*", "/", "+", "-"]
  aux = lista
  if True:
    for x in operandos:
      for c in aux:
        if x == c == "/":
          m = aux.index("/")
          m1f = float(aux[m-1])
          m2f = float(aux[m+1])
          if m2f != 0:
            r = m1f / m2f
            aux2 = aux[:m-1] + [str(r)] + aux[m+2:]
            aux = aux2
          else:
            print("No se puede dividir entre 0")
        elif x == c == "*":
          m = aux.index("*")
          m1f = float(aux[m-1])
          m2f = float(aux[m+1])
          r = m1f * m2f
          aux2 = aux[:m-1] + [str(r)] + aux[m+2:]
          aux = aux2
        elif x == c == "+":
          m = aux.index("+")
          m1f = float(aux[m-1])
          m2f = float(aux[m+1])
          r = m1f + m2f
          aux2 = aux[:m-1] + [str(r)] + aux[m+2:]
          aux = aux2
        elif x == c == "-":
          m = aux.index("-")
          m1f = float(aux[m-1])
          m2f = float(aux[m+1])
          r = m1f - m2f
          aux2 = aux[:m-1] + [str(r)] + aux[m+2:]
          aux = aux2
        elif x == c == "cos":
          m = aux.index("cos")
          m1f = float(aux[m+1])
          r = math.cos(math.radians(m1f))
          aux2 = aux[:m] + [str(r)] + aux[m+2:]
          aux = aux2
        elif x == c == "sin":
          m = aux.index("sin")
          m1f = float(aux[m+1])
          r = math.sin(math.radians(m1f))
          aux2 = aux[:m] + [str(r)] + aux[m+2:]
          aux = aux2
        elif x == c == "tan":
          m = aux.index("tan")
          m1f = float(aux[m+1])
          r = math.tan(math.radians(m1f))
          aux2 = aux[:m] + [str(r)] + aux[m+2:]
          aux = aux2
        elif x == c == "sqr":
          m = aux.index("sqr")
          m1f = float(aux[m+1])
          r = math.pow(m1f, 2)
          aux2 = aux[:m] + [str(r)] + aux[m+2:]
          aux = aux2
        elif x == c == "sqroot":
          m = aux.index("sqroot")
          m1f = float(aux[m+1])
          if m1f < 0:
            print("No se puede hacer raiz cuadrada de un numero negativo")
          else:
            r = math.sqrt(m1f)
            aux2 = aux[:m] + [str(r)] + aux[m+2:]
            aux = aux2
        elif x == c == "div":
          m = aux.index("div")
          m1f = float(aux[m-1])
          m2f = float(aux[m+1])
          if m2f != 0:
            r = m1f // m2f
            aux2 = aux[:m-1] + [str(r)] + aux[m+2:]
            aux = aux2
          else:
            print("No se puede dividir entre 0")
        elif x == c == "%":
          m = aux.index("%")
          m1f = float(aux[m-1])
          m2f = float(aux[m+1])
          if m2f != 0:
            r = m1f % m2f
            aux2 = aux[:m-1] + [str(r)] + aux[m+2:]
            aux = aux2
          else:
            print("No se puede dividir entre 0")
        elif x == c == "factorial!":
          m = aux.index("factorial!")
          m1f = float(aux[m+1])
          if m1f > 0:
            r = factorial(m1f)
            aux2 = aux[:m] + [str(r)] + aux[m+2:]
            aux = aux2
          else:
            print("No se puede hacer factorial de un numero menor a 0")
    return aux
  else:
    return lista
  
def factorial(n):
  #factorial
  if n == 0:
    return 1
  else:
    r = n * factorial(n-1)
    return r
    


  
def main():
  #creditos 
  print()
  print("    ***","CALCULADORA","***")
  print("          cc1-BN")
  print("            18")
  print("                      Creditos:")
  print("                  Derek Tortola")
  print("                       23002939")
  print("                  Gerardo Corado")
  print("                       23000175")
  
main()
while True:
  #el input. Mira si los parentesis abiertos son los mismos que los cerrados. Manda a llamar a la subrutina expre. Si no regresa valor imprime no valido
  cal = input("calculadora >>").lower()
  salir = ("quit")
  abi = 0
  cer = 0
  for pa in cal:
    if pa == "(":
      abi +=1
    elif pa ==")":
      cer +=1
  if abi == cer:
    if cal == salir:
      print("Saliendo...")
      break
    else:
      try:
        resultado = expre(cal)
        print("resultado >>", resultado[0])
      except:
        print("No valido")
  else:
    print("Los parentesis abiertos no coiciden con los parentesis cerrados")