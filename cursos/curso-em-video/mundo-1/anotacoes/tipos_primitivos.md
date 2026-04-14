# Tipos Primitivos em Python 🐍

Em Python, todo valor tem um **tipo**. Entender esses tipos é fundamental para manipular dados corretamente.

---

### 1. Os Quatro Tipos Básicos

*   **`int` (Inteiros):** Números sem casas decimais, positivos ou negativos.
    *   *Exemplos:* `7`, `-4`, `0`, `9875`.
    *   *Uso:* Contagens, idades, anos.
*   **`float` (Ponto Flutuante):** Números reais, com casas decimais (usamos ponto `.`, não vírgula).
    *   *Exemplos:* `4.5`, `0.076`, `-15.223`, `7.0`.
    *   *Uso:* Preços, pesos, medidas precisas.
*   **`bool` (Booleanos):** Valores lógicos de Verdadeiro ou Falso.
    *   *Valores:* `True` ou `False`. (Sempre com a primeira letra maiúscula).
    *   *Uso:* Condições e testes lógicos.
*   **`str` (Strings):** Cadeias de caracteres (textos).
    *   *Exemplos:* `'Olá'`, `"7.5"`, `''` (vazia).
    *   *Uso:* Nomes, mensagens, qualquer dado textual.

---

### 2. Descobrindo o Tipo com `type()`

Para saber qual o tipo de uma variável ou valor, usamos a função `type()`:

```python
n = 5
print(type(n))  # Saída: <class 'int'>
```

---

### 3. Métodos de Verificação (`is...`)

Strings possuem métodos que verificam o conteúdo da variável e retornam um valor booleano (`True` ou `False`). Os mais comuns são:

*   **`.isnumeric()`**: Verifica se o conteúdo pode ser convertido em um número.
*   **`.isalpha()`**: Verifica se o conteúdo é composto apenas por letras (alfabético).
*   **`.isalnum()`**: Verifica se é alfanumérico (letras e/ou números).
*   **`.isupper()`**: Verifica se está tudo em letras maiúsculas.
*   **`.islower()`**: Verifica se está tudo em letras minúsculas.
*   **`.isspace()`**: Verifica se contém apenas espaços em branco.
*   **`.istitle()`**: Verifica se está capitalizada (ex: "Python" -> True).

**Exemplo Prático:**
```python
algo = input('Digite algo: ')
print(f'É numérico? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
```
