import uuid

# Obtenemos la dirección MAC en formato hexadecimal
mac_num = hex(uuid.getnode())

# La limpiamos un poco para que se vea como la de ipconfig
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                         for ele in range(0, 8*6, 8)][::-1])

print(f"Tu dirección MAC es: {mac_address.upper()}")

# Vamos a ver el primer octeto para saber si es Unicast
primer_octeto_hex = mac_address.split(':')[0]
primer_octeto_bin = bin(int(primer_octeto_hex, 16))[2:].zfill(8)

print(f"Primer octeto en Hex: {primer_octeto_hex}")
print(f"Primer octeto en Binario: {primer_octeto_bin}")

if primer_octeto_bin[-1] == '0':
    print("Resultado: Es una dirección UNICAST (lo normal)")
else:
    print("Resultado: Es una dirección MULTICAST")