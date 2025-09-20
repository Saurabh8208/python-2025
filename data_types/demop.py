# Data types

# Numeric types

#int
data = 10 
print(data)
print(type(data))

# float
data = 10.4
print(data)
print(type(data))

# complex
data = 3 + 4j 
print(data)
print(type(data))

# boolean
data = True
print(data)
print(type(data))

# List 
data =[10,20,30,40,50]
print(data)
print(type(data))




# Tupul
data =(10,20,30,40,50)
data = (101,"saurabh","data science")
data = (101,"saurabh",True)  # we can write combine of (float,string,bool) also
print(data)
print(type(data))

# set
data ={10,20,30,40,50}
print(data)
print(type(data))


# dictionary
data_a = {"name":"saurabh","id":101,"course":"data science","location":"hyd"}
print(data)
print(type(data))

# ex. of dict
data_b = {"name":"Nikhil","id":102,"course":"data analytics","loc":"hyd"}
print(data)
print(id(data))

print(id(data_a))
print(id(data_b))
print(type(data_a))
print(type(data_b))

# None type
x = None
print(type(x))


# User defined data types

class student:
    
    pass
student_john = student()
print(type(student_john)) #  '__main__.student' __main__ indicates user defined data type


# type conversion (it automaticaly contain float value by python)
a = 10
print(type(a))
b = 3.5
print(type(b))
c = a + b 
print(type(c))

# Type casting
pi = 3.14 
print(type(pi))
print(pi)


pi_round_int = int(pi)
print(type(pi_round_int))
print(pi_round_int)

# Ex.1 

value = 2.13
print(type(value))
print(value)

# ex.1 of round of  value
value_round_int = int(value)
print(type(value_round_int))
print(value_round_int)

# ex.2
rate = 5.18
print(type(rate))
print(rate)

# ex2. round of rate
value_round = int(rate)
print(type(value_round))
print(value_round)

# ex.3
rating = "5"
print(type(rating))
print(rating)



rating_round = float(rating)
print(type(rating_round)) # string to float
print(rating_round)


rating_round = int(rating)
print(type(rating_round))
print(rating_round)


rating = "5"
print(type(rating))
print(rating)

# It is increasing a value like this
increament_rating = int(rating) + 5
print(increament_rating)
print(type(increament_rating))

increament_rating = float(rating) * 5
print(increament_rating)
print(type(increament_rating))

