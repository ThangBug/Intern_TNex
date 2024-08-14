# Chương trình
* Chương trình này là một ứng dụng web được xây dựng bằng FastAPI và SQLAlchemy, sử dụng cơ sở dữ liệu bất đồng bộ. Chương trình cung cấp các API endpoint để thực hiện các thao tác CRUD (Create, Read, Update, Delete) trên một bảng cơ sở dữ liệu.

# Cấu trúc
1. Thư mục app
  - __init__.py:
    + Tệp này giúp Python nhận diện thư mục app là một package. Nó có thể rỗng hoặc chứa mã khởi tạo package.
  - main.py:
    + Tệp này chứa mã khởi tạo ứng dụng FastAPI và định nghĩa các route (API Endpoints). Đây là tệp chính để chạy ứng dụng.
  - models.py:
    + Tệp này định nghĩa các mô hình cơ sở dữ liệu sử dụng SQLAlchemy. Các lớp trong tệp này thường đại diện cho các bảng trong cơ sở dữ liệu.
  - crud.py:
    + Tệp này chứa các chức năng CRUD (Create, Read, Update, Delete) để tương tác với cơ sở dữ liệu. Các chức năng này thực hiện các thao tác cơ bản trên dữ liệu như thêm, sửa, xóa và đọc.
  - database.py:
    + Tệp này thiết lập kết nối với cơ sở dữ liệu, cấu hình SQLAlchemy, và khởi tạo phiên làm việc với cơ sở dữ liệu. Nó thường chứa các thông tin cấu hình cơ sở dữ liệu và các hàm để lấy kết nối cơ sở dữ liệu
  - schemas.py:
    + Tệp này định nghĩa các schema sử dụng Pydantic để kiểm tra và xác thực dữ liệu đầu vào và đầu ra của các API. Nó bao gồm các lớp mô tả cấu trúc dữ liệu mà API yêu cầu và trả về.
2. Tệp requirements.txt
  - requirements.txt:
    + Tệp này liệt kê tất cả các thư viện và phiên bản cần thiết cho dự án. Khi bạn cài đặt môi trường ảo, bạn có thể sử dụng tệp này để cài đặt tất cả các phụ thuộc bằng lệnh: pip install -r requirements.txt

# API Endpoints
1. POST /items/
  * Endpoint này dùng để tạo một đối tượng 'Item' mới trong cơ sở dữ liệu.
    - Request Body: Dữ liệu cho đối tượng 'Item' mới cần tạo. Dữ liệu này phải phù hợp với schema 'ItemCreate'.
    - Response: Trả về đối tượng 'Item' mới được tạo, bao gồm cả 'id' được gán tự động.
2.  GET /items/
  * Endpoint này dùng để lấy danh sách các đối tượng 'Item' từ cơ sở dữ liệu.
    - Query Parameters:
      + skip: Số lượng đối tượng cần bỏ qua (mặc định là 0).
      + limit: Số lượng đối tượng tối đa cần trả về (mặc định là 10).
    - Response: Trả về danh sách các đối tượng 'Item'.
3. GET /items/{item_id}
  * Endpoint này dùng để lấy thông tin của một đối tượng 'Item' cụ thể theo 'item_id'.
    - Path Parameter: 'item_id' - ID của đối tượng 'Item' cần lấy.
    - Response: Trả về đối tượng 'Item' tương ứng với item_id. Nếu không tìm thấy đối tượng nào với 'item_id' này, trả về lỗi 404.
4. PUT /items/{item_id}
  * Endpoint này dùng để cập nhật thông tin của một đối tượng 'Item' cụ thể theo 'item_id'.
    - Path Parameter: 'item_id' - ID của đối tượng 'Item' cần cập nhật.
    - Request Body: Dữ liệu cập nhật cho đối tượng 'Item'. Dữ liệu này phải phù hợp với schema ItemUpdate.
    - Response: Trả về đối tượng 'Item' đã được cập nhật. Nếu không tìm thấy đối tượng nào với 'item_id' này, trả về lỗi 404.
5. DELETE /items/{item_id}
  * Endpoint này dùng để xóa một đối tượng 'Item' cụ thể theo 'item_id'.
    - Path Parameter: item_id - ID của đối tượng 'Item' cần xóa.
    - Response: Trả về đối tượng 'Item' đã bị xóa. Nếu không tìm thấy đối tượng nào với 'item_id' này, trả về lỗi 404.

# Các lệnh
- venv\Scripts\activate: kích hoạt môi trường ảo venv
- deactivate: tắt môi trường ảo
- uvicorn app.main:app --reload: chạy ứng dụng
- 