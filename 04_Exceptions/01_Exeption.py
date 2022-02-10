x = 0
# Versuchen: Risiko Code
try:
    x = int(input("Enter a number: ")) # 5

# Error
except Exception as e:    # e: shows the error message from interpreter
    print("This is an error.")
    print(e)

# Kein Fehler
else: 
    print(x)

# finally = in any case. Auf jeden Fall finally wird ausgeführt
finally: 
    print("Aufwiedersehen!")

