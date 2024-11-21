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
    ten_lop = forms.ModelChoiceField(
        queryset=Lop.objects.all(),
        label='Chọn tên lớp',
        empty_label='Chọn lớp',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    ten_hoc_vien = forms.ModelChoiceField(
        queryset=HocVien.objects.all(),
        label='Chọn tên học viên',
        empty_label='Chọn học viên',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    ten_mon_hoc = forms.ModelChoiceField(
        queryset=MonHoc.objects.all(),
        label='Chọn môn học',
        empty_label='Chọn môn học',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    hoc_ki = forms.ChoiceField(
        choices=HOC_KI_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Chọn học kỳ"
    )
    diem = forms.FloatField(
        required=True,
        min_value=1,  # Giá trị nhỏ nhất
        max_value=10,  # Giá trị lớn nhất
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Nhập điểm từ 1 đến 10'
        }),
        label="Điểm"
    )


class DanhSachLopForm(forms.Form):
    ten_lop = forms.ModelChoiceField(
        queryset=Lop.objects.all(),
        label='Chọn tên lớp',
        empty_label='Chọn lớp',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

class SuaDiemForm(forms.ModelForm):
    class Meta:
        model = Diem
        fields = ["diem"]  # Chỉ hiển thị trường 'diem' để chỉnh sửa
        widgets = {
            "diem": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 10}),
        }
        labels = {
            "diem": "Điểm",
        }