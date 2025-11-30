import json
import xml.etree.ElementTree as ET


def leer_xml(ruta_xml: str) -> ET.Element:
    tree = ET.parse(ruta_xml)
    return tree.getroot()


def convertir_a_dicccionario(root: ET.Element) -> dict:
    datos = {"usuarios": []}

    for usuario in root.findall("usuario"):
        usuario_diccionario = {
            "id": int(usuario.findtext("id", default="0")),
            "nombre": usuario.findtext("nombre", default=""),
            "edad": int(usuario.findtext("edad", default="0"))
        }
        datos["usuarios"].append(usuario_diccionario)

    return datos


def guardar_json(datos: dict, ruta_json: str) -> None:
    with open(ruta_json, "w") as archivo:
        json.dump(datos, archivo, indent=4)


def main():
    ruta_xml = "xml.xml"
    ruta_json = "xml.json"

    # Leer XML
    root = leer_xml(ruta_xml)

    # Convertir
    datos = convertir_a_dicccionario(root)

    # Guardar
    guardar_json(datos, ruta_json)



if __name__ == "__main__":
    main()
