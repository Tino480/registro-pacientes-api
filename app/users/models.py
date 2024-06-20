from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from datetime import datetime

import enum
from sqlalchemy import Integer, Enum

class kinship(enum.Enum):
    dad = "dad"
    mom = "mom"
    brother = "brother"
    sister = "sister"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    kinship = Column(Enum(kinship))

class university_degree(enum.Enum):
    DN = "DN"
    ASP = "ASP"
    QTA = "QTA"
    TICS = "TICS"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    university_degree = Column(Enum(university_degree))

class symptom(enum.Enum):
    agresividad = "agresividad"
    alcoholismo = "alcoholismo"
    alucinaciones = "alucinaciones"
    ansiedad = "ansiedad"
    falta_de_concentracion = "falta_de_concentracion"
    auto_agresion = "auto_agresion"
    bajo_autoestima = "bajo_autoestima"
    bajo_redimiento_escolar = "bajo_redimiento_escolar"
    cefaleas = "cefaleas"
    chupeteo_de_dedo = "chupeteo_de_dedo"
    convulciones = "convulciones"
    desmayos = "desmayos"
    enuresis = "enuresis"
    encopresis = "encopresis"
    farmaco_dependiente = "farmaco_dependiente"
    fobias = "fobias"
    hiperactividad = "hiperactividad"
    intentos_de_suicidio = "intentos_de_suicidio"
    ideas_de_muerte = "ideas_de_muerte"
    impulsividad = "impulsividad"
    insomio = "insomio"
    intolerante = "intolerante"
    llano_execivo = "llano_execivo"
    maltrato_fisico = "maltrato_fisico"
    maltrato_sexual = "maltrato_sexual"
    mareos = "mareos"
    obesidad = "obesidad"
    obsesiones = "obsesiones"
    onicofagia = "onicofagia"
    pesadillas = "pesadillas"
    problemas_de_alimentacion = "problemas_de_alimentacion"
    problemas_visuales = "problemas_visuales"
    sonambulismo = "sonambulismo"
    tartamudez = "tartamudez"
    tics = "tics"
    timidez = "timidez"
    transtorno_de_aprendizaje = "transtorno_de_aprendizaje"
    transtorno_auditivo = "transtorno_auditivo"
    capacidad_de_insigth = "capacidad_de_insigth"

class user(base):
    __tablename__ = "users"
    id = Column (Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    symptom = Column(Enum(symptom))

class type_family(enum.Enum):
    completa = "completa"
    incompleta = "incompleta"
    funcional = "funcional"
    nuclear = "nuclear"
    extensa_funcional = "extensa_funcional"
    integrada = "integrada"
    desintegrada = "desintegrada"
    otro = "otro"
class user(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    type_family = Column(Enum(type_family))
        


    name = Column(String, unique=True)
    gender = Column(String, nullable=False, unique=True)
    age = Column(int, unique=True)
    date_of_birth = Column(String, unique=True)
    municipality = Column(String, nullable=False, unique=True)
    address = Column(String, nullable=False, unique=True)
    phone = Column(int, unique=True)
    religion = Column(String, nullable=False, unique=True)
    civil_status = Column(String, unique=True)
    university_degree = Column(String, nullable=False)   #lleva clase
    registration = Column(String, unique=True)
    tutor = Column(String, unique=True)
    children = Column(bool, unique=True)
    assitance_psychologist = Column(String, unique=True)
    emergency_number = Column(int, unique=True)
    kinchip = Column(String, nullable=False)             #lleva clase
    note_one = Column(String, nullable=False)
    symptom = Column(String, nullable=False)             #lleva clase
    type_psychologist = Column(String, nullable=False, unique=True)
    type_medic = Column(String, nullable=False)
    accident = Column(String, nullable=False)
    type_family = Column(String, nullable=False)        #lleva clase
    diagnostic_print = Column(String, nullable=False)
    note_two = Column(String, nullable=False)



    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("now()"),
        nullable=False,
        onupdate=datetime.now,
    )
    
