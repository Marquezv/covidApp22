import os
import requests
import csv
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup as soup

import pygal

date = datetime.now().strftime("%Y-%m-%d")



def webscraping():
	none = 'none'
	url = "https://www.worldometers.info/coronavirus/"
	info = fazer_csv(pegar_info(fazer_requests(url)), none)
	return info

def fazer_requests(url):
	response = requests.get(url, allow_redirects=True)
	response.headers
	soup_response = soup(response.text, "html.parser")
	return soup_response

def pegar_info(soup_response):

	table = soup_response.find("table", id="main_table_countries_today").find("tbody")
	rows = table.find_all("tr", style="")
	global_info = []
	for row in rows:
		columns = row.find_all("td")
		contry_info = [column.text.strip() for column in columns]
		del contry_info[7]
		global_info.append(contry_info)


	return global_info


def fazer_csv(global_info, pais):
	if pais == 'none':
		pass
		covid_csv = pd.DataFrame(global_info, columns=['Numero', 'Local', 'TotalCasos', 
													'NovosCasos', 'TotalMortes', 'NovasMortes', 
													'TotalRecuperados', 'Casos Ativos', 'CasosSerios',
													'TotalCasos/1M', 'TotalMortes/1M', 'TotalTestes',
													'Testes/1M', 'Populacao', 'Continente', 'Casos/10', 
													'Mortes/10', 'Teste/10', 'Novos/1M', 'Mortes/1M', 'Ativos/1M'])
		covid_csv.to_csv(f'data/covid.csv', index=False)

	else:
		covid_csv = pd.DataFrame(global_info, columns=['Numero', 'Local', 'TotalCasos', 
													'NovosCasos', 'TotalMortes', 'NovasMortes', 
													'TotalRecuperados', 'Casos Ativos', 'CasosSerios',
													'TotalCasos/1M', 'TotalMortes/1M', 'TotalTestes',
													'Testes/1M', 'Populacao', 'Continente', 'Casos/10', 
													'Mortes/10', 'Teste/10', 'Novos/1M', 'Mortes/1M', 'Ativos/1M'])
		covid_total.to_csv(f'data/{pais}.csv', index=False)
	# covid_10.to_csv('data/corona_10.csv', index=False)

def pesquisa(pais):
	covid_csv = pd.read_csv('data/covid.csv', sep=',')
	pais_input = covid_csv[covid_csv["Local"]==pais]

	if pais_input.empty:
		pais = 'covid'
		return pais
	else:
		places = []
		covid_csv = pd.read_csv('data/covid.csv', sep=',')	
		pais_input = covid_csv[covid_csv["Local"]==pais]
		pais_input.to_csv(f'data/local.csv', index=False)
		return pais



if __name__ =='__main__':
	webscraping()
	pesquisa(pais)