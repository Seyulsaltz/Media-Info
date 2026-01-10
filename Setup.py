import json
import shutil
import os
import sys

# Carpeta REAL del .exe (no TEMP de PyInstaller)
SCRIPT_DIR = os.path.dirname(sys.executable)

JSON_PATH = os.path.join(SCRIPT_DIR, "project.json")
BACKUP_PATH = JSON_PATH + ".bak"

NEW_PROPERTIES = {
    "emptyspace0": {
        "condition": "mediainfobyseyul.value == true",
        "index": 0,
        "order": 400,
        "text": "",
        "type": "text",
        "value": False
    },
    "emptyspace00": {
        "condition": "mediainfobyseyul.value == true",
        "index": 21,
        "order": 421,
        "text": "",
        "type": "text",
        "value": False
    },
    "emptyspace1": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyuladditions.value == 2",
        "index": 5,
        "order": 405,
        "text": "",
        "type": "text",
        "value": False
    },
    "emptyspace10": {
        "condition": "mediainfobyseyul.value == true",
        "index": 46,
        "order": 446,
        "text": "",
        "type": "text",
        "value": False
    },
    "emptyspace2": {
        "condition": "mediainfobyseyul.value == true",
        "index": 15,
        "order": 415,
        "text": "",
        "type": "text",
        "value": False
    },
    "emptyspace3": {
        "condition": "mediainfobyseyul.value == true",
        "index": 13,
        "order": 413,
        "text": "",
        "type": "text",
        "value": False
    },
    "emptyspace4": {
        "condition": "mediainfobyseyul.value == true",
        "index": 23,
        "order": 423,
        "text": "",
        "type": "text",
        "value": False
    },
    "emptyspace5": {
        "condition": "mediainfobyseyul.value == true",
        "index": 29,
        "order": 429,
        "text": "",
        "type": "text",
        "value": False
    },
    "emptyspace6": {
        "condition": "mediainfobyseyul.value == true",
        "index": 34,
        "order": 434,
        "text": "",
        "type": "text",
        "value": False
    },
    "emptyspace7": {
        "condition": "mediainfobyseyul.value == true",
        "index": 38,
        "order": 438,
        "text": "",
        "type": "text",
        "value": False
    },
    "emptyspace8": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyuladditions.value == 4",
        "index": 8,
        "order": 408,
        "text": "",
        "type": "text",
        "value": False
    },
    "mediainfobyseyul": {
        "index": 1,
        "order": 401,
        "text": "<b>🎵 Media Info. By Seyul</b>",
        "type": "bool",
        "value": False
    },
    "mediainfobyseyuladditions": {
        "condition": "mediainfobyseyul.value == true",
        "index": 4,
        "options": [
            {"label": "Bar", "value": "1"},
            {"label": "Bars", "value": "2"},
            {"label": "Progress Bar", "value": "3"},
            {"label": "Buttons", "value": "4"},
            {"label": "Spectrum", "value": "5"},
            {"label": "None", "value": "6"}
        ],
        "order": 404,
        "text": "‎ <b><small>🔸Additions</small></b>",
        "type": "combo",
        "value": "5"
    },
    "mediainfobyseyulalpha": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyulnoise.value == true",
        "fraction": True,
        "index": 28,
        "max": 1,
        "min": 0,
        "order": 428,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤㅤ<small>└ Alpha</small>",
        "type": "slider",
        "value": 0.6
    },
    "mediainfobyseyulamountofblur": {
        "condition": "mediainfobyseyul.value == true",
        "fraction": True,
        "index": 24,
        "max": 2,
        "min": 0,
        "order": 424,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤ<small>🔹Amount of Blur</small>",
        "type": "slider",
        "value": 0.5
    },
    "mediainfobyseyulaudioresponseagitation": {
        "condition": "mediainfobyseyul.value == true",
        "index": 31,
        "order": 431,
        "text": "ㅤ<small>🔹Audio Response Agitation</small>",
        "type": "bool",
        "value": True
    },
    "mediainfobyseyulbarscount": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyuladditions.value == 2",
        "fraction": True,
        "index": 6,
        "max": 50,
        "min": 5,
        "order": 406,
        "precision": 1,
        "step": 1,
        "text": "ㅤ<small>🔹Bar Count</small>",
        "type": "slider",
        "value": 40
    },
    "mediainfobyseyulbarspacing": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyuladditions.value == 2",
        "fraction": True,
        "index": 7,
        "max": 1,
        "min": 0,
        "order": 407,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤ<small>🔹Bar Spacing</small>",
        "type": "slider",
        "value": 0.5
    },
    "mediainfobyseyulbordercolor": {
        "condition": "mediainfobyseyul.value == true",
        "index": 36,
        "order": 436,
        "text": "ㅤ<small>🔹Edge</small>",
        "type": "color",
        "value": "0 0 0"
    },
    "mediainfobyseyulbordersize": {
        "condition": "mediainfobyseyul.value == true",
        "fraction": True,
        "index": 37,
        "max": 0.6,
        "min": 0.001,
        "order": 437,
        "precision": 4,
        "step": 0.001,
        "text": "ㅤ<small>🔹Thickness</small>",
        "type": "slider",
        "value": 0.1
    },
    "mediainfobyseyulchromaticaberration": {
        "condition": "mediainfobyseyul.value == true",
        "index": 41,
        "order": 441,
        "text": "ㅤ<small>🔹Chromatic Aberration (Album Cover)</small>",
        "type": "bool",
        "value": True
    },
    "mediainfobyseyulchromaticaberrationrectangle": {
        "condition": "mediainfobyseyul.value == true",
        "index": 39,
        "order": 439,
        "text": "ㅤ<small>🔹Chromatic Aberration (Rectangle)",
        "type": "bool",
        "value": True
    },
    "mediainfobyseyulcolorofadditions": {
        "condition": "mediainfobyseyul.value == true",
        "index": 22,
        "order": 422,
        "text": "ㅤ<small>🔹Additions</small>",
        "type": "color",
        "value": "1 1 1"
    },
    "mediainfobyseyuldarkness": {
        "condition": "mediainfobyseyul.value == true",
        "fraction": True,
        "index": 25,
        "max": 1,
        "min": 0,
        "order": 425,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤ<small>🔹Darkness</small>",
        "type": "slider",
        "value": 0.35
    },
    "mediainfobyseyuldraganddrop": {
        "condition": "mediainfobyseyul.value == true",
        "index": 14,
        "order": 414,
        "text": "ㅤ<small>🔹Drag and Drop</small>",
        "type": "bool",
        "value": True
    },
    "mediainfobyseyulemptyspace000": {
        "condition": "mediainfobyseyul.value == true",
        "index": 43,
        "order": 443,
        "text": "",
        "type": "text",
        "value": False
    },
    "mediainfobyseyulenablezoom": {
        "condition": "mediainfobyseyul.value == true",
        "index": 30,
        "order": 430,
        "text": "ㅤ<small>🔹Enable Zoom</small>",
        "type": "bool",
        "value": True
    },
    "mediainfobyseyulfont": {
        "condition": "mediainfobyseyul.value == true",
        "index": 16,
        "options": [
            {"label": "Akira", "value": "1"},
            {"label": "Alte Haas Grotesk", "value": "2"},
            {"label": "Arcade", "value": "3"},
            {"label": "Bronson", "value": "4"},
            {"label": "Built Titling BD", "value": "5"},
            {"label": "Coolvetica", "value": "6"},
            {"label": "Decima Mono Cyr", "value": "7"},
            {"label": "Fake Pearl", "value": "8"},
            {"label": "Gobold", "value": "9"},
            {"label": "Heavitas", "value": "10"},
            {"label": "Kenyan Coffee", "value": "11"},
            {"label": "Moderniz", "value": "12"},
            {"label": "Montserrat", "value": "13"},
            {"label": "Nasalization", "value": "14"},
            {"label": "Nature", "value": "15"},
            {"label": "Rezerv", "value": "16"},
            {"label": "Robloxian", "value": "17"},
            {"label": "Roboto", "value": "18"},
            {"label": "Superbastone", "value": "19"},
            {"label": "Sylfaen", "value": "20"},
            {"label": "Tommy", "value": "21"},
            {"label": "Vin Mono Pro", "value": "22"},
            {"label": "Whitrabt", "value": "23"},
        ],
        "order": 416,
        "text": "ㅤ<small>🔹Font Type</small>",
        "type": "combo",
        "value": "14"
    },
    "mediainfobyseyulfontcolor": {
        "condition": "mediainfobyseyul.value == true",
        "index": 17,
        "order": 417,
        "text": "ㅤ<small>🔹Font Color</small>",
        "type": "color",
        "value": "1 1 1"
    },
    "mediainfobyseyulforce": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyulchromaticaberrationrectangle.value == true",
        "fraction": True,
        "index": 40,
        "max": 2,
        "min": 0,
        "order": 440,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤㅤ<small>└ Force</small>",
        "type": "slider",
        "value": 1
    },
    "mediainfobyseyulforcealbum": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyulchromaticaberration.value == true",
        "fraction": True,
        "index": 42,
        "max": 2,
        "min": 0,
        "order": 442,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤㅤ<small>└ Force</small>",
        "type": "slider",
        "value": 1
    },
    "mediainfobyseyulguideandlisofcommands": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyuladditions.value == 4",
        "index": 9,
        "order": 409,
        "text": "<b><center><a href='https://steamcommunity.com/sharedfiles/filedetails/?id=3627191896'>Guide And List Of Commands For Media Info Buttons</a></center></b>",
        "type": "text",
        "value": False
    },
    "mediainfobyseyulmaxvalue": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyulaudioresponseagitation.value == true",
        "fraction": True,
        "index": 33,
        "max": 5,
        "min": 0,
        "order": 433,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤㅤ<small>└ Max. Value</small>",
        "type": "slider",
        "value": 0.75
    },
    "mediainfobyseyulminvalue": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyulaudioresponseagitation.value == true",
        "fraction": True,
        "index": 32,
        "max": 4.5,
        "min": 0,
        "order": 432,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤㅤ<small>├ Min. Value</small>",
        "type": "slider",
        "value": 0.7
    },
    "mediainfobyseyulnoise": {
        "condition": "mediainfobyseyul.value == true",
        "index": 26,
        "order": 426,
        "text": "ㅤ<small>🔹Noise</small>",
        "type": "bool",
        "value": True
    },
    "mediainfobyseyulnoisescale": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyulnoise.value == true",
        "fraction": True,
        "index": 27,
        "max": 300,
        "min": 0.01,
        "order": 427,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤㅤ<small>├ Scale</small>",
        "type": "slider",
        "value": 200
    },
    "mediainfobyseyulplasticalbumcover": {
        "condition": "mediainfobyseyul.value == true",
        "index": 44,
        "order": 444,
        "text": "ㅤ<small>🔹Plastic Album Cover</small>",
        "type": "bool",
        "value": True
    },
    "mediainfobyseyulpointsizealbumtitle": {
        "condition": "mediainfobyseyul.value == true",
        "fraction": True,
        "index": 19,
        "max": 15,
        "min": 0,
        "order": 419,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤㅤ<small>├ Size (Album)</small>",
        "type": "slider",
        "value": 6
    },
    "mediainfobyseyulpointsizeartistname": {
        "condition": "mediainfobyseyul.value == true",
        "fraction": True,
        "index": 20,
        "max": 15,
        "min": 0,
        "order": 420,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤㅤ<small>└ Size (Artist)</small>",
        "type": "slider",
        "value": 5
    },
    "mediainfobyseyulpointsizetitlesong": {
        "condition": "mediainfobyseyul.value == true",
        "fraction": True,
        "index": 18,
        "max": 15,
        "min": 0,
        "order": 418,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤㅤ<small>├ Size (Song)</small>",
        "type": "slider",
        "value": 8
    },
    "mediainfobyseyulroundedcorner": {
        "condition": "mediainfobyseyul.value == true",
        "fraction": True,
        "index": 35,
        "max": 5,
        "min": 0,
        "order": 435,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤ<small>🔹Rounded Corner</small>",
        "type": "slider",
        "value": 0
    },
    "mediainfobyseyulsize": {
        "condition": "mediainfobyseyul.value == true",
        "fraction": True,
        "index": 45,
        "max": 4.5,
        "min": 0,
        "order": 445,
        "precision": 3,
        "step": 0.01,
        "text": "ㅤ<small>🔹Size</small>",
        "type": "slider",
        "value": 0.7
    },
    "mediainfobyseyultypemedia": {
        "condition": "mediainfobyseyul.value == true",
        "index": 2,
        "options": [
            {"label": "Left", "value": "1"},
            {"label": "Rigth", "value": "2"},
            {"label": "Centered", "value": "3"},
            {"label": "None", "value": "4"}
        ],
        "order": 402,
        "text": "‎ <b><small>🔸Type Media</small></b>",
        "type": "combo",
        "value": "1"
    },
    "mediainfobyseyultyperectangle": {
        "condition": "mediainfobyseyul.value == true",
        "index": 3,
        "options": [
            {"label": "Default", "value": "1"},
            {"label": "Album Cover", "value": "2"}
        ],
        "order": 403,
        "text": "‎ <b><small>🔸Type Rentangle</small></b>",
        "type": "combo",
        "value": "2"
    },
    "newproperty12": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyuladditions.value == 4",
        "index": 10,
        "order": 410,
        "text": "ㅤ<small>🔹P./Pause</small>",
        "type": "usershortcut",
        "value": ""
    },
    "newproperty13": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyuladditions.value == 4",
        "index": 11,
        "order": 411,
        "text": "ㅤ<small>🔹Previous</small>",
        "type": "usershortcut",
        "value": ""
    },
    "newproperty14": {
        "condition": "mediainfobyseyul.value == true && mediainfobyseyuladditions.value == 4",
        "index": 12,
        "order": 412,
        "text": "ㅤ<small>🔹Next</small>",
        "type": "usershortcut",
        "value": ""
    }
}


def main():
    print("Iniciando...")

    if not os.path.exists(JSON_PATH):
        input("❌ project.json NO encontrado\nEnter para salir")
        return

    if not os.path.exists(BACKUP_PATH):
        shutil.copy2(JSON_PATH, BACKUP_PATH)
        print("✔ Backup creado")
    else:
        print("ℹ Backup ya existe")

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    data.setdefault("general", {})
    data["general"].setdefault("properties", {})

    props = data["general"]["properties"]
    added = 0

    for key, value in NEW_PROPERTIES.items():
        if key not in props:
            props[key] = value
            added += 1

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    input(f"✔ Terminado\nPropiedades añadidas: {added}\n\nEnter para salir")

if __name__ == "__main__":
    main()
