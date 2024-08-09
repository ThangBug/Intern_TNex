# Lý thuyết
1. Container là gì?
- Container là một phương pháp đóng gói ứng dụng và các phụ thuộc của nó vào một đơn vị độc lập, giúp chạy ứng dụng đó trên bất kỳ hệ thống nào mà không cần lo lắng về sự khác biệt giữa các môi trường.
2. Các thành phần chính:
- Image: Là bản sao của hệ thống tệp và cấu hình cần thiết để chạy một container. Images thường được xây dựng từ Dockerfile.
- Container: Là một thể hiện đang chạy của một image. Containers chia sẻ kernel của hệ điều hành nhưng có hệ thống tệp, mạng, và môi trường riêng.
- Docker Daemon: Chạy trên hệ thống và quản lý các containers và images.
- Docker CLI: Công cụ dòng lệnh cho phép người dùng tương tác với Docker Daemon.
3. Lợi ích
- Nhẹ: Containers có trọng lượng nhẹ hơn so với máy ảo vì chúng chia sẻ kernel của hệ điều hành.
- Di động: Có thể chạy trên bất kỳ môi trường nào có Docker, từ máy cá nhân đến máy chủ hoặc môi trường đám mây.
- Nhất quán: Đảm bảo rằng ứng dụng chạy giống nhau trên các môi trường khác nhau.
# Câu Lệnh docker container Cơ Bản
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
