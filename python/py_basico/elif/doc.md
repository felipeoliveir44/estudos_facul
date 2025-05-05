# Comando `elif` em Python

O comando `elif` (abreviação de "else if") é usado em estruturas condicionais para testar múltiplas expressões diferentes. Ele é utilizado após um `if` e antes de um `else`, permitindo verificar várias condições de forma ordenada.

## Sintaxe

```python
if condição1:
    # bloco se condição1 for verdadeira
elif condição2:
    # bloco se condição2 for verdadeira
elif condição3:
    # bloco se condição3 for verdadeira
else:
    # bloco se nenhuma condição anterior for verdadeira
```

## Exemplo

```python
nota = 85

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")
```

**Saída:**
```
B
```

## Funcionamento

- O Python avalia as condições de cima para baixo.
- Assim que uma condição for `True`, o bloco correspondente é executado e o restante é ignorado.
- O `else` é opcional e executado apenas se **nenhuma das condições anteriores** for satisfeita.

## Exemplo sem `else`

```python
numero = 0

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
# Nenhuma ação é tomada se for zero
```

**Saída:**
(nenhuma, pois número é zero)

## Boas Práticas

- Use `elif` quando houver **mais de duas possibilidades exclusivas**.
- Mantenha as condições organizadas por ordem lógica ou prioridade.
- Evite sobreposição de condições para garantir
