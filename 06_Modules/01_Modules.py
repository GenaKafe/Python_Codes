from greetings import *
# Caller = App = Consumer
print("Welcome in Restaurant Acasa")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("please choose your language:")
print("[1] DE")
print("[2] EN")
print("[3] SP")
print("[4] CN")
user_lang = int(input("> "))
print()


if user_lang == 1: # DE
    greeting_de()
elif user_lang == 2: # EN
    greeting_en()
elif user_lang == 3: # SP
    greeting_sp()
elif user_lang == 4: # CN Chinese
    greeting_cn()
else:
    print("The language is not available. We will continue in English.")
    greeting_en

'''
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
Now we can use the module we just created, by using the import statement.
The module can contain functions, as already described,
but also variables of all types (arrays, dictionaries, objects etc).

'''