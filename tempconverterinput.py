# (Celsius * 9/5) + 32 = Farenheit
celcius= input("Enter a temperature in Degrees Celcius")
celcius = float(celcius)

def convert_F_C(celcius):
    farenheit = (celcius * 9/5) + 32
    message = str(celcius) + " degrees Celcius are " + str(farenheit) + " degrees Farenheit"
    return(print(message))

convert_F_C(celcius)
