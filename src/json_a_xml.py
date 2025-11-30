import json
import xml.etree.ElementTree as ET


def leer_json(ruta_json: str) -> dict:
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def convertir_a_xml(datos: dict) -> ET.Element:
    root = ET.Element("usuarios")

    for usuario in datos.get("usuarios", []):
        usuario_elemento = ET.SubElement(root, "usuario")

        id_elemento = ET.SubElement(usuario_elemento, "id")
        id_elemento.text = str(usuario.get("id", ""))

        nombre_elemento = ET.SubElement(usuario_elemento, "nombre")
        nombre_elemento.text = usuario.get("nombre", "")

        edad_elemento = ET.SubElement(usuario_elemento, "edad")
        edad_elemento.text = str(usuario.get("edad", ""))

    return root


def guardar_xml(root: ET.Element, ruta_xml: str):
    arbol = ET.ElementTree(root)
    arbol.write(ruta_xml, encoding="utf-8", xml_declaration=True)


def main():
    ruta_json = "json.json"
    ruta_xml = "json.xml"

    # Leer
    datos = leer_json(ruta_json)

    # Convertir
    root_xml = convertir_a_xml(datos)

    # Guardar
    guardar_xml(root_xml, ruta_xml)




if __name__ == "__main__":
    main()
