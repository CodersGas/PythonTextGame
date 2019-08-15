from mini_game_func import *

print("\n")
print("\t\t\t\t----------- WELCOME TO THE GAME ------------")

print("\n")

print("\n Caution :- Read about the main characters of the story thoroughly and then proceed.")

print("\n")

print(""" 1.) Good King Victor -: He is very good with his weapons and
                         has a very good knowledge of weapons. He has even defeated
                         one of the most skilled weaponmaster  and the king is capable
                         of one shotting everyone with any weapon.""")
print("\n")

print(""" 2.) Evil king Camio -:  A very evil minded creature and a great
                         trickster.He is a great escape artist and
                         is capable of escaping from even extreme situations.
                         He was also a good swordsman once and challenged king
                         Victor to fight him. And as a price, he(Camio) lost
                         his kingdom too. Now he seeks revenge and planned to
                         kidnap and make the daughter of king Victor hostage in her
                         own palace. Would King Victor be able to save his daughter?""")
print("\n")

print(""" 3.) Coral leo(Camio's Brother) -: A fool minded creature for whom
                                   nothing is much bigger than money. He can even betray
                                   his blood relations for money. Could he be of any help
                                   to us?""")

print("\n")

print("Let's start the GAME.")

print("""\n The King Victor has gone out to the neighbouring state to meet their king.
    He receives a letter and it read as follows : """)

letter = open("letter.txt")

print("\n")
print(letter.read())

print("\n")

print("""After reading this letter , king Victor at once left for his palace.""")

print("\n")

print("""After reaching his palace, king Victor saw that people of Camio were gaurding
   the main gate.""")

path = path_choices()

if "left" in path:
    left_path()
    exit(0)

elif "right" in path:
    right_path()
    exit(0)

elif "underground" in path:
    under_path()
    plan = plan_choices()

    if "rush" in plan:
        rush()

    elif "greed" in plan:
        greed_the_coral()
        camio_attacked()
else:
    print("\n No other path.")
    exit(0)

the_end()
