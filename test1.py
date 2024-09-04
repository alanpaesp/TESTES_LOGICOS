def pertence_fibonacci(numero):
  """Verifica se um número pertence à sequência de Fibonacci.

  Args:
    numero: O número a ser verificado.

  Returns:
    True se o número pertence à sequência, False caso contrário.
  """

  a, b = 0, 1
  while b <= numero:
    if b == numero:
      return True
    a, b = b, a + b
  return False

# Obtendo o número a ser verificado
# Você pode substituir esta linha por outras formas de entrada, como input()
numero = int(input("Digite um número: "))

# Chamando a função e imprimindo o resultado
if pertence_fibonacci(numero):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")
