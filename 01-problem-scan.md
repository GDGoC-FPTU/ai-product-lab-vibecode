# 01 - Problem Scan

## Thông tin nhóm
- Tên nhóm: vibecode
- Thành viên: 
  - Nguyễn Văn Hưng – 2A202601251
  - Vũ Bình Minh – MSSV 2A202601295
  - Lê Thị Thúy – MSSV 2A202601381

## Phase 1 — SCAN: Tìm kiếm cơ hội

| # | Subsidiary | Lens | Mô tả bài toán |
|---|------------|------|----------------|
| 1 | Xanh SM | Lặp lại | Điều phối viên phải điều chỉnh lại lộ trình khi khách hàng đổi điểm đón giữa chừng. |
| 2 | Xanh SM | Tốn thời gian | Tài xế báo sự cố hết pin giữa đường, điều phối viên phải tra cứu trạm sạc và soạn tin nhắn thủ công. |
| 3 | VinFast | Lặp lại | So khớp dữ liệu sạc điện và đối chiếu thông tin trạm sạc đối tác theo chu kỳ. |
| 4 | Vinhomes | AI-upgrade | Phân loại và tổng hợp phản hồi cư dân từ app để giảm thời gian xử lý CSKH. |
| 5 | Vinmec | Pain từ người khác | Bác sĩ mất thời gian tóm tắt hồ sơ xuất viện cho từng bệnh nhân. |

## Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

### Card 1 — Xanh SM: Xử lý sự cố hết pin thực địa
- Bài toán: Tài xế Xanh SM báo hết pin giữa đường và cần được hỗ trợ nhanh.
- Actor: Điều phối viên và tài xế.
- Workflow thủ công hiện tại: nhận cuộc gọi -> tra cứu vị trí xe -> tra cứu trạm sạc -> soạn tin nhắn -> gọi cứu hộ nếu cần.
- Bottleneck: Bước tra cứu trạm và soạn hướng dẫn bằng tay mất khoảng 10 phút.
- AI có thể hỗ trợ: tự động lấy dữ liệu vị trí, gợi ý trạm gần nhất, tạo bản nháp tin nhắn.
- Metric thành công: giảm thời gian xử lý từ 15 phút xuống dưới 3 phút.
- Kiến trúc đề xuất: LLM Feature với HITL approval.

### Card 2 — Vinhomes: Tự động phân loại phản hồi cư dân
- Bài toán: Phản hồi cư dân có nhiều mẫu câu lặp lại và cần được phân loại nhanh.
- Actor: Nhân viên CSKH.
- Workflow thủ công hiện tại: nhận phản hồi -> đọc nội dung -> phân loại -> chuyển cho bộ phận phù hợp.
- Bottleneck: Phải đọc và phân nhóm thủ công nhiều lần.
- AI có thể hỗ trợ: phân loại và gợi ý hành động tự động.
- Metric: giảm thời gian xử lý từ 12 giờ xuống dưới 2 giờ.
- Kiến trúc đề xuất: Rule + LLM.

### Card 3 — Xanh SM: Tóm tắt lý do hủy chuyến
- Bài toán: Tóm tắt nguyên nhân hủy chuyến từ ghi âm và ghi chú tài xế.
- Actor: Back-office analyst.
- Workflow thủ công hiện tại: nghe ghi âm -> ghi chú -> tổng hợp pattern.
- Bottleneck: mất nhiều thời gian và dễ bỏ sót thông tin.
- AI có thể hỗ trợ: tóm tắt tự động và gợi ý nguyên nhân chính.
- Metric: giảm thời gian phân tích từ 30 phút xuống dưới 10 phút.
- Kiến trúc đề xuất: LLM Feature.

## Quyết định lựa chọn
Nhóm chọn bài toán “Xử lý sự cố hết pin thực địa” vì có tác động trực tiếp đến vận hành real-time, dữ liệu dễ thu thập và giải pháp AI có thể triển khai nhanh với ranh giới an toàn rõ ràng.
