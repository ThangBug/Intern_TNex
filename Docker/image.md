Docker Image là một thành phần cốt lõi trong hệ sinh thái Docker, đóng vai trò là mẫu để tạo các container. Dưới đây là các khái niệm cơ bản và lệnh liên quan đến Docker Image:

## Các Khái Niệm Cơ Bản về Docker Image
1. Docker Image:
- Là một bản sao không thay đổi của phần mềm, bao gồm mã nguồn, thư viện, và các phụ thuộc cần thiết để chạy ứng dụng.
- Các image được sử dụng để tạo các container, và container sẽ chạy các ứng dụng dựa trên image đó.
2. Layers:
- Docker Image được xây dựng từ nhiều lớp (layers). Mỗi lớp đại diện cho một thay đổi hoặc bổ sung vào image, chẳng hạn như cài đặt phần mềm hoặc sao chép tệp tin.
- Các lớp này được lưu trữ và chia sẻ giữa các image, giúp tiết kiệm không gian lưu trữ.
3. Dockerfile:
- Là một tập tin cấu hình chứa các chỉ dẫn để tạo Docker Image.
- Bao gồm các lệnh như FROM, RUN, COPY, và CMD để định nghĩa các bước xây dựng image.
4. Repository:
- Là nơi lưu trữ các Docker Images. Docker Hub là dịch vụ phổ biến nhất, nhưng bạn cũng có thể sử dụng các dịch vụ khác hoặc tự chạy một registry riêng.

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

