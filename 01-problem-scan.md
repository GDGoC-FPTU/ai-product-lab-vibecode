# Phase 1 & 2 — Problem Scan & Quick Cards: Vin Smart Future

**Học viên / Tác giả:** [Điền họ tên và MSSV]

**Nhóm:** Vin Smart Future — Lab 02

**Phạm vi:** Các công ty thành viên Vingroup

> **Lưu ý về số liệu:** Các mốc thời gian và tỷ lệ dưới đây là **giả định vận hành ban đầu để scoping**, không phải số liệu nội bộ đã được xác nhận. Trước khi làm prototype cần đo baseline trên tối thiểu 100 lượt xử lý hoặc 2 tuần log thực tế.

---

# 🔍 Phase 1 — SCAN: Bảng quét cơ hội

| # | Công ty thành viên | Lens chính | Bài toán thực tế và nút thắt |
|---:|---|---|---|
| 1 | **Vinhomes** | **Lặp lại** | Nhân viên CSKH phải đọc nội dung tự do và ảnh đính kèm của từng phản ánh trên ứng dụng cư dân, gắn nhóm sự cố, mức ưu tiên và chuyển đúng Ban Quản lý/kỹ thuật. Ticket thiếu mã căn hoặc vị trí thường bị chuyển qua lại. |
| 2 | **Vinmec** | **Tốn thời gian** | Trước khi bệnh nhân nội trú xuất viện, bác sĩ phải rà lại diễn biến điều trị, xét nghiệm, thủ thuật và đơn thuốc ở nhiều màn hình để soạn bản tóm tắt xuất viện. Đây là công việc hành chính dài nhưng vẫn cần bác sĩ chịu trách nhiệm chuyên môn. |
| 3 | **Xanh SM (GSM)** | **Stakeholder Pain** | Cuối ca, điều phối viên phải ghép xe với điểm sạc dựa trên % pin, giờ nhận ca kế tiếp, vị trí xe và số chỗ sạc còn trống. Phân công bằng bảng tính/điện thoại dễ làm tài xế phải chờ hoặc chạy vòng. |
| 4 | **VinFast** | **Lặp lại** | Cố vấn dịch vụ nhập lại nội dung từ mô tả của khách hàng và ghi chú kiểm tra xe vào phiếu sửa chữa/bảo hành; cách viết không đồng nhất khiến kỹ thuật viên phải hỏi lại hoặc thiếu thông tin bắt buộc. |
| 5 | **Vinpearl** | **AI-upgrade** | Nhân viên đặt phòng phải trả lời các yêu cầu nhiều ràng buộc như phòng cho gia đình có trẻ nhỏ, giờ đến muộn, đưa đón và combo vui chơi. Công cụ hỏi–đáp theo từ khóa khó tổng hợp chính sách và tình trạng dịch vụ thành một phương án phù hợp. |
| 6 | **VinWonders** | **Stakeholder Pain** | Khi thời tiết xấu hoặc một trò chơi tạm dừng, nhân viên vận hành phải cập nhật thủ công lịch hoạt động và hướng dẫn khách sang khu thay thế; thông tin giữa quầy, bảng điện tử và nhân viên hiện trường có thể không đồng nhất. |
| 7 | **VinFast** | **Tốn thời gian** | Nhân viên chuỗi cung ứng phải đọc email của nhà cung cấp, đối chiếu mã linh kiện, số lượng và ngày giao với đơn mua hàng để phát hiện thay đổi giao hàng; dữ liệu nằm trong cả email, PDF và ERP. |
| 8 | **Vinpearl** | **Lặp lại** | Bộ phận buồng phòng nhận danh sách phòng check-out/check-in rồi gọi hoặc nhắn tin để cập nhật trạng thái dọn phòng. Việc tổng hợp trạng thái thủ công làm lễ tân khó biết phòng nào sẵn sàng sớm. |

## Vì sao chọn ba bài toán #1, #2 và #3?

