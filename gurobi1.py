# -*- coding: utf-8 -*-


from gurobipy import *                  #gurobipyモジュールからすべてをimport

model = Model("lo1")                    #モデルのオブジェクトmodelに名前lo1とつける。省略可

x1 = model.addVar(name="x1")　　　　　　#変数の定義。addVarメソッド(下限,上限,目的関数の係数,変数のタイプ,名前)
x2 = model.addVar(name="x2")
x3 = model.addVar(ub=30,name="x3")

model.update()                          #Gurobiにモデルが変更されたことを伝えるメソッド。制約追加前に必ず行う。

model.addConstr(2*x1 + x2 + x3 <=60)    #制約条件。Ver 4.6より前は異なる。
model.addConstr(x1 + 2*x2 + x3 <=60)

model.setObjective(15*x1 + 18*x2 + 30*x3, GRB.MAXIMIZE) #目的関数。最大化。

model.optimize()                        #最適化の実行。最適化の前にupdateは自動で行われる。

print "Opt. Value=", model. ObjVal      #目的関数値の出力

for v in model.getVars():               #最適解の出力。getVarsメソッドで変数オブジェクトのリストを呼び出す。
    print v. Varname, v.X　　　　　　   #その要素vに対し変数名の属性(VarName)や最適値の属性(X)を使って表示。
