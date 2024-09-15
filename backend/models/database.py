from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Constantes de configuración de la conexión a SQL Server
USERNAME = "hackmty-admin"
PASSWORD = "GF62.7Cr777"
SERVER = "hackmty.database.windows.net"  # Puede ser localhost o la IP del servidor
DATABASE_NAME = "hackmty"
DRIVER = "ODBC+Driver+17+for+SQL+Server"

# Crear la URL de conexión utilizando f-string
DATABASE_URL = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE_NAME}?driver={DRIVER}"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# Configurar la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative Base para los modelos
Base = declarative_base()
