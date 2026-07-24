# 03 - AI Log & Reflection

## Thông tin nhóm
- Tên nhóm: vibecode
- Thành viên: 
  - Nguyễn Văn Hưng – 2A202601251
  - Vũ Bình Minh – MSSV 2A202601295
  - Lê Thị Thúy – MSSV 2A202601381

## AI đã giúp gì?
Trong quá trình làm lab, tôi sử dụng AI để hỗ trợ brainstorm các bài toán vận hành, xây dựng prompt cho prototype và kiểm tra các trường hợp tấn công prompt. AI giúp tôi rút ngắn thời gian viết cấu trúc prompt và đề xuất các quy tắc an toàn rõ ràng hơn.

## AI sai gì?
Một điểm AI dễ mắc lỗi là khi người dùng cố tình yêu cầu bỏ qua các quy tắc, hệ thống có thể vẫn cố gắng trả lời theo hướng không an toàn. Trong một số trường hợp, AI cũng có thể hiểu sai ngữ cảnh và đề xuất trạm sạc không phù hợp nếu không có ranh giới chặt.

## Tôi đã sửa đổi như thế nào?
Tôi đã bổ sung các quy tắc rõ ràng vào prompt, bắt buộc tiền tố [DRAFT_ONLY] và ép trường hợp pin dưới 5% phải chuyển sang dispatch_mobile_charger. Ngoài ra, tôi còn thêm các test case tấn công để kiểm tra xem hệ thống có giữ đúng boundary hay không.

## Nhận xét cá nhân
AI rất hữu ích như một trợ lý hỗ trợ tư duy, nhưng cần được điều khiển bằng ràng buộc và kiểm thử chặt chẽ. Với bài toán vận hành thực tế, yếu tố an toàn và con người phê duyệt vẫn là điều bắt buộc.
