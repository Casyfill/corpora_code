#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import csv

path = "/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_05_08_Corpora/Mine/to_Normalise.csv"


print
# print 'started'

OBJ = {}
with open(path, 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for line in reader:
		OBJ[int(line[0])] = int(line[2])

# print 'nornalised'
diapasons = [[1700,1750],[1751,1800],[1801,1850],[1851,1900],[1901,1920],[1921,1940], [1941,1960], [1961,1980], [1981,2000], [2001,2020]]
def epoch(integer, diapasons):
	for diap in diapasons:
		if integer >= diap[0] and integer<=diap[1]:
			return diap[0]
			break
	print 'error: ', integer, ' not found'


# def utf8_encoder(data):
# 	for line in data:
# 		yeld line.encode('utf-8')

# dataPath = "/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_05_08_Corpora/Mine/bribes.csv"
# dataPath = "/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_05_08_Corpora/Mine/vorovaiky.csv"
dataPath = "/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_05_08_Corpora/Mine/roads_grouped1.csv"

GroupedData = {}

with open(dataPath, 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	count = 1
	for line in reader:
		line = [unicode(cell,'utf-8') for cell in line]
		group = line[0] + '|' + line[-1]
		# try:
		nYear = int(float(line[1].strip()))
		# except:
			# print count, 'lalalalalalalalala'
		count+=1
		e = epoch(nYear, diapasons)
		# print nYear, ':', e
		try:
			if group in GroupedData:
				if e in GroupedData[group]:
					GroupedData[group][e]+=1
				else:
					GroupedData[group][e]=1
			else:
				GroupedData[group]={}
		except: print group, '|', e


	
# print 'data read'
# print ', '.join(GroupedData)
# print 'group|epoch|total|normal'
years = [x[0] for x in diapasons]
print 'word|', '|'.join([str(year) for year in years])
for group in GroupedData:
	normalised = []
	for year in years:
			if year in GroupedData[group]:
				# n = str(GroupedData[group][year])
				n = str(1000000000*float(GroupedData[group][year])/OBJ[e])
				normalised.append(n)
			else:
				normalised.append('')
	print group.strip(), '|', '|'.join(normalised)



	



# 		total = GroupedData[group][e]
# 		normal = 100000000*float(total)/OBJ[e]
# 		print '|'.join([group, str(e), str(total), str(normal)])


