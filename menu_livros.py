import funcoes

done = False
largura = 10
texto = "Menu de Livros"
dec = "-"

while not done:
    print(f"\n{dec*10} {texto} {dec*10}")
    print("""
        [1] - Adicionar
        [2] - Remover
        [3] - Atualizar
        [4] - Buscar
        [5] - Listar
        [6] - Sair
        """)
    print(f"{dec*10} {texto} {dec*10}")

    escolha = (int(input("\n-> Opção:\n")))
    match escolha:
        case 1:
            funcoes.inserir_dados_livros()            
        case 2:
            funcoes.remover_dados_livros()
        case 3:
            funcoes.atualizar_valores()
        case 4:
            funcoes.buscar_valores()
        case 5:
            print()
            funcoes.listar_valores()
        case 6:
            print("\nSaindo...\n")
            break
        case _:
            print("Número inválido")
            