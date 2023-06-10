from helpers.crearTablasHtml import crearTabla
#from helpers.crearBarras import graficarPromedioSalarial
#from helpers.crearTorta import calcularPromedioSalariosPorEdad
import pandas as pd
from matplotlib import pyplot as plt
#Crear Dataframe
tablaSiembras = pd.read_csv("./data/Siembras.csv")

#Efectuando filtros con python

#1.Encontrar todos los datos de santa fe de Antioquia donde se tengan siembras de + de 250 arboles
filtroUno = tablaSiembras.query('Ciudad == "Santa Fe de Antioquia" and Arboles > 250')
#2. Filtrar todos los datos de Caucasia e interpretar sus estadísticas
filtroDos = tablaSiembras.query('Ciudad == "Caucasia"')
interpretacion = filtroDos.describe()
#3. Filtrar todos los datos de las veredas Rio arriba y la Salazar de Belmira
filtroTres = tablaSiembras.query('Ciudad == "Belmira"  and Vereda == "La Salazar"')
filtroTresUno = tablaSiembras.query('Ciudad == "Belmira" and Vereda == "Rio Arriba"')
#4. Encontrar los datos de las veredas Quitasol de Bello mostrando además las medias de cada ítem del dataframe
filtroCuatro = tablaSiembras.query('Ciudad == "Bello" and Vereda == "Quitasol"')
media = pd.DataFrame(filtroCuatro)
print(media)
#5. Encontrar todos los datos de caramanta donde se tengan siembras de + de 100 arboles
filtroCinco = tablaSiembras.query('Ciudad == "Caramanta" and Arboles > 100')
#6. Encontrar los datos de la vereda mallarino del municipio de Yarumal
filtroSeis = tablaSiembras.query('Vereda == "Mallarino" and Ciudad == "Yarumal"')
#7. Creamos la tabla HTML con el html del frito
crearTabla(filtroUno,"Filtro1")
crearTabla(filtroDos,"Filtro2")
crearTabla(interpretacion,"interpretacionFiltoDos")
crearTabla(filtroTres,"Filtro3")
crearTabla(filtroTresUno,"Filtro31")
crearTabla(filtroCuatro,"Filtro4")
crearTabla(filtroCinco,"Filtro5")
crearTabla(filtroSeis,"Filtro6")

#3. Generar graficas

#graficarPromedioSalarial(empleadosADespedir,'cargo','salario','graficajubilados')
#calcularPromedioSalariosPorEdad(empladosJovenesAnalista1,[20,30,40,50,60],'edad','salario','graficadetortaanalisis1')



