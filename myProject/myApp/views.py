from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Lop,HocVien,MonHoc,Diem,LichHoc
from .form import TimKiemForm,DanhSachLopForm,NhapDiemForm,SuaDiemForm


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
    return render (request, 'home.html')

def danhsach_view(request):
    content:None
    if request.method == 'POST':  
        form = DanhSachLopForm(request.POST)  
        if form.is_valid(): 
            ten_lop = form.cleaned_data.get('ten_lop')
            ma_lop_in =str(ten_lop).split(':')[0]
            content = HocVien.objects.filter(ma_lop = ma_lop_in)
        else: 
            form = DanhSachLopForm()
    else:
        form = DanhSachLopForm()
        content = HocVien.objects.filter(ma_lop = 'rgrtiuh6345u')
    return render(request,'danhsach.html', {'form': form, 'content':content})
def tracuu_view(request):
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
            ma_hv_in = str(ten_hoc_vien).split(':')[0]
            ma_mh_in = str(ten_mon_hoc).split(':')[0]
            ma_lop_in =str(ten_lop).split(':')[0]
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
    return render(request,'tracuu.html', {'form': form, 'content':content})
def suadiem_view(request):
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
            ma_hv_in = str(ten_hoc_vien).split(':')[0]
            ma_mh_in = str(ten_mon_hoc).split(':')[0]
            ma_lop_in =str(ten_lop).split(':')[0]
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
    return render(request,'suadiem.html', {'form': form, 'content':content})


def lichhoc_view(request):
    return render(request,'lichhoc.html')
def Suadiem_btn_view(request,id):
    diem = get_object_or_404(Diem, id=id)
    print(diem.ma_hv)
    if request.method == "POST":
        # Người dùng đã gửi form
        form = SuaDiemForm(request.POST, instance=diem)
        if form.is_valid():
            form.save()  # Lưu thông tin mới vào database
            return redirect("suadiem")  # Điều hướng về trang chính (cần thay tên URL)
    else:
        # Hiển thị form với giá trị hiện tại
        form = SuaDiemForm(instance=diem)
    return render(request, 'Suadiem_btn.html', {'diem': diem,'form': form,})
def Xoadiem_btn_view(request,id):
    diem = get_object_or_404(Diem, id=id)
    if request.method == "POST":
        diem.delete()
        messages.success(request, "Xóa điểm thành công!")
        return redirect("suadiem")  # Thay bằng tên trang chính của bạn
    return render(request,'Xoadiem_btn.html')

def Nhapdiem_view(request):
    if request.method == 'POST':
        form = NhapDiemForm(request.POST)
        if form.is_valid():
            # Lấy dữ liệu từ form
            ma_lop = form.cleaned_data['ten_lop']
            ma_hv = form.cleaned_data['ten_hoc_vien']
            ma_mh = form.cleaned_data['ten_mon_hoc']
            hoc_ki = form.cleaned_data['hoc_ki']
            diem = form.cleaned_data['diem']
            if Diem.objects.filter(
                ma_lop=ma_lop,
                ma_hv=ma_hv,
                ma_mh=ma_mh,
                hoc_ki=hoc_ki,
            ).exists():
                messages.error(request, "Thông tin nhập đã tồn tại trong hệ thống.")
            else:
            # Lưu thông tin điểm vào database
                Diem.objects.create(
                    ma_lop=ma_lop,
                    ma_hv=ma_hv,
                    ma_mh=ma_mh,
                    hoc_ki=hoc_ki,
                    diem=diem
                )
                messages.success(request, "Điểm đã được thêm thành công.")
                return redirect('Nhapdiem')  # Thay bằng URL phù hợp
    else:
        form = NhapDiemForm()
    return render(request,'nhapdiem.html', {'form': form})

def lich_hoc_list(request):
    lich_hoc = LichHoc.objects.all()  # Lấy tất cả dữ liệu từ bảng LichHoc
    context = {'lich_hoc': lich_hoc}
    return render(request, 'lich_hoc_list.html', context)