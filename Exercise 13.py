'''
The user must think of one of the following characters: LIO MESSI, MAURICIO MACRI and MIRTHA LEGRAND. 
The program through some appropriate questions (age, sex, occupation, etc.) 
should show what character it is. Example: if he is a man and an athlete, he will have to say Lio Messi
'''
def lio(p):
    li=int(input("Es atleta?\n1-Si\n2-No\n"))
    l=int(input("Juega como 10 en la seleccion Argentina?\n1-Si\n2-No\n"))
    if li ==1 and l ==1:
        print(f"Como sus respuestas son {li} y {l}, su personaje es LIO MESSI")
    else:
        print(f"mmmm...Liar!")

def mauricio(p):
    ma=int(input("Se dedica a la politica?\n1-Si\n2-No\n"))
    m=int(input("Fue presidente de boca junior?\n1-Si\n2-No\n"))
    if ma == 1 and m ==1:
        print(f"Como sus respuestas son {ma} y {m}, su personaje es MAURICIO MACRI")
    else:
        print(f"mmm...Liar!")

def mirtha(p):
    mir=int(input("Es conductora de TV?\n1-Si\n2-No\n"))
    mi=int(input("Su nieta es JUANA VIALE?\n1-Si\n2-No\n"))
    if mir ==1 and mi ==1:
        print(f"Como sus respuestas son {mir} y {mi}, su personaje es MIRTHA LEGRAND")
    else:
        print(f"mmmm... Liar!")

pj=int(input("Ingrese personaje(number):\n1-Lio Messi\n2-Mauricio Macri\n3-Mirtha Legrand\n"))
if pj == 1:
    lio(pj)
elif pj ==2:
    mauricio(pj)
elif pj==3:
    mirtha(pj)