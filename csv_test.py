import csv
csv_file = csv.reader(open('Top_50_Products_ZipWise.csv', "rb"), delimiter=",")
def tes(val):



#loop through csv list
  for row in csv_file:
    print(row[0])
    #if current rows 2nd value is equal to input, print that row
    if val== row[0].strip() :
        return row
	


print(tes('02050'))


