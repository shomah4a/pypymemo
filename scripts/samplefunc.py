#-*- coding:utf-8 -*-

from pypy.objspace.flow import model
from pypy.interpreter import baseobjspace

from pypy.rpython import rtyper
from pypy.annotation import annrpython

from pypy.annotation import model as rtmodel


# 引数
x = model.Variable('x')
y = model.Variable('y')

x.concretetype = rtmodel.SomeInteger()
y.concretetype = rtmodel.SomeInteger()

# 演算結果格納
tmpvar = model.Variable('tmp')

# 加算
add_op = model.SpaceOperation('add', [x, y], tmpvar)

# 返り値
retvar = model.Variable('ret')

# 演算するところ
block = model.Block([x, y])
block.operations = [add_op]

# 関数データ
func = model.FunctionGraph('add', block, retvar)

# 返り値ブロックへのリンク
link = model.Link([tmpvar], func.returnblock)
link.prevblock = block

# リンク貼る
block.exits = (link, )

print func
print block
print link
print add_op


# Annotator
an = annrpython.RPythonAnnotator()

# RTyper
rt = rtyper.RPythonTyper(an)

print rt.getcallable(func)._T

# flow graph に型情報設定
rettype = an.build_graph_types(func, [rtmodel.SomeInteger(), rtmodel.SomeInteger()])

# flow graph から関数? オブジェクトを取得
f = rt.getcallable(func)

