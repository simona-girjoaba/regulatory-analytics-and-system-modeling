# Beispiel 1 : Einen Ausdruck in Python lösen
#value_1=2*(3+2)**2/5-4
#print(value_1)

# Beispiel 2 : Mit Klammern für Klarheit sorgen
#value_2=2*((3+2)**2/5)-4
#print(value_2)

# Bespiel 3: Eine variable in Python, die dann multipliziert wird
#x = int(input("Bitte eine Zahl eingeben\n"))
#product = 3 * x
#print(product)

# Bespiel 4: Grieschische Variablennamen in Python
#beta = 1.75
#theta = 30.0 

# Beispiel 5: Indizierte Variablen in Python ausdrücken

#x_1 = 3
#x_2 = 10
#x_3 = 33

# Beispiel 6: Eine lineare Funktion in Python deklarieren

#def f(x):
#    return 2* x + 1

#x_values = [0,1,2,3]

#for x in x_values:
#    y =f(x)
#    print(y)

# Beispiel 7 : Eine lineare Funktion in Python mithilfe von Sympy als Graph darstellen
#from sympy import *
#x = symbols('x') 
#f = 2 * x + 1
#plot(f)

# Beispiel 8 : Diagrammdarstellung einer Potenzfunktion
#from sympy import *
#x = symbols('x')
#f = x**2 + 1
#plot(f)

# Beispiel 9 : Eine Funktion mit zwei unabhängigen Variablen in Python deklarieren
#from sympy import *
#from sympy.plotting import plot3d
#x, y = symbols('x y')
#f = 2*x+3*y
#plot3d(f)

# Beispiel 10 : Eine Summation in Python ausführen

#summation = sum(2*i for i in range(1,6))
#print(summation)

# Beispiel 11 : Summation von Elementen in Python

#x =[1,4,6,2]
#n = len(x)

#summation = sum(10*x[i] for i in range(0,n))
#print(summation)

# Beispiel 12 : Die Funktion log in Python verwenden 

# from math import log
# 2 erhoben zu welcher Potenz liefert mir 8
# x = log(8,2)
# print(x) 

# Beispiel 13: Zinseszinsberechnung in Python
# p = 100
# r =.20
# t = 2.0
# n = 12
# a = p *(1+(r/n))**(n*t)
# print(a)

# Beispiel 14 : Den kontinuierlichen Zins berechnen

from math import exp
p = 100
r = .20
t = 2.0
a = p * exp(r*t)
print(a)
