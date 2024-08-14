Container là một phần quan trọng trong Docker, giúp bạn triển khai và quản lý ứng dụng và dịch vụ một cách linh hoạt và nhất quán. Dưới đây là các khái niệm cơ bản về container và cách quản lý chúng:

## Các khái niệm cơ bản
1. Container
- Là một môi trường nhẹ và tách biệt cho ứng dụng và các phụ thuộc của nó.
- Chạy trên một hệ điều hành chung của Docker Engine mà không cần phải cài đặt hệ điều hành riêng biệt cho mỗi container.
- Chia sẻ hệ điều hành với các container khác nhưng cung cấp môi trường độc lập cho mỗi ứng dụng.
2. Docker Image:
- Là một bản sao không thay đổi của container, bao gồm mã nguồn, thư viện, và cấu hình cần thiết để chạy ứng dụng.
- Các container được tạo từ Docker Image.
3. Dockerfile:
- Là một tập tin cấu hình dùng để tạo Docker Image.
- Định nghĩa các bước để xây dựng hình ảnh, chẳng hạn như cài đặt phần mềm và cấu hình môi trường.

## Các lệnh quản lý container
- Liệt kê số lượng container đang chạy trên host:
  
  `docker ps`
- Thêm tham số `-a` để liệt kê tất cả container bao gồm chạy và dừng:
  
  `docker ps -a`
- Tạo một container từ image, nếu image không có sẵn trên local host thì docker sẽ tìm trên docker hub image phiên bản latest để tải về và chạy:
  
  `docker run <options> <image-name>`
- Dừng một container đang chạy:
  
  `docker stop <container-id>`
- Xóa một container
  
  `docker rm <container-id>`
- Khởi động lại container
  
  `docker start <container-id>`
- Xem log của container
  
  `docker logs <container-id>`
- Vào container đang chạy
  
  `docker exec -it <container-id> bash`

mở một shell trong một container đang chạy(ví dụ sử dụng bash)
- Xem thông tin container
  
  `docker inspect <container-id>`
- Xem các network của container
  
  `docker network ls`
- Xem các container kết nối đến một network cụ thể
  
  `docker network inspect <network-id>`
- Tạo container từ một dockerfile và chạy container
  
  `docker build -t <image-name>`

  `docker run -d <image-name>`
