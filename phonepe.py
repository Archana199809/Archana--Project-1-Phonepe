#Required libraries for the program

import os
import pandas as pd
import json


#This is to direct the path to get the data as states[aggregated insurance]
path1="C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/data/aggregated/insurance/country/india/state"
Agg_insur_state_list=os.listdir(path1)
print(Agg_insur_state_list)

#This is to extract the data's to create a dataframe

clm1={"States":[], "Years":[], "Quarter":[], "Insurance_type":[], "Insurance_count":[],"Insurance_amount":[]}

for i in Agg_insur_state_list:
    p_i=path1+"/"+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            A=json.load(Data)
    
            for z in A["data"]["transactionData"]:
                Name = z["name"]
                count = z["paymentInstruments"][0]["count"]
                amount = z["paymentInstruments"][0]["amount"]
                clm1["Insurance_type"].append(Name)
                clm1["Insurance_count"].append(count)
                clm1["Insurance_amount"].append(amount)
                clm1["States"].append(i)
                clm1["Years"].append(j)
                clm1["Quarter"].append(int(k.strip(".json")))
        
#Succesfully created a dataframe
Agg_insurance=pd.DataFrame(clm1)

Agg_insurance["States"] = Agg_insurance["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_insurance["States"] = Agg_insurance["States"].str.replace("-"," ")
Agg_insurance["States"] = Agg_insurance["States"].str.title()
Agg_insurance['States'] = Agg_insurance['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
print(Agg_insurance)


#This is to direct the path to get the data as states[aggregated transaction]

path2="C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/data/aggregated/transaction/country/india/state"
Agg_trans_state_list=os.listdir(path2)
print(Agg_trans_state_list)

#This is to extract the data's to create a dataframe

clm2={'States':[], 'Years':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Agg_trans_state_list:
    p_i=path2+"/"+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            B=json.load(Data)
    
            for z in B['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm2['Transaction_type'].append(Name)
              clm2['Transaction_count'].append(count)
              clm2['Transaction_amount'].append(amount)
              clm2['States'].append(i)
              clm2['Years'].append(j)
              clm2['Quarter'].append(int(k.strip('.json')))
        
#Succesfully created a dataframe
Agg_transaction=pd.DataFrame(clm2)

Agg_transaction["States"] = Agg_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_transaction["States"] = Agg_transaction["States"].str.replace("-"," ")
Agg_transaction["States"] = Agg_transaction["States"].str.title()
Agg_transaction['States'] = Agg_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
print(Agg_transaction)

# This is to direct the path to get the data as states[aggregated user]

path3=r"C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/data/aggregated/user/country/india/state"
Agg_user_state_list=os.listdir(path3)
print(Agg_user_state_list)

#This is to extract the data's to create a dataframe

clm3={"States":[], "Years":[], "Quarter":[], "Brands":[],"Transaction_count":[], "Percentage":[]}

for i in Agg_user_state_list:
    p_i=path3+"/"+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            C=json.load(Data)
            try:
             for z in C["data"]["usersByDevice"]:
               brand = z["brand"]
               count = z["count"]
               percentage = z["percentage"]
               clm3["Brands"].append(brand)
               clm3["Transaction_count"].append(count)
               clm3["Percentage"].append(percentage)
               clm3["States"].append(i)
               clm3["Years"].append(j)
               clm3["Quarter"].append(int(k.strip(".json")))
            except:
                pass
#Succesfully created a dataframe
Agg_user=pd.DataFrame(clm3)
Agg_user["States"] = Agg_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_user["States"] = Agg_user["States"].str.replace("-"," ")
Agg_user["States"] = Agg_user["States"].str.title()
Agg_user['States'] = Agg_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
print(Agg_user)

#This is to direct the path to get the data as states[map insurance]

path4="C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/data/map/insurance/hover/country/india/state"
map_insur_state_list=os.listdir(path4)
print(map_insur_state_list)

#This is to extract the data's to create a dataframe

clm4={"States":[], "Years":[], "Quarter":[], "District":[], "Insurance_count":[],"Insurance_amount":[]}

for i in map_insur_state_list:
    p_i=path4+"/"+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
    
            try:
                for z in D["data"]["hoverDataList"]:
                    name = z["name"]
                    count = z["metric"][0]["count"]
                    amount = z["metric"][0]["amount"]
                    clm4["District"].append(name)
                    clm4["Insurance_count"].append(count)
                    clm4["Insurance_amount"].append(amount)
                    clm4["States"].append(i)
                    clm4["Years"].append(j)
                    clm4["Quarter"].append(int(k.strip(".json")))
            except:
                pass
#Succesfully created a dataframe
map_insurance=pd.DataFrame(clm4)
map_insurance['States'] = map_insurance['States'].astype(str)
map_insurance["States"] = map_insurance["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_insurance["States"] = map_insurance["States"].str.replace("-"," ")
map_insurance["States"] = map_insurance["States"].str.title()
map_insurance['States'] = map_insurance['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
print(map_insurance)

# This is to direct the path to get the data as states[map transaction]

path5="C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/data/map/transaction/hover/country/india/state"
map_trans_state_list=os.listdir(path5)
print(map_trans_state_list)

#This is to extract the data's to create a dataframe

clm5={"States":[], "Years":[], "Quarter":[],"District":[], "Transaction_count":[],"Transaction_amount":[]}

for i in map_trans_state_list:
    p_i=path5+"/"+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            E=json.load(Data)
            for z in E['data']['hoverDataList']:
              Name=z['name']
              count=z['metric'][0]['count']
              amount=z['metric'][0]['amount']
              clm5['District'].append(Name)
              clm5['Transaction_count'].append(count)
              clm5['Transaction_amount'].append(amount)
              clm5['States'].append(i)
              clm5['Years'].append(j)
              clm5['Quarter'].append(int(k.strip('.json')))
#Succesfully created a dataframe
map_transaction=pd.DataFrame(clm5)
map_transaction["States"] = map_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_transaction["States"] = map_transaction["States"].str.replace("-"," ")
map_transaction["States"] = map_transaction["States"].str.title()
map_transaction['States'] = map_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
print(map_transaction)

#This is to direct the path to get the data as states[map user]

path6="C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/data/map/user/hover/country/india/state"
map_user_state_list=os.listdir(path6)
print(map_user_state_list)

#This is to extract the data's to create a dataframe

clm6={"States":[], "Years":[], "Quarter":[], "District":[], "RegisteredUser":[], "AppOpens":[]}

for i in map_user_state_list:
    p_i=path6+"/"+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            F=json.load(Data)
            for Z in F["data"]["hoverData"].items():
                district = Z[0]
                registereduser = Z[1]["registeredUsers"]
                appopens = Z[1]["appOpens"]
                clm6["District"].append(district)
                clm6["RegisteredUser"].append(registereduser)
                clm6["AppOpens"].append(appopens)
                clm6["States"].append(i)
                clm6["Years"].append(j)
                clm6["Quarter"].append(int(k.strip(".json")))

#Succesfully created a dataframe
map_user=pd.DataFrame(clm6)
map_user["States"] = map_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
map_user["States"] = map_user["States"].str.replace("-"," ")
map_user["States"] = map_user["States"].str.title()
map_user['States'] = map_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
print(map_user)

#This is to direct the path to get the data as states[Top insurance]

path7= "C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/data/top/insurance/country/india/state"
top_insur_state_list=os.listdir(path7)
print(top_insur_state_list)

#This is to extract the data's to create a dataframe

clm7={"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Insurance_count":[], "Insurance_amount":[]}

for i in top_insur_state_list:
    p_i=path7+"/"+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            G=json.load(Data)
            

            for z in G["data"]["pincodes"]:
                entityName = z["entityName"]
                count = z["metric"]["count"]
                amount = z["metric"]["amount"]
                clm7["Pincodes"].append(entityName)
                clm7["Insurance_count"].append(count)
                clm7["Insurance_amount"].append(amount)
                clm7["States"].append(i)
                clm7["Years"].append(j)
                clm7["Quarter"].append(int(k.strip(".json")))
        
#Succesfully created a dataframe
top_insurance=pd.DataFrame(clm7)

top_insurance["States"] = top_insurance["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
top_insurance["States"] = top_insurance["States"].str.replace("-"," ")
top_insurance["States"] = top_insurance["States"].str.title()
top_insurance['States'] = top_insurance['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
print(top_insurance)
# #This is to direct the path to get the data as states[top transaction]

path8="C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/data/top/transaction/country/india/state"
top_trans_state_list=os.listdir(path8)
print(top_trans_state_list)

#This is to extract the data's to create a dataframe

clm8={'States':[], 'Years':[],'Quarter':[],"Pincodes":[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in top_trans_state_list:
    p_i=path8+"/"+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            H=json.load(Data)
            for z in H["data"]["pincodes"]:
                entityName = z["entityName"]
                count = z["metric"]["count"]
                amount = z["metric"]["amount"]
                clm8["Pincodes"].append(entityName)
                clm8["Transaction_count"].append(count)
                clm8["Transaction_amount"].append(amount)
                clm8["States"].append(i)
                clm8["Years"].append(j)
                clm8["Quarter"].append(int(k.strip(".json")))
#Succesfully created a dataframe
top_transaction=pd.DataFrame(clm8)
top_transaction["States"] = top_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
top_transaction["States"] = top_transaction["States"].str.replace("-"," ")
top_transaction["States"] = top_transaction["States"].str.title()
top_transaction['States'] = top_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
print(top_transaction)

#This is to direct the path to get the data as states[top user]

path9="C:/Users/Archana/OneDrive/Attachments/Desktop/MDTM46B/Phonepay_project/data/top/user/country/india/state"
top_user_state_list=os.listdir(path9)
print(top_user_state_list)

#This is to extract the data's to create a dataframe

clm9={'States':[], 'Years':[],'Quarter':[],"Pincodes":[], "RegisteredUser":[]}

for i in top_user_state_list:
    p_i=path9+"/"+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            I=json.load(Data)
            for z in I["data"]["pincodes"]:
                name = z["name"]
                registeredusers = z["registeredUsers"]
                clm9["Pincodes"].append(name)
                clm9["RegisteredUser"].append(registeredusers)
                clm9["States"].append(i)
                clm9["Years"].append(j)
                clm9["Quarter"].append(int(k.strip(".json")))
#Succesfully created a dataframe
top_user=pd.DataFrame(clm9)

top_user["States"] = top_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
top_user["States"] = top_user["States"].str.replace("-"," ")
top_user["States"] = top_user["States"].str.title()
top_user['States'] = top_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
print(top_user)


df_List_strings = ['Agg_insurance', 'Agg_transaction','Agg_user','map_insurance','map_transaction','map_user','top_insurance','top_transaction','top_user']
dfs = [Agg_insurance, Agg_transaction,Agg_user,map_insurance,map_transaction,map_user,top_insurance,top_transaction,top_user ]
columns = {}
for i in range(0, len(df_List_strings), 1):
  columns_names = list(dfs[i].columns)
  columns[df_List_strings[i]] = columns_names
print(columns)



#pymysql connection
import pymysql

try:
    # Connection Parameters
    connection = pymysql.connect(
         host = 'localhost', user = 'root',
         password = '12345', database = 'Phonepe')
    print("connection = ", connection)
    cursor = connection.cursor()
    print("cursor = ", cursor)
    #Creating a table and inserting values in SQL
   #aggregated Insurance table
    create_query1 = '''CREATE TABLE if not exists aggregated_insurance (States varchar(50),
                                                                      Years int,
                                                                      Quarter int,
                                                                      Insurance_type varchar(50),
                                                                      Insurance_count bigint,
                                                                      Insurance_amount bigint
                                                                      )'''
    cursor.execute(create_query1)
    connection.commit()

    for index,row in Agg_insurance.iterrows():
     insert_query1 = '''INSERT INTO aggregated_insurance (States, Years, Quarter, Insurance_type, Insurance_count, Insurance_amount)
                                                        values(%s,%s,%s,%s,%s,%s)'''
     values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Insurance_type"],
              row["Insurance_count"],
              row["Insurance_amount"])
     cursor.execute(insert_query1,values)
     connection.commit()

  #aggregated Transactiom table
    create_query2 = '''CREATE TABLE if not exists aggregated_transaction (States varchar(50),
                                                                      Years int,
                                                                      Quarter int,
                                                                      Transaction_type varchar(50),
                                                                      Transaction_count bigint,
                                                                      Transaction_amount bigint
                                                                      )'''
    cursor.execute(create_query2)
    connection.commit()

    for index,row in Agg_transaction.iterrows():
     insert_query2 = '''INSERT INTO aggregated_transaction (States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount)
                                                        values(%s,%s,%s,%s,%s,%s)'''
     values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Transaction_type"],
              row["Transaction_count"],
              row["Transaction_amount"]
              )
     cursor.execute(insert_query2,values)
     connection.commit()

     #aggregated user table
    create_query3 = '''CREATE TABLE if not exists aggregated_user (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                Brands varchar(50),
                                                                Transaction_count bigint,
                                                                Percentage float
                                                                      )'''
    cursor.execute(create_query3)
    connection.commit()

    for index,row in Agg_user.iterrows():
     insert_query3 = '''INSERT INTO aggregated_user (States, Years, Quarter, Brands, Transaction_count, Percentage)
                                                        values(%s,%s,%s,%s,%s,%s)'''
     values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Brands"],
              row["Transaction_count"],
              row["Percentage"]
              )
     cursor.execute(insert_query3,values)
     connection.commit()

     #map Insurance table
    create_query4 = '''CREATE TABLE if not exists map_insurance (States varchar(50),
                                                                      Years int,
                                                                      Quarter int,
                                                                      District varchar(50),
                                                                      Insurance_count bigint,
                                                                      Insurance_amount bigint
                                                                      )'''
    cursor.execute(create_query4)
    connection.commit()

    for index,row in map_insurance.iterrows():
     insert_query4 = '''INSERT INTO map_insurance (States, Years, Quarter, District, Insurance_count, Insurance_amount)
                                                        values(%s,%s,%s,%s,%s,%s)'''
     values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["District"],
              row["Insurance_count"],
              row["Insurance_amount"]
              )
     cursor.execute(insert_query4,values)
     connection.commit()

     #map transaction table
    create_query5 = '''CREATE TABLE if not exists map_transaction (States varchar(50),
                                                                      Years int,
                                                                      Quarter int,
                                                                      District varchar(50),
                                                                      Transaction_count bigint,
                                                                      Transaction_amount bigint
                                                                      )'''
    cursor.execute(create_query5)
    connection.commit()

    for index,row in map_transaction.iterrows():
     insert_query5 = '''INSERT INTO map_transaction (States, Years, Quarter, District, Transaction_count, Transaction_amount)
                                                        values(%s,%s,%s,%s,%s,%s)'''
     values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["District"],
              row["Transaction_count"],
              row["Transaction_amount"]
              )
     cursor.execute(insert_query5,values)
     connection.commit()

     #map user table
    create_query6= '''CREATE TABLE if not exists map_user (States varchar(50),
                                                        Years int,
                                                        Quarter int,
                                                        District varchar(50),
                                                        RegisteredUser bigint,
                                                        AppOpens bigint
                                                                      )'''
    cursor.execute(create_query6)
    connection.commit()

    for index,row in map_user.iterrows():
     insert_query6 = '''INSERT INTO map_user (States, Years, Quarter, District, RegisteredUser, AppOpens)
                                                        values(%s,%s,%s,%s,%s,%s)'''
     values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["District"],
              row["RegisteredUser"],
              row["AppOpens"]
              )
     cursor.execute(insert_query6,values)
     connection.commit()

 #top Insurance table
    create_query7 = '''CREATE TABLE if not exists top_insurance (States varchar(50),
                                                                      Years int,
                                                                      Quarter int,
                                                                      Pincodes int,
                                                                      Insurance_count bigint,
                                                                      Insurance_amount bigint
                                                                      )'''
    cursor.execute(create_query7)
    connection.commit()

    for index,row in top_insurance.iterrows():
     insert_query7 = '''INSERT INTO top_insurance (States, Years, Quarter,Pincodes, Insurance_count, Insurance_amount)
                                                        values(%s,%s,%s,%s,%s,%s)'''
     values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["Insurance_count"],
              row["Insurance_amount"]
              )
     cursor.execute(insert_query7,values)
     connection.commit()

     #top_transaction table
    create_query8 = '''CREATE TABLE if not exists top_transaction (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                pincodes int,
                                                                Transaction_count bigint,
                                                                Transaction_amount bigint
                                                                      )'''
    cursor.execute(create_query8)
    connection.commit()

    for index,row in top_transaction.iterrows():
     insert_query8 = '''INSERT INTO top_transaction (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount)
                                                        values(%s,%s,%s,%s,%s,%s)'''
     values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["Transaction_count"],
              row["Transaction_amount"])
     cursor.execute(insert_query8,values)
     connection.commit()

     #top user table
    create_query9 = '''CREATE TABLE if not exists top_user (States varchar(50),
                                                        Years int,
                                                        Quarter int,
                                                        Pincodes int,
                                                        RegisteredUser bigint
                                                                      )'''
    cursor.execute(create_query9)
    connection.commit()

    for index,row in top_user.iterrows():
     insert_query9 = '''INSERT INTO top_user (States, Years, Quarter, Pincodes, RegisteredUser)
                                                        values(%s,%s,%s,%s,%s)'''
     values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["RegisteredUser"])
     cursor.execute(insert_query9,values)
     connection.commit()

except Exception as e:
    print(str(e))