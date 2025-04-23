import os
import shutil

# 1. Đọc và hiển thị nội dung tệp image.data
print("Nội dung tệp image.data:")
with open('image.data', 'r') as file:
    content = file.read()
    print(content)

# 2. Đọc dữ liệu vào các biến n, m, k
with open('image.data', 'r') as file:
    # Đọc n, m từ dòng đầu tiên
    n, m = map(int, file.readline().split())

    # Đọc mảng k (n x m)
    k = []
    for _ in range(n):
        row = list(map(float, file.readline().split()))
        k.append(row)

# 3. Đếm số phần tử 0, thay thế bằng trung bình cột, ghi vào image2.txt
zero_count = 0
col_sums = [0] * m
col_counts = [0] * m

# Tính tổng và số phần tử không 0 của mỗi cột
for i in range(n):
    for j in range(m):
        if k[i][j] == 0:
            zero_count += 1
        else:
            col_sums[j] += k[i][j]
            col_counts[j] += 1

# Tính trung bình mỗi cột (loại trừ các phần tử 0)
col_avgs = [col_sums[j] / col_counts[j] if col_counts[j] > 0 else 0 for j in range(m)]

# Thay thế phần tử 0 bằng trung bình cột
for i in range(n):
    for j in range(m):
        if k[i][j] == 0:
            k[i][j] = col_avgs[j]

# Ghi dữ liệu sau khi thay thế vào image2.txt
with open('image2.txt', 'w') as file:
    file.write(f"{n} {m}\n")
    for i in range(n):
        file.write(" ".join(map(str, k[i])) + "\n")

print(f"Số phần tử 0 trong k: {zero_count}")

# 4. Tạo hai tệp: 100 dòng đầu tiên và các dòng còn lại
# Tệp 1: 100 dòng đầu tiên
with open('image_part1.txt', 'w') as file:
    n1 = min(100, n)  # Số dòng thực tế (nếu n < 100)
    m1 = m
    file.write(f"{n1} {m1}\n")
    for i in range(n1):
        file.write(" ".join(map(str, k[i])) + "\n")

# Tệp 2: Các dòng còn lại
with open('image_part2.txt', 'w') as file:
    n2 = max(0, n - 100)  # Số dòng còn lại
    m2 = m
    file.write(f"{n2} {m2}\n")
    for i in range(100, n):
        file.write(" ".join(map(str, k[i])) + "\n")

# 5. Tạo thư mục, copy image2.txt, xóa file gốc
# Tạo thư mục IMAGE_DIR
image_dir = 'IMAGE_DIR'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)
    print(f"Đã tạo thư mục {image_dir}")

# Copy image2.txt vào IMAGE_DIR
shutil.copy('image2.txt', os.path.join(image_dir, 'image2.txt'))
print(f"Đã copy image2.txt vào {image_dir}")

# Xóa file image.data gốc
if os.path.exists('image.data'):
    os.remove('image.data')
    print("Đã xóa file image.data")
else:
    print("File image.data không tồn tại!")