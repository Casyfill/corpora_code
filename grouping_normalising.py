#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import csv

path = "/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_05_08_Corpora/Mine/to_Normalise.csv"


OBJ = []
with open(path, 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for line in reader:
		period = {}
		period['s'] = line[0]
		period['e'] = line[1]
		period['norm'] = line[2]
		OBJ.append(period)

def epoch(integer):
	diapasons = [[1700,1750],[1751,1800],[1801,1850],[1851,1900],[1901,1950],[1951,2000], [2001,2020]]
	for diap in diapasons:
		if integer >= diap[0] and integer<=diapasons[1]:
			return diap[0]


dataPath = "/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_05_08_Corpora/Mine/vorovaiky.csv"
GroupedData = {}

with open(dataPath, 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for line in reader:
		group = line[0]
		nYear = int(line[1])
		e = epoch(nYear)
		# obj = {}
		if GroupedData[group]:
			GroupedData[group][epoch]+=1
		else:
			GroupedData[group][epoch]=1


		# GroupedData{group}
