from Individuo import Individuo
import random
import math

NUM_INDIVIDUOS = 20
NUM_GENERACIONES = 2
PRECISION = 0.03
RANG_MIN = 0
RANG_MAX = 20.0
PROBABILIDAD_CRUZAMIENTO = 0.7
PROBABILIDAD_MUTACION = 0.01
POPULATION_SIZE = 20



def client_logger(mensaje):
    print(f'[CLIENT] {mensaje}')


def server_logger(mensaje):
    print(f'[SERVER] {mensaje}')

# La lista population se convierta a string
def population_to_string(population):
    messages = []
    for individual in population:
        message = f"{individual.x}/{individual.y}/{individual.fitness}"
        messages.append(message)
    messages = ",".join(messages)

    return messages


# de string a lista
def string_to_population(message):
    individuals = message.split(",")
    population = []

    for individual in individuals:
        data = individual.split("/")
        population.append(Individuo(float(data[0]), float(data[1])))

    return population


# Realiza el cruzamiento entre dos individuos
def cruzar(padre, madre):
    x = (padre.x + madre.x) / 2.0
    y = (padre.y + madre.y) / 2.0

    return Individuo(x, y)


# Selecciona aleatoriamente un individuo de la poblacion
def seleccionar_aleatorio(poblacion):
    index = random.randint(0, len(poblacion) - 1)

    return poblacion[index]


def realizar_cruzamiento(poblacion):
    nueva_poblacion = []
    print('hola')
    print(len(nueva_poblacion))


    while len(nueva_poblacion)<POPULATION_SIZE:
        print('nuevapoblacion: madre y padre')

        padre = seleccionar_aleatorio(poblacion)
        madre = seleccionar_aleatorio(poblacion)
        madre.print()
        padre.print()

        if random.random() < PROBABILIDAD_CRUZAMIENTO:
            print("hijos")
            
            hijo = cruzar(padre, madre)

            nueva_poblacion.append(hijo)
            hijo.print()

    population_to_string(nueva_poblacion)
    return nueva_poblacion

def funcion(x,y):
    return math.pow(x,2)+math.pow(y,2)


def seleccionar_mejores(poblacion):
    poblacion.sort(key=lambda ind: ind.fitness, reverse=True)
    return poblacion[:POPULATION_SIZE // 2]

def evaluarPoblacion(poblacion):
    for individuo in poblacion:
        individuo.fitness = funcion(individuo.x, individuo.y)


def generate_random_double(min_val, max_val):
    return min_val + (max_val - min_val) * random.random()

def mutar(individuo):
    individuo.x += generate_random_double(-PRECISION, PRECISION)
    individuo.y += generate_random_double(-PRECISION, PRECISION)


def realizar_mutacion(poblacion):
    for individuo in poblacion:
        if random.random() < PROBABILIDAD_MUTACION:
            mutar(individuo)
