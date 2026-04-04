def super_heros_keys(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(i)

def super_heros_values(**kwargs):
    for value in kwargs.values():
        print(value)

def super_heros(**kwargs):
    for key,value in kwargs.items():
        print(f"{key.capitalize()} : {value}")

super_heros_keys(name="shaktiman", power="all", enemy  ="Dr.jackall")
super_heros_values(name="superman",power="kindness",enemy  ="Lex Luthor")
super_heros(name="batman",power="planning  ",enemy  ="the Joker")