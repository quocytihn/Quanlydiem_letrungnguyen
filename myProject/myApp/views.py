from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Lop,HocVien,MonHoc,Diem
from .form import TimKiemForm


# decorator: kiểm tra xem user có phải là admin???
# view_func đại diện cho view sẽ được áp dùng
def admin_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            # Thêm Điều hướng đến trang thông báo lỗi!
            return HttpResponse('Bạn không phải là admin')
        return view_func(request, *args, **kwargs)
    return wrapped_view

#----------------------------------------------------------------------
# View login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không chính xác")
    return render(request, 'login.html')
# View cho logout
def logout_view(request):
    logout(request)
    return redirect('login')
#----------------------------------------------------------------------
# View cho manager 
# View cho danh sách đăng kí 
# View cho form nhật ký
#----------------------------------------------------------------------
# View cho trang home
#@login_required(login_url='login')

def home_view(request):
    
    if request.method == 'POST':  
        content:None
        form = TimKiemForm (request.POST)  
        if form.is_valid(): 
            # Bắt buộc phải nhập tên lớp
            ten_lop = form.cleaned_data.get('ten_lop') 
            ten_hoc_vien = form.cleaned_data.get('ten_hoc_vien') or None
            ten_mon_hoc = form.cleaned_data.get('ten_mon_hoc') 
            hoc_ki_in = form.cleaned_data.get('hoc_ki') 
            #kiểm tra xem học viên này có nằm trong lớp này hay không
            ma_hv_in = str(ten_hoc_vien).split('/')[0]
            ma_mh_in = str(ten_mon_hoc).split('/')[0]
            ma_lop_in =str(ten_lop).split('/')[0]
            Lop = HocVien.objects.filter(ma_lop = ma_lop_in)
            # Tìm kiếm
            if ten_hoc_vien is not None:
                if ten_hoc_vien in Lop:
                    content= Diem.objects.filter(ma_hv = ma_hv_in, ma_mh = ma_mh_in, ma_lop = ma_lop_in, hoc_ki=hoc_ki_in)
                else: 
                    content = Diem.objects.filter(ma_hv = 'gfhniui345h23')
            else:
                content = Diem.objects.filter(ma_mh = ma_mh_in, ma_lop = ma_lop_in, hoc_ki=hoc_ki_in)
        else: 
            form = TimKiemForm()
    else:
        form = TimKiemForm()
        content = Diem.objects.filter(ma_hv = 'ad41145v148051')

    return render (request, 'home.html', {'form': form, 'content':content})


