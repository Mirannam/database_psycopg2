import psycopg2
from pprint import pprint as pp
import random
conn = psycopg2.connect(
    dbname='homework',
    user='home',
    password='12345',
    host='localhost'
)

cur =  conn.cursor()
# cur.execute("CREATE TABLE inner_flights("+
#     "id SERIAL PRIMARY KEY,"+
#     "from_region VARCHAR,"+
#     "to_destination VARCHAR,"+
#     "company VARCHAR,"+
#     "quantity INT);")
# cur.execute("CREATE TABLE outter_flights("+
#     "id SERIAL PRIMARY KEY,"+
#     "from_country VARCHAR,"+
#     "to_country VARCHAR,"+
#     "flight_type VARCHAR,"+
#     "company VARCHAR,"+
#     "neighbors INT);"       
#     )
town = ['bishkek','osh','naryn','talas','kemin','karakol','jalalabad']
city =['turkey','bishkek','moscow','astana','paris','london','rome','new york','tashkent','madrid','dublin']
comp =['her air', 'sasa','air','katar air','kg air','pegasus']
quant=[50,60,70,90,45,47,52,21,36,54]
ftype =['cargo', 'passanger']
neighbor =[1,2,3,4,5,6,7,8,9]
l = []


for i in range(15):
    l.append(random.choice(town))
    l.append(random.choice(town))
    l.append(random.choice(comp))
    l.append(random.choice(quant))
    
    
    


# for j in range(15):
      
#     cur.execute("INSERT INTO inner_flights("+
#         "from_region,"+
#         "to_destination,"+
#         "company,"+
#         "quantity)" +
#         "VALUES("+
        # f"'{random.choice(town)}',"+
        # f"'{random.choice(town)}',"+
        # f"'{random.choice(comp)}',"+
        # f"{random.choice(quant)});")
    
# cur.execute("SELECT * FROM inner_flights;")
# records = cur.fetchall()
# conn.commit()
# for k in range(15):
      
#     cur.execute("INSERT INTO outter_flights("+
#         "from_country,"+
#         "to_country,"+
#         "flight_type,"+
#         "company,"+
#         "neighbors)" +
#         "VALUES("+
#         f"'{random.choice(city)}',"+
#         f"'{random.choice(city)}',"+
#         f"'{random.choice(ftype)}',"+
#         f"'{random.choice(comp)}',"+
#         f"{random.choice(neighbor)});")
cur.execute("SELECT * from inner_flights where id > 10;")
# cur.execute("SELECT * FROM outter_flights;")
# cur.execute("select * from inner_flights where from_region = 'osh' or from_region ='bishkek';")
# cur.execute("select * from inner_flights where quantity > 60;")
# cur.execute("select company from outter_flights where flight_type ='cargo';")
# cur.execute("SELECT * FROM outter_flights where neighbors > 7;")
# cur.execute("select * from outter_flights where flight_type='passanger' and neighbors < 5;")
# cur.execute("select company, to_country from outter_flights;")
records = cur.fetchall()
conn.commit()
print('результат', records)

