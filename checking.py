'''
import parameters

ZIPcode="95445"
Firstname="Dan"
Lastname="Lewis"

ZIPcode1="95445"
Firstname1="Eric"
Lastname1="Smith"

Linkedin_details=[[ZIPcode,Firstname,Lastname],[ZIPcode1,Firstname1,Firstname1]]

j=0
for details in parameters.Linkedin_details:
    for d in details:
        print(d)
    j+=1
    if(j==2):
        break

'''



"""
from pandas import DataFrame

Cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000],'price1':[300]
        }

print(type(Cars))
df = DataFrame(Cars, columns= ['Brand', 'Price'])

export_csv = df.to_csv (r'F:\sales-force-requierment\export_dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

print (df)
"""







import pandas as pd
import csv
#from pandas import read_excel 
#df = pd.read_csv("01_CA_Sea_Ranch_Gualala_Anchor_Bay_19_09_30.xlsx", usecols = ['OWNER 1 FIRST NAME','MAIL ZIP CODE','OWNER 1 LAST NAME'])
#print(df.head[10])
#project_data['project_is_approved'].value_counts()

project_data = pd.read_excel(r'F:\sales-force-requierment\01_CA_Sea_Ranch_Gualala_Anchor_Bay_19_09_30.xlsx',usecols = ['OWNER 1 FIRST NAME','MAIL ZIP CODE','OWNER 1 LAST NAME'],sheet_name='ListReport')
print("Number of data points in train data", project_data.shape)
print('-'*50)
print("The attributes of data :", project_data.columns.values)
print("head of the values",project_data.head())
print("lengths of column values",len(project_data['OWNER 1 FIRST NAME']),len(project_data['OWNER 1 LAST NAME']),len(project_data['MAIL ZIP CODE']),len(project_data))
#print("data frame",project_data.iloc[0:3])
i=0
for j in project_data['OWNER 1 FIRST NAME']:
    print("checking the loop values",project_data['OWNER 1 FIRST NAME'][i])
    print("checking the loop values1",project_data['OWNER 1 LAST NAME'][i])
    print("checking the loop values2",project_data['MAIL ZIP CODE'][i])
    linkedin_url="url"+str(i)
    row = [project_data['OWNER 1 FIRST NAME'][i],project_data['OWNER 1 LAST NAME'][i],project_data['MAIL ZIP CODE'][i],linkedin_url,linkedin_url]

    with open(r'test1.csv', 'a',newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
        
    i+=1
    if(i>10):
        break;
    





