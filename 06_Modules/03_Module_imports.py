# 1. Variant: import the whole module.
import wbsweiterbildung

wbsweiterbildung.weiterbildung_anmeldung()
wbsweiterbildung.weiterbildung_abbuchung()
print()
#########################################
# 2. Variant: import the whole module with alias (nickname)
import wbsweiterbildung as wbs

wbs.weiterbildung_anmeldung()
wbs.weiterbildung_abbuchung()
print()
##########################################
# 3. Variant: import specific function(s) --> we call the functions directly
from wbsweiterbildung import weiterbildung_anmeldung #  We can import one function
from wbsweiterbildung import weiterbildung_abbuchung, weiterbildung_Zertifikat # Several with comma

weiterbildung_anmeldung() # without module name
weiterbildung_Zertifikat()
print()
############################################
# 4. Variant: import specific function(s) with alias (nickname)
from wbsweiterbildung import weiterbildung_abbuchung as abb, weiterbildung_Zertifikat as zert

abb() # weiterbildung_abbuchung()
zert() # weiterbildung_zertifikat()
print()
#############################################
# 5. Variant: import all functions and call them directly
from wbsweiterbildung import * 

weiterbildung_Zertifikat()
weiterbildung_abbuchung()
weiterbildung_anmeldung()

