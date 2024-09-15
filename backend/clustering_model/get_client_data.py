from sqlalchemy import create_engine
import pandas as pd

# Conexión a la base de datos
DATABASE_URL = "mssql+pyodbc://username:password@server/database_name?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(DATABASE_URL)

# Consulta para obtener los datos de cliente
query = """
SELECT cliente.id_cliente, cliente.edad, cliente.sexo, visita.fecha, producto.nombre_producto 
FROM cliente 
LEFT JOIN visita ON cliente.id_cliente = visita.id_cliente 
LEFT JOIN producto ON visita.id_visita = producto.id_producto;
"""

# Cargar datos en un DataFrame
df = pd.read_sql(query, engine)

# Preprocesamiento básico (convertir sexo y producto en números, y manejar valores nulos)
df['sexo'] = df['sexo'].map({0: 'mujer', 1: 'hombre'})
df.fillna(0, inplace=True)
