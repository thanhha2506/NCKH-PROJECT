import pandas as pd
import os

# Đường dẫn thư mục chứa các file CSV
folder_path = 'E:/Downloads/NCKH/DATA/date'

# Lấy danh sách các file CSV trong thư mục
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Tạo một danh sách để lưu các DataFrame
dataframes = []

# Đọc từng file CSV và thêm vào danh sách
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Nối tất cả các DataFrame thành một DataFrame duy nhất
merged_df = pd.concat(dataframes, ignore_index=True)

# Xuất DataFrame hợp nhất thành một file CSV mới
output_file = 'Date_scrap_final.csv'
merged_df.to_csv(output_file, index=False)

print(f"Đã nối xong và lưu vào file {output_file}")
