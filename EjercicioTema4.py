from builtins import print
import sqlite3
import pymysql
from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://dm2:dm2@localhost/olimpiadas',echo = True)


class Deportista(Base):
   __tablename__ = 'Deportista'

   id_deportista = Column(Integer, primary_key=True)
   nombre = Column(String)
   sexo = Column(String)
   peso = Column(Integer)
   altura = Column(Integer)


class Olimpiada(Base):
   __tablename__ = 'Olimpiada'

   id_olimpiada = Column(Integer, primary_key=True)
   nombre = Column(String)
   anio = Column(String)
   temporada = Column(String)
   ciudad = Column(String)


class Deporte(Base):
   __tablename__ = 'Deporte'

   id_deporte = Column(Integer, primary_key = True)
   nombre = Column(String)


class Equipo(Base):
   __tablename__ = 'Equipo'

   id_equipo = Column(Integer, primary_key = True)
   nombre = Column(String)
   iniciales = Column(String)


class Evento(Base):
   __tablename__ = 'Evento'

   id_evento = Column(Integer, primary_key = True)
   nombre = Column(String)
   id_olimpiada = Column(Integer, ForeignKey('Olimpiada.id_olimpiada'))
   id_deporte = Column(Integer, ForeignKey('Deporte.id_deporte'))
   olimpiada = relationship("Olimpiada", back_populates="eventos")
   deporte = relationship("Deporte", back_populates="eventos")


Olimpiada.eventos = relationship("Evento", order_by = Olimpiada.id_olimpiada, back_populates = "olimpiada")
Deporte.eventos = relationship("Evento", order_by = Deporte.id_deporte, back_populates = "deporte")


class Participacion(Base):
   __tablename__ = 'Participacion'
   id_deportista = Column(Integer, ForeignKey('Deportista.id_deportista'), primary_key=True)
   id_evento = Column(Integer, ForeignKey('Evento.id_evento'), primary_key=True)
   id_equipo = Column(Integer, ForeignKey('Equipo.id_equipo'))
   edad = Column(Integer)
   medalla = Column(String)
   deportista = relationship("Deportista", back_populates="participaciones")
   evento = relationship("Evento", back_populates="participaciones")
   equipo = relationship("Equipo", back_populates="participaciones")


Deportista.participaciones = relationship("Participacion", order_by=Deportista.id_deportista, back_populates="deportista")
Evento.participaciones = relationship("Participacion", order_by=Evento.id_evento, back_populates="evento")
Equipo.participaciones = relationship("Participacion", order_by=Equipo.id_equipo, back_populates="equipo")


class EjercicioTema4:

    @staticmethod
    def listadoDeport():
        """Metodo que lista los deportistas que hayan participado en diferentes deportes"""


        querySeason = """SELECT id_olimpiada, nombre FROM Olimpiada WHERE temporada="""

        querySport = """SELECT id_deporte, nombre FROM Deporte WHERE EXISTS( \
                        SELECT * FROM Evento WHERE `Evento`.`id_deporte` = `Deporte`.`id_deporte`  \
                        AND	`Evento`.`id_olimpiada`="""

        queryEvent = """SELECT id_evento, nombre FROM Evento WHERE `id_olimpiada`= """

        queryDeportis = """SELECT nombre, sexo, altura, peso FROM Deportista WHERE EXISTS( \
                        SELECT * FROM Participacion WHERE `Deportista`.`id_deportista` = `Participacion`.`id_deportista` \
                        AND `Participacion`.`id_evento`= """







        print("""En que BBDD quieres buscar: 1. MySql
                            2. SQLITE""")
        resp = int(input())
        if resp == 1:

            Session = sessionmaker(bind=engine)
            session = Session()


        elif resp == 2:
            conex = sqlite3.connect("Olimpiadas.sqlite")
            cursor = conex.cursor()


        print("Dime la temporada 'W' o 'S'")
        temp = input()
        if temp == "W" or temp == "w":
            tempo = 'Winter'
        elif temp == "S" or temp == "s":
            tempo = 'Summer'
        else:
            print("Temporada incorrecta")

        if resp == 1:

            result = session.query(Olimpiada).filter(Olimpiada.temporada == tempo)
            for row in result:
                    print(row)   #devuelve objetos

        elif resp == 2:
            cursor.execute(querySeason + "?", tempo)
            olimpiadas = cursor.fetchall()
            print(olimpiadas)

        print("Seleciona la edicion olimpica")
        edicion = input()

        if resp == 1:
            cursor.execute(querySport + "%s)", [edicion])
            deportes = cursor.fetchall()
            print(deportes)

        elif resp == 2:
            cursor.execute(querySport + "?)", [edicion])
            deportes = cursor.fetchall()
            print(deportes)

        print("Seleciona el deporte")
        deporte = input()

        # if resp == 1:


        # elif resp == 2:



        print("Seleciona el evento")
        evento = [input()]

        if resp == 1:



            for i in Deportistas:
                print(i)

        elif resp == 2:
            cursor.execute(queryDeportis + "?)", evento)


            for i in Deportistas:
                print(i)




    @staticmethod
    def menu():
        """Metodo para la ejecucion del menu del programa"""
        resp = 9
        while (resp != 0):
            print("""
   1. Listado de deportistas en diferentes deportes
   2. Listado de deportistas participantes
   3. Modificar medalla deportista
   4. Añadir deportista/participación
   5. Eliminar participación

   0. Salir""")

            resp = int(input())
            Tema4 = EjercicioTema4()
            if (resp == 1):
                Tema4.listadoDeport()

            elif (resp == 2):
                Tema4.listadoDeport2()

            elif (resp == 3):
                Tema4.modifiMeda()

            elif (resp == 4):
                Tema4.nuevaParticipacionDeportista()

            elif (resp == 5):
                Tema4.eliminarPart()




Tema4 = EjercicioTema4()
Tema4.menu()
