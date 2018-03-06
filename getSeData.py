import urllib.request, json 
from pandas.io.json import json_normalize
import pandas as pd

''' Answer for Q1 '''

with urllib.request.urlopen("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2016-10-01&endtime=2016-10-02") as url:
    data = json.loads(url.read().decode())
    #print(data)
print ('Data Type of features:')
print (type(data['features']))

'''############################'''

''' Answer for Q2 '''
print ('Length of Features')
print (len(data['features']))

''' Answer for Q3 '''
print ('Data type of first element of features')
print (type(data['features'][0]))

''' Answer for Q4 '''
flatjson= (json_normalize(data['features']))

flatlist=[]
flatlist.append(flatjson['properties.title'].rename("Title"))
flatlist.append(flatjson['properties.mag'])
flatlist.append(flatjson['properties.place'])
#print (pd.Series([item[0] for item in flatjson['geometry.coordinates']]))

flatlist.append(pd.Series([item[0] for item in flatjson['geometry.coordinates']]).rename("Latitude"))
flatlist.append (pd.Series([item[1] for item in flatjson['geometry.coordinates']]).rename("Longitude"))

#fDF=pd.DataFrame(flatlist,columns=["Title","Magnitude","Place","LAT/LONG"]).T
fDF=pd.DataFrame(flatlist).T

print ('CSV file created from data frame')
fDF.to_csv('jigsaw-04.csv', sep='\t', encoding='utf-8')

''' Answer for Q5 '''
print ('Number of records with magnitude >2')
print (len(fDF[fDF['properties.mag']>2]))

''' Answer for Q6 '''
print ('Number of records with "California" in place description')
print (len(fDF[fDF['properties.place'].str.contains("California")]))

''' Answer for Q7 '''
print ('Number of records with magnitude >5')
print (len(fDF[fDF['properties.mag']>5]))


