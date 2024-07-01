import enum
from datetime import datetime

from sqlalchemy import Boolean, Column, Enum, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.database import Base 

class kinship(enum.Enum):
    dad = "dad"
    mom = "mom"
    brother = "brother"
    sister = "sister"

class UniversityDegree(enum.Enum):
    DN = "DN"
    ASP = "ASP"
    QTA = "QTA"
    TICS = "TICS"

class Symptom(enum.Enum):
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

class TypeFamily(enum.Enum):
    completa = "completa"
    incompleta = "incompleta"
    funcional = "funcional"
    nuclear = "nuclear"
    extensa_funcional = "extensa_funcional"
    integrada = "integrada"
    desintegrada = "desintegrada"
    otro = "otro"


class User(Base):
    __tablename__ = "users"    
    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    name = Column(String, unique=True)
    gender = Column(String, nullable=False, unique=True)
    age = Column(Integer, unique=True)
    date_of_birth = Column(String, unique=True)
    municipality = Column(String, nullable=False, unique=True)
    address = Column(String, nullable=False, unique=True)
    phone = Column(Integer, unique=True)
    religion = Column(String, nullable=False, unique=True)
    civil_status = Column(String, unique=True)
    university_degree = Column(Enum(UniversityDegree))  #lleva clase
    registration = Column(String, unique=True)
    tutor = Column(String, unique=True)
    children = Column(Boolean, unique=True)
    assitance_psychologist = Column(String, unique=True)
    emergency_number = Column(Integer, unique=True)
    kinship = Column(Enum(kinship))            #lleva clase
    note_one = Column(String, nullable=False)
    symptom = Column(Enum(Symptom))           #lleva clase
    type_psychologist = Column(String, nullable=False, unique=True)
    type_medic = Column(String, nullable=False)
    accident = Column(String, nullable=False)
    type_family = Column(Enum(TypeFamily))        #lleva clase
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
    
