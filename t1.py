import os
import time

# --- GLOBAIS ---------------
# conjunto A e seu tamanho (n)
A = [1, 2, 3, 4, 5]
n = len(A)
# ----------------------------

# verifica se a relação é simétrica
def is_symmetric(relation):
    for (a, b) in relation:
        if (b, a) not in relation:
            return False
    return True

# verifica se a relação é transitiva
def is_transitive(relation):
    for (a, b) in relation:
        for (c, d) in relation:
            if b == c and (a, d) not in relation:
                return False
    return True

# verifica se a relação é reflexiva
def is_reflexive(relation):
    for a in A:
        if (a, a) not in relation:
            return False
    return True

# verifica se a relação é equivalente
def is_equivalent(relation):
    return is_symmetric(relation) and is_transitive(relation) and is_reflexive(relation)

# verifica se a relação é irreflexiva
def is_irreflexive(relation):
    for a in A:
        if (a, a) in relation:
            return False
    return True

# verifica se a relação é função
def is_function(relation):
    for a in A:
        b_values = [b for (x, b) in relation if x == a]
        if len(b_values) > 1:
            return False
    return True

# verifica se a relação é função injetora
def is_injection(relation):
    b_values = [b for (a, b) in relation]
    return len(set(b_values)) == len(b_values)

# verifica se a relação é função sobrejetora
def is_surjection(relation):
    a_values = [a for (a, b) in relation]
    return set(a_values) == A

# verifica se a relação é função bijetora
def is_bijection(relation):
    return is_function(relation) and is_injection(relation) and is_surjection(relation)


# classifica
def classify(relation):
    classification = ""
    if is_symmetric(relation):
        classification += "S"
    if is_transitive(relation):
        classification += "T"
    if is_reflexive(relation):
        classification += "R"
    if is_equivalent(relation):
        classification += "E"
    if is_irreflexive(relation):
        classification += "I"
    if is_function(relation):
        classification += "Fu"
    if is_bijection(relation):
        classification += "Fb"
    if is_surjection(relation):
        classification += "Fs"
    if is_injection(relation):
        classification += "Fi"
    return classification

# retorna conjunto (relação)
def c_pares(subconj,n):
    relation = [(A[i//n], A[i%n]) for i in range(n*n)  if subconj & (1<<(i)) != 0]        
    return relation

# main
def insert_data():
    aux = 0
    with open("clasification.txt", "w") as f:
        for subconj in range(2**(n*n)):
            relation = c_pares(subconj,n)
            clas = classify(relation)
            # escrever as relações e suas classificações em um arquivo texto
            f.write(str(relation) +" "+ clas + "\n")
            aux += 1
    return aux

def print_info(aux):
    # imprimir o tamanho do arquivo texto
    print("Tamanho do arquivo texto: ", os.path.getsize("clasification.txt"), "bytes")
    # imprimir o tempo de execução
    print("Tempo de execucao: ", time.process_time(), "segundos")
    # imprimir o numro de ralações binárias
    print(f"Numero de relacoes binarias: {aux}")

def main():
    aux = insert_data()
    print_info(aux)


main()


