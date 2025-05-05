# Laço `while` em Python

O laço `while` é uma estrutura de repetição que executa um bloco de código enquanto uma condição for verdadeira.

## Sintaxe

```python
while condição:
    # bloco de código
```

- A **condição** é avaliada antes de cada iteração.
- O **bloco de código** é executado repetidamente enquanto a condição for `True`.
- Quando a condição se torna `False`, a execução do laço é interrompida.

## Exemplo Básico

```python
contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1
```

**Saída:**
```
Contador: 0  
Contador: 1  
Contador: 2  
Contador: 3  
Contador: 4
```

## Uso com `break`

```python
while True:
    entrada = input("Digite 'sair' para encerrar: ")
    if entrada == "sair":
        break
```

## Uso com `continue`

```python
numero = 0

while numero < 5:
    numero += 1
    if numero == 3:
        continue # Irá sair do laço.
    print(numero)
```

**Saída:**
```
1  
2  
4  
5
```

## Loops Infinitos

```python
while True:
    # Executa para sempre até que um break seja acionado
    ...
```

## Cuidados

- Certifique-se de que a condição eventualmente se tornará falsa.
- Loops infinitos não controlados podem travar o programa.

## Comparação com `for`

- Use `for` quando souber previamente o número de repetições (por exemplo, iterar sobre listas).
- Use `while` quando a repetição depende de uma **condição dinâmica**.

## Conclusão

O `while` é uma ferramenta poderosa para controle de fluxo em Python, ideal para situações em que a quantidade de repetições não é previamente conhecida. Com o uso de `break` e `continue`, é possível construir comportamentos complexos e eficientes.
