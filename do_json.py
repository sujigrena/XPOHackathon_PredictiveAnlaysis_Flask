import json

fi=open("filenames.csv","r")
data={}
data['name']='test'
data['children']=[]

for i in fi.readlines():
	val=i.split(',')
	data['children'].append({
	'name':val[0],
	'img':val[1],
	'total':val[2].split('\n')[0]
}
)

jsonf = open('myjson.json','w') 
val = json.dumps(data)
jsonf.write(val)
jsonf.close() 

