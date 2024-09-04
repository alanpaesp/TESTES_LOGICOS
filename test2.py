def contar_as(frase):
  """Conta a quantidade de vezes que a letra 'a' (maiúscula ou minúscula) aparece em uma frase.

  Args:
    frase: A frase a ser analisada.

  Returns:
    O número de vezes que a letra 'a' aparece na frase.
  """

  # Converte a frase toda para minúsculas para facilitar a contagem
  frase_minuscula = frase.lower()

  # Conta as ocorrências da letra 'a' usando o método count()
  quantidade_as = frase_minuscula.count('a')

  return quantidade_as

# Obtendo a frase do usuário
frase = input("Digite uma frase: ")

# Chamando a função e imprimindo o resultado
quantidade_as = contar_as(frase)
print(f"A letra 'a' aparece {quantidade_as} vezes na frase.")