========
 RTyper
========

実行順

- :py:meth:`build_graph_types <pypy.annotation.annrpython.RPythonTyper.build_graph_types` で flow graph に型情報を設定する。
- :py:meth:`getcallable <pypy.rpython.rtyper.RPythonTyper.getcallable>` で function object を生成する。


クラスメモ
==========

.. py:class:: pypy.rpython.rtyper.RPythonTyper(annotator, type_system="lltype")

  :param annotator: 型アノテータ
  :type annotator: :py:class:`RPythonAnnotator <pypy.annotation.annrpython.RPythonAnnotator>`
  :param str type_system: 型システム

  RTyper のインタフェイス?


  .. py:method:: getcallable(graph)

    :param graph: flow graph
    :type graph: :py:class:`FunctionGraph <pypy.objspace.flow.model.FunctionGraph>`

    flow graph から Function オブジェクトを生成する。
  

.. py:class:: pypy.annotation.annrpython.RPythonAnnotator(translator=None, policy=None, bookkeeper=None)

  :param translator: トランスレータ。詳細はこれから
  :type translator: :py:class:`TranslationContext <pypy.translator.translator.TranslationContext>`
  :param policy: ポリシ。詳細はこれから
  :type policy: :py:class:`AnnotatorPolicy <pypy.annotation.policy.AnnotatorPolicy>`
  :param bookkeeper: ブックキーパー
  :type bookkeeper: :py:class:`Bookkeeper <pypy.annotation.bookkeeper.Bookkeeper>`

  型アノテータなのでしょう。


  .. py:method:: build_graph_types(flowgraph, inputcells, complete_now=True)

    :param flowgraph: flow graph オブジェクト
    :type flowgraph: :py:class:`FunctionGraph <pypy.objspace.flow.model.FunctionGraph>`
    :param inputcells: 型リスト
    :type inputcells: [;py:class:`SomeObject <pypy.annotation.model.SomeObject>`]
    :return: 推論結果
    :rtype: ;py:class:`SomeObject <pypy.annotation.model.SomeObject>`
  
    flowgraph の関数に inputcells の型情報を渡して呼び出した結果の型を推論する。

    それと同時に flow graph に型情報を設定する。
    


.. py:class:: pypy.annotation.model.SomeObject()

  FunctionGraph に対して Annotation する際の基底型
  


.. py:class:: pypy.annotation.policy.AnnotatorPolicy


.. py:class:: pypy.annotation.bookkeeper.Bookkeeper
