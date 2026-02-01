import datetime
import ctypes

# 1. Definimos la fecha de tu matrimonio
fecha_boda = datetime.date(2026, 3, 26) 

# 2. Obtenemos la fecha de hoy
hoy = datetime.date.today()

# 3. Calculamos la diferencia de días
diferencia = fecha_boda - hoy
dias_faltantes = diferencia.days

# 4. Creamos el texto del mensaje
titulo = "Cuenta Regresiva para el Gran Día"
mensaje = f"¡Hola! Quedan {dias_faltantes} días para el 26 de marzo.\n\n¡Amanda y Alfredo!"

# 5. Función de Windows para mostrar la ventana
if dias_faltantes >= 0:
    ctypes.windll.user32.MessageBoxW(0, mensaje, titulo, 0x40)