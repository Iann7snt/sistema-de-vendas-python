produtos = []
vendas = []

def cadastrar_produto():
    print("\n===== CADASTRAR PRODUTO =====")

    # Pedir o nome do produto
    while True:
        nome = input("Nome do produto: ").strip()

        if nome != "":
            break
        else:
            print("O nome não pode ficar vazio!")

    # Pedir o preço do produto
    while True:
        try:
            preco = float(input("Preço do produto: R$ ").replace(",", "."))

            if preco < 0:
                print("O preço não pode ser negativo!")
            else:
                break

        except ValueError:
            print("Digite um preço válido!")

    # Pedir a quantidade do produto
    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))

            if quantidade < 0:
                print("A quantidade não pode ser negativa!")
            else:
                break

        except ValueError:
            print("Digite um número inteiro válido!")

    # Criar o produto
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    # Adicionar o produto à lista
    produtos.append(produto)

    print("\nProduto cadastrado com sucesso!")
    print("Total de produtos cadastrados:", len(produtos))

def listar_produtos():
    print("\n===== PRODUTOS CADASTRADOS =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado!")

    else:
        for numero, produto in enumerate(produtos, start=1):
            print("\nProduto", numero)
            print("Nome:", produto["nome"])
            print("Preço: R$", f'{produto["preco"]:.2f}')
            print("Quantidade:", produto["quantidade"])
            print("------------------------")

def calcular_desconto(valor):
    if valor < 100:
        desconto = 0
    elif valor < 300:
        desconto = valor * 0.05
    else:
        desconto = valor * 0.10

    return desconto

def realizar_venda():
    print("\n===== REALIZAR VENDA =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado!")
        return

    carrinho = {}

    while True:
        listar_produtos()

        print("\n0 - Cancelar venda")
        print("-1 - Finalizar carrinho")

        try:
            escolha = int(input("Digite o número do produto: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if escolha == 0:
            print("Venda cancelada! Voltando ao menu...")
            return

        if escolha == -1:
            if len(carrinho) == 0:
                print("O carrinho está vazio!")
                continue
            break

        if escolha < 1 or escolha > len(produtos):
            print("Produto inválido!")
            continue

        indice = escolha - 1
        produto = produtos[indice]

        reservado = carrinho.get(indice, 0)
        disponivel = produto["quantidade"] - reservado

        if disponivel <= 0:
            print("Produto sem estoque disponível!")
            continue

        try:
            quantidade = int(input(
                "Quantidade (0 para cancelar a venda): "
            ))
        except ValueError:
            print("Digite uma quantidade válida!")
            continue

        if quantidade == 0:
            print("Venda cancelada! Voltando ao menu...")
            return

        if quantidade < 0 or quantidade > disponivel:
            print("Quantidade inválida ou estoque insuficiente!")
            continue

        carrinho[indice] = reservado + quantidade
        print("Produto adicionado ao carrinho!")

    valor_bruto = 0
    quantidade_total = 0
    descricao = []

    print("\n===== RESUMO DO CARRINHO =====")

    for indice, quantidade in carrinho.items():
        produto = produtos[indice]
        subtotal = produto["preco"] * quantidade

        valor_bruto += subtotal
        quantidade_total += quantidade

        descricao.append(
            f"{produto['nome']} ({quantidade} un.)"
        )

        print(
            f"{produto['nome']} - {quantidade} un. "
            f"- R$ {subtotal:.2f}"
        )

    desconto = calcular_desconto(valor_bruto)
    valor_final = valor_bruto - desconto

    print(f"\nValor bruto: R$ {valor_bruto:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total a pagar: R$ {valor_final:.2f}")

    confirmar = input("Confirmar compra? (s/n): ").lower().strip()

    if confirmar != "s":
        print("Compra cancelada! Estoque preservado.")
        return
    
    itens_venda = []

    for indice, quantidade in carrinho.items():
        produto = produtos[indice]

        produto["quantidade"] -= quantidade

        item = {
            "nome": produto["nome"],
            "quantidade": quantidade,
            "preco_unitario": produto["preco"],
            "subtotal": produto["preco"] * quantidade
        }

        itens_venda.append(item)

    venda = {
        "produto": ", ".join(descricao),
        "quantidade": quantidade_total,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final,
        "itens": itens_venda
    }

    vendas.append(venda)


    print("\n===== VENDA REALIZADA COM SUCESSO =====")
    print(f"Total pago: R$ {valor_final:.2f}")
    print("Estoque atualizado!")
        
def calcular_faturamento(lista_vendas):
    total = 0

    for venda in lista_vendas:
        total += venda["valor_final"]

    return total

def gerar_relatorio():
    print("\n===== RELATÓRIO DE VENDAS =====")

    numero_vendas = len(vendas)
    faturamento = calcular_faturamento(vendas)

    print("Número de vendas:", numero_vendas)
    print(f"Faturamento total: R$ {faturamento:.2f}")

    if numero_vendas == 0:
        print("Nenhuma venda realizada até o momento!")

    else:
        print("\n===== VENDAS REGISTRADAS =====")

        for numero, venda in enumerate(vendas, start=1):
            print("\nVenda", numero)
            print("Produto:", venda["produto"])
            print("Quantidade:", venda["quantidade"])
            print(f"Valor final: R$ {venda['valor_final']:.2f}")
            print("------------------------")
            
def contagem_regressiva(n):
    print(n)

    if n == 0:
        return

    contagem_regressiva(n - 1)

while True: 
    print("===== SISTEMA DE VENDAS =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Realizar venda")
    print("4 - Calcular desconto")
    print("5 - Relatório de vendas")
    print("6 - Contagem regressiva")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
       listar_produtos()

    elif opcao == "3":
        realizar_venda()
        
    elif opcao == "4":
        print("\n===== CALCULAR DESCONTO =====")

        try:
            valor = float(input("Digite o valor da compra: R$ ").replace(",", "."))

            if valor < 0:
                print("O valor não pode ser negativo!")
            else:
                desconto = calcular_desconto(valor)
                valor_final = valor - desconto

                print(f"Valor da compra: R$ {valor:.2f}")
                print(f"Desconto: R$ {desconto:.2f}")
                print(f"Total a pagar: R$ {valor_final:.2f}")

        except ValueError:
            print("Digite um valor válido!")

    elif opcao == "5":
        gerar_relatorio()

    elif opcao == "6":
        print("\n===== CONTAGEM REGRESSIVA =====")

        try:
            numero = int(input("Digite um número inteiro não negativo: "))

            if numero < 0:
                print("O número não pode ser negativo!")
            else:
                contagem_regressiva(numero)
                print("Contagem finalizada!")

        except ValueError:
            print("Digite um número inteiro válido!")

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")