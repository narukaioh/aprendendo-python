clientes = [{
  'nome': "Supermecado Dosul",
  'quantidade_produtos': 100,
  'tem_bonus': False
},{
  'nome': "zafari",
  'quantidade_produtos': 300,
  'tem_bonus': False
}]

def add_cliente ():
  nome = input("Digite o nome:")
  quantidade_produto = int(input("Digite a quantidade:"))

  clientes.append({
    'nome': nome,
    'quantidade_produtos': quantidade_produto,
    'tem_bonus': quantidade_produto > 1000
  })

def icms (preco):
  return preco * 0.18


def ipi (preco):
  return preco * 0.04


def pis (preco):
  return preco * 0.0186


def cofins (preco):
  return preco * 0.0854

def imprimir_tributos (preco) :
  print("--- tributos ---")
  print(f"ICMS: {icms(preco)}")
  print(f"IPI: {ipi(preco)}")
  print(f"PIS: {pis(preco)}")
  print(f"COFINS: {cofins(preco)}")


def main ():
  preco_unitario = 4.5
  add_cliente()

  for cliente in clientes:
    preco_total = cliente['quantidade_produtos'] * preco_unitario
    imprimir_tributos(preco_total)


main()