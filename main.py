'''
Visszaszámlálás.

Egy rakéta indítása előtt több órával visszaszámlálást kezdenek és óránként egyet számolnak vissza a rakéta indításáig. 
A felhasználó határozza meg, hogy hány órás a visszaszámlálás. 
A visszaszámlálást minden órában egy órára felfüggeszthetik, ha valamilyen váratlan esemény – műszaki hiba, időjárási probléma – merül fel. 
Amikor a visszaszámlálás eléri a 0-t, a rakétát fellövik.

Írjon programot, amely a visszaszámlálás számait jeleníti meg a képernyőn! 
Természetesen nem kell a visszaszámlálás lépései között eltelni időnek – minden üzenet megjelenését azonnal követheti a következő. 
A visszaszámlálás minden lépésénél kérdezze meg a felhasználót, hogy az adott órában szükség volt-e a visszaszámlálás fölfüggesztésére! 
A visszaszámlálás megjelenítését követően a program írja ki, hogy a visszaszámlálás kezdetétől hány óra telt el – a visszaszámlálás eredetileg tervezett hosszát a felfüggesztésekkel megnövelve!
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Hány órás visszaszámlálást tervezünk? 5
Visszaszámlálás: 5
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 4
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 3
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 2
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 1
Fel kell függeszteni a visszaszámlálást (i/n)? n
A rakéta a visszaszámlálást követően ennyi órával indult: 5
-----
Hány órás visszaszámlálást tervezünk? 4
Visszaszámlálás: 4
Fel kell függeszteni a visszaszámlálást (i/n)? i
Visszaszámlálás: 3
Fel kell függeszteni a visszaszámlálást (i/n)? i
Visszaszámlálás: 2
Fel kell függeszteni a visszaszámlálást (i/n)? i
Visszaszámlálás: 1
Fel kell függeszteni a visszaszámlálást (i/n)? n
A rakéta a visszaszámlálást követően ennyi órával indult: 7
'''

'''visszaszamlalas = int(input("Hány órás visszaszámlálást tervezünk ?"))
i = visszaszamlalas

while i >= 1:
  kerdes = input("Fel kell függeszteni a visszaszámlálást (i/n)?")
  if kerdes == "n":
    print(f"visszaszamlalas {i}")
  elif kerdes == "i":
    print(f"visszaszamlalas {i}")
  i -=1
  if kerdes == 'i':
    visszaszamlalas +=1

print(f"A rakéta a visszaszámlálástkövetően ennyi órával indult: {vissza}")'''


vissza = int(input("Hány órás visszaszámlását tervezünk?"))
i = vissza
while i >= 1:
    kerdes = input("Fel kell függeszteni a visszaszámlálást (i/n) ?")
    if kerdes == 'n':
        print(f"Visszaszámlálás : {i}")
    elif kerdes == 'i':
        print(f"Visszaszámlálás:{i}")
    i -= 1
    if kerdes == 'i':
        vissza += 1
print(f"A rakéta a visszaszámlálástkövetően ennyi órával indult: {vissza}")