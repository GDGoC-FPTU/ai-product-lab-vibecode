- Tên nhóm: vibecode
- Thành viên: 
  - Nguyễn Văn Hưng – 2A202601251
  - Vũ Bình Minh – MSSV 2A202601295
  - Lê Thị Thúy – MSSV 2A202601381
# 01-problem-scan.md

## Phase 1 — SCAN

### Bảng quét cơ hội

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | Xanh SM | Lặp lại | Điều phối xe điện khi tài xế báo pin thấp và cần gợi ý trạm sạc gần nhất. |
| 2 | Xanh SM | Tốn thời gian | Điều phối viên phải tra cứu thủ công vị trí xe, trạm sạc và soạn tin nhắn hướng dẫn. |
| 3 | VinFast | AI-upgrade | Hỗ trợ đề xuất trạm sạc phù hợp cho từng dòng xe điện và loại cổng sạc. |
| 4 | Vinhomes | Pain từ người khác | Phân loại và điều hướng phản ánh cư dân vào đúng bộ phận xử lý. |
| 5 | Vinmec | Tốn thời gian | Soạn tóm tắt hồ sơ xuất viện bằng cách trích xuất thông tin từ bệnh án. |

## Phase 2 — QUICK-ASSESS

### Quick Problem Card 1
- Bài toán: Xử lý sự cố pin thấp của tài xế Xanh SM giữa đường.
- Công ty: Xanh SM
- Actor: Tài xế và điều phối viên
- Workflow thủ công: nhận cuộc gọi -> tra cứu vị trí -> tra cứu trạm sạc -> soạn tin nhắn -> gọi cứu hộ nếu cần.
- Bước tốn thời gian nhất: tra cứu trạm sạc và soạn chỉ dẫn (khoảng 10-12 phút/lượt).
- AI có thể hỗ trợ: tự động đề xuất trạm sạc gần nhất và soạn bản nháp chỉ dẫn.
- Metric: giảm thời gian xử lý từ 15 phút xuống dưới 3 phút.
- Quick Architecture: LLM

### Quick Problem Card 2
- Bài toán: Hỗ trợ đề xuất trạm sạc phù hợp cho VinFast.
- Công ty: VinFast
- Actor: Tài xế và đội vận hành
- Workflow: nhận yêu cầu -> tra cứu loại xe -> tra cứu trạm sạc -> gửi chỉ dẫn.
- Bước tốn thời gian nhất: tra cứu trạm phù hợp với loại cổng sạc.
- AI có thể hỗ trợ: phân loại trạm phù hợp và draft chỉ dẫn.
- Metric: giảm thời gian tra cứu từ 8 phút xuống dưới 2 phút.
- Quick Architecture: Rule / LLM

### Quick Problem Card 3
- Bài toán: Tự động phân loại phản ánh cư dân tại Vinhomes.
- Công ty: Vinhomes
- Actor: Nhân viên vận hành
- Workflow: nhận phản ánh -> phân loại -> chuyển cho bộ phận liên quan -> phản hồi.
- Bước tốn thời gian nhất: phân loại và điều hướng phản ánh.
- AI có thể hỗ trợ: phân loại nội dung và đề xuất bộ phận xử lý.
- Metric: giảm thời gian phân loại từ 6 phút xuống dưới 2 phút.
- Quick Architecture: Rule / LLM
