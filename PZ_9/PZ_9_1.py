voyage = {"Мексика", "Канада", "Израиль", "Италия", "США"}
reina = {"Англия", "Япония", "Канада", "ЮАР"}
raduga = {"США", "Испания", "Швеция", "Австралия"}

print("Исходные данные:")
print("Вояж:", voyage)
print("РейнаТур:", reina)
print("Радуга:", raduga)
print("-" * 50)

# 1. В каких турагентствах есть туры в Японию
japan_agencies = []
if "Япония" in voyage:
    japan_agencies.append("Вояж")
if "Япония" in reina:
    japan_agencies.append("РейнаТур")
if "Япония" in raduga:
    japan_agencies.append("Радуга")

# 2. В каких турагентствах НЕТ туров в ЮАР
no_uar = []
if "ЮАР" not in voyage:
    no_uar.append("Вояж")
if "ЮАР" not in reina:
    no_uar.append("РейнаТур")
if "ЮАР" not in raduga:
    no_uar.append("Радуга")

# 3. Полный список всех туров
all_tours = voyage | reina | raduga


print("1. Туры в Японию можно приобрести в:", japan_agencies)
print("2. Туры в ЮАР отсутствуют в:", no_uar)
print("3. Полный список всех туров:", all_tours)
