
def imprimir_tributos (icms, ipi, pis, cofins) :
  print("--- tributos ---")
  print(f"ICMS: {icms}")
  print(f"IPI: {ipi}")
  print(f"PIS: {pis}")
  print(f"COFINS: {cofins}")


def icms (qualquer):
  return qualquer * 0.18


def ipi (preco):
  return preco * 0.04


def pis (preco):
  return preco * 0.0186


def cofins (preco):
  return preco * 0.0854

quantidade = 400
preco = 4.50

valor_icms = icms(preco * quantidade)
valor_ipi = ipi(preco * quantidade)
valor_pis = pis(preco * quantidade)
valor_cofins = cofins(preco * quantidade)

imprimir_tributos(valor_icms, valor_ipi, valor_pis,valor_cofins)





