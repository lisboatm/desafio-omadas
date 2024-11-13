def max_devices(T1, T2, T3, T4):
    # Calcula o número máximo de dispositivos que podem ser conectados
    total = T1 + T2 + T3 + T4 - 3
    return total

# Leitura da entrada
T1, T2, T3, T4 = map(int, input().split())

# Exibe o resultado
print(max_devices(T1, T2, T3, T4))
