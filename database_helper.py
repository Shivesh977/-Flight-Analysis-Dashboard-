# All sql commands will be written here 
# this file will be connected to app.py file
 
import mysql.connector

# we are using self. such that it can be used in class
class DB: # making a class 
    def __init__(self):
 # constructor off the class
        # connect to database server
        try : 
            self.conn=mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='shivesh',
                database='flights'
            )
            
            self.mycursor=self.conn.cursor() # it will return cursor object
            print('connection established ')

        except Exception as e:
            print("connection error:", e)
    
    
##############################    Extracting unique source and destination city name #####################################
    def fetch_city_name(self):
        city = []
        self.mycursor.execute(""" 
                              select distinct(Source)
                                from flights.flights
                                union
                                select distinct(Destination)
                                from flights.flights;
                              """)
        data=self.mycursor.fetchall() # to fetch data
        for i in data:
            city.append(i[0])
        return city
    
######################################## Extracting flights between source and destination ##################
    def fetch_all_flights(self,source,destination):
        self.mycursor.execute(""" 
                            select Airline,Route,Dep_Time,Duration,Price
                            from flights.flights
                            where Source='{}' and Destination='{}' """
                            .format(source,destination))
        data=self.mycursor.fetchall()
        return data
    
######################################## Extracting airline frequency to plot a pie char #####################
    def airline_frequence(self):
        airline=[]
        frequency=[]
        self.mycursor.execute("""
                            select Airline,count(*)
                            from flights.flights
                            group by Airline;
                              """)
        data=self.mycursor.fetchall()
        for i in data:
            airline.append(i[0])
            frequency.append(i[1])
        return airline,frequency

############################################## Finding busissiest airport and mapping a bar chart ##########################

    def bussiest_airport(self):
        city=[]
        frequecy=[]
        self.mycursor.execute(""" 
                            SELECT Source,Count(Destination) as 'dest'
                            FROM flights.flights
                            group by Source;
                              """)
        data = self.mycursor.fetchall()
        for i in data:
            city.append(i[0])
            frequecy.append(i[1])
        return city,frequecy
############################################## Finding average price of airlines #################
    def average_price(self):
        airline=[]
        price=[]
        self.mycursor.execute(""" 
                              select Airline,avg(Price)
                                from flights
                                group by Airline
                                Order by avg(Price) asc;
                              """)
        data=self.mycursor.fetchall()
        for i in data:
            airline.append(i[0])
            price.append(i[1])
        return airline,price