====================
 translatorshell.py
====================

translatorshell.py を足がかりに読み進める。


FunctionGraph を作るところ
==========================

- :py:class:`Translation <pypy.translator.interactive.Translation>` に関数を渡す
- :py:meth:`TranslationContext.buildflowgraph <pypy.translator.translator.TranslationContext.buildflowgraph>` で生成してキャッシュ
- :py:meth:`FlowObjSpace.build_flow <pypy.objspace.flow.objspace.FlowObjSpace.build_flow>` でバイトコードから flow graph を作る?
- :py:meth:`PyCode._from_code <pypy.interpreter.pycode.PyCode._from_code>` でバイトコードからつくっているらしい


RTyper なところ
===============


クラスとかメモ
==============


.. py:class:: pypy.translator.interactive.Translation

  translatorshell.py で使われる対話変換用のクラス

  .. py:data:: context

      :py:class:`pypy.translator.translator.TranslationContext`



.. py:class:: pypy.translator.translator.TranslationContext

  文脈?

  .. py:method:: buildflowgraph(func, mute_dot=False)

    Python 関数 -> Flow Graph の変換を行う。

    変換する際は :py:class:`pypy.objspace.flow.objspace.FlowObjSpace` を使うらしい。
  
    で、変換したあと関数ごとに FlowGraph をキャッシュする。



.. py:class:: pypy.objspace.flow.objspace.FlowObjSpace

  NOT_RPYTHON

  inherit :py:class:`pypy.interpreter.baseobjspace.ObjSpace`

  名前空間なのかな?

  The flow objspace space is used to produce a flow graph by recording

  だそうです。

  .. py:method:: build_flow(func, constargs={})

    バイトコードから Flow Graph を作るっぽい。

    Python のバイトコードからの変換は :py:class:`pypy.interpreter.pycode.PyCode._from_code` がやっているような。

    :py:class:`pypy.objspace.flow.flowcontext.FlowExecutionContext` で組み立てている模様。



.. py:class:: pypy.interpreter.pycode.PyCode

  .. py:classmethod:: _from_code(space, code, hidden_applevel=False, code_hook=None)

    CPython のバイトコードから PyCode クラスのインスタンスを作る


.. py:class:: pypy.objspace.flow.flowcontext.FlowExecutionContext









