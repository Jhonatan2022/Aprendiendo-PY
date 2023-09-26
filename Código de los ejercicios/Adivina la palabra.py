"""
    Reto #13: Adivina la palabra
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""
# Importamos la librería random para poder generar números aleatorios
# Importamos la librería requests_html para poder capturar una palabra aleatoria de una web
from requests_html import HTMLSession
import random

# Turnos de juego
difficulty = {"easy": 10, "normal": 5, "hard": 3}

# Línea para separar
LINE = "*" * 70


# Función que captura una palabra aleatorio de una web y retorna la misma.
def catch_a_word():
    # Capturamos la página web
    word_page = HTMLSession().get(
        "https://www.palabrasaleatorias.com/?fs=1&fs2=0&Submit=Nueva+palabra#"
    )

    # Retornamos la palabra en minúsculas
    return word_page.html.find("tr", first=True).find("div", first=True).text.lower()


# Función que crea los elementos del juego
def make_game_elements(base_word):
    # Creamos una lista con los índices de la palabra
    long_word = len(base_word)
    list_index_word = list(range(long_word))
    result_word = list(base_word)

    # Creamos una lista con las letras que se van a ocultar
    letter_of_the_word = []

    # Creamos un bucle que oculte letras aleatorias de la palabra
    for i in range(int(long_word * 0.6)):
        # Seleccionamos un índice aleatorio de la lista
        index = random.choice(list_index_word)
        list_index_word.remove(index)
        letter_of_the_word.append(result_word[index])

        # Ocultamos la letra
        result_word[index] = "_"

    # Retornamos la palabra base, la palabra oculta, las letras ocultas y la longitud de la palabra
    return base_word, "".join(result_word), letter_of_the_word, long_word


# Función que ejecuta el juego
def game(turns):
    # Creamos los elementos del juego
    word, hidden_word, list_letters, long_word = make_game_elements(catch_a_word())

    # Creamos un bucle que se repita mientras el usuario no acierte la palabra
    while turns > 0:
        # Imprimimos los elementos del juego
        print(
            f"Palabra: {hidden_word} \nLongitud: {long_word}\nTURNOS RESTANTES {turns} \n"
            + LINE
        )

        # Pedimos al usuario que introduzca una letra o la palabra
        user_input = input("Inserta una letra o la palabra a adivinar: ")

        # Creamos un bucle que compruebe que el usuario ha introducido una letra o la palabra
        while len(user_input) > 1 and len(user_input) != long_word:
            print("\nENTRADA INVALIDA\n" + LINE)
            user_input = input("Inserta una letra o la palabra a adivinar: ")

        # Descubre la palabra
        if user_input == word:
            # Imprimimos el mensaje de victoria y la palabra
            print(f"\n¡¡¡HAS GANADO!!!\n Palabra:{word}")
            break

        # Descubre una letra
        elif user_input in list_letters:
            # Imprimimos el mensaje de acierto y la palabra
            print("\nLETRA DESCUBIERTA")
            hidden_word = list(hidden_word)
            count = 0

            # Creamos un bucle que sustituya las letras ocultas por las letras descubiertas
            for letter in word:
                # Comprobamos si la letra de la palabra es igual a la letra introducida por el usuario
                if letter == user_input:
                    # Sustituimos la letra oculta por la letra descubierta
                    hidden_word[count] = user_input

                # Aumentamos el contador
                count += 1

            # Convertimos la lista en una cadena
            hidden_word = "".join(hidden_word)

            # Creamos un bucle que compruebe si la palabra está descubierta
            if word == hidden_word:
                # Imprimimos el mensaje de victoria y la palabra
                print(f"\n¡¡¡HAS GANADO!!!\n Palabra:{word}")
                break

        # No descubre ni la palabra ni una letra
        else:
            # Imprimimos el mensaje de fallo
            print("\nHAS FALLADO")
            turns -= 1

    # Creamos un bucle que compruebe si se han terminado los turnos
    if turns == 0:
        # Imprimimos el mensaje de derrota y la palabra
        print(f"\nSE TERMINARON LOS TURNOS\n Palabra: {word}")


# Ejecutamos el juego
if __name__ == "__main__":
    # Imprimimos el mensaje de bienvenida y las opciones de dificultad
    game(difficulty["normal"])