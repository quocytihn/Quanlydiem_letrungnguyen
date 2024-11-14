from django import forms
from .models import Lop,HocVien,MonHoc,Diem

HOC_KI_CHOICES = [
        (1, 'Học kỳ 1'),
        (2, 'Học kỳ 2'),
    ]

class TimKiemForm(forms.Form):
    ten_lop = forms.ModelChoiceField(
        queryset=Lop.objects.all(),
        label='Chọn tên lớp',
        empty_label='Chọn lớp',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    ten_hoc_vien = forms.ModelChoiceField(
        queryset= HocVien.objects.all(),
        label='Chọn tên học viên',
        empty_label='Chọn học viên',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    ten_mon_hoc = forms.ModelChoiceField(
        queryset= MonHoc.objects.all(),
        label='Chọn môn học',
        empty_label='Chọn môn học',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    hoc_ki = forms.ChoiceField(
        choices=HOC_KI_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Chọn học kỳ"
    )

class NhapDiemForm(forms.Form):
    pass