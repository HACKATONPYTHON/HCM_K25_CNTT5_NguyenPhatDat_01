
# Danh sách nhân viên
list_employees =[
    {
        "id": "NV001",
        "full_name": "Nguyen Van A",
        "salary": 400000,
        "working_day": 25,
        # Tiền phụ cấp
        "allowance": 1500000,
        "total_salary": 930,
        # Phân loại thu nhập
        "income_classification": "Khá"
    }
    
]
def display_list_employees():
    # Trước khi hiển thị tiến hành chạy ngầm cập nhật phân loại thu nhập
    auto_classify()
    header = f"{"Mã nhân viên":<20} | {"Họ tên nhân viên":<20} | {"Lương ngày cơ bản":<20} | {"Số ngày công làm việc":<25} | {"Tiền phụ cấp":<20} | {"Tổng thu nhập":<20} | {"Phân loại thu nhập":<20} |"
    print("-- DANH SÁCH NHÂN VIÊN --".center(len(header)," "))
    print(header)
    if list_employees:
        for employee in list_employees:
            body = f"{employee['id']:<20} | {employee['full_name']:<20} | {employee['salary']:<20} | {employee['working_day']:<25} | {employee['allowance']:<20} | {employee['total_salary']:<20} | {employee['income_classification']:<20} |"
            print(body)
    else:
        print("-- DANH SÁCH ĐANG TRỐNG --".center(len(header)," "))
        
def add_employee():
    id = input("Nhập mã NV: ")      
    
    # Kiểm tra trống id
    if not id.strip():
        print("ID không được để trống, vui lòng thử lại")
        return
    
    # kiểm tra id trùng lặp
    for employee in list_employees:
        if id.lower() == str(employee['id']).lower():
            print("ID đã tồn tại!!, vui lòng thử lại")
            return
    full_name = input("Họ tên NV: ")
    if not full_name.strip():
        print("Họ và tên nhân viên không được để trống!!")
        return
    
    salary = int(input("Lương ngày: "))
    allowance = int(input("Phụ cấp: "))
    
    # kiểm tra lương ngày cơ bản và phụ cấp
    if salary < 0 or allowance < 0:
        print("Lương ngày cơ bản và tiền phụ cấp phải là số >= 0!!")
        return
    try:
        working_day = input("Số ngày công: ")
        
        # Kiểm tra là FLOAT
        working_day = float(working_day)
        # Kiểm tra là INT
        working_day = int(working_day)

        if working_day < 0 or working_day > 31:
            print("Số ngày công phải từ 0 đến 31 ngày!!")
            return
    except:
        print("Số ngày công nhập vào không hợp lệ!!")
        return
        
    
    total_salary = (salary * working_day) + allowance
    
    new_employee = {
        "id": id,
        "full_name": full_name,
        "salary": salary,
        "working_day": working_day,
        # Tiền phụ cấp
        "allowance": allowance,
        "total_salary": total_salary,
        # Phân loại thu nhập
        "income_classification": ""
    }
    
    list_employees.append(new_employee)
    # Cập nhật tự động phân loại thu nhập
    auto_classify()
    print("Đã thêm mới nhân viên thành công!!!")

def update_employee():
    id = input("Nhập mã nhân viên cần cập nhật: ")
    for index,employee in enumerate(list_employees):
        if employee['id'] == id:
            salary = int(input("Lương ngày: "))
            allowance = int(input("Phụ cấp: "))
            
            # kiểm tra lương ngày cơ bản và phụ cấp
            if salary < 0 or allowance < 0:
                print("Lương ngày cơ bản và tiền phụ cấp phải là số >= 0!!")
                return
            try:
                working_day = input("Số ngày công: ")
                
                # Kiểm tra là FLOAT
                working_day = float(working_day)
                # Kiểm tra là INT
                working_day = int(working_day)

                if working_day < 0 or working_day > 31:
                    print("Số ngày công phải từ 0 đến 31 ngày!!")
                    return
            except:
                print("Số ngày công nhập vào không hợp lệ!!")
                return
            
            total_salary = (salary * working_day) + allowance
            
            list_employees[index].update({'salary':salary,'working_day':working_day,'allowance':allowance,'total_salary':total_salary})
            # Cập nhật tự động phân loại thu nhập
            auto_classify()
            print("Cập nhật thành công")
            break
    else:
        print("Không tìm thấy mã NV, Hãy thử lại!!!")    
    
