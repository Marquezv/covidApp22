from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import csv
from corona_csv import *
import pygal

app = Flask(__name__)


  
@app.route('/', methods=['GET', 'POST'])

def index():
  webscraping()
  if request.method == "GET":
    with open('data/covid.csv') as csv_file:
      data = csv.reader(csv_file, delimiter=',')
      first_line = True
      places = []
      for row in data:
        if not first_line:
          places.append({
            "posicao": row[0],
            "local": row[1],
            "totalCasos": row[2],
            "totalMortes": row[4],
            "totalRecuperados": row[6],
            "populacao": row[13],
          })
        else:
          first_line = False
        totalCasos = places
      return render_template('index.html', places=places, totalCasos=totalCasos)
  else:
    webscraping()
    pais = str(request.form.get("input_pais"))
    r_pais = pesquisa(pais)
    if pais == '':
       with open(f'data/covid.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        places = []
        for row in data:
          if not first_line:
            places.append({
              "posicao": row[0],
              "local": row[1],
              "totalCasos": row[2],
              "novosCasos": row[3],
              "totalMortes": row[4],
              "novasMortes": row[5],
              "totalRecuperados": row[6],
              "casosAtivos": row[7],
              "morte1m": row[10],
              "populacao": row[13],
            })
          else:
            first_line = False
    else:       
        with open(f'data/local.csv') as csv_file:
            data = csv.reader(csv_file, delimiter=',')
            first_line = True
            places = []
            for row in data:
              if not first_line:
                places.append({
                  "posicao": row[0],
                  "local": row[1],
                  "totalCasos": row[2],
                  "novosCasos": row[3],
                  "totalMortes": row[4],
                  "novasMortes": row[5],
                  "totalRecuperados": row[6],
                  "casosAtivos": row[7],
                  "morte1m": row[10],
                  "populacao": row[13],
                })
              else:
                first_line = False

    return render_template("index.html", places=places, pais = pais)



@app.route('/<string:nome>')
def error(nome):
  variavel = f'Página ({nome}) não encontrada!'
  return render_template('error.html', variavel=variavel)

if __name__ == "__main__":
  app.run(debug=True)

