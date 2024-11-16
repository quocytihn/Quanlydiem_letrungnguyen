from django.db import models
from django.contrib.auth.models import User
  

class Lop(models.Model):
    #Đảm bảo là không có hai lớp cùng 1 tên, theo logic thì có thể, còn trên db chưa ràng buộc!
    ma_lop = models.CharField(max_length=10, primary_key=True)  
    ten_lop = models.CharField(max_length=100)  
    id_user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.ma_lop}: {self.ten_lop}"
    
class HocVien(models.Model):
    ma_hv = models.CharField(max_length=10, primary_key=True)  
    name = models.CharField(max_length=100) 
    date = models.DateField()  
    ma_lop = models.ForeignKey(Lop, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ma_hv}: {self.name}"

class MonHoc(models.Model):
    ma_mh = models.CharField(max_length=10, primary_key=True)  
    ten_mh = models.CharField(max_length=100)  
    def __str__(self):
        return f"{self.ma_mh}: {self.ten_mh}"

HOC_KI_CHOICES = [
        (1, 'Học kỳ 1'),
        (2, 'Học kỳ 2'),
    ]

class Diem(models.Model):
    ma_hv = models.ForeignKey(HocVien, on_delete=models.CASCADE)  
    ma_mh = models.ForeignKey(MonHoc, on_delete=models.CASCADE) 
    ma_lop = models.ForeignKey(Lop, on_delete=models.CASCADE)
    hoc_ki = models.IntegerField(choices=HOC_KI_CHOICES)    
    diem = models.FloatField() 

    def __str__(self):
        return f"{self.hoc_ki}"





