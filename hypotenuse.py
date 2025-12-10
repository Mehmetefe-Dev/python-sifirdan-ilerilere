# Project: Hypotenuse Calculator
# Author: Mehmet Efe Özdemir
# Description: Calculates the hypotenuse of a right-angled triangle.
import math
print(" dik bir üçgenin hipotenüsünü bulma programına hoş geldiniz")
x = float(input("Üçgenin dik kenarlarından birini giriniz giriniz: "))
y = float(input("Diğer kenarını giriniz: "))
print("hipotenüs uzunluğu",math.sqrt(x*x + y*y))
