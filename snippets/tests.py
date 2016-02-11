# coding=utf-8
from django.test import TestCase

# Create your tests here.


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# 根据我们使用的是 python 2 或是 python 3
# 这一import会自动引入 `StringIO.StringIO` 或 `io.BytesIO`
from rest_framework.compat import BytesIO

# Create your tests here.


class SnippetTestCase(TestCase):

    def setUp(self):
        self.snippet1 = Snippet(code='foo = "bar"\n')
        self.snippet1.save()

        self.snippet2 = Snippet(code='print "hello, world"\n')
        self.snippet2.save()

    def testSerializerSnippet(self):
        # 序列化其中一个实例:
        serializer = SnippetSerializer(self.snippet2)
        print serializer.data
        # {'pk': 2, 'title': u'', 'code': u'print "hello, world"\n', 'linenos': False, 'language':u'python', 'style': u'friendly'}

    def testRenderSnippet(self):
        # 序列化其中一个实例:
        serializer = SnippetSerializer(self.snippet2)
        print serializer.data
        # {'pk': 2, 'title': u'', 'code': u'print "hello, world"\n', 'linenos': False, 'language':u'python', 'style': u'friendly'}

        # 以上代码已将snippet实例转化为Python基本数据类型, 接下来我们完成序列化:
        content = JSONRenderer().render(serializer.data)
        print content
        # '{"pk": 2, "title": "", "code": "print \\"hello, world\\"\\n", "linenos": false,    "language": "python", "style": "friendly"}'

    def testCreateSnippet(self):
        # 序列化其中一个实例:
        serializer = SnippetSerializer(self.snippet2)
        print serializer.data
        # {'pk': 2, 'title': u'', 'code': u'print "hello, world"\n', 'linenos': False, 'language':u'python', 'style': u'friendly'}

        # 以上代码已将snippet实例转化为Python基本数据类型, 接下来我们完成序列化:
        content = JSONRenderer().render(serializer.data)
        print content
        # '{"pk": 2, "title": "", "code": "print \\"hello, world\\"\\n", "linenos": false,    "language": "python", "style": "friendly"}'

        # 反序列化也是类似的, 首先将stream转为python基本类型:
        stream = BytesIO(content)
        data = JSONParser().parse(stream)

        # 然后我们将它转化为snippet实例:
        serializer = SnippetSerializer(data=data)
        self.assertEqual(serializer.is_valid(), True)
        # True
        print serializer.object
        # <Snippet: Snippet object>

    def testSerializerAllSnippet(self):
        # 当我们输入参数many=True时, serializer还能序列化queryset:

        serializer = SnippetSerializer(Snippet.objects.all(), many=True)
        print serializer.data
    # [{'pk': 1, 'title': u'', 'code': u'foo = "bar"\n', 'linenos': False, 'language': u'python',
#     'style': u'friendly'}, {'pk': 2, 'title': u'', 'code': u'print "hello, world"\n', 'linenos': False,
#     'language': u'python', 'style': u'friendly'}]