def delete_employee():
    id = input("Nhập mã NV: ")
    for employee in list_employees:
        if employee['id'] == id:
            check_sure = input("Bạn có chắc muốn xóa nhân viên này không?(Y/N: ")
            if check_sure.lower() == "y":
                list_employees.remove(employee)
                print("Đã xóa nhân viên thành công!!")
                break
            elif check_sure.lower() == "n":
                print("Đã hủy thao tác xóa nhân viên!!")
                break
            else:
                print("Lỗi cú pháp, kí tự phải là Y/N")
    else:
        print("Mã nhân viên không tồn tại, vui lòng thử lại!!1")

def find_employee():
    list_find_employee = ""
    find_input = input("Nhập và mã nhân viên hoặc tên nhân viên: ")
    for employee in list_employees:
        if str(employee['id']).lower() == find_input.lower() or find_input.lower() in str(employee['full_name']).lower():

            
            body = f"{employee['id']:<20} | {employee['full_name']:<20} | {employee['salary']:<20} | {employee['working_day']:<25} | {employee['allowance']:<20} | {employee['total_salary']:<20} | {employee['income_classification']:<20} |"
            list_find_employee += body
    if list_find_employee:
        print("--- NHÂN VIÊN HỢP LỆ ---".center(len(list_find_employee)," "))
        print(list_find_employee)
    else:
        print("Mã nhân viên không tồn tại!!!")


def personnel_statistics():
    
    # Nhóm nhân viên kiểu "Cao"
    type_1 = 0
    # Nhóm nhân viên kiểu "Khá"
    type_2 = 0
    # Nhóm nhân viên kiểu "Trung bình"
    type_3 = 0
    # Nhóm nhân viên kiểu "Thấp"
    type_4 = 0
    
    for employee in list_employees:
        if employee['income_classification'] == "Cao":
            type_1 += 1
        elif employee['income_classification'] == "Khá":
            type_2 += 1
        elif employee['income_classification'] == "Trung bình":
            type_3 += 1
        else:
            type_4 += 1
    
    print("-- DANH SÁCH THỐNG KÊ --")
    print(f"Nhân viên[Cao]: {type_1}")
    print(f"Nhân viên[Khá]: {type_2}")
    print(f"Nhân viên[Trung bình]: {type_3}")
    print(f"Nhân viên[Thấp]: {type_4}")

def auto_classify():
    for index,employee in enumerate(list_employees):
        total_salary = employee['total_salary']
        if total_salary < 9000000:
            income_classification = "Thấp"
        elif total_salary < 15000000:
            income_classification = "Trung bình"
        elif total_salary < 30000000:
            income_classification = "Khá"
        else:
            income_classification = "Cao"
            
        list_employees[index].update({'income_classification':income_classification})
    
while True:
    print("="*50)
    print("--- CHƯƠNG TRÌNH QUẢN LÝ NHÂN SỰ ---".center(50," "))
    print("="*50)
    print("1. Hiển thị danh sách nhân viên")
    print("2. Tiếp nhận nhân viên mới")
    print("3. Cập nhật thông tin và ngày công")
    print("4. Xóa nhân viên")
    print("5. Tìm kiếm nhân viên")
    print("6. Thống kê quỹ lương và nhân sự")
    print("7. Phân loại thu nhập tự động")
    print("8. Thoát chương trình")
    
    user_choice = input("Nhập vào lựa chọn của bạn: (1 - 8): ")
    match user_choice:
        case "1":
            display_list_employees()
        case "2":
            add_employee()
        case "3":
            update_employee()
        case "4":
            delete_employee()
        case "5":
            find_employee()
        case "6":
            personnel_statistics()
        case "7":
            auto_classify()
            print("Đã thực hiện tự động cập nhật phân loại thu nhập!!")
        case "8":
            print("Thoát chương trình thành công!!")
            break
        case _:
            print("Lỗi cú pháp, vui lòng thử lại!!!")
            
