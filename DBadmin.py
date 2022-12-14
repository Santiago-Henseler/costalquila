# imports
import sqlite3
import numpy as np


# config
connection = sqlite3.connect("Database/data", check_same_thread=False)
cursor = connection.cursor()


def getAllLoc():
    allLocs = cursor.execute("SELECT Localidad FROM Propiedades;").fetchall()
    locs = np.unique(allLocs)
    return locs


def getHome():
    home = cursor.execute("SELECT * FROM Propiedades ORDER BY RANDOM();").fetchall()
    return home


def getOneHome(id):
    home = cursor.execute(f"SELECT * FROM Propiedades WHERE ID = '{id}';").fetchone()
    return home


def getHomeCustom(id):
    home = cursor.execute(f"SELECT * FROM Propiedades WHERE ID = '{id}';").fetchall()
    return home


def getSearchHome(l, v, c):
    v1 = int(v)
    v2 = v1 + 20
    c1 = int(c)
    c2 = c1 + 2
    if v1 == 120:
        if c2 == 8:
            home = cursor.execute(f"""SELECT * FROM Propiedades WHERE Localidad = '{l}'
                                     AND Valores >= '{v1}'
                                     AND Npersonas >= '{c1}' ;""").fetchall()
        else:
            home = cursor.execute(f"""SELECT * FROM Propiedades WHERE Localidad = '{l}'
                                              AND Valores >= '{v1}'
                                              AND Npersonas between '{c1}' AND '{c2}';""").fetchall()
    else:
        if c2 == 8:
            home = cursor.execute(f"""SELECT * FROM Propiedades WHERE Localidad = '{l}'
                                     AND Valores >= '{v1}'
                                     AND Npersonas >= '{c1}' ;""").fetchall()
        else:
            home = cursor.execute(f"""SELECT * FROM Propiedades WHERE Localidad = '{l}'
                                              AND Valores >= '{v1}'
                                              AND Npersonas between '{c1}' AND '{c2}';""").fetchall()

    return home


def getComodidades(id):
    comodidades = cursor.execute(f"SELECT * FROM Comodidades WHERE ID = '{id}';").fetchone()
    return comodidades


def getHomeComodidades(id, Dmar, mascota, parrilla, cochera):
    c1 = int(Dmar)
    c2 = int(Dmar)+100
    comodidades = ""
    if c1 == 500:
        comodidades = cursor.execute(f"""SELECT * FROM Comodidades WHERE ID = '{id}'
                                                 AND Dmar >= '{c2}'
                                                 AND Mascotas = '{mascota}'
                                                 AND parrilla = '{parrilla}'
                                                 AND Cochera = '{cochera}'
                                             ;""").fetchall()
    else:
        comodidades = cursor.execute(f"""SELECT * FROM Comodidades WHERE ID = '{id}'
                                         AND Dmar between '{c1}' AND '{c2}'
                                         AND Mascotas = '{mascota}'
                                         AND parrilla = '{parrilla}'
                                         AND Cochera = '{cochera}'
                                     ;""").fetchall()

    print(comodidades)
    return comodidades
