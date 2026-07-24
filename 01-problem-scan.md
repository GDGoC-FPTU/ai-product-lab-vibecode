# Phase 1 & 2: Problem Scan & Quick Cards — Vin Smart Future

**Học viên / Tác giả:** Nguyễn Văn A (MSSV: 24020001)  
**Nhóm:** Vin Smart Future - Lab 02  
**Công ty mục tiêu:** Vin Smart Future (Vingroup)  

---

# 🔍 Phase 1 — SCAN: Bảng Quét Cơ Hội Tối Ưu AI

Dưới đây là 6 bài toán vận hành thực tế được phát hiện thông qua việc sử dụng **4 Lenses** quét qua các công ty thành viên thuộc Vingroup:

| # | Công ty thành viên | Lens áp dụng | Mô tả bài toán & Nút thắt vận hành (Bottleneck) |
|---|--------------------|--------------|------------------------------------------------|
| 1 | **Xanh SM (GSM)** | **Tốn thời gian** | Điều phối viên xử lý thủ công các báo cáo khẩn cấp từ tài xế xe taxi điện về sự cố sạc pin hoặc cạn pin thực địa (mất 12-15 phút/lượt). |
| 2 | **VinFast** | **Lặp lại** | Tra cứu, đối chiếu và so khớp thủ công hóa đơn sạc điện hằng tuần của người dùng tại các trạm sạc đối tác thứ 3. |
| 3 | **Vinhomes** | **AI-upgrade** | Phân loại tự động và điều hướng (route) phản hồi / khiếu nại của cư dân trên App Vinhomes Resident (hiện tại CSKH trả lời rập khuôn, trễ SLA 12 tiếng). |
| 4 | **Vinmec** | **Pain từ người khác** | Bác sĩ mất quá nhiều thời gian viết tóm tắt hồ sơ bệnh án xuất viện (mất 20-30 phút/bệnh nhân, bác sĩ phàn nàn vì khối lượng hành chính quá tải). |
| 5 | **Vinpearl / VinWonders** | **AI-upgrade** | Tư vấn tự động lịch trình vui chơi và đặt phòng cá nhân hóa theo thời gian thực cho du khách (chatbot hiện tại chưa hiểu ngữ cảnh phức tạp). |
| 6 | **Xanh SM (GSM)** | **Lặp lại** | Tóm tắt lý do khách hàng hủy chuyến từ cuộc gọi ghi âm và ghi chú của tài xế để phân tích pattern lỗi hệ thống. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Từ 6 bài toán ở Phase 1, 3 bài toán tiềm năng nhất được lựa chọn để phân tích bằng **Quick Problem Cards**:

---

## 📌 QUICK PROBLEM CARD #1

