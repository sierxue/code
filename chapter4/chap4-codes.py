from sympy import (Symbol, symbols, factor, expand, pprint,
                   init_printing, sympify, solve)
from sympy.core.sympify import SympifyError
from sympy.plotting import plot as plts

x = Symbol('x')
x + x + 1
x.name
a = Symbol('x')
a.name

x, y, z = symbols('x, y, z')
s = x*y + x*y
s
res = s.subs({x: 1, y: 2})
res

expr = x**2 - y**2
factor(expr)
factors = factor(expr)

expand(factors)

pprint(expr)

expr = 1 + 2*x + 2*x**2
pprint(expr)


def print_series(n):
    # Initialize printing system with reverse order
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)


print_series(5)

expr = 'x**2 + 3*x + x**3 + 2*x'
try:
    expr = sympify(expr)
except SympifyError:
    print('Invalid input')
expr

# expr = 'x**2 + 3*x + x**3 + 2x'
# try:
#     expr = sympify(expr)
# except SympifyError:
#     print('Invalid input')
#
# expr


def product(expr1, expr2):
    prod = expand(expr1 * expr2)
    print(prod)


expr1 = x
expr2 = y
product(expr1, expr2)

x = Symbol('x')
expr_QE = x**2 + 5*x + 4
expr_QE2 = x**2 + x + 1
sol = solve(expr_QE, dict=True)
sol2 = solve(expr_QE2, dict=True)
print

print(sol)
print()
pprint(sol)
print()
pprint(sol2)

print('Solveing one variable in terms of others')

x, a, b, c = symbols('x, a, b, c')
expr_QE3 = a*x**2 + b*x + c
sol_QE3 = solve(expr_QE3, x, dict=True)
print(sol_QE3)
print()
pprint(sol_QE3)


print('Solveing a system of linear equation')

x, y = symbols('x, y')
expr_LE1 = 2*x + 3*y - 6
expr_LE2 = 3*x + 2*y - 12
sol_LE = solve((expr_LE1, expr_LE2), dict=True)
sol_LE2 = sol_LE[0]
# sol_LE3 = sol_LE[1] # ganx next: look up the manual
print()
print(sol_LE)
print(sol_LE2)
print()
# print(sol_LE3)
print()

print('Verify that the solution is correct')

v1 = expr_LE1.subs({x: sol_LE2[x], y: sol_LE2[y]})
print(v1)
v2 = expr_LE2.subs({x: sol_LE2[x], y: sol_LE2[y]})
print(v2)

if (v1 == 0) and (v2 == 0):
    print('The solution is verified')


print('Plotting using sympy')

expr_plts = 2*x + 3
expr_plts2 = 3*x + 1
plts(expr_plts)
plts(expr_plts, (x, -5, 5))
plts(expr_plts2, expr_plts, (x, -5, 5))
