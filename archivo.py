import random

modelo = [[[0, 8, 0, 2, 8, 7, 4, 2, 6, 3, 8, 6, 8, 7, 3, 1], 0], [
    [8, 2, 9, 3, 0, 3, 7, 3, 8, 5, 3, 4, 1, 7, 1, 7], 1], [
    [5, 9, 3, 0, 7, 1, 1, 1, 6, 9, 6, 4, 7, 8, 1, 8], 3], [
    [9, 7, 5, 6, 5, 9, 2, 1, 3, 7, 5, 6, 7, 6, 4, 9], 3], [
    [2, 9, 3, 7, 0, 9, 6, 3, 9, 4, 9, 1, 7, 0, 9, 4], 3], [
    [7, 4, 5, 6, 6, 5, 1, 7, 1, 2, 1, 0, 4, 0, 1, 3], 3], [
    [1, 0, 1, 2, 1, 7, 8, 8, 9, 5, 4, 3, 3, 8, 0, 0], 2], [
    [1, 7, 1, 1, 3, 4, 0, 5, 3, 6, 7, 2, 6, 1, 7, 9], 3], [
    [3, 7, 5, 1, 9, 0, 0, 4, 1, 0, 2, 5, 6, 8, 6, 4], 1], [
    [3, 1, 2, 8, 1, 1, 5, 6, 5, 3, 2, 3, 4, 2, 2, 9], 2], [
    [2, 7, 3, 2, 0, 8, 4, 3, 1, 3, 8, 0, 3, 1, 7, 5], 3], [
    [8, 6, 3, 2, 4, 8, 2, 2, 2, 9, 0, 0, 3, 4, 8, 1], 3], [
    [0, 4, 2, 1, 0, 1, 6, 9, 3, 3, 8, 7, 4, 7, 5, 5], 2], [
    [0, 8, 0, 4, 1, 6, 5, 3, 9, 2, 0, 9, 2, 3, 3, 7], 2], [
    [7, 2, 1, 9, 8, 1, 4, 8, 3, 3, 2, 2, 7, 3, 7, 8], 1], [
    [0, 4, 1, 5, 7, 4, 0, 4, 8, 9, 8, 2, 4, 7, 4, 9], 2], [
    [4, 3, 3, 0, 7, 7, 5, 6, 1, 1, 6, 3, 0, 9, 4, 7], 2], [
    [4, 8, 9, 1, 9, 2, 2, 5, 2, 1, 6, 9, 9, 6, 1, 6], 1], [
    [3, 0, 5, 4, 7, 3, 5, 4, 3, 8, 4, 6, 9, 1, 3, 8], 3], [
    [4, 5, 2, 8, 7, 1, 5, 2, 9, 8, 2, 0, 2, 8, 4, 6], 1], [
    [8, 7, 3, 9, 3, 8, 5, 4, 3, 9, 0, 5, 8, 6, 3, 9], 1], [
    [1, 4, 2, 4, 2, 7, 1, 4, 1, 6, 1, 2, 7, 0, 5, 8], 2]]

#Ejercicio de Prueba
#[[[9,0,3,4,2],2],[[7,0,7,9,4],0],[[3,9,4,5,8],2],[[3,4,1,0,9],1],[[5,1,5,4,5],2],[[1,2,5,3,1],1]]

largo = 16
repeticiones = 10
buenos = 3
probabilidad_mutacion = 0.5

print("\n\nModelo: %s\n" % (modelo))


def crear_individual(min, max):

    return[random.randint(min, max) for i in range(largo)]


def crear_poblacion():

    return [crear_individual(0, 9) for i in range(repeticiones)]


def funcion_objetivo(crear_individual):
    fitness = 0
    i = 0
    e = 0
    for e in range(len(modelo)):
        c = 0
        for i in range(len(crear_individual)):
            if crear_individual[i] == modelo[e][0][i]:
                c += 1
        if c == modelo[e][1]:
            fitness += 1
        if c != modelo[e][1]:
            fitness -= 1000
    return fitness


def funcion_cruce(poblacion):
    ordenados = [(calcularFitness(i), i) for i in poblacion]
    ordenados = [i[1] for i in sorted(ordenados)]
    poblacion = ordenados

    mejores = ordenados[(len(ordenados)-buenos):]

    for i in range(len(poblacion)-buenos):
        punto_corte = random.randint(1, largo-1)
        padre = random.sample(mejores, 2)

        poblacion[i][:punto_corte] = padre[0][:punto_corte]
        poblacion[i][punto_corte:] = padre[1][punto_corte:]

    return poblacion


def funcion_mutacion(poblacion):

    for i in range(len(poblacion)-buenos):
        if random.random() <= probabilidad_mutacion:
            punto_corte = random.randint(0, largo-1)
            nuevo_valor = random.randint(0, 9)

            while nuevo_valor == poblacion[i][punto_corte]:
                nuevo_valor = random.randint(0, 9)

            poblacion[i][punto_corte] = nuevo_valor

    return poblacion


poblacion = crear_poblacion()
print("Poblacion Inicial:\n%s" % (poblacion))


#while funcion_objetivo(poblacion[(len(poblacion)-1)])<-1000:
for i in range(1000):
    poblacion = funcion_cruce(poblacion)
    poblacion = funcion_mutacion(poblacion)


MEJOR = poblacion[(len(poblacion)-1)]
Mejor_Fitness = funcion_objetivo(MEJOR)


print("\nPoblacion Final:\n%s" % (MEJOR))
print("\nPoblacion Final2:\n%s" % (Mejor_Fitness))
print("\n\n")
