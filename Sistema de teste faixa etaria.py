
def faixa_etaria(numero):
    if numero < 18:
        return "Inválido (Menor que 18)"
    elif 18 <= numero <= 59 :
        return "Válido (Entre 18 e 59 )"
    else:
        return "Inválido (Maior que 59)"
    
valores_teste = [17, 19, 20, 57, 58, 61]

for valor in valores_teste:
    print(f"Entrada: {valor} Classe: {faixa_etaria(valor)}")

    
