isa = ['', 'iray', 'roa', 'telo', 'efatra', 'dimy', 'enina', 'fito', 'valo', 'sivy', 'folo']
folo = ['', '', 'roapolo', 'telopolo', 'efapolo', 'dimapolo', 'enimpolo', 'fitopolo', 'valopolo', 'sivifolo']
zato = ['', 'zato', 'roanjato', 'telonjato', 'efajato', 'dimanjato', 'eninjato', 'fitonjato', 'valonjato', 'sivinjato']

def isa_(n: int, valiny: list) -> (None):
  if (n % 10 == 1) and ((n - 1) % 100 == 0) and ((n - 1) // 100 != 1):
    valiny.append(isa[1])
  elif (n % 10 == 1):
    valiny.append('iraika')
  else :
    valiny.append(isa[n % 10])
  diovina(valiny)

def folo_(n: int, valiny: list) -> (None):
  if (len(valiny) == 0) and (n % 10 == 1):
    valiny.append('folo')
  elif (n % 10 == 1):
    valiny.append("ambin'ny folo")
  elif (n % 10 != 0):
    if (len(valiny) != 0):
      valiny.append('amby')
    valiny.append(folo[n % 10])
  diovina(valiny)

def zato_(n: int, valiny: list) -> (None):
  if (n % 10 == 1):
    if (len(valiny) != 0):  
      valiny.append('amby')
    valiny.append(zato[n % 10])
  elif (n % 10 != 0):
    if (len(valiny) != 0):
      valiny.append('sy')
    valiny.append(zato[n % 10])
  diovina(valiny)

def arivo_(n: int, valiny: list) -> (None):
  if (n % 10 == 1):
    if (len(valiny) != 0):
      valiny.append('sy')
    valiny.append('arivo')
  elif (n % 10 != 0):
    isa_2(n, valiny, 'arivo')
  diovina(valiny)

def alina_(n: int, valiny: list) -> (None):
  isa_2(n, valiny, 'alina')
  diovina(valiny)

def hetsy_(n: int, valiny: list) -> (None):
  isa_2(n, valiny, 'hetsy')
  diovina(valiny)

def tapitrisa_(n: int, valiny: list) -> (None):
  if (len(valiny) != 0):
    valiny = valiny.extend(['sy', to_s(n), 'tapitrisa'])
  else:
    valiny = valiny.extend([to_s(n), 'tapitrisa'])

def zaraina_folo(n: int) -> (int):
  return n // 10
  
def lany_ve(n: int) -> (bool):
    return n == 0

def diovina(valiny: list) -> (None):
  if (valiny.__contains__('')):
    valiny.remove('')

def isa_2(n: int, valiny: list, s: str) -> (None):
  if (n % 10 != 0):
    if (len(valiny) != 0):
      valiny.append('sy')
    valiny.append(isa[n % 10])
    valiny.append(s)

def to_s2(s: list) -> (str):
  return ' '.join(s)

def to_s(n: int) -> (str):
  valiny = []
  if (n == 0):
    return 'aotra'
  
  if (n <= 10):
    return isa[n]
  
  isa_(n, valiny)
  
  n = zaraina_folo(n)
  folo_(n, valiny)
  
  n = zaraina_folo(n)
  if lany_ve(n): return to_s2(valiny)
  zato_(n, valiny)

  n = zaraina_folo(n)
  if lany_ve(n): return to_s2(valiny)
  arivo_(n, valiny)

  n = zaraina_folo(n)
  if lany_ve(n): return to_s2(valiny)
  alina_(n, valiny)
  
  n = zaraina_folo(n)
  if lany_ve(n): return to_s2(valiny)
  hetsy_(n, valiny)

  n = zaraina_folo(n)
  if lany_ve(n): return to_s2(valiny)
  tapitrisa_(n, valiny)

  return to_s2(valiny)

n = int(input())
print(to_s(n))
