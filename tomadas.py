# Leitura dos quatro inteiros que representam as tomadas de cada régua
T1, T2, T3, T4 = map(int, input().split())

# Cálculo do número máximo de aparelhos que podem ser conectados
max_aparelhos = T1 + T2 + T3 + T4 - 3

# Exibe o resultado
print(max_aparelhos)
