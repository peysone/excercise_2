"""
Stwórz program, który pozwoli wczytać (z klawiatury) imię psa i jego datę urodzenia. Zapisz dane w postaci słownika.
"""
# while True:
#     doggo_name = {str(input("podaj imie psiurka: "))}
#     doggo_birthdate = {str(input("podaj date urodzenia psiurka: "))}
#     dict_of_doggos = [doggo_name, doggo_birthdate]
#     if doggo_name or doggo_birthdate == "q":
#         break
#
#
# print(100 * "-")
# print(dict_of_doggos)

dict_of_doggos = {}
for i in range(5):
    doggo_name = str(input("Podaj imię psiurka: "))
    doggo_birthdate = int(input("Podaj ile ma lat: "))

    dict_of_doggos[doggo_name] = doggo_birthdate

print(dict_of_doggos)