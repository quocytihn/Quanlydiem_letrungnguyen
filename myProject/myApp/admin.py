from django.contrib import admin
from .models import *


class LopAdmin(admin.ModelAdmin):
    list_display = ('ma_lop', 'ten_lop', 'id_user')  
    search_fields = ('ma_lop', 'ten_lop') 
    list_filter = ('id_user',)  

class HocVienAdmin(admin.ModelAdmin):
    list_display = ('ma_hv', 'name', 'date', 'ma_lop')  
    search_fields = ('ma_hv', 'name')  
    list_filter = ('ma_lop',)  

class MonHocAdmin(admin.ModelAdmin):
    list_display = ('ma_mh', 'ten_mh')  
    search_fields = ('ma_mh', 'ten_mh')  

class DiemAdmin(admin.ModelAdmin):
    list_display = ('ma_hv', 'ma_mh', 'hoc_ki', 'diem','ma_lop')  
    search_fields = ('ma_hv__name', 'ma_mh__ten_mh')  
    list_filter = ('hoc_ki', 'ma_hv', 'ma_mh')  

@admin.register(LichHoc)
class LichHocAdmin(admin.ModelAdmin):
    list_display = ('id', 'ma_lop', 'ma_mh', 'ngay_hoc', 'giang_duong')  # Các trường hiển thị trong bảng
    list_filter = ('ma_lop', 'ma_mh', 'ngay_hoc')  # Bộ lọc bên phải
    search_fields = ('ma_lop__ten_lop', 'ma_mh__ten_mh', 'giang_duong')  # Tìm kiếm
    ordering = ('ngay_hoc',)  # Sắp xếp theo ngày học
admin.site.register(Lop,LopAdmin)
admin.site.register(HocVien,HocVienAdmin)
admin.site.register(MonHoc,MonHocAdmin)
admin.site.register(Diem,DiemAdmin)

