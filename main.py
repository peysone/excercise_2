"""
Stwórz program, który pozwoli wczytać (z klawiatury) imię psa i jego datę urodzenia. Zapisz dane w postaci słownika.
"""
while True:
    doggo_name = {str(input("podaj imie psiurka: "))}
    doggo_birthdate = {str(input("podaj date urodzenia psiurka: "))}
    if doggo_name or doggo_birthdate == "q":
       break

dict_of_doggos = [doggo_name, doggo_birthdate]
print(100 * "-")
print(dict_of_doggos)