Ba bài toán này có actor rõ, xảy ra thường xuyên, đầu vào/đầu ra có thể kiểm tra và đại diện cho ba cách giải khác nhau: xử lý ngôn ngữ bằng **LLM**, hỗ trợ soạn thảo có **Human-in-the-loop**, và **Rule/optimization** không cần LLM. Nhờ vậy việc chọn kiến trúc dựa trên bản chất bài toán thay vì mặc định “có AI là dùng LLM”.

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

## Quick Problem Card #1 — Phân loại và chuyển tuyến phản ánh cư dân

| Trường | Nội dung |
|---|---|
| **Bài toán** | Tự động đọc, chuẩn hóa, phân loại và đề xuất nơi xử lý cho phản ánh của cư dân trên ứng dụng Vinhomes. |
| **Công ty thành viên** | **Vinhomes** |
| **Actor / Operator đang gặp khó khăn** | Nhân viên CSKH trực ticket là operator chính; Ban Quản lý/kỹ thuật bị ảnh hưởng khi ticket thiếu dữ liệu hoặc chuyển sai; cư dân bị ảnh hưởng khi phải chờ và cung cấp lại thông tin. |
| **Tần suất giả định để scoping** | Khoảng **150–300 ticket/khu đô thị/ngày**; cần xác nhận bằng log của hệ thống ticket. |

### Workflow thủ công hiện tại

`Cư dân nhập nội dung + ảnh` → `CSKH đọc và tra mã căn/khu vực` → `chọn loại sự cố và mức ưu tiên` → `kiểm tra thông tin còn thiếu` → `chuyển ticket tới đội phụ trách` → `soạn phản hồi xác nhận`

### Nút thắt

- Bước **đọc, phân loại, kiểm tra thiếu thông tin và chọn đội xử lý** mất ước tính **6–8 phút/ticket**.
- Nội dung có thể ngắn, sai chính tả hoặc chứa nhiều yêu cầu; ticket chuyển sai phải quay lại hàng đợi, làm trễ SLA.

### Bước AI tham gia

LLM đọc nội dung và mô tả ảnh (nếu có), trích xuất `khu/căn`, `loại sự cố`, `vị trí`, `mức khẩn cấp`, `thông tin còn thiếu`; sau đó đề xuất category và soạn câu xác nhận. Một lớp rule tra bảng `category → đội phụ trách`, kiểm tra quyền truy cập và bắt buộc chuyển các từ khóa an toàn như “cháy”, “khói”, “mắc kẹt thang máy” sang luồng khẩn cấp.

**Human-in-the-loop:** CSKH duyệt category, mức ưu tiên và nội dung phản hồi trước khi gửi. Hệ thống không tự kết luận trách nhiệm, hứa bồi thường hoặc đóng ticket.

### Metric thành công

- Giảm thời gian xử lý ban đầu trung vị từ **7 phút xuống ≤ 2 phút/ticket**.
- **≥ 90%** ticket được đề xuất đúng category/đội xử lý khi đối chiếu với kết quả cuối do CSKH xác nhận.
- Giảm tỷ lệ ticket bị chuyển lại do sai đội từ baseline đo được xuống **< 5%**.
- **100%** ticket khẩn cấp theo danh sách rule phải được đưa vào hàng đợi ưu tiên; không dùng LLM làm cơ chế duy nhất cho cảnh báo an toàn.

### Quick Architecture

| No AI | Rule | LLM | Agent |
|---|---|---|---|
| Không đủ cho văn bản tự do | Dùng cho cảnh báo, kiểm tra trường và routing sau phân loại | **Chọn — LLM feature + structured output + HITL** | Chưa cần; không cho phép tự gửi/chuyển/đóng ticket trong MVP |

**Luồng sơ bộ:** App cư dân → API ẩn dữ liệu không cần thiết → LLM trả JSON có confidence → rule kiểm tra/routing → màn hình CSKH duyệt → hệ thống ticket ghi nhận quyết định và feedback.

---

## Quick Problem Card #2 — Soạn nháp tóm tắt hồ sơ xuất viện

