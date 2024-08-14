## Thực hành image

Tìm kiếm một image từ docker hub, ví dụ tìm kiếm image về apache:

`docker search apache`
- Thay `apache` bằng tên image bạn muốn tìm
Tải một image về máy:

`docker pull httpd`
- thay `httpd` bằng tên image bạn muốn tải về local
Liệt kê tất cả các image đang có trên local:

`docker images`
Xem chi tiết thông tin về image:

`docker image inspect httpd`
Xem lịch sử các commit của image:

`docker history httpd`
- thay `httpd` bằng tên hoặc ID của image bạn muốn xem thông tin.
Xóa một image:

`docker rmi httpd`
- thay `httpd` bằng tên hoặc ID image bạn muốn xóa
- Xóa tất cả các image bằng lệnh `docker rmi -f $(docker images -qa)`
- Khi `image` đang được sử dụng để `run` một `container` thì muốn xóa, bạn cần thêm tham số `-f`
Đổi lại `tag` của một image:

`docker tag httpd httpd:1.0`
- `httpd` là image đang có. `httpd:1.0` là tên mới của image có phiên bản `1.0`, nếu không điền thì được mặc định là `latest`
- có thể chỉ định thêm `repository` sẽ upload image, tôi sử dụng `repository` là `tannt`: `docker tag httpd tannt/httpd:1.0`
Cách tra cứu cú pháp các command về image:

`docker [command] --help`
Ví dụ:

```docker image --help

docker image pull --help
```
