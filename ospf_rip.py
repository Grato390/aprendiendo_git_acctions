# Diccionario que mapea el CIDR a su correspondiente máscara de subred
cidr_a_mascara = {
    8: "255.0.0.0", 9: "255.128.0.0", 10: "255.192.0.0", 11: "255.224.0.0", 
    12: "255.240.0.0", 13: "255.248.0.0", 14: "255.252.0.0", 15: "255.254.0.0", 
    16: "255.255.0.0", 17: "255.255.128.0", 18: "255.255.192.0", 19: "255.255.224.0", 
    20: "255.255.240.0", 21: "255.255.248.0", 22: "255.255.252.0", 23: "255.255.254.0", 
    24: "255.255.255.0", 25: "255.255.255.128", 26: "255.255.255.192", 27: "255.255.255.224", 
    28: "255.255.255.240", 29: "255.255.255.248", 30: "255.255.255.252", 31: "255.255.255.254", 
    32: "255.255.255.255"
}

# Función para calcular la wildcard mask a partir de la máscara de subred
def calcular_wildcard(mascara_subred):
    mascara_octetos = mascara_subred.split('.')
    wildcard_octetos = [str(255 - int(octeto)) for octeto in mascara_octetos]
    wildcard = '.'.join(wildcard_octetos)
    return wildcard

# Función para generar la configuración de OSPF
def generar_configuracion_ospf(subredes):
    configuracion = []
    configuracion.append("ena")
    configuracion.append("conf t")
    configuracion.append("router ospf 1")  # Asumiendo OSPF con área 0 por defecto

    # Agregar las subredes de la lista
    for subred in subredes:
        red, cidr = subred.split('/')
        cidr = int(cidr)
        
        # Obtener la máscara de subred basada en el CIDR
        mascara_bin = cidr_a_mascara[cidr]
        
        # Calcular la wildcard mask
        wildcard = calcular_wildcard(mascara_bin)
        
        # Agregar la red con su máscara wildcard a la configuración
        configuracion.append(f"network {red} {wildcard} area 0")

    # Retornar el bloque de configuración
    return "\n".join(configuracion)

# Función para generar la configuración de RIP
def generar_configuracion_rip(subredes):
    configuracion = []
    configuracion.append("ena")  # Activar modo privilegiado
    configuracion.append("conf t")  # Entrar en modo de configuración global
    configuracion.append("router rip")
    configuracion.append("version 2")  # Configurar RIP versión 2
    
    # Agregar las subredes de la lista
    for subred in subredes:
        red, cidr = subred.split('/')
        red = red.strip()  # Asegurarse de eliminar cualquier espacio extra
        
        # Agregar la red con RIP
        configuracion.append(f"network {red}")

    # Retornar el bloque de configuración
    return "\n".join(configuracion)

# Lista de subredes con CIDR
subredes = [
    "20.16.1.0/25", "192.168.2.0/9", "192.168.3.0/24", "192.168.4.0/24", "192.168.5.0/24"
]

# Pedir la selección del protocolo
protocolo = input("Selecciona el protocolo  (OSPF = 1 o RIP = 2): ").strip()

# Validar la entrada y generar la configuración correspondiente
if protocolo == "1":
    config = generar_configuracion_ospf(subredes)
elif protocolo == "2":
    config = generar_configuracion_rip(subredes)
else:
    config = "Protocolo no válido. Elige 'OSPF' o 'RIP'."

# Imprimir la configuración generada
print(config)
