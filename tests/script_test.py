from random import random
from pathlib import Path

archivos = [
    "sdsd.txt",
    "ssdsd.img",
    "ggg.png",
    "aag.mp3",
    "aaag.mp4",
    "sdsdm.jpg",
    "cdcd.doc",
    "sdsdsd.exe",
    "sdsdsd.py",
    "sdsdsd",
    "dsds.txt",
    "sdsd.img",
    "dfgfg.png",
    "fgfn.mp3",
    "xsd.mp4",
    "cdom.jpg"
]

for archivo in archivos:
    archivo = Path(archivo)
    if not archivo.exists():
        with open(archivo, "x") as a:
            pass

