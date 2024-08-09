## Network
- Trong Docker, mạng (network) cho phép các container giao tiếp với nhau và với hệ thống bên ngoài. Docker cung cấp nhiều loại mạng và tùy chọn cấu hình để phù hợp với các nhu cầu khác nhau của ứng dụng.

## Các loại mạng trong docker
1. Bridge network
- Đây là loại mạng mặc định khi bạn không chỉ định loại mạng khi tạo container.
- Các container kết nối với bridge network có thể giao tiếp với nhau thông qua địa chỉ IP nội bộ của mạng đó.
- Thích hợp cho các ứng dụng đơn giản hoặc môi trường phát triển.
2. Host network
- Container sử dụng mạng của host máy, nghĩa là container sẽ không có mạng riêng biệt và sẽ sử dụng mạng của hệ thống host.
- Được sử dụng khi bạn cần container giao tiếp trực tiếp với các dịch vụ mạng của máy chủ mà không cần NAT (Network Address Translation).
- Lưu ý: Tùy chọn này làm giảm tính tách biệt giữa host và container, có thể gây ra các vấn đề về bảo mật.
3. Overlay Network:
- Được sử dụng khi bạn có nhiều Docker hosts và cần kết nối các container trên các host khác nhau.
- Thích hợp cho các môi trường Docker Swarm hoặc Kubernetes, nơi bạn có nhiều node.
- Overlay network hoạt động thông qua một lớp mạng ảo và sử dụng các dịch vụ như VXLAN để tạo các mạng ảo.
4. Macvlan Network:
- Cho phép bạn gán một địa chỉ MAC và IP duy nhất cho mỗi container.
- Thích hợp cho các trường hợp cần container giao tiếp với mạng vật lý như là một thiết bị mạng riêng biệt.
- Hữu ích trong các ứng dụng yêu cầu địa chỉ IP riêng biệt cho từng container.
5. None Network:
- Tùy chọn này tắt toàn bộ kết nối mạng của container.
- Sử dụng khi bạn muốn kiểm soát hoàn toàn cấu hình mạng của container hoặc không cần kết nối mạng.

## Các lệnh quản lý network
- Tạo Network: 
  
  `docker network create <OPTIONS> NETWORK_NAME`
- Liệt kê Các Network: 
  
  `docker network ls`
- Xem Thông Tin Network: 
  
  `docker network inspect NETWORK_NAME`
- Xóa Network: 
  
  `docker network rm NETWORK_NAME`
- Xóa Tất Cả Network Không Còn Sử Dụng: 
  
  `docker network prune`

## Sử dụng network trong container
Khi tạo container, bạn có thể chỉ định mạng sử dụng tùy chọn --network:
- Gán Container vào một Network:
  
  `docker run -d --name my_container --network my_network my_image`
- Tạo và Sử Dụng Network Bridge:
  
  `docker network create --driver bridge my_bridge_network`
  `docker run -d --name container1 --network my_bridge_network my_image`
  `docker run -d --name container2 --network my_bridge_network my_image`
- Sử Dụng Network Overlay trong Docker Swarm:
  
  `docker network create --driver overlay my_overlay_network`

