from builtins import print
import sqlite3
# import mysql.connector as mysql
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

engine = create_engine('mysql+pymysql://dm2:dm2@localhost/olimpiadas')
conn = engine.connect()
meta = MetaData()
Deportistas = Table(
    'Deportista', meta,
    Column('id_deportista', Integer, primary_key=True),
    Column('nombre', String),
    Column('sexo', String),
    Column('peso', String),
    Column('altura', String)
)

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








        Deporte = Table(
            'Deporte', meta,
            Column('id_deporte', Integer, primary_key=True),
            Column('nombre', String)

        )



        Equipo = Table(
            'Equipo', meta,
            Column('id_equipo', Integer, primary_key=True),
            Column('nombre', String),
            Column('iniciales', String)
        )

        Evento = Table(
            'Evento', meta,
            Column('id_evento', Integer, primary_key=True),
            Column('nombre', String),
            Column('id_olimpiada', Integer),
            Column('id_deporte', Integer)
        )
        # faltan claves ajenas



        print("""En que BBDD quieres buscar: 1. MySql
                            2. SQLITE""")
        resp = int(input())
        if resp == 1:

            d = Deportistas.select()
            conn = engine.connect()
            result = conn.execute(d)
            for i in result:
                print(i)

        elif resp == 2:
            conex = sqlite3.connect("Olimpiadas.sqlite")
            cursor = conex.cursor()


        print("Dime la temporada 'W' o 'S'")
        temp = input()
        if temp == "W" or temp == "w":
            temporada = ['Winter']
        elif temp == "S" or temp == "s":
            temporada = ['Summer']
        else:
            print("Temporada incorrecta")

        if resp == 1:
            cursor.execute(querySeason + "%s", temporada)
            olimpiadas = cursor.fetchall()
            print(olimpiadas)
        elif resp == 2:
            cursor.execute(querySeason + "?", temporada)
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

            # elif (resp == 4):
                # Tema4.nuevaParticipacionDeportista()

            # elif (resp == 5):
                # Tema4.eliminarPart()




Tema4 = EjercicioTema4()
Tema4.menu()
