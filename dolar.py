def converter_dolar_para_real():
    conversao_real = float(input("Digite o valor em real: "))
    

    
    dolar = conversao_real / 5.64
    print("-----------------------------------------------------")
    print(f"seu valor em dolar é:{dolar: .2f}$")

def coverter_real_para_dolar():
    cotacao_dolar = 5.64
    reais = float(input("Digite seu valor em reais: "))
    dolares = reais / cotacao_dolar
    print("-----------------------------------------")
    print(f"{reais} BRL equivale a US$ {dolares:.2f}")

def menu():
    while True:
        print("\nConvensor de Moedas")
        print("[1] Converter Dolar para Real")
        print("[2] Converter Real para Dolar")
        print("[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            converter_dolar_para_real()
        elif opcao == '2':
            coverter_real_para_dolar()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("!!! Opção inválida. Tente novamente !!!")
menu()