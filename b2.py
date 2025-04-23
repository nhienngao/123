# Phần 1: Tạo tệp matrix.txt nếu chưa có (tương tự bài 5.1)
def create_matrix_file():
    # Nhập kích thước ma trận
    n = int(input("Nhập số hàng n: "))
    m = int(input("Nhập số cột m: "))

    # Khởi tạo ma trận
    a = []
    print("Nhập các phần tử của ma trận:")
    for i in range(n):
        row = []
        for j in range(m):
            value = float(input(f"Nhập a[{i}][{j}]: "))
            row.append(value)
        a.append(row)

    # Xuất ma trận ra tệp văn bản
    with open('matrix.txt', 'w') as f:
        f.write(f"{n} {m}\n")
        for row in a:
            row_str = ' '.join(str(x) for x in row)
            f.write(f"{row_str}\n")
    print("Tệp matrix.txt đã được tạo.")



def read_matrix_file():
    try:
        print("\nToàn bộ nội dung tệp matrix.txt:")
        with open('matrix.txt', 'r') as f:
            content = f.read()
            print(content, end='')


        print("\nĐọc vào biến n, m, a:")
        with open('matrix.txt', 'r') as f:
            # Đọc dòng đầu tiên để lấy n, m
            n, m = map(int, f.readline().split())


            a = []
            for _ in range(n):
                row = list(map(float, f.readline().split()))
                a.append(row)

           
            print(f"n = {n}")
            print(f"m = {m}")
            print("Ma trận a:")
            for row in a:
                print(' '.join(str(x) for x in row))

    except FileNotFoundError:
        print("Không tìm thấy tệp matrix.txt. V please chạy phần tạo tệp trước.")
    except Exception as e:
        print(f"Lỗi khi đọc tệp: {e}")



print("Bạn muốn tạo tệp matrix.txt mới? (y/n): ")
if input().lower() == 'y':
    create_matrix_file()

read_matrix_file()