# import all function(s) and variable(s) locally
from wbsweiterbildung import *



weiterbildung_anmeldung()
print(first_name) # Thomas - value from the module but local variable

# changes the value of the variable which came from the module
first_name = "Sara" 

print(first_name) # Sara
print(last_name) # Meier
