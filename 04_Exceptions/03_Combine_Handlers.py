# Vesuchen: Risiko Code
try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    result = x / y

except (ValueError, ZeroDivisionError) as e: 
    print("[Errror: 1001]",e, "\n", "This is an error")

else:
    print(f" {x} / {y} = {result}")

finally:
    print("Aufwiedersehen")

print("Ende")