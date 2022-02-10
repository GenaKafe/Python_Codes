def greeting(first_name, last_name, plz = ""):
    print(f"Hello First Name: {first_name}, Last Name: {last_name}, PLZ {plz}")

# Callers

# Positional
greeting("Thomas", "Meier")
greeting("Meier", "Thomas")

# Keyword
greeting(last_name="Meier", first_name="Ingo", plz ="25412")
