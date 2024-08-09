## Lý thuyết
- Là bản sao hoàn chỉnh của một ứng dụng và môi trường của nó, bao gồm hệ điều hành, thư viện, và cấu hình cần thiết. Images được xây dựng từ Dockerfile.
## Các câu lệnh image
- Tạo image từ dockerfile:
  
  `docke build -t <name_image>:<tag>`
- Liệt kê
  
  `docker images`
or
  `docker image ls`
- Xem chi tiết image
  
  `docker inspect <name_image>:<tag>`
 
- Xóa image
  
  `docker rmi <name_image>:<tag>`
- Lấy image từ docker hub
  
  `docker pull <name_image>:<tag>`
- Đẩy image lên docker hub
  
  `docker push <name_image>:<tag>`
- Xem các layers của image
  
  `docker history <name_image>:<tag>`
- Chạy container từ image
  `docker run <option> <name_image>:<tag>`

