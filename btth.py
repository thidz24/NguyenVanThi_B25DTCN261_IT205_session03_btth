from datetime import datetime
# Nhập dữ liệu
name_patient = input("Nhập tên bệnh nhân: ")
if name_patient == "" :
    print("Tên không hợp lệ!")
    exit()
year_birth = int(input("Nhập năm sinh: "))
if year_birth < 1900 and year_birth > datetime.now().year :
    print("Năm sinh không hợp lệ")
    exit()
number_day_desease = int(input("Nhập số ngày bị bệnh: "))
if number_day_desease < 0 :
    print("Số ngày không hợp lệ: ")
    exit()
body_temperature = float(input("Nhập nhiệt độ cơ thể(°C): "))
if body_temperature < 30 or body_temperature > 45 :
    print("Nhiệt độ cơ thể không hợp lệ!")
    exit()
price_exam = float(input("Nhập chi phí khám bệnh: "))
if price_exam < 0 :
    print("Chi phí khám không hợp lệ!")
    exit()

# Tính toán thông tin
calculate_age = datetime.now().year - year_birth
surcharge = price_exam * 0.1
total_price = price_exam + surcharge

# Phân loại tình trạng sức khỏe
if body_temperature > 38 and number_day_desease > 3:
    status = "Nguy hiểm"
elif body_temperature > 38:
    status = "Sốt cao"
elif body_temperature > 37.5:
    status = "Sốt nhẹ"
else:
    status = "Bình thường"

# Đánh giá mức độ ưu tiên (Nested If)
if status == "Nguy hiểm":
    if calculate_age > 60:
        priority_level = "Cấp cứu"
    else:
        priority_level = "Ưu tiên cao"
else:
    priority_level = "Bình thường"

# Đánh giá mức chi phí (Toán tử 3 ngôi)
cost_level = "Cao" if total_price > 500000 else "Thấp"

# In phiếu
print("--- KẾT QUẢ ---")
print("Tên: ",name_patient)
print("Tuổi: ",calculate_age)
print("Nhiệt độ: ",body_temperature)
print("Số ngày bệnh: ",number_day_desease)

print("Tình trạng: ",status)
print("Mức độ ưu tiên: ",priority_level)


print("Tổng chi phí: ",total_price)
print("Mức chi phí: ",cost_level)