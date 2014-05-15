# -*- encoding: utf-8 -*-

from gurobipy import *

I,d = multidict({1:80, 2:270, 3:250, 4:160, 5:180})  #demand_i 顧客iの需要量d_i
J,M = multidict({1:500, 2:500, 3:500})               #supply_j 工場jの容量M_j

#multidict関数は辞書を引数として入力すると、第一の返値としてキーのリスト、二番目以降の返値として辞書を返す。


c = {(1,1):4, (1,2):6, (1,3):9,                      #輸送費用c_ij (顧客と工場)
     (2,1):5, (2,2):4, (2,3):7,                      #添え字のタプルをキー、費用を値とした辞書cで表現
     (3,1):6, (3,2):3, (3,3):4,
     (4,1):8, (4,2):5, (4,3):3,
     (5,1):10,(5,2):8, (5,3):4}

model = Model("transportation")
x={}                                                 #空の辞書xを作成
for i in I:                                          #すべての顧客i
    for j in J:                                      #すべての工場j
        x[i,j] = model.addVar(vtype="C", name="x(%s, %s)" % (i,j))   #空の辞書xに変数オブジェクトを保管していく 


                                                     #変数にx(i,j)と名前つけている
                                                     # %s は文字列(string型)に変換して代入

model.update()

for i in I:
    model.addConstr(quicksum(x[i,j] for j in J) == d[i], name="Demand(%s)" %i)

#制約にDemand(i)と名前つけている
#quicksum(x[i,j] for j in Jによって変数オブジェクトx[i,j]をJ内の要素jに対して合計した線形表現を計算)

for j in J:
    model.addConstr(quicksum(x[i,j] for i in I) <= M[j], name="Capacity(%s)" % j)

model.setObjective(quicksum(c[i,j]*x[i,j] for (i,j) in x), GRB.MINIMIZE)

model.optimize()

print "Optimal Value:", model.ObjVal
EPS = 1.e-6
for (i,j) in x:
    if x[i,j] .X > EPS:                              # 0でない変数だけ出力する
        print "sending quantity %10s from factory %3s to customer %3s" % (x[i,j].X, j, i)

# %10s は10桁の文字数に、 %3sは3桁の文字列に変換して代入することを意味する
