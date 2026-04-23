---
name: Manipulação e Verificação de Strings em Python
description: Guia para iniciantes sobre as principais técnicas de manipulação e verificação de strings no backend Python.
type: reference
---

# Manipulação e Verificação de Strings em Python

Este documento apresenta as formas mais utilizadas de trabalhar com **strings** em Python, focado no desenvolvimento backend e direcionado a iniciantes.

---
## 1. Criação de Strings

```python
# Strings simples
texto = "Olá, Mundo!"

# Strings com aspas simples ou duplas
texto1 = 'Python'
texto2 = "Python"

# Strings cruas (raw) – útil para caminhos Windows ou expressões regulares
caminho = r"C:\Users\mario\projetos"

# String multilinha usando três aspas
multilinha = """Esta é uma string
que ocupa várias linhas.
"""
```
---
## 2. Concatenar e Repetir

```python
# Concatenar com +
nome = "Maria"
saudacao = "Olá, " + nome

# Interpolação (f‑strings) – recomendado
saudacao = f"Olá, {nome}!"

# Repetir strings com *
linha = "-" * 30
```
---
## 3. Métodos de Consulta

| Método | Descrição |
|--------|-----------|
| `len(s)` | tamanho da string |
| `s.startswith(prefix)` | verifica início |
| `s.endswith(suffix)` | verifica final |
| `s.find(sub)` | posição da primeira ocorrência ou `-1` |
| `s.index(sub)` | mesma coisa, lança `ValueError` se não houver |
| `s.count(sub)` | quantas vezes aparece |
| `s.isnumeric()` / `s.isdigit()` | contém apenas dígitos |
| `s.isalpha()` | contém apenas letras |
| `s.isspace()` | contém apenas espaços em branco |

---
## 4. Transformação de Strings

```python
texto = "   Python é incrível!   "

# Remover espaços
texto = texto.strip()          # "Python é incrível!"
texto = texto.lstrip()         # remove à esquerda
texto = texto.rstrip()         # remove à direita

# Maiúsculas/minúsculas
texto.upper()   # 'PYTHON É INCRÍVEL!'
texto.lower()   # 'python é incrível!'
texto.title()   # 'Python É Incrível!'

# Substituir substrings
texto = texto.replace("incrível", "fantástico")
```
---
## 5. Divisão e Junção

```python
frase = "maçã,banana,laranja"
lista = frase.split(',')   # ['maçã', 'banana', 'laranja']

# Unir novamente
nova_frase = ', '.join(lista)   # 'maçã, banana, laranja'
```
---
## 6. Formatação Avançada

```python
valor = 12345.6789
# Formatação com f‑string
print(f"Valor formatado: {valor:,.2f}")   # Valor formatado: 12,345.68

# Padding e alinhamento
nome = "Ana"
print(f"{nome:<10}")   # à esquerda, largura 10
print(f"{nome:>10}")   # à direita
print(f"{nome:^10}")   # centralizado
```
---
## 7. Expressões Regulares (regex)

```python
import re
texto = "Contato: maria@example.com"
# Encontrar e validar email simples
padrao = r"[\w.-]+@[\w.-]+\.\w+"
match = re.search(padrao, texto)
if match:
    print("Email encontrado:", match.group())
```
---
## 8. Codificação e Decodificação

```python
# Texto Unicode para bytes
s = "Olá"
bytes_s = s.encode('utf-8')   # b'Ol\xc3\xa1'

# Bytes de volta para string
s2 = bytes_s.decode('utf-8')  # 'Olá'
```
---
## 9. Exemplos Práticos (Backend)

### 9.1. Validar Dados de API
```python
def validar_usuario(payload: dict) -> bool:
    email = payload.get('email', '')
    nome = payload.get('nome', '').strip()

    # Email simples com regex
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return False

    # Nome deve ter ao menos 2 caracteres
    if len(nome) < 2:
        return False
    return True
```

### 9.2. Normalizar Texto antes de salvar no banco
```python
def normalizar(texto: str) -> str:
    texto = texto.strip().lower()
    # Remove acentos (exemplo simples)
    import unicodedata
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join(c for c in texto if not unicodedata.combining(c))
    return texto
```
---
## 10. Dicas para Iniciantes

1. **Prefira f‑strings** – são mais legíveis e eficientes.
2. Use **`strip`** para limpar entradas de usuários antes de validar.
3. Quando precisar de verificação mais complexa, **expressões regulares** são poderosas, mas mantenha-as simples.
4. Sempre teste **casos de borda** – strings vazias, espaços, caracteres não‑ASCII.
5. Lembre‑se que strings são **imutáveis**; cada operação cria um novo objeto.

---
> **Próximos passos** – Explore o módulo `textwrap` para formatar texto em colunas e o pacote `python‑slugify` para gerar slugs seguros para URLs.
