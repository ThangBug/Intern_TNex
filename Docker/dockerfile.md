Dockerfile là một tập tin cấu hình dùng để tạo Docker Images. Nó chứa các lệnh và chỉ dẫn để xây dựng image theo cách bạn muốn. Dockerfile cung cấp một phương pháp tự động hóa quá trình xây dựng image, giúp bạn duy trì môi trường phát triển và triển khai nhất quán.

# Dockerfile

1. Ghi chép về Dockerfile
- Dockerfile có thể hình dung như một script dùng để build các image trong container.
- Dockerfile bao gồm các câu lệnh liên tiếp nhau được thực hiện tự động trên một image gốc để tạo ra một image mới. Dockerfile giúp đơn giản hóa tiến trình từ lúc bắt đầu đến khi kết thúc.
- Trong Dockerfile có các câu lệnh chính sau:
```FROM
RUN
CMD
....còn nữa
```
2. Dockerfile Systax
```# Comment
INSTRUCTION arguments
```
- Các INSTRUCTION là các chỉ thị, được docker quy định. Khi khai báo, các bạn phải viết chữ in hoa.
- Các arguments là đoạn nội dung mà chỉ thị sẽ làm gì.
- Ví dụ:
```# Comment
RUN echo 'we are running some # of cool things'
```
- Chúng ta sẽ đi tìm hiểu các INSTRUCTION

3. Dockerfile Commands

3.1 FROM
- Dùng để chỉ ra image được build từ đâu (từ image gốc nào)
```FROM ubuntu

hoặc có thể chỉ rõ tag của image gốc

FROM ubuntu14.04:lastest
```
3.2 RUN
- Dùng để chạy một lệnh nào đó khi build image, ví dụ về một Dockerfile
```FROM ubuntu
RUN apt-get update
RUN apt-get install curl -y
```
3.3 CMD
- Lệnh CMD dùng để truyền một lệnh của Linux mỗi khi thực hiện khởi tạo một container từ image (image này được build từ Dockerfile)
- Có các cách (trong docs nói có 3 cách) sử dụng lệnh CMD, ví dụ
```#Cách 1
FROM ubuntu
RUN apt-get update
RUN apt-get install curl -y
CMD ["curl", "ipinfo.io"]
```
hoặc

```#Cách 2
FROM ubuntu
RUN apt-get update
RUN apt-get install wget -y
CMD curl ifconfig.io
```
3.4 LABEL
`LABEL <key>=<value> <key>=<value> <key>=<value> ...`
- Chỉ thị LABEL dùng để add các metadata vào image.

- Ví dụ:
```LABEL "com.example.vendor"="ACME Incorporated"
LABEL com.example.label-with-value="foo"
LABEL version="1.0"
LABEL description="This text illustrates \
that label-values can span multiple lines."
```
- Để xem các label của images, dùng lệnh docker inspect. "Labels": { "com.example.vendor": "ACME Incorporated" "com.example.label-with-value": "foo", "version": "1.0", "description": "This text illustrates that label-values can span multiple lines.", "multi.label1": "value1", "multi.label2": "value2", "other": "value3" },

3.5 MAINTAINER
`MAINTAINER <name>`
- Dùng để đặt tên giả của images.

- Hoặc bạn có thể sử dụng

`LABEL maintainer "SvenDowideit@home.org.au"`

3.6 EXPOSE
`EXPOSE <port> [<port>...]`
- Lệnh EXPOSE thông báo cho Docker rằng image sẽ lắng nghe trên các cổng được chỉ định khi chạy. Lưu ý là cái này chỉ để khai báo, chứ ko có chức năng nat port từ máy host vào container. Muốn nat port, thì phải sử dụng cờ -p (nat một vài port) hoặc -P (nat tất cả các port được khai báo trong EXPOSE) trong quá trình khởi tạo contrainer.

3.7 ENV
```ENV <key> <value>
ENV <key>=<value> ...
```
- Khai báo cáo biến giá trị môi trường. Khi run container từ image, các biến môi trường này vẫn có hiệu lực.

3.8 ADD
```ADD has two forms:
ADD <src>... <dest>
ADD ["<src>",... "<dest>"] (this form is required for paths containing whitespace)
```
- Chỉ thị ADD copy file, thư mục, remote files URL (src) và thêm chúng vào filesystem của image (dest)
- src: có thể khai báo nhiều file, thư mục, có thể sử dụng các ký hiệu như *,?,...
- dest phải là đường dẫn tuyệt đối hoặc có quan hệ với chỉ thị WORKDIR
Note: If your URL files are protected using authentication, you will need to use RUN wget, RUN curl or use another tool from within the container as the ADD instruction does not support authentication.

