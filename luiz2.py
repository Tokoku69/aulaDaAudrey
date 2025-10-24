# Função para preencher o vetor conforme o problema
def preenche_vetor(valor_inicial):
    """
    Essa função aceita um valor inteiro inicial e cria um vetor de tamanho 10.
    O primeiro elemento do vetor é o valor inicial e cada elemento subsequente é o dobro do valor do elemento anterior.
   
    Args:
    valor_inicial (int): o valor para a primeira posição do vetor.
   
    Returns:
    list of str: uma lista de strings que representam a saída formatada.
    """
    # Criação do vetor com 10 posições
    N = [0] * 10
   
    # Definição do primeiro valor do vetor
    N[0] = valor_inicial
   
    # Preenchendo o vetor com o dobro do valor da posição anterior
    for i in range(1, 10):
        N[i] = N[i - 1] * 2
   
    # Criando a saída formatada
    resultado = []
    for i in range(10):
        resultado.append(f"N[{i}] = {N[i]}")
   
    return resultado

# Código principal
if __name__ == "__main__":
    # Recebe a entrada do usuário
    valor_inicial = int(input("Digite um valor inteiro (<= 50): "))
   
    # Verifica se o valor está dentro do limite especificado
    if valor_inicial > 50:
        print("O valor deve ser menor ou igual a 50.")
    else:
        # Chama a função e obtém o resultado
        resultado = preenche_vetor(valor_inicial)
       
        # Exibe o resultado linha por linha
        for linha in resultado:
            print(linha)