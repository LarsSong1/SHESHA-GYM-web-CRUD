import sqlite3 as sql
"""
Base de datos
"""

d_b = "registro.db"
coneccion = sql.connect(d_b)
cursor = coneccion.cursor()
coneccion.commit()
coneccion.close()