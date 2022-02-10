temperature = 25
klima_status = "an"  # "aus"

if temperature >=30:
    if klima_status == "aus":
        print("Klima an machen.")
        klima_status = "an"
    else:
        print("Klima ist sowieso an.")
else:
    if klima_status == "an":
        print("Klima aus machen.")
        klima_status = "aus"

    else:
        print("Klima ist sowieso aus.")
        