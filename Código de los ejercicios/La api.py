import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")


def names():
    if response.status_code == 200:
        data = response.json()

        result = data.get("results", [])
        if result:
            name = []
            for pokemon in result:
                name.append(pokemon["name"])
            print(name)


def individual(num):
    if response.status_code == 200:
        data = response.json()

        result = data.get("results", [])
        if result:
            name = []
            for pokemon in result:
                name.append(pokemon["name"])
            print(name[num])


if __name__ == "__main__":
    # print("Acontinuación verás la lista completa de pokemon")
    # names()
    num = int(input("Ingrese un número para ver el pokemon correspondiente: "))
    individual(num)
