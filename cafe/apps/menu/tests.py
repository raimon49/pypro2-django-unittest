import unittest
from django.test import TestCase as DjangoTest

from menu.models import Tea
from menu.forms import TestSearchForm


row = lambda L: (dict(zip(L[0], x)) for x in L[1:])

class TeaManagerTest(DjangoTest):
    def setUp(self):
        datas = (
            ("name", "kind"),
            (u"ダージリン", "english"),
            (u"スリランカ", "english"),
            (u"ウーロン茶", "chinese"),
            (u"鉄観音茶", "chinese"),
            (u"プーアル茶", "chinese"),
            (u"静岡茶", "japanese"),
        )
        for data in row(datas):
            Tea.objects.create(price=100, **data)

    def test_count_each_kind(self):
        result = Tea.objects.count_each_kind()
        self.assertEqual(form.is_valid(), True, form.errors_as_text())
