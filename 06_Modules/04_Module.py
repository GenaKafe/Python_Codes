# import all function(s) and variable(s) locally
import wbsweiterbildung # GK every time we have to type the name of the module


wbsweiterbildung.weiterbildung_anmeldung()

print(wbsweiterbildung.first_name) # Thomas
print(wbsweiterbildung.last_name) # Meier

wbsweiterbildung.weiterbildung_Zertifikat()


print(wbsweiterbildung.first_name) # Thomas

first_name = "Sara"
last_name = "Möller"
print(first_name) # Sara
print(last_name) # Meier

print(wbsweiterbildung.last_name) # Meier

wbsweiterbildung.last_name = "Meier"

print(wbsweiterbildung.last_name) # Meier
 