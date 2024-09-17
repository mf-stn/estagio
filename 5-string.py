def inverter_string(string):
    invertida = ''
    for char in string:
        invertida = char + invertida
    return invertida

# Exemplo de uso
string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")
