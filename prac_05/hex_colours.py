
COLOR_TO_HEX = {
    "acidgreen": "#b0bf1a",
    "grey": "#bebebe",
    "aqua": "#00ffff",
    "bananayellow": "#ffe135",
    "ginger": "#b06500",
    "beige": "#f5f5dc",
    "chocolate": "#d2691e",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "darkorange": "#ff8c00"
}

color_name = input("Enter color name: ").lower()
while color_name != "":
    try:
        print(f"{color_name.capitalize()} hex code is {COLOR_TO_HEX[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").lower()