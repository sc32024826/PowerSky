from django import forms
from django.core.exceptions import ValidationError


# 定义验证规则
class JoinForm(forms.Form):
    product_name = forms.CharField(
        label='产品',
        min_length=2,
        required=True,
    )

    area = forms.CharField(
        label='地区',
        min_length=2,
        required=True,
    )

    name = forms.CharField(
        label='姓名',
        min_length=2,
        required=True,
    )

    tel = forms.CharField(
        label='手机',
        min_length=11,
        max_length=11,
        required=True,
    )