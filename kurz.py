import httpx
from termcolor import colored


def stahni_data():
    url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
    return httpx.get(url)


def stahni_kurzy():
    data = stahni_data()
    radky = data.text.split("\n")[2:-1]
    res = {}
    for r in radky:
        r_data = r.split("|")
        res[r_data[-2]] = float(float(r_data[-1].replace(",", ".")) / float(r_data[2]))
    return res


def pocatecni_mena():
    while True:
        try:
            puvodni = input("Zadejte původní měnu velkými písmeny (příklad CZK): ")
            if puvodni != "CZK" and not puvodni in kurzy.keys():
                raise ValueError()
            break
        except ValueError:
            print(colored("Zadejte platnou měnu", "red"))
    while True:
        try:
            mnozstvi = float(input("Zadejte počet " + puvodni + ": "))
            if not mnozstvi > 0.0:
                raise ValueError()
            break
        except ValueError:
            print(colored("Zadejte platné množství", "red"))
    return {"mena": puvodni, "mnozstvi": mnozstvi}


def konecna_mena():
    while True:
        try:
            vysledna = input("Zadejte výslednou měnu velkými písmeny (příklad EUR): ")
            if vysledna != "CZK" and not vysledna in kurzy.keys():
                raise ValueError()
            return vysledna
        except ValueError:
            print(colored("Měna není v seznamu", "red"))


def spocitej():
    if vysledna == puvodni["mena"]:
        return puvodni["mnozstvi"]

    if vysledna == "CZK":
        return puvodni["mnozstvi"] * kurzy[puvodni["mena"]]
    elif puvodni["mena"] == "CZK":
        return puvodni["mnozstvi"] / kurzy[vysledna]
    else:
        return (puvodni["mnozstvi"] * kurzy[puvodni["mena"]]) / kurzy[vysledna]


print(colored("Kurzovní lístek", "yellow"))

kurzy = stahni_kurzy()
puvodni = pocatecni_mena()
vysledna = konecna_mena()
exchange = spocitej()

vetsi = "green" if exchange > puvodni["mnozstvi"] else "red"

print(
    colored(str(puvodni["mnozstvi"]) + " " + puvodni["mena"], "blue")
    + colored(" je ", "yellow")
    + colored(str(exchange) + " " + vysledna, vetsi)
)