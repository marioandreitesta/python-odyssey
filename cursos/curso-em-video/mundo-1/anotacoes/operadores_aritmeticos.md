
# Operadores Aritméticos em Python 🧮

Os operadores aritméticos são símbolos usados para realizar cálculos matemáticos fundamentais em Python.

---

### 1. Os Sete Operadores Básicos

*   **`+` (Adição):** Soma dois valores.
    *   *Exemplo:* `5 + 2 == 7`
*   **`-` (Subtração):** Subtrai o segundo valor do primeiro.
    *   *Exemplo:* `5 - 2 == 3`
*   **`*` (Multiplicação):** Multiplica dois valores.
    *   *Exemplo:* `5 * 2 == 10`
*   **`/` (Divisão):** Divide o primeiro pelo segundo (sempre resulta em um `float`).
    *   *Exemplo:* `5 / 2 == 2.5`
*   **`**` (Potência):** Eleva o primeiro valor à potência do segundo.
    *   *Exemplo:* `5 ** 2 == 25`
*   **`//` (Divisão Inteira):** Realiza a divisão e descarta a parte decimal.
    *   *Exemplo:* `5 // 2 == 2`
*   **`%` (Resto da Divisão):** Retorna o resto que sobra de uma divisão inteira.
    *   *Exemplo:* `5 % 2 == 1`

---

### 2. Ordem de Precedência

Assim como na matemática, o Python segue uma ordem específica para resolver as operações:

1.  **`()`** - Parênteses (Tudo o que estiver dentro deles é resolvido primeiro).
2.  **`**`** - Potências.
3.  **`*`, `/`, `//`, `%`** - Multiplicação, divisões e resto (quem aparecer primeiro da esquerda para a direita).
4.  **`+`, `-`** - Adição e subtração.

---

### 3. Dicas e Curiosidades

*   **Raiz Quadrada:** Você pode calcular a raiz quadrada de um número elevando-o a `0.5` ou `(1/2)`.
    *   *Exemplo:* `81 ** (1/2) == 9.0`
*   **Operadores com Strings:** O sinal de `+` pode ser usado para **concatenar** (juntar) textos, e o `*` para **repetir** textos.
    *   *Exemplo:* `'Olá' + 'Mundo'` resulta em `'OláMundo'`.
    *   *Exemplo:* `'Oi' * 5` resulta em `'OiOiOiOiOi'`.

---

### 4. Quando usar `int` ou `float`?

A escolha entre `int` (inteiro) e `float` (ponto flutuante) depende da precisão necessária e da natureza do dado.

*   **`int` (Inteiro):** Use quando estiver lidando com contagens de itens que não podem ser divididos.
    *   *Exemplo:* Quantidade de pessoas, número de repetições, dias da semana.
    *   *Código:* `pessoas = 10`
*   **`float` (Ponto Flutuante):** Use para medidas que exigem casas decimais ou maior precisão.
    *   *Exemplo:* Preços, alturas, pesos, médias escolares.
    *   *Código:* `preco = 19.90` ou `altura = 1.75`

**Exemplo Prático:**
```python
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.3f}')
print(f'Divisão inteira {di} e potência {e}')
```
