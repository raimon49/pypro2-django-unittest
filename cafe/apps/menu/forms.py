# -*- coding: utf-8 -*-

from django import forms

from menu.models import Tea, TEA_KINDS


class TeaSearchForm(forms.Form):
    name = forms.CharField(label=u"", max_length=255, required=False)
    kind = forms.MultipleChoiceField(
                label=u"種類", choices=TEA_KINDS, required=False)
    extra_report = forms.BooleanField(
                label=u"追加レポートも出力する", required=False)

    def clean(self):
        clnd = self.cleaned_data
        if not self.is_valid():
            return clnd

        if not clnd["name"] and not clnd["kind"]:
            raise froms.ValidationError(
                    u"名称と種類のどちらかは入力してください。")

        return clnd
