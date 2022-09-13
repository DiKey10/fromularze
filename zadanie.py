import requests,csv,pickle

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()[0]
################

#print(data["rates"])
dane_csv = data["rates"]

################

zerowe=dane_csv[0]
zmienna_slowa = ""
for item in zerowe:
    zmienna_slowa = zmienna_slowa + item + ";"

aktualne_dane_csv=zmienna_slowa[:-1]

####################

raz=[]
for x in range(0,8):
    zmienna_slowa2 = ""
    for item in dane_csv[x].values():
        zmienna_slowa2 = zmienna_slowa2 + str(item) + ";"
    aktualne_dane_csv2 = zmienna_slowa2[:-1]
    raz.append(aktualne_dane_csv2)


with open("raz.csv", 'wb') as f:
    pickle.dump(raz, f)

with open("raz.csv", "rb") as f:
    raz = pickle.load(f)
print(raz)

########