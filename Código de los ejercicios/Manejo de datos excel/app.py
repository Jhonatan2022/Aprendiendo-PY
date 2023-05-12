# Importamos openpyxl para poder trabajar con archivos excel
import openpyxl

# Importamos tabulate para poder imprimir los datos en forma de tabla
from tabulate import tabulate
#--------------------------------------------------------------------------------




#--------------------------------------------------------------------------------
# Creamos una variable para almacenar el nombre del archivo excel y usamos la función load_workbook para cargar el archivo
excel = openpyxl.load_workbook("personas.xlsx")


# Creamos una variable para sacar le libro que está activo
libro_activo = excel.active


# Creamos una lista vacía para almacenar los datos
datos = []

# Creamos un ciclo for para recorrer las filas del archivo excel
# Usamos 1 como inicio porque la fila 0 son los encabezados
# Usamos max_row para que recorra todas las filas del archivo
# Usamos range para que recorra las filas de 1 en 1
for row in range(1,libro_activo.max_row):

    # Creamos una lista vacía para almacenar los datos de cada fila del archivo excel
    _row = [row,]

    # Creamos un ciclo for para recorrer las columnas del archivo excel
    # Usamos 1 como inicio porque la columna 0 son los encabezados
    # Usamos max_column para que recorra todas las columnas del archivo
    # Usamos iter_cols para que recorra las columnas
    for col in libro_activo.iter_cols(1, libro_activo.max_column):

        # Agregamos los datos de cada columna a la lista _row
        _row.append(col[row].value)

    # Agregamos los datos de cada fila a la lista datos
    datos.append(_row)

# Creamos una lista para almacenar los encabezados
headers = ["#", "ID", "Nombre", "Company", "Email", "Mac_Adress"]

# Alineamos los encabezados de manera central
# Usamos len para saber cuantos encabezados hay y multiplicamos por "center" para que todos los encabezados se alineen al centro
header_align = (("center",) * len(headers))


# Imprimimos los datos en forma de tabla
# Usamos tabulate para imprimir los datos en forma de tabla
# Usamos headers para imprimir los encabezados
# Usamos tablefmt para darle formato a la tabla (fancy_grid) = Tabla con bordes
print(tabulate(datos, headers=headers, tablefmt="fancy_grid", colalign=header_align))