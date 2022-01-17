### Class Math

import math

class Math():

    def square_root(self, number):
        result = number**(1/2)
        return result

    def mean_liste(self, liste):
        result1 = sum(liste)/len(liste)
        return result1

    def paired(self, number):
        result2 = number%2
        if result2 == 0 :
            return (print(number,"est paire!"))
        else:
            return (print(number,"est impaire!"))

    def somme_liste(self,liste):
        result4 = sum(liste)
        return result4


    def somme_liste1(self, liste):
        r=0
        for v in liste:
            r+=v
        return r

mathfive= Math()

print(mathfive.square_root(9))

print(mathfive.mean_liste([10,30,20,10]))

mathfive.paired(5)

print(mathfive.somme_liste([10,30,10,40,20]))

print(mathfive.somme_liste1([10,30,10,40,20]))

#liste = [1,2,3,5]
#print(sum(liste)/len(liste))

### Imputer

class Imputer():
    def __init__(self, lista):
        self.lista = lista

    def avg(self):
        r = 0
        l = 0
        copy_liste1 = list(self.lista)


        for v in self.lista:
            if v != None:
                r+=v
                l+=1
        print(r)
        print(l)
        i = 0

        for v1 in copy_liste1:

            if v1 == None :
                m = r/l
                copy_liste1[i] = m
            i+=1

        print(copy_liste1)

        return copy_liste1

    def mediane(self):
        l = 0
        new_liste =[]
        copy_liste2 = list(self.lista)
        i = 0

        for v in self.lista:
            if v != None :
                l+=1
                new_liste.append(v)
        new_liste1 = sorted(new_liste)

        print(new_liste1)
        print(l)

        if l%2 == 0:
            r = l/2
        else:
            r = (l+1)/2


        mediane = new_liste1[int(r-1)]

        for v1 in copy_liste2:
            if v1 == None :
                copy_liste2[i] = mediane
            i+=1

        print(copy_liste2)
        return copy_liste2








my_liste =[None, 2, 4, 6, None]

liste1 = Imputer(my_liste)
liste1.avg()

my_liste2 = [None, 2, 3, 12, 5, 6, None]

liste2 = Imputer(my_liste2)

liste2.avg()

liste2.mediane()


print("J'ai modifié")

print("c'est cool!") 

