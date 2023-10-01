import pyshorteners

url = "https://github.com/jhonatan2022"

s = pyshorteners.Shortener()

short = s.tinyurl.short(url)

print("La url acortada es: ", short)
