so_gio_lam = float(input("Nhập số giờ làm."))
luong_gio = float(input("Nhập thù làm mỗi giờ làm tiêu chuẩn."))
gio_tieu_chuan  =44 
so_gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + so_gio_vuot_chuan *   luong_gio * 1.5
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")