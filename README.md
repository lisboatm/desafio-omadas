# Desafio: Tomadas 🔌

### 📝 Descrição
O time da Universidade finalmente se classificou para a Final Nacional da Maratona de Programação da SBC. Os três membros da equipe e o técnico estão ansiosos para competir, e além de treinar muito, estão planejando todos os detalhes para a viagem até São Paulo, onde será realizada a competição.

Durante a viagem, eles pretendem levar todos os seus equipamentos eletrônicos, como celular, tablet, notebook, ponto de acesso Wi-Fi, câmeras, etc. No entanto, eles foram avisados de que no quarto de hotel onde ficarão hospedados há apenas uma tomada disponível. 

Para resolver esse problema, cada um dos quatro membros comprou uma régua de tomadas. As réguas permitem conectar vários aparelhos à única tomada disponível no quarto, e é possível ligar uma régua em outra para expandir o número de tomadas. Este desafio consiste em calcular o número máximo de aparelhos que podem ser conectados ao mesmo tempo, dadas as tomadas das quatro réguas.

---

### 📥 Entrada
A entrada consiste de uma única linha contendo quatro números inteiros:
```
T1 T2 T3 T4
```
- Cada número representa o número de tomadas em uma das quatro réguas.
- Restrições: \( 2 \leq Ti \leq 6 \)

---

### 📤 Saída
A saída deve conter um único número inteiro, indicando o número máximo de aparelhos que podem ser conectados simultaneamente.

---

### 💡 Exemplo de Entrada e Saída

#### Exemplo 1:
**Entrada:**
```
2 4 3 2
```
**Saída:**
```
8
```

#### Exemplo 2:
**Entrada:**
```
6 6 6 6
```
**Saída:**
```
21
```

#### Exemplo 3:
**Entrada:**
```
2 2 2 2
```
**Saída:**
```
5
```

---

### 🚀 Explicação da Solução
Para resolver o problema, devemos considerar que ao conectar uma régua à outra, ocupamos uma das tomadas da régua anterior. Portanto, para calcular o número total de aparelhos que podem ser conectados:

1. Somamos o número de tomadas de todas as quatro réguas.
2. Subtraímos 3 tomadas (pois ao conectar uma régua à outra, ocupamos uma tomada para cada conexão).

A fórmula para o cálculo é:
```
Máximo de aparelhos = T1 + T2 + T3 + T4 - 3
```

---

### 🛠️ Implementação em Python

```python
# Leitura dos quatro inteiros que representam as tomadas de cada régua
T1, T2, T3, T4 = map(int, input().split())

# Cálculo do número máximo de aparelhos que podem ser conectados
max_aparelhos = T1 + T2 + T3 + T4 - 3

# Exibe o resultado
print(max_aparelhos)
```

---

### 🏅 Complexidade
A solução possui uma complexidade **O(1)**, já que a operação envolve apenas somas e subtrações simples, independentemente do valor das entradas.

---

### 🏷️ Tags
- Python
- Matemática
- Lógica Simples
- Competição de Programação
- Olimpíada Brasileira de Informática

---

### 📂 Licença
Distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
