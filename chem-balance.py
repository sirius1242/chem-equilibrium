#!/usr/bin/env python3
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
rea_dim = len(rea_comp)
pro_dim = len(pro_comp)
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
init_dat = {}
data = input("please enter the data in the begining of reaction (for example: 'H2S: 1.5; H2SO4: 1', if no data input we will view it as 0 \n")
init_data = re.split('\ ?;\ ?', data)
if init_data == []:
    print('Error: please enter the initial data!')
    exit()
for i in init_data:
    comp, dat = re.split('\ ?:\ ?', i)
    init_dat[comp] = float(dat)
x = Symbol('x')
rea_int = []
pro_int = []
for i in rea_comp:
    if i in init_dat:
        rea_int.append(init_dat[i])
    else:
        rea_int.append(0)
for i in pro_comp:
    if i in init_dat:
        pro_int.append(init_dat[i])
    else:
        pro_int.append(0)
reaction = []
product = []
for i in range(len(rea_int)):
    reaction.append('('+str(rea_coeff[i])+'*x-'+str(rea_int[i])+')**'+str(rea_coeff[i]))
for i in range(len(pro_int)):
    product.append('('+str(pro_coeff[i])+'*x+'+str(pro_int[i])+')**'+str(pro_coeff[i]))
x_val = solve(eval('('+'*'.join(reaction)+')/('+'*'.join(product)+')-K'), x)
fin_dat = ['0']*(rea_dim + pro_dim)
for i in x_val:
    if 'I' not in str(i):
        #print("the delta of "+rea_comp[0]+" is: "+str(-rea_coeff[0]*i))
        for j in range(rea_dim):
            if rea_coeff[j] * -i + rea_int[j] < 0:
                break
            fin_dat[j] = rea_coeff[j] * -i + rea_int[j]
        if j < rea_dim - 1:
            continue
        for j in range(pro_dim):
            if pro_coeff[j] * i + pro_int[j] < 0:
                break
            fin_dat[j+rea_dim] = pro_coeff[j] * i + pro_int[j]
        if j < pro_dim - 1:
            continue
        for j in range(rea_dim + pro_dim):
            print((rea_comp + pro_comp)[j] + " : " + str(fin_dat[j]) + " ;")