- Các quy định:
- The path must be inside the context of the build: Có nghĩa là phải nằm trong thư mục đang build (chứa dockerfiles).
- If is a directory, the entire contents of the directory are copied, including filesystem metadata. The directory itself is not copied, just its contents.
- If multiple resources are specified, either directly or due to the use of a wildcard, then must be a directory, and it must end with a slash /.
- If does not end with a trailing slash, it will be considered a regular file and the contents of will be written at .
- If doesn’t exist, it is created along with all missing directories in its path.

3.9 COPY
```COPY <src>... <dest>
COPY ["<src>",... "<dest>"] (this form is required for paths containing whitespace)
```
- Chỉ thị COPY, copy file, thư mục (src) và thêm chúng vào filesystem của container (dest).
- Các lưu ý tương tự chỉ thị ADD.

3.10 ENTRYPOINT
```ENTRYPOINT ["executable", "param1", "param2"] (exec form, preferred)
ENTRYPOINT command param1 param2 (shell form)
```
- Hai cái CMD và ENTRYPOINT có tác dụng tương tự nhau. Nếu một Dockerfile có cả CMD và ENTRYPOINT thì CMD sẽ thành param cho script ENTRYPOINT. Lý do người ta dùng ENTRYPOINT nhằm chuẩn bị các điều kiện setup như tạo user, mkdir, change owner... cần thiết để chạy service trong container.

3.11 VOLUME
`VOLUME ["/data"]`
- mount thư mục từ máy host và container. Tương tự option -v khi tạo container.
- Thư mục chưa volumes là /var/lib/docker/volumes/. Ứng với mỗi container sẽ có các thư mục con nằm trong thư mục này. Tìm thư mục chưa Volumes của container sad_euclid:
```root@adk:/var/lib/docker/volumes# docker inspect sad_euclid | grep /var/lib/docker/volumes
                "Source": "/var/lib/docker/volumes/491a2a775a4cf02bbaca105ec25995008cc7adbc5511e054bb9c6a691a2681ee/_data",
```
3.12 USER
`USER daemon`
- Set username hoặc UID để chạy các lệnh RUN, CMD, ENTRYPOINT trong dockerfiles.

3.13 WORKDIR
`WORKDIR /path/to/workdir`
- Chỉ thị WORKDIR dùng để đặt thư mục đang làm việc cho các chỉ thị khác như: RUN, CMD, ENTRYPOINT, COPY, ADD,...

3.14 ARG
`ARG <name>[=<default value>]`
- Chỉ thị ARG dùng để định nghĩa các giá trị của biến được dùng trong quá trình build image (lệnh docker build --build-arg =).
- biến ARG sẽ không bền vững như khi sử dụng ENV.

3.15 STOPSIGNAL
`STOPSIGNAL signal`
- Gửi tín hiệu để container tắt đúng cách.

3.16 SHELL
`SHELL ["executable", "parameters"]`
- Chỉ thị Shell cho phép các shell form khác có thể ghi đè shell mặc định.
- Mặc định trên Linux là ["/bin/sh", "-c"] và Windows là ["cmd", "/S", "/C"].
Ví dụ:

```FROM microsoft/windowsservercore

# Executed as cmd /S /C echo default
RUN echo default

# Executed as cmd /S /C powershell -command Write-Host default
RUN powershell -command Write-Host default

# Executed as powershell -command Write-Host hello
SHELL ["powershell", "-command"]
RUN Write-Host hello

# Executed as cmd /S /C echo hello
SHELL ["cmd", "/S"", "/C"]
RUN echo hello
```
3.17 ONBUILD
`ONBUILD [INSTRUCTION]`
- Chỉ thị ONBUILD được khai báo trong base image. Và khi child image build image từ base image thì lệnh ONBUILD mới được thực thi.
- Ví dụ + ref: http://container42.com/2014/02/06/docker-quicktip-3-onbuild/


# Ví dụ dockerfile
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

# Các Lệnh Xây Dựng Docker Image từ Dockerfile
- Xây dựng image từ dockerfile
  
  `docker build -t my_flask_app:latest`
- Xem danh sách các image
  
  `docker images`
- Chạy container từ image
  
  `docker run -d -p 5000:5000 my_flask_app:latest`
