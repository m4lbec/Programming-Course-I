'''
Find the length of the hypotenuse of a triangle given the measure of its legs
'''

def hipotenusa(cate1,cate2):
    
    hip=cate1**2+cate2**2

    return hip




cat1=float(input("Ingrese valor cateto 1:\n"))
cat2=float(input("Ingrese valor cateto 2:\n"))
hip=hipotenusa(cat1,cat2)
print(f"La hipotenusa es {hip}")