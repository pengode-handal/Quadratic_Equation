import math
from sympy import symbols, abc, Eq, solve, init_printing, init_session
init_printing()
import sympy as sm
print(sm.latex('x**2'))
input('''
Quadratic Formula => ax*x + bx + c = 0; f(x) = Equality; ax + b = 0
Menyelesaikan Persamaan Biasa, Kuadrat, Mencari Himpunan akar
1. Mencari himpunan (Persamaan Kuadrat)
2. Mencari X; diket A,B,C (Persamaan Kuadrat)
3. Mencari X; (Persamaan Biasa)
4. Mencari Variabel Selain X, diket X (Persamaan)
5. Mencari Dua Variabel (Persamaan, Persamaan Kuadrat)
Note: jangan spasi, kuadrat= **2, kali=*, bagi=/, PASTIKAN SUDAH DIPINDAH RUAS DAN (= 0), Variabel Hanya (A,B,C,Y,X)''')
x, y, a, b, c = symbols('x y a b c')

simbol = (a, b, c, x, y)
pilih1 = input("""
1. Persamaan Biasa(SPLSV)
2. Persamaan Kuadrat
3. Persamaan Mencari 2 variabel
4. f(x) = Persamaan
Pilih: """)
kumpulan = []
def pk(eq: str):
    for i in range(len(simbol)):
        try: 
            print(solve(eq.replace(str(simbol[i]), '*'+str(simbol[i])), simbol, dict=True))
        except: pass

def equationroots(): 
    a = input('Nilai a: ')
    b = input('Nilai b: ')
    c = input('Nilai c: ')
    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 

    # checking condition for discriminant
    if dis > 0: 
        print(" real and different roots ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 

    elif dis == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 

    # when discriminant is less than 0
    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 


# If a is 0, then incorrect equation
# if a == 0: 
#         print("Input correct quadratic equation") 
# else:
#     equationroots(a, b, c)

if pilih1 == 1 or '1': 
    pk(input('Masukkan Persamaan Biasa (contoh: ax+b=0; ditulis 2x+8)\nroot@persamaan~: '))
# elif pilih1 == 2 or '2':
    