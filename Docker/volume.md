## Các loại volume
1. Named Volumes: Được tạo ra và quản lý bởi Docker. Chúng có thể được chia sẻ giữa các containers và có tên cụ thể để dễ quản lý.

2. Anonymous Volumes: Là các volumes không có tên cụ thể và thường được tạo tự động khi không chỉ định tên.

3. Bind Mounts: Được sử dụng để ánh xạ một thư mục hoặc tập tin từ máy chủ host vào container. Điều này cho phép bạn làm việc với các tập tin bên ngoài Docker.

4. tmpfs Mounts: Là các volumes lưu trữ dữ liệu trong bộ nhớ tạm thời, không lưu trữ trên đĩa.
## Các lệnh quản lý volume
- Tạo volume
  
  `docker volume create <option> <volume_name>`
- Liệt kê Volumes
  
  `docker volume ls`
- Xem thông tin volume
  
  `docker volume inspect <volume_name>`
- Xóa volume
  
  `docker volume rm <volume_name>`
- Xóa tất cả volumes không còn sử dụng
  
  `docker volume prune`

## Sử dụng volume trong container
  Để sử dụng volume trong một container, bạn có thể sử dụng tùy chọn -v hoặc --mount khi chạy container
- Sử dụng với `-v`:
  
  `docker run -d -v my_volume:/app/data my_image`
trong vd trên `my_volume` sẽ đc gắn vào thư mục `/app/data` trong container
- Sử dụng với `--mount`:
  
  `docker run -d --mount source=my_volume, target=/app/data my_image`
Tùy chọn `--mount` cung cấp nhiều tùy chọn hơn và là cú pháp chính thức hơn.

## ví dụ cụ thể
- Tạo và sử dụng 1 volume:
  
  `docker volume create mu_data`
  `docker run -d --name my_container -v my_data:/data my_image`
- Liệt kê all volume
  
  `docker volume ls`
- Inspect một volume
  
  `docker volume inspect my_data`
- Xóa một volume
  
  `docker volume rm my_data`
- Xóa all volume không còn sử dụng
  
  `docker volume prune`