| Trường | Nội dung |
|---|---|
| **Bài toán** | Tạo bản nháp tóm tắt xuất viện từ dữ liệu đã có trong hồ sơ bệnh án điện tử, để bác sĩ rà soát và ký. |
| **Công ty thành viên** | **Vinmec** |
| **Actor / Operator đang gặp khó khăn** | Bác sĩ điều trị là operator và người chịu trách nhiệm cuối; điều dưỡng/bộ phận thủ tục và bệnh nhân bị ảnh hưởng nếu hồ sơ xuất viện hoàn tất chậm. |
| **Tần suất giả định để scoping** | Thử nghiệm tại **một khoa**, trên các ca có cấu trúc hồ sơ tương đối đồng nhất; chưa mở rộng toàn viện ở MVP. |

### Workflow thủ công hiện tại

`Bác sĩ mở hồ sơ` → `rà diễn biến, chẩn đoán, xét nghiệm, thủ thuật và thuốc` → `chọn thông tin quan trọng` → `gõ tóm tắt theo mẫu` → `đối chiếu lại nguồn` → `ký xác nhận`

### Nút thắt

- Hai bước **rà nhiều mục hồ sơ và gõ lại bản tóm tắt** mất ước tính **20–30 phút/ca**.
- Rủi ro chính không chỉ là chậm mà còn là bỏ sót hoặc chép sai thuốc, liều dùng, kết quả và mốc thời gian.

### Bước AI tham gia

LLM chỉ tạo **bản nháp** theo mẫu cố định từ các trường dữ liệu được cấp quyền; mỗi ý trong bản nháp phải kèm liên kết/citation về bản ghi nguồn và thời gian ghi nhận. Rule kiểm tra trường bắt buộc, dị ứng, đối chiếu tên thuốc–liều–đường dùng và đánh dấu xung đột để bác sĩ xem.

**Human-in-the-loop bắt buộc:** Bác sĩ phải xem nguồn, sửa và ký. AI không chẩn đoán mới, không đề xuất thuốc, không thay đổi đơn, không ký hay phát hành hồ sơ. Nếu dữ liệu thiếu/xung đột hoặc confidence thấp, hệ thống trả về mẫu trống có cảnh báo thay vì tự điền.

### Metric thành công

- Giảm thời gian từ lúc mở hồ sơ đến khi có bản sẵn sàng ký trung vị từ **25 phút xuống ≤ 10 phút/ca** trong pilot.
- **100%** câu chứa thuốc, xét nghiệm hoặc thủ thuật trong bản nháp có citation về dữ liệu nguồn.
- **0 lỗi nghiêm trọng** về tên thuốc, liều, dị ứng hoặc thủ thuật trong bộ kiểm thử trước triển khai; trong pilot, mọi lỗi đều được chặn trước khi phát hành nhờ bước bác sĩ duyệt.
- Tỷ lệ bác sĩ chấp nhận bản nháp sau chỉnh sửa nhẹ đạt **≥ 80%** sau 4 tuần pilot.

### Quick Architecture

| No AI | Rule | LLM | Agent |
|---|---|---|---|
| Mẫu tự điền xử lý được dữ liệu có cấu trúc nhưng không tóm tắt tốt diễn biến tự do | Dùng để validate trường bắt buộc và dữ liệu thuốc | **Chọn — LLM summarization có citation + HITL bắt buộc** | Không phù hợp vì rủi ro y khoa; không trao quyền tự hành |

**Luồng sơ bộ:** EHR (read-only, theo quyền) → chuẩn hóa/ẩn dữ liệu không cần thiết → LLM tạo draft có citation → rule validator → giao diện so sánh draft–nguồn → bác sĩ sửa và ký → audit log.

---

## Quick Problem Card #3 — Xếp xe vào điểm sạc cuối ca

| Trường | Nội dung |
|---|---|
| **Bài toán** | Đề xuất kế hoạch ghép xe Xanh SM với điểm và khung giờ sạc cuối ca dựa trên dữ liệu vận hành có cấu trúc. |
| **Công ty thành viên** | **Xanh SM (GSM)** |
| **Actor / Operator đang gặp khó khăn** | Điều phối viên đội xe là operator chính; tài xế ca sau và nhân viên trạm sạc bị ảnh hưởng khi xe chưa đủ pin hoặc nhiều xe đến cùng lúc. |
| **Đơn vị xử lý giả định** | Một đợt phân công **30–50 xe** tại một depot/ca; cần đo lại theo quy mô đội xe thực tế. |

