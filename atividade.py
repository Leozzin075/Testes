def calculando():
    if x > 0 and y > 0:
        return print("Primeiro quadrante")
    elif x < 0 and y > 0:
        return print("Segundo quadrante")
    elif x < 0 and y < 0:
        return print("Terceiro quadrante")
    elif x > 0 and y < 0:
        return print("Quarto quadrante")
    else: 
        return None


while True:
    resposta = str(input("Voce quer testar? (S/N): "))
    if resposta == "S" or resposta == "s":
        x = int(input("Digite um numero do X:\n"))
        y = int(input("Digite um numero do Y:\n"))    
    
        if x == 0 or y == 0:
            print("Nao é possivel achar um quadrante")
            print("Programa encerrado!!")
            break
        
        else:
            calculando()
            continue
    
    elif resposta == "N" or resposta == "n":
        print("Fim do programa")
        break
    
    else:
        print("Voce digitou algo errado, tente novamente")
        continue