=================
 Flow Graph メモ
=================

translatorshell.py で色々内部を見てみた結果のメモ。

.. blockdiag:: /_static/functiongraph.diag

pypy.objspace.flow.model
========================

.. py:currentmodule:: pypy.objspace.flow.model

.. py:class:: FunctionGraph(self, name, startblock, return_var=None)

  :param str name: 関数名?
  :param startblock: 開始ブロック
  :type startblock: :py:class:`Block`
  :param return_var: 返り値
  :type return_var: :py:class:`Variable` or :py:class:`Constant`

  :member: - name - 名前
           - returnblock (:py:class:`Block`) - 返り値を取ってくるブロック

  これが最小単位?


.. py:class:: Block(inputargs)

  :param inputargs: ブロックが受け取る引数リスト
  :type inputargs: [:py:class:`Variable`]

  :member: - isstartblock - :py:class:`FunctionGraph` の開始ブロックなら True
           - inputargs - 引数と同じ
           - operations - :py:class:`SpaceOperation` のリスト。初期値は空リスト
           - exitswitch - :py:class:`Variable` か :py:class:`Constant` (last_exception)
           - exits - :py:class:`Link` のリスト。 exitswitch を評価した結果と exits のそれぞれの要素の exitcase を比較して一致したらその Link に飛ぶ

  プログラムの制御に用いる最小単位?
  
  一連のオペレーションと分岐が定義される。


.. py:class:: Link(args, target, exitcase=None)

  :param args: 次のブロックに渡す引数リスト
  :type args: [:py:class:`Variable` or :py:class:`Constant`]
  :param target: 次のブロック
  :type target: :py:class:`Block`
  :param exitcase: 分岐条件。卽値っぽい
  :type exitcase: :py:class:`object`

  :member: - prevblock - 前のブロック
           - last_exception - exitcase と同じ? 違う?
           - last_exc_value (:py:class:`Variable`) - 例外が入っている変数名

  ブロックと次のブロックをつなぐもの。

  分岐条件などが定義されている。


.. py:class:: Variable(name=None)

  :param str name: 変数名
  :member: - concretetype (:py:class:`SomeObject <pypy.annotation.model.SomeObject>`) - 型情報 推論の結果設定されたりする

  変数


.. py:class:: Constant(value, concretetype=None)

  :param value: 値
  :param concretetype: 型情報
  :type concretetype: :py:class:`SomeObject <pypy.annotation.model.SomeObject>`

  定数


.. py:class:: SpaceOperation(opname, args, result, offset=-1)

  :param str opname: 演算名
  :param args: 引数名
  :type args: [:py:class:`Variable` or :py:class:`Constant`]
  :param result: 返り値を保存する先
  :type result: :py:class:`Variable`
  :param int offset: ソースコード上のオフセット? 何用?

  演算一個分

  演算名は :py:data:`pypy.interpreter.baseobjspace.ObjSpace.MethodTable` にあるらしい。



作ってみる
==========

引数を2つ取って加算して返す関数を定義してみる。

これでいいのかな?

.. literalinclude:: ../scripts/samplefunc.py



