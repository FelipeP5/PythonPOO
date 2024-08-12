idade = 17
tem_cartao = True

if idade >= 18:
    if tem_cartao:
        print("Você pode comprar o produto.")
    else:
        print("Você NÃO pode comprar o produto pois lhe falta o cartão.")
else:
    print("Você é menor de idade e por isso pode levar o produto de graça.")
    while tem_cartao:
        print("Por favor leve de graça")
        tem_cartao = input()