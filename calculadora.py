import math
def buscar(operacion1):
  if operacion1[0] != "(":
    r = operacion1
    print(r)
    return r
    
  else:
    primer = operacion1.rfind("(")
    ultimo = operacion1.find(")")
    cal = operacion1[primer+1:ultimo]
    print (cal)
    r = operacion(cal)
    operacion2 = operacion1[0:primer] + str(r) + operacion1[ultimo+1:]
    p = buscar(operacion2)
    return p
  
  

def operacion(cal):
  if True:
    for op in cal:
      if op == "*":
        q = cal.find("*")
        cala = cal[:q]
        calb = cal[q+1:]
        a = float(cala)
        b = float(calb)
        r = multiplicacion(a, b)
        return r
      elif op == "/":
        q = cal.find("/")
        cala = cal[:q]
        calb = cal[q+1:]
        calas = cala.strip()
        calbs = calb.strip()
        a = float(calas)
        b = float(calbs)
        r = division(a,b)
        return r
      elif op == "+":
        q = cal.find("+")
        cala = cal[:q]
        calb = cal[q+1:]
        calas = cala.strip()
        calbs = calb.strip()
        a = float(calas)
        b = float(calbs)
        r = suma(a,b)
        return r
      elif op == "-":
        q = cal.find("-")
        cala = cal[:q]
        calb = cal[q+1:]
        calas = cala.strip()
        calbs = calb.strip()
        a = float(calas)
        b = float(calbs)
        r = resta(a,b)
        return r
      elif op == "%":
        q = cal.find("%")
        cala = cal[:q]
        calb = cal[q+1:]
        calas = cala.strip()
        calbs = calb.strip()
        a = float(calas)
        b = float(calbs)
        r = resta(a,b)
        return r
  else:
    r = cal
    return r
    
def residuo(a,b):
  r = a%b
  return r
def expre(cal):
  cal = buscar(cal)
  return cal
  

def multiplicacion(a,b):
  m = a*b
  return m

def division(a,b):
  d = a/b
  return d

def resta(a,b):
  r = a-b
  return r
  
def suma(a,b):
  s = a+b
  return s


def main():
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
  cal = input("calculadora >>")
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
        print("resultado >>", resultado)
      except:
        print("No valido")
  else:
    print("Los parentesis abiertos no coiciden con los parentesis cerrados")
    