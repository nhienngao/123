import os
import shutil

# Đường dẫn đến thư mục và file
source_file = 'DATA54.txt'  # File dữ liệu từ bài 5.3
bai44_dir = 'BAI44'
new_file = os.path.join(bai44_dir, 'Data.dat')

# 1. Tạo thư mục BAI44
if not os.path.exists(bai44_dir):
    os.makedirs(bai44_dir)
    print(f"Đã tạo thư mục {bai44_dir}")

# 2. Copy file DATA54.txt vào thư mục BAI44 và đổi tên thành Data.dat
if os.path.exists(source_file):
    shutil.copy(source_file, new_file)
    print(f"Đã copy và đổi tên file thành {new_file}")
else:
    print(f"File {source_file} không tồn tại!")

# 3. Xóa file Data.dat trong thư mục BAI44
if os.path.exists(new_file):
    os.remove(new_file)
    print(f"Đã xóa file {new_file}")
else:
    print(f"File {new_file} không tồn tại!")

# 4. Xóa thư mục BAI44
if os.path.exists(bai44_dir):
    shutil.rmtree(bai44_dir)
    print(f"Đã xóa thư mục {bai44_dir}")
else:
    print(f"Thư mục {bai44_dir} không tồn tại!")