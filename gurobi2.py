" -*- coding: utf-8 -*-


from gurobipy import *

model = Model("puzzle")

x = model.addVar(vtype="I")       #変数タイプ(vtype)として整数(integer)
y = model.addVar(vtype="I")
z = model.addVar(vtype="I")

model.update()

model.addConstr(x + y + z == 32)
model.addConstr(2*x + 4*y + 8*z == 80)

model.setObjective(y + z, GRB.MINIMIZE)

model.optimize()

print "Opt. Val.=", model.ObjVal
print "(x,y,z)=",x.X, y.X, z.X       #前例ではgetVarsメソッドで変数オブジェクトのリストを得たが、
                                     #ここでは直接変数オブジェクトx,y,zの最適値の属性Xを出力している。

