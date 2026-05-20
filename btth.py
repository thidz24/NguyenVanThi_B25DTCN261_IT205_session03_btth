# Tạo biến thoát vòng lặp while
break_while = ""
# Tạo vòng lặp while
while not break_while == "n":
    # Nhập số lượng nhân viên
    quantity_staff = int(input("Nhập số lượng nhân viên: "))
    if quantity_staff < 0:
        print("Số lượng không hợp lệ!")
    else:
        for i in range (1, quantity_staff + 1):
            print("Nhân viên ",i)
            # Nhập thông tin nhân viên
            name_staff = input("Nhập tên nhân viên: ")
            number_working = int(input("Nhập số ngày đi làm: "))
            # Đánh giá chuyên cần 
            if number_working < 20:
                evaluate_diligence = "Cần cải thiện chuyên cần"
            else:
                evaluate_diligence = "Nhân viên chuyên cần tốt"
            # Hiển thị thông tin nhân viên
            print(f"""
                  Tên: {name_staff}
                  Số ngày đi làm: {number_working}
                  {evaluate_diligence}""")
            # Tiếp tục hoặc kết thúc chương trình
        break_while = input("Tiếp tục chương trình? (y/n): ")
print("Kết thúc chương trình")
