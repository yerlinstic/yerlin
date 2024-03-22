import storage.oficina as of
# Devuelve un listado con el código de 
# oficina y la ciudad donde hay oficinas.

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "código": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

# Devuelve un listado con la ciudad y el teléfono 
# de las oficinas de España.

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get("pais") == pais):
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "teléfono": val.get("telefono"),
                "oficinas": val.get("codigo_oficina"),
                "pais": val.get("pais")
            })
    return ciudadTelefono