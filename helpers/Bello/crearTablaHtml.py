
def crearTablaBelloQuitasol(dataframe,nombreTabla):
    archivoHtml = dataframe.to_html()
    archivo=open(f"./tablas/Bello/{nombreTabla}.html","w", encoding="utf-8") 
    archivo.write(''' 
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    </head>
    <body>
    ''')

    archivo.write(archivoHtml)
    archivo.write('''
    </body>
    </html>
    ''')
    archivo.close()