### Workflow thủ công hiện tại

`Xuất danh sách xe và % pin` → `xem lịch nhận xe ca kế tiếp` → `gọi/nhắn trạm để hỏi chỗ trống` → `lọc xe cần sạc` → `ghép xe–trạm–khung giờ trên bảng tính` → `gửi danh sách cho tài xế`

### Nút thắt

- Bước **đối chiếu bốn nguồn và ghép lịch** mất ước tính **20–30 phút/đợt 30–50 xe**.
- Khi trạng thái trạm thay đổi, điều phối viên phải sửa nhiều dòng; các quyết định không nhất quán giữa các ca.

### Bước hệ thống thông minh tham gia

Không cần LLM. Bộ tối ưu nhận dữ liệu có cấu trúc gồm `SOC`, vị trí xe, quãng đường dự kiến, giờ nhận ca sau, công suất/số khe trạm và thời gian sạc dự kiến. Rule loại các phương án vi phạm ngưỡng an toàn; thuật toán tối ưu xếp lịch để giảm tổng quãng đường rỗng và thời gian chờ. Điều phối viên xem lý do, sửa nếu cần rồi mới phát hành.

**Human-in-the-loop:** Điều phối viên phê duyệt kế hoạch và xử lý ngoại lệ như xe lỗi, trạm mất kết nối hoặc nhu cầu điều xe đột xuất. Khi thiếu dữ liệu thời gian thực, fallback là bảng tính hiện tại.

### Metric thành công

- Giảm thời gian lập kế hoạch từ **25 phút xuống ≤ 5 phút/đợt 30–50 xe**.
- **≥ 95%** xe được phân công đáp ứng ngưỡng pin mục tiêu trước giờ nhận ca kế tiếp.
- Giảm thời gian chờ sạc trung vị ít nhất **30% so với baseline 2 tuần** tại depot pilot.
- **100%** phương án đề xuất không vi phạm các hard constraint đã cấu hình (giờ nhận ca, khe sạc, ngưỡng pin dự phòng).

### Quick Architecture

| No AI | Rule | LLM | Agent |
|---|---|---|---|
| Bảng tính thủ công là fallback | **Chọn — rules + constraint optimization** | Không cần vì đầu vào/đầu ra đều có cấu trúc | Chưa cần; tự động gửi lệnh cho xe/tài xế làm tăng rủi ro vận hành |

**Luồng sơ bộ:** Fleet/telematics + lịch ca + trạng thái trạm → kiểm tra chất lượng dữ liệu → rule tạo hard constraints → solver tối ưu → điều phối viên duyệt/chỉnh → gửi kế hoạch → ghi nhận kết quả để đo KPI.

---

# Kết luận quick-assess

| Ưu tiên | Bài toán | Giá trị kỳ vọng | Khả thi dữ liệu | Rủi ro | Kiến trúc đề xuất |
|---:|---|---|---|---|---|
| 1 | Vinhomes — phân loại phản ánh | Cao, tần suất lớn, dễ đo | Khá cao nếu có lịch sử ticket | Trung bình | **LLM + Rule + HITL** |
| 2 | Xanh SM — xếp lịch sạc | Cao, ảnh hưởng trực tiếp vận hành | Cao nếu API trạng thái trạm đủ tin cậy | Thấp–trung bình | **Rule + optimization** |
| 3 | Vinmec — tóm tắt xuất viện | Cao nhưng cần pilot hẹp | Trung bình, phụ thuộc chất lượng EHR | Cao | **LLM có citation + HITL bắt buộc** |

**Đề xuất để deep-dive:** Chọn bài toán **Vinhomes phân loại và chuyển tuyến phản ánh cư dân**. Scope MVP đủ hẹp để thử nghiệm, có tập ticket lịch sử để đánh giá offline, metric rõ và sai sót có thể kiểm soát bằng bước duyệt của CSKH. Trước khi bắt đầu, cần lấy mẫu 100 ticket, đo thời gian xử lý thực tế, thống nhất taxonomy category/đội phụ trách và xác định danh sách tình huống khẩn cấp phải đi bằng rule.
