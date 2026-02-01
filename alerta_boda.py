import datetime
import ctypes

# Configuración de la fecha
fecha_boda = datetime.date(2026, 3, 26) 
hoy = datetime.date.today()
dias_faltantes = (fecha_boda - hoy).days

# Configuración del mensaje
titulo = "Cuenta Regresiva para la Boda"
mensaje = f"¡Hola! Quedan {dias_faltantes} días para el 26 de marzo.\n\n Amanda y Alfredo"

# Mostrar alerta en Windows
if dias_faltantes >= 0:
    ctypes.windll.user32.MessageBoxW(0, mensaje, titulo, 0x40)