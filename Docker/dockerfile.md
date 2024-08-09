Dockerfile là một tập tin cấu hình dùng để tạo Docker Images. Nó chứa các lệnh và chỉ dẫn để xây dựng image theo cách bạn muốn. Dockerfile cung cấp một phương pháp tự động hóa quá trình xây dựng image, giúp bạn duy trì môi trường phát triển và triển khai nhất quán.

## Cấu trúc cơ bản của dockerfile
Một Dockerfile thường bao gồm các lệnh sau:

1. FROM:

- Chỉ định image cơ sở để xây dựng image mới. Đây là bước đầu tiên và bắt buộc.
  
  `FROM python:3.9`
2. RUN:

- Chạy các lệnh trong image, chẳng hạn như cài đặt phần mềm hoặc thực thi các script.

  `RUN apt-get update && apt-get install -y \`
      
      `curl \`
      
      `vim`
3. COPY:

- Sao chép tệp tin hoặc thư mục từ máy chủ vào image.
  
  `COPY requirements.txt /app/requirements.txt`
4. ADD:
- Tương tự như COPY, nhưng có thêm khả năng giải nén các tệp nén và tải dữ liệu từ URL.
  
  `ADD myfile.tar.gz /app/`
5. WORKDIR:
- Đặt thư mục làm việc cho các lệnh tiếp theo.
  
  `WORKDIR /app`
6. CMD:
- Chỉ định lệnh mặc định để chạy khi container khởi động. Chỉ một CMD có hiệu lực, nếu có nhiều CMD, chỉ lệnh cuối cùng sẽ được sử dụng.
  
  `CMD ["python", "app.py"]`
7. ENTRYPOINT:
- Cung cấp một lệnh cố định để chạy khi container khởi động. Có thể kết hợp với CMD để bổ sung tham số cho lệnh.
  
  `ENTRYPOINT ["python"]`
8. EXPOSE:
- Khai báo các cổng mà container sẽ lắng nghe. Đây chỉ là thông tin để Docker, không thực sự mở cổng.
  
  `EXPOSE 80`
9. VOLUME:
- Định nghĩa một điểm gắn (mount point) để lưu trữ dữ liệu.
  
  `VOLUME /data`

10. ENV:

- Thiết lập biến môi trường trong container.
  
  `ENV APP_ENV=production`
11. USER:

- Chỉ định người dùng để chạy các lệnh tiếp theo trong Dockerfile.
  
  `USER myuser`

## Ví dụ dockerfile
Dưới đây là một ví dụ đơn giản về Dockerfile cho một ứng dụng Python Flask:

  ```# Sử dụng image cơ sở
FROM python:3.9-slim

#Thiết lập thư mục làm việc
WORKDIR /app

#Sao chép tệp cấu hình yêu cầu
COPY requirements.txt .

#Cài đặt các phụ thuộc
RUN pip install -r requirements.txt

# Sao chép mã nguồn vào image
COPY . .

# Mở cổng 5000
EXPOSE 5000

# Đặt lệnh mặc định để chạy ứng dụng
CMD ["python", "app.py"]
```

## Các Lệnh Xây Dựng Docker Image từ Dockerfile
- Xây dựng image từ dockerfile
  
  `docker build -t my_flask_app:latest`
- Xem danh sách các image
  
  `docker images`
- Chạy container từ image
  
  `docker run -d -p 5000:5000 my_flask_app:latest`
