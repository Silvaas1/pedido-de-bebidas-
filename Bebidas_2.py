bebida1 = "Whisky"
bebida2 = "Refrigerante"
bebida3 = "Água"
bebida4 = "Suco"
bebida5 = "Cerveja"

valor1 = 4.99
valor2 = 7.99
valor3 = 2.99
valor4 = 10.99
valor5 = 8.99

nome = input("Olá tudo bem? Poderia nos informar o seu nome?")
idade = int(input("Digite sua idade: "))

print(f"Olá{nome} como você está?")
print(f"Que legal você tem {idade} anos.")

if idade >= 18:
    
    print(f"Neste caso você pode entrar normalmente na festa por possuir {idade} anos.")
    print("Só tome cuidado, e uma ótima festa")
    
    print("Poderia me ver uma bebida por gentileza?") 
    
    print(f"Claro, temos em nosso cardápio {bebida1, bebida2, bebida3, bebida4, bebida5}.")
    
    
    
    while(True):
        bebida = int(input(f"Digite 1 para {bebida1}\n Digite 2 para {bebida2}\n Digite 3 para {bebida3}\n Digite 4 para {bebida4}\n Digite 5 para {bebida5}"))
    
        if bebida == 1:
            
            print(f"Seu {bebida1} irá custar {valor1} reais.")
            break
        elif bebida == 2:
            print(f"Seu {bebida2} irá custar R$ {valor2} reais.")
            break
        elif bebida == 3:
            print(f"Seu {bebida3} irá custar R$ {valor3} reais.")
            break
        elif bebida == 4:
            print(f"Seu {bebida4} irá custar R$ {valor4} reais.")
            break
        elif bebida == 5:
            print(f"Seu {bebida5} irá custar R$ {valor5} reais.")
            break
        else:
            print("Digite novamente, bebida não encontrada!!!")
              
        
    while(True):   
        pag = input("Qual seria a forma de pagamento?")
        if pag == "Pix":
            print(f"Perfeito Sr. {nome}, pagamento realizado! Agradecemos pela preferência, tenha um ótimo final de semana")
            break
        elif pag == "Dinheiro":
            print(f"Perfeito Sr. {nome}, pagamento realizado! Agradecemos pela preferência, tenha um ótimo final de semana")
            break
        elif pag == "Débito":
            print(f"Perfeito Sr. {nome}, pagamento realizado! Agradecemos pela preferência, tenha um ótimo final de semana")
            break
        else:
            print("Verifique outra forma de pagamento por favor.")
            
                
else:
    print("Você não pode entrar pois não tem a idade o suficiente")
    