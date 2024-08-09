# Cài đặt docker
## Cài đặt trên ubuntu
- Cập nhật danh sách gói
  ```sudo apt update```
- Cài các gói phụ thuộc
  ```sudo apt install apt-transport-https ca-certificates curl software-properties-common```
- Thêm kho lưu trữ docker
  ```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```
- Cập nhật lại danh sách gói
  ```sudo apt update```
- Cài đặt docker
  ```sudo apt install docker-ce```
- Kiểm tra docker đã cài đặt thành công chưa
  ```sudo systrmctl status docker```
- Kiểm tra phiên bản
  ```docker --version```
## Cài đặt trên windows
- Tải xuống docker desktop: https://www.docker.com/
- Chạy tệp cài đặt
- Kích hoạt WSl(nếu cần)
- Hoàn tất cài đặt, khởi động docker desktop
- kiểm tra docker desktop
  ```docker version```
