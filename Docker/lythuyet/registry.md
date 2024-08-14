Docker Registry là một dịch vụ lưu trữ và phân phối Docker Images. Nó cho phép bạn lưu trữ các Docker Images và chia sẻ chúng với người dùng khác hoặc với các hệ thống khác. Dưới đây là các khái niệm cơ bản và lệnh liên quan đến Docker Registry:

## Các Khái Niệm Cơ Bản về Docker Registry
1. Docker Hub:
- Docker Hub là dịch vụ Docker Registry công cộng và phổ biến nhất.
- Cung cấp các Docker Images chính thức và community-contributed.
- Được sử dụng để tìm kiếm, tải xuống và chia sẻ Docker Images.
2. Docker Registry:
- Docker Registry là dịch vụ lưu trữ Docker Images. Có thể sử dụng Docker Registry công cộng như Docker Hub hoặc triển khai registry riêng (private registry) cho nhu cầu cụ thể.
- Được cấu hình để chứa và quản lý các Docker Images.
3. Docker Repository:
- Là một tập hợp các Docker Images với các tag khác nhau. Ví dụ: một repository có thể chứa nhiều version của một image (như my_app:latest, my_app:v1.0, etc.).
4. Docker Image Tag:
- Là nhãn để phân loại và phiên bản của Docker Images. Tag giúp xác định version cụ thể của image.
- Ví dụ: `my_app:latest, my_app:v1.0`.
## Lệnh quản lý docker registry
- Đẩy image lên docker hub hoặc private registry
  
  `docker push <option> <image_name>:<tag>`
- Tải image từ docker hub hoặc private registry
  
  `docker pull <image_name>:<tag>`
- Tìm kiếm images trên docker hub
  
  `docker search <options> <term>`

## Cài đặt docker registry riêng
Nếu bạn muốn triển khai một Docker Registry riêng (private registry), bạn có thể sử dụng Docker Registry image. Dưới đây là cách đơn giản để triển khai một Docker Registry riêng:
1. Chạy docker registry container:
  
  `docker run -d -p 5000:5000 --name my_registry registry:2`
2. Đẩy image lên registry riêng
  
  `docker push localhost:5000/my_image:latest`
3. Tải image từ registry riêng
  
  `docker pull localhost:5000/my_image:latest`

## Cấu hình registry
- `config.yml`:
	- Bạn có thể cấu hình registry bằng cách chỉnh sửa tệp `config.yml`. Ví dụ, cấu hình bảo mật, lưu trữ, và các cài đặt khác.
- `certs`:
	- Để triển khai một registry an toàn, bạn có thể sử dụng SSL/TLS. Bạn cần cấu hình chứng chỉ và khóa riêng trong thư mục `certs`.

## Ví dụ cấu hình `config.yml`
  
  ```version: 0.1
log:
  fields:
    service: registry
storage:
  filesystem:
    rootdirectory: /var/lib/registry
http:
  headers:
    X-Content-Type-Options: nosniff
health:
  storagedriver:
    enabled: true
    interval: 10s
    timeout: 10s
```

