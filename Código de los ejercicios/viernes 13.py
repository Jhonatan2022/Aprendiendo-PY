# /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13
#  * en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */

# Importamos la librería datetime para poder trabajar con fechas
import datetime

# Creamos la función que recibe el mes y el año
def is_friday_13th(month, year):

    # Creamos una variable que almacene la fecha
    date = datetime.date(year, month, 1)

    # Creamos un bucle que recorra los días del mes y año indicados
    while date.month == month:

        # Si el día de la semana es viernes y el día es 13
        if date.weekday() == 4 and date.day == 13:

            # Retornamos verdadero
            return True
        
        # Sumamos un día a la fecha
        date += datetime.timedelta(days=1)

    # Retornamos falso
    return False

# Imprimimos el resultado
print(is_friday_13th(10, 2023))