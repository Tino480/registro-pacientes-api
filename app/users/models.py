import enum
from datetime import datetime

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
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

    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer)
    date_of_birth = Column(String)
    municipality = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(Integer)
    religion = Column(String, nullable=False)
    civil_status = Column(String)
    university_degree = Column(Enum(UniversityDegree))  # lleva clase
    registration = Column(String)
    tutor = Column(String)
    emergency_number = Column(Integer)
    kinship = Column(Enum(kinship))

    diagnostic_print = Column(String, nullable=False)

    consultations = relationship("Consultation", back_populates="user")

    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("now()"),
        nullable=False,
        onupdate=datetime.now,
    )


class Consultation(Base):
    __tablename__ = "consultations"
    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="consultations")
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
    update_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("now()"),
        nullable=False,
        onupdate=datetime.now,
    )
    note_two = Column(String, nullable=False)
    note_one = Column(String, nullable=False)
    type_family = Column(Enum(TypeFamily))
    children = Column(Boolean)
    type_medic = Column(String, nullable=False)
    accident = Column(String, nullable=False)
    symptom = Column(Enum(Symptom))
    assitance_psychologist = Column(String)
    type_psychologist = Column(String, nullable=False)
