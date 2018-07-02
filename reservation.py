hotels = [] # defin a list for hotels 
customers = [] # define a list for customers 
reservations = [] # defin a list for reservations 

# first functions to add hotels and it's data & information
def add_hotel(number,hotel_name,city,total_rooms,empty_rooms):
    
    hotels.append([number,hotel_name,city,total_rooms,empty_rooms])

# adding some hotels for test 

add_hotel(1,'hilton','giza',500, 0)
add_hotel(2,'rotana','giza',500, 100)
add_hotel(3,'blue','giza',500, 100)



#second function to add customer 
def add_customer(customer_name):
    customers.append(customer_name)


#reservation function 

def reserve_room(hotel_name, customer_name):
    for i in hotels:
        if i[1] == hotel_name:
            if i[4] == 0 :
                
                return False
            else:
                i[4] -= 1
                return True 

def add_new_reservation(hotel_name,customer_name):
    if reserve_room(hotel_name,customer_name):
        
        reservations.append([hotel_name, customer_name])
        print 'confirmed'
    else: 
        print 'sorry no rooms available '

# test 
add_new_reservation('rotana','ahmed')
add_new_reservation('rotana','omar')
add_new_reservation('blue','salma')

# end test

# FUNCTION TO display hiltons by city 
def list_hotels_in_city(city_name):
    hotels_list = []
    for i in hotels:
        if i[2] == city_name:
            hotels_list.append(i[1])
    print hotels_list


def list_resevrations_for_hotel(hotel_name):
    customer_list = []
    for i in reservations:
        if i[0] == hotel_name:
            customer_list.append(i[1])

    print customer_list

