from datetime import datetime
fechas = ["2025-10-20", "2026-10-15", "2024-10-25"]

fechas_convertidas = []
for f in fechas:
    fecha = datetime.strptime(f, "%Y-%m-%d")
    fechas_convertidas.append(fecha)
    
print(type(fechas_convertidas[0]))
fechas_convertidas.sort()
print(fechas_convertidas)
#print(type(fechas[0]))



print("*****")
fechas = ["2025-10-20", "2026-10-15", "2024-10-25"]
fechas.sort()
print(fechas)

