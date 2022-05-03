#import pandas as pd
import sqlalchemy
from csv import reader

database_username = 'root'
database_password = 'root'
database_ip       = '127.0.0.1:33066'
database_name     = 'main'
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))
with open('flights.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
       query="INSERT INTO `flights_flights` (`origin_city` ,`origin_airport` ,`dest_city` ,`dest_airport` , `datetime` , `price`, `carrier`, `flight_class`, `plane_type`, `reserved`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
       my_data=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],0)
       id=database_connection.execute(query,my_data)
       print("ID of Row Added  = ",id.lastrowid)


#data = pd.read_csv (r'flights.csv')   
#df = pd.DataFrame(data)
#df.to_sql(con=database_connection, name='flights_flights', if_exists='replace')
#df.to_sql(name=database, con=conn, if_exists = 'replace', index=False, flavor = 'mysql')
#print(df.to_json())


