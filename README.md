VietnamNet News Scraper
Dự án này là một trình thu thập web dựa trên Python, thu thập các bài báo từ VietnamNet. Nó chọn một danh mục tin tức ngẫu nhiên (ví dụ: Công nghệ, Kinh doanh, Giải trí), thu thập dữ liệu bài viết (tiêu đề, mô tả, hình ảnh, nội dung) trên tất cả các trang và lưu dữ liệu vào các tệp Excel và CSV. Tập lệnh được lên lịch chạy hàng ngày lúc 6 giờ sáng.
Tính năng

Chọn ngẫu nhiên một danh mục tin tức.
Thu thập tiêu đề bài viết, mô tả, URL hình ảnh, liên kết bài viết và toàn bộ nội dung.
Xử lý phân trang để thu thập dữ liệu từ tất cả các trang.
Lưu dữ liệu vào baiviet_vnn_.xlsx.
Lên lịch thực hiện hàng ngày lúc 6 giờ sáng bằng thư viện lịch trình.

Điều kiện tiên quyết

Python 3.8 trở lên
Trình duyệt Microsoft Edge đã cài đặt
Microsoft Edge WebDriver (tương thích với phiên bản trình duyệt của bạn)
Git (để sao chép kho lưu trữ)

Cài đặt
1. Sao chép Kho lưu trữ
git clone https://github.com/quoctrung227/tintuc.git
cd tintuc

2. Thiết lập Môi trường ảo (Tùy chọn nhưng được khuyến nghị)
python -m venv venv
source venv/bin/activate # Trên Windows: venv\Scripts\activate

3. Cài đặt Phụ thuộc
Cài đặt các gói Python bắt buộc được liệt kê trong requirements.txt:
pip install -r requirements.txt

4. Cài đặt Microsoft Edge WebDriver

Tải xuống Edge WebDriver từ Microsoft Edge Driver.
Đảm bảo phiên bản WebDriver khớp với phiên bản trình duyệt Edge đã cài đặt của bạn.
Đặt tệp thực thi msedgedriver vào PATH hệ thống của bạn (ví dụ: /usr/local/bin trên Linux/Mac hoặc C:\Windows trên Windows).

Ngoài ra, bạn có thể chỉ định đường dẫn đến WebDriver trong tập lệnh bằng cách sửa đổi dòng:
trinh_duyet = webdriver.Edge()

to:
trinh_duyet = webdriver.Edge(executable_path="/path/to/msedgedriver")

5. Xác minh Thiết lập
Đảm bảo các gói sau đã được cài đặt:

selenium==4.17.2
beautifulsoup4==4.12.3
pandas==2.2.0
schedule==1.2.1

Chạy pip list để xác nhận.
Cách sử dụng

Chạy Tập lệnh theo cách thủ công:
python scraper.py

Điều này sẽ:

Mở VietnamNet, chọn một danh mục ngẫu nhiên và thu thập tất cả các bài viết.
Lưu dữ liệu vào VNNetNews.xlsx và VNNetNews.csv trong thư mục dự án.
In số lượng bài viết đã lưu.

Chạy Tác vụ theo lịch trình: Tập lệnh được định cấu hình để chạy hàng ngày lúc 6 giờ sáng. Để bắt đầu trình lập lịch:
python scraper.py

Giữ terminal mở để cho phép trình lập lịch chạy. Nó sẽ đợi đến 6 giờ sáng để thực thi và lặp lại hàng ngày.

Dừng Script: Nhấn Ctrl+C trong terminal để dừng script.

Output

VNNetNews.xlsx: Tệp Excel chứa các bài viết đã trích xuất.
VNNetNews.csv: Tệp CSV có cùng dữ liệu, được mã hóa theo UTF-8.
Mỗi hàng bao gồm:
Tiêu đề: Tiêu đề bài viết
Mô mô tả: Mô tả bài viết
Hình ảnh: URL hình ảnh
Liên kết bài viết: URL bài viết
Nội dung: Nội dung bài viết đầy đủ

Khắc phục sự cố

Lỗi WebDriver: Đảm bảo Edge WebDriver đã được cài đặt và khớp với phiên bản trình duyệt của bạn. Kiểm tra PATH hoặc chỉ định đường dẫn thực thi trong script.

Không lưu dữ liệu: Xác minh cấu trúc trang web chưa thay đổi. Script dựa trên các lớp HTML cụ thể (horizontalPost__main, maincontent, ArticleContent).
Sự cố Timeout: Tăng giá trị time.sleep() nếu trang web tải chậm.
Các phụ thuộc: Đảm bảo tất cả các gói được cài đặt đúng cách bằng pip install -r requirements.txt.

Lưu ý

Tập ​​lệnh bỏ qua bước nút tìm kiếm vì VietnamNet không có tính năng tìm kiếm nổi bật trong phần điều hướng.
Tập lệnh sử dụng Microsoft Edge. Để sử dụng Chrome, hãy cài đặt chromedriver và sửa đổi tập lệnh để sử dụng webdriver.Chrome().
Hãy cập nhật trình duyệt của bạn để tránh các sự cố tương thích với WebDriver.

Đóng góp
Hãy thoải mái fork kho lưu trữ này, cải thiện và gửi yêu cầu kéo. Đối với các sự cố, hãy mở một phiếu trên kho lưu trữ GitHub.
Giấy phép
Dự án này được cấp phép theo Giấy phép MIT.
Liên hệ
Nếu có thắc mắc, hãy liên hệ với chủ sở hữu kho lưu trữ qua GitHub issues.