```text
┌───────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                     │
│                                                                           │
│ Bài toán: Tài xế Xanh SM báo cáo sự cố pin / hết pin khẩn cấp thực địa   │
│ cần chỉ hướng trạm sạc trống hoặc điều động xe sạc cứu hộ di động.        │
│ Công ty thành viên: [x] Xanh SM (GSM)                                     │
│                                                                           │
│ Ai đang đau (Actor)? Tài xế (lo lắng cạn pin), Điều phối viên (quá tải)   │
│                                                                           │
│ Workflow thủ công hiện tại (5 bước):                                      │
│   1. Tài xế gọi điện / báo khẩn cấp lên tổng đài điều vận Xanh SM.        │
│   ──> 2. Điều phối viên tra cứu vị trí GPS hiện tại của xe trên bản đồ.   │
│   ──> 3. Tra cứu thủ công các trạm sạc VinFast lân cận còn trụ trống.     │
│   ──> 4. Soạn thảo tin nhắn SMS / App chỉ đường gửi cho tài xế.           │
│   ──> 5. Liên hệ đội xe cứu hộ pin di động nếu pin xe báo dưới 5%.        │
│                                                                           │
│ Bước tốn thời gian nhất? Bước 3 & 4 (⏱ 10 phút/lượt)                       │
│ AI nhảy vào ở bước nào? Bước 3 & 4 (Tự động lấy vị trí -> gợi ý trạm sạc   │
│ trống phù hợp -> Soạn nháp tin nhắn chỉ đường [DRAFT_ONLY]).             │
│                                                                           │
│ Metric đo thành công:                                                     │
│   Giảm tổng thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút.             │
│                                                                           │
│ Quick Architecture: [x] LLM Feature (Tự động hóa soạn draft chỉ dẫn)      │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## 📌 QUICK PROBLEM CARD #2

```text
┌───────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                     │
│                                                                           │
│ Bài toán: Tự động phân loại và route yêu cầu hỗ trợ cư dân Vinhomes.      │
│ Công ty thành viên: [x] Vinhomes                                          │
│                                                                           │
│ Ai đang đau (Actor)? Cư dân Vinhomes (chờ phản hồi), Ban Quản Lý (quá tải) │
│                                                                           │
│ Workflow thủ công hiện tại (4 bước):                                      │
│   1. Cư dân gửi phản hồi / khiếu nại lên App Vinhomes Resident.           │
│   ──> 2. Nhân viên CSKH đọc thủ công và phân loại bài toán (kỹ thuật, phí)│
│   ──> 3. Chuyển tiếp ticket đến bộ phận kỹ thuật / kế toán tương ứng.     │
│   ──> 4. CSKH viết email phản hồi lại cư dân sau khi có kết quả.          │
│   ──> 5. Đóng ticket trên hệ thống.                                       │
│                                                                           │
│ Bước tốn thời gian nhất? Bước 2 & 4 (⏱ 15 phút/ticket)                    │
│ AI nhảy vào ở bước nào? Bước 2 & 4 (Đọc hiểu văn bản -> Phân loại ticket  │
│ -> Tạo draft email phản hồi chuẩn chỉnh).                                 │
│                                                                           │
│ Metric đo thành công:                                                     │
│   Rút ngắn thời gian phản hồi ban đầu từ 12 giờ ──> dưới 15 phút.         │
│                                                                           │
│ Quick Architecture: [x] LLM Feature (Text Classification & Response Draft) │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## 📌 QUICK PROBLEM CARD #3

```text
┌───────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                     │
│                                                                           │
│ Bài toán: Tóm tắt thông tin hồ sơ xuất viện y tế cho bác sĩ Vinmec.        │
│ Công ty thành viên: [x] Vinmec                                            │
│                                                                           │
│ Ai đang đau (Actor)? Bác sĩ điều trị (tốn thời gian nhập liệu hành chính)  │
│                                                                           │
│ Workflow thủ công hiện tại (4 bước):                                      │
│   1. Bác sĩ rà soát toàn bộ kết quả xét nghiệm, đơn thuốc, tiến trình bệnh│
│   ──> 2. Bác sĩ gõ tay bản tóm tắt bệnh án xuất viện.                     │
│   ──> 3. Đánh giá tình trạng sức khỏe xuất viện & dặn dò bệnh nhân.        │
│   ──> 4. In ấn và ký tên xác nhận hồ sơ xuất viện.                        │
│                                                                           │
│ Bước tốn thời gian nhất? Bước 1 & 2 (⏱ 20-30 phút/bệnh nhân)              │
│ AI nhảy vào ở bước nào? Bước 1 & 2 (Tóm tắt hồ sơ y tế -> Tạo draft summary│
│ để bác sĩ chỉ cần review và chỉnh sửa).                                   │
│                                                                           │
│ Metric đo thành công:                                                     │
│   Giảm thời gian lập hồ sơ xuất viện từ 25 phút ──> dưới 5 phút.          │
│                                                                           │
│ Quick Architecture: [x] LLM Feature (Summarization + HITL verification)   │
└───────────────────────────────────────────────────────────────────────────┘
```
