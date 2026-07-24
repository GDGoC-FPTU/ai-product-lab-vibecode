# 02 - Deep Dive Report

## Thông tin nhóm
- Tên nhóm: vibecode
- Thành viên: 
  - Nguyễn Văn Hưng – 2A202601251
  - Vũ Bình Minh – MSSV 2A202601295
  - Lê Thị Thúy – MSSV 2A202601381

## 1. Quyết định lựa chọn bài toán
Nhóm quyết định chọn bài toán “Xử lý sự cố hết pin thực địa” cho Xanh SM. Đây là vấn đề có ảnh hưởng trực tiếp đến trải nghiệm tài xế và hiệu quả vận hành trong giờ cao điểm.

## 2. Problem Statement (6-field)

| Field | Nội dung |
|---|---|
| Actor / Operator | Điều phối viên trung tâm điều vận Xanh SM và tài xế xe điện. |
| Current Workflow | Khi tài xế báo hết pin, điều phối viên tra cứu vị trí xe, tra cứu trạm sạc gần nhất, soạn tin nhắn chỉ dẫn và gọi cứu hộ nếu cần. |
| Bottleneck | Bước tra cứu trạm sạc phù hợp và soạn hướng dẫn mất nhiều thời gian, dễ sai sót. |
| Business Impact | Mỗi ngày có nhiều sự cố thực địa, làm tăng thời gian chờ đợi cho tài xế và giảm hiệu quả vận hành. |
| Success Metric | Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút; đạt tỷ lệ hướng dẫn đúng trên 98%. |
| Operational Boundary | AI chỉ có thể tạo bản nháp, không tự ý gửi tin cho tài xế mà không có phê duyệt của điều phối viên. |

## 3. Future-State Flow & AI Fit
- AI Fit: LLM Feature.
- Quy trình tương lai:
  1. Nhận thông tin sự cố từ tài xế.
  2. Tự động lấy vị trí xe và tra cứu trạm sạc gần nhất.
  3. AI tạo bản nháp tin nhắn chỉ dẫn và đề xuất hành động.
  4. Điều phối viên duyệt trước khi gửi tới tài xế.
  5. Nếu AI gặp lỗi hoặc không đủ tin cậy, điều phối viên tự xử lý thủ công.

## 4. Ranh giới an toàn
- Luôn bắt đầu câu trả lời bằng tag [DRAFT_ONLY].
- Nếu pin dưới 5%, không đề xuất trạm sạc xa; thay vào đó đề xuất dispatch_mobile_charger.
- Mọi quyết định gửi thông điệp cho tài xế đều cần có con người phê duyệt.

## 5. Evaluate

| Checklist | Đánh giá |
|---|---|
| Bài toán cụ thể và có metric rõ ràng | Có |
| Có thể xây dựng prompt prototype nhanh | Có |
| Ranh giới an toàn có thể kiểm tra bằng test cases | Có |
| Ảnh hưởng kinh doanh rõ ràng | Có |

### Kết luận
Dự án đạt mức GO vì bài toán có ý nghĩa vận hành, tối ưu hóa được quy trình thủ công và có thể kiểm soát rủi ro bằng prompt engineering và human-in-the-loop.
