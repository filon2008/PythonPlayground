#!/usr/bin/python
# Filename: Twenty_Four.py

import sys

def calculate(operand, operator, orders):
    s_operand = []
    s_orders = list(orders)
    for i in range(0,4) : 
        s_operand.append(str(operand[i]))
    for i in range(0,3) : 
        formula = '(' + str(s_operand[s_orders[i]]) + operator[orders[i]] + str(s_operand[s_orders[i]+1]) + ')'
        s_operand.pop(s_orders[i]+1)
        s_operand.pop(s_orders[i])
        s_operand.insert(s_orders[i], formula)
        for j in range(i,3) : 
            if s_orders[j] > s_orders[i] : 
                s_orders[j] = s_orders[j] -1
    return s_operand[0], eval(s_operand[0])

input = input("Input number : ")
operands = input.split(' ')
if len(operands) != 4 :
    print("wrong number of operands")
operators = ('+', '-', '*', '/')
for i in range(0,4) :
    for j in range(0,4) :
        if j != i :
            for k in range(0,4) :
                if k != i and k != j:
                    for l in range(0,4) :
                        if l != i and l != j and l != k :
                            for m in operators :
                                for n in operators :
                                    for o in operators : 
                                        for p in range(0,3) : 
                                            for q in range(0,3) : 
                                                if q != p :
                                                    for r in range(0,3) : 
                                                        if r != p and r != q:
                                                            try :
                                                                re = calculate((operands[i], operands[j], operands[k], operands[l]),(m, n, o), (p,q,r))
                                                                if re[1] == 24:
                                                                    print(re[0], '=', 24)
#                                                                    sys.exit(0)
                                                            except :
                                                                pass
