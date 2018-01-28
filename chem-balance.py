from sympy import Symbol, solve
import re
balance={
        'CO2+H2=CO+H2O': 1.4,
        'CO+H2O=CO2+H2': 23.2,
        'N2+3H2=2NH3': 152
        }
n = re.compile(r'^\ ?\d+\ ?')
equation = input("please enter the chemical equation\n")
if equation in balance:
    K = balance[equation]
else:
    K = float(input('please enter the equilibrium constant:\n'))
rea, pro = equation.split('=')
rea_comp = rea.split('+')
pro_comp = pro.split('+')
rea_coeff = []
pro_coeff = []
for i in range(len(rea_comp)):
    if n.findall(rea_comp[i]) != []:
        rea_coeff.append(int(n.findall(rea_comp[i])[0]))
        rea_comp[i] = n.sub('', rea_comp[i])
    else:
        rea_coeff.append(1)
for i in range(len(pro_comp)):
    if n.findall(pro_comp[i]) != []:
        pro_coeff.append(int(n.findall(pro_comp[i])[0]))
        pro_comp[i] = n.sub('', pro_comp[i])
    else:
        pro_coeff.append(1)
print(rea_coeff)
print(rea_comp)
print(pro_coeff)
print(pro_comp)
