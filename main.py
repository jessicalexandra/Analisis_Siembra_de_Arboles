from helpers.Santa_Fe_De_Antioquia.crearTablas import crearTabla as graficarTablaStaFe
from helpers.Belmira.la_salazar.crearTablas import crearTabla as graficarTablaLaSalazar
from helpers.Belmira.rio_arriba.crearTablas import crearTabla as graficarTablaRioArriba
from helpers.Belmira.la_salazar.crearBarras import graficarEstadisticas as graficarBarrasLaSalazar
from helpers.Belmira.rio_arriba.crearBarras import graficarEstadisticas as graficarBarrasRioArriba
from helpers.Caucasia.crearTablas import crearTabla as graficarTablaCaucasia
from helpers.Bello.crearTablaHtml import crearTablaBelloQuitasol
from helpers.Bello.crearBarras import graficarVeredasQuitasol
from helpers.Bello.crearTorta import calcularPromedioArbolesPorNombreComun
from helpers.Caramanta.crearTablaHtml import crearTablaCaramanta
from helpers.Caramanta.crearBarras import graficarSiembraCaramanta
from helpers.Yarumal.crearBarras import graficarVeredaMarinillo
from helpers.Yarumal.crearTablaHtml import crearTablaVeredaMarinillo
import pandas as pd
#Crear Dataframe
tablaSiembras = pd.read_csv("./data/Siembras.csv")

#Efectuando filtros con python

#1.Encontrar todos los datos de santa fe de Antioquia donde se tengan siembras de + de 250 arboles
filtroUno = tablaSiembras.query('Ciudad == "Santa Fe de Antioquia" and Arboles > 250')
#2. Filtrar todos los datos de Caucasia e interpretar sus estadísticas
filtroDos = tablaSiembras.query('Ciudad == "Caucasia"')
interpretacion = filtroDos.describe()
#3. Filtrar todos los datos de las veredas Rio arriba y la Salazar de Belmira
cantidadArboles=tablaSiembras.query('Arboles > 250 and Ciudad == "Santa Fe de Antioquia" ')
datosGeneralesBelmiraLaSalazar=tablaSiembras.query('Ciudad == "Belmira" and Vereda == "La Salazar"')
datosGeneralesBelmiraRioArriba=tablaSiembras.query('Ciudad == "Belmira" and Vereda == "Rio Arriba"')
graficarTablaLaSalazar(datosGeneralesBelmiraLaSalazar, 'Tabla_La_Salazar')
graficarTablaRioArriba(datosGeneralesBelmiraRioArriba, 'Tabla_Rio_Arriba')
graficarBarrasLaSalazar(datosGeneralesBelmiraLaSalazar, 'Hectareas', 'Arboles', 'Barras_La_Salazar')
graficarBarrasRioArriba(datosGeneralesBelmiraRioArriba, 'Hectareas', 'Arboles', 'Barras_Rio_Arriba')

#4. Encontrar los datos de las veredas Quitasol de Bello mostrando además las medias de cada ítem del dataframe
BelloveredasQuitasol = tablaSiembras[['Nombre comun','Ciudad','Vereda','Arboles','Hectareas']].query('Vereda == "Quitasol" and Ciudad == "Bello" ')
graficarVeredasQuitasol(BelloveredasQuitasol, 'Hectareas', 'Arboles', 'MediabelloVeredasQuitasol')

crearTablaBelloQuitasol(BelloveredasQuitasol, "belloVeredasQuitasol")
calcularPromedioArbolesPorNombreComun(BelloveredasQuitasol,['Almendra', 'misperos', 'casco de vaca', 'ceiba', 'pino' 'vela'], 'Hectareas', 'Arboles','Distribución_Árboles_Hectáreas')

#media
BelloveredasQuitasol = tablaSiembras[['Nombre comun','Ciudad','Vereda','Arboles','Hectareas']].query('Vereda == "Quitasol" and Ciudad == "Bello" ')
graficarVeredasQuitasol(BelloveredasQuitasol, 'Hectareas', 'Arboles', 'MediabelloVeredasQuitasol')
#5. Encontrar todos los datos de caramanta donde se tengan siembras de + de 100 arboles
filtroCinco = tablaSiembras.query('Ciudad == "Caramanta" and Arboles > 100')
crearTablaCaramanta(filtroCinco, "siembraCaramanta")
graficarSiembraCaramanta(filtroCinco, ['Cabecera Municipal', 'El Balso', 'La Unión', 'Olibales', 'Olibales'], 'Arboles', 'graficarSiembraCaramanta')


#6. Encontrar los datos de la vereda mallarino del municipio de Yarumal
filtroSeis = tablaSiembras.query('Vereda == "Mallarino" and Ciudad == "Yarumal"')
graficarVeredaMarinillo(filtroSeis, 'Hectareas', 'Arboles', 'graficarVeredaMarinillo')
crearTablaVeredaMarinillo(filtroSeis, "veredaMallarino")
#7. Creamos la tabla HTML con el html del frito
graficarTablaStaFe(filtroUno,"Filtro1")
graficarTablaCaucasia(filtroDos,"Filtro2")
#crearTabla(interpretacion,"interpretacionFiltoDos")
graficarTablaLaSalazar(filtroTres,"Filtro3")
graficarTablaRioArriba(filtroTresUno,"Filtro31")
crearTablaBelloQuitasol(filtroCuatro,"Filtro4")
crearTablaCaramanta(filtroCinco,"Filtro5")
crearTablaVeredaMarinillo(filtroSeis,"Filtro6")

#3. Generar graficas

#graficarPromedioSalarial(empleadosADespedir,'cargo','salario','graficajubilados')
#calcularPromedioSalariosPorEdad(empladosJovenesAnalista1,[20,30,40,50,60],'edad','salario','graficadetortaanalisis1')



