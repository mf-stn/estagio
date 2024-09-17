def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def esta_na_fibonacci(n):
    sequencia = fibonacci(n)
    return n in sequencia

num = int(input("Digite um número: "))
if esta_na_fibonacci(num):
    print(f"{num} está na sequência de Fibonacci.")
else:
    print(f"{num} não está na sequência de Fibonacci.")