# 02-deep-dive-report.md

## Quyết định lựa chọn

Nhóm chọn bài toán: xử lý sự cố pin thấp của tài xế Xanh SM giữa đường, với mục tiêu giảm thời gian điều phối và đảm bảo an toàn.

## Problem Statement (6-field)

| Field | Nội dung |
|---|---|
| 1. Actor / Operator | Điều phối viên trung tâm Xanh SM và tài xế đang gặp sự cố pin thấp. |
| 2. Current Workflow | Khi tài xế báo pin thấp, điều phối viên tra cứu vị trí xe, tra cứu trạm sạc gần nhất, soạn tin nhắn chỉ dẫn, và gọi xe cứu hộ nếu cần. |
| 3. Bottleneck | Tra cứu thủ công trạm sạc phù hợp và soạn tin nhắn chỉ dẫn mất nhiều thời gian và dễ sai. |
| 4. Business Impact | Mỗi lượt xử lý gây lãng phí thời gian điều phối và có thể làm tăng sự chậm trễ trong vận hành, ảnh hưởng đến trải nghiệm khách hàng. |
| 5. Success Metric | Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút và đạt độ chính xác đề xuất trạm sạc trên 95%. |
| 6. Operational Boundary | AI được phép draft tin nhắn và đề xuất trạm sạc. AI không được tự ý gửi tin mà không có phê duyệt, và không được đề xuất trạm sạc nguy hiểm khi pin dưới ngưỡng an toàn. |

## Future-State Flow & AI Fit

- AI Fit: LLM Feature
- Future-State Flow:
  1. Nhận thông tin sự cố từ tài xế.
  2. AI tra cứu vị trí và đề xuất trạm sạc gần nhất.
  3. AI draft tin nhắn hướng dẫn và cảnh báo an toàn.
  4. Điều phối viên phê duyệt trước khi gửi.
  5. Nếu AI không tự tin, dùng fallback thủ công.

## Evaluate

- Có sẵn dữ liệu mẫu và quy trình rõ ràng.
- Rủi ro có thể kiểm soát bằng human-in-the-loop và fallback.
- Quyết định cuối cùng: GO.

### Justification

Giải pháp phù hợp với scope hẹp, có thể triển khai nhanh, và rủi ro được kiểm soát tốt bằng ranh giới an toàn và bước phê duyệt người dùng.
