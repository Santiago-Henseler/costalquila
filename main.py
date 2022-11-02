# imports
from flask import Flask, render_template, request, session, redirect, url_for, flash, copy_current_request_context
from flask_wtf.csrf import CSRFProtect
from DBadmin import *
import math


# server config
app = Flask(__name__)
app.secret_key = "secret"
csrf = CSRFProtect(app)


# manejo de errores
@app.errorhandler(404)
def pageNotFound(e):
    return redirect(url_for('inicio', id=1))


#ruta inicial , SomeHose=
@app.route("/")
def init():
    return redirect(url_for('inicio', id=1))

@app.route("/inicio/<int:id>", methods=['GET', 'POST'])
def inicio(id):
    n = math.ceil(len(getHome()) / 15)
    homes = []
    if id == 1:
        homes.append(getHome()[0:15])
    elif id in range(1, n + 1) and id != 1:
        homes.append(getHome()[15 * (id - 1):15 * id])

    return render_template("index.html", Alloc=getAllLoc(), home=homes[0], n=n, id=id)


#explicacion como publicar
@app.route("/ComoPublicar")
def ComoPublicar():
    return render_template("ComoPublicar.html")


#publicar
@app.route("/Publicar")
def Publicar():
    return render_template("Publicar.html")


#ver casas
@app.route("/Alquileres/<int:id>", methods=['GET', 'POST'])
def Alquileres(id):
    fotos = getOneHome(id)[11].split(sep=',')
    comodidades = getComodidades(id)
    return render_template("propiedad.html", home=getOneHome(id), fotos=fotos, comodidades=comodidades)


@app.route("/Buscar/<int:id>", methods=['GET', 'POST'])
def Buscar(id):
    Localidad = request.form['Localidad']
    valor = request.form['valor']
    Cpersonas = request.form['Cpersonas']
    getSearchHome(Localidad, valor, Cpersonas)
    n = math.ceil(len(getSearchHome(Localidad, valor, Cpersonas)) / 15)
    homes = []
    if id == 1:
        homes.append(getSearchHome(Localidad, valor, Cpersonas)[0:15])
    elif id in range(1, n + 1) and id != 1:
        homes.append(getSearchHome(Localidad, valor, Cpersonas)[15 * (id - 1):15 * id])
    return render_template("Busqueda.html", home=homes[0], n=n, id=id,
                           nhome=bool(homes[0]), loc=Localidad, val=valor, cp=Cpersonas, Alloc=getAllLoc())


@app.route("/Buscar/filtro/<int:id>", methods=['POST'])
def filtro(id):
    Dmar = request.form['dmar']
    mascota = request.form['mascotas']
    parrilla = request.form['parrilla']
    val = request.form['val']
    cp = request.form['cp']
    loc = request.form['loc']
    n = math.ceil(len(getSearchHome(loc, val, cp)) / 15)
    homes = []
    if id == 1:
        homes.append(getSearchHome(loc, val, cp)[0:15])
    elif id in range(1, n + 1) and id != 1:
        homes.append(getSearchHome(loc, val, cp)[15 * (id - 1):15 * id])

    comHome = []
    for i in homes[0]:
        if bool(getHomeComodidades(i[0], Dmar, mascota, parrilla)):
            comHome.append(getHomeCustom(i[0]))

    if bool(comHome):
        return render_template("Busqueda.html", home=comHome[0], n=n, id=id,
                               nhome=bool(comHome[0]), loc=loc, val=val, cp=cp,
                               Alloc=getAllLoc())
    else:
        return render_template("Busqueda.html",  n=n, id=id,
                               nhome=False, loc=loc, val=val, cp=cp,
                               Alloc=getAllLoc())



if __name__ == "__main__":
    app.run(debug=True)
