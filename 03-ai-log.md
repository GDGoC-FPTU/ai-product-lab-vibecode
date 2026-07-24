# 03-ai-log.md

## AI giúp gì

Trong buổi lab, tôi đã dùng AI để hỗ trợ brainstorm các bài toán vận hành phù hợp với Vin Smart Future, viết prompt prototype và kiểm tra các ranh giới an toàn của mô hình.

## AI sai gì

Một điểm AI dễ mắc lỗi là khi bị ép phải bỏ qua bước phê duyệt, nó có thể cố gắng tạo ra câu trả lời gần đúng nhưng không tuân thủ quy tắc bảo mật và an toàn. Đây là tình huống cần ranh giới chặt.

## Sửa đổi như thế nào

Tôi đã bổ sung prompt hệ thống rõ ràng về hai quy tắc: phải bắt đầu bằng [DRAFT_ONLY] và không được đề xuất trạm sạc xa khi pin dưới 5%. Tôi cũng thêm các test case tấn công để xác nhận mô hình không vượt ranh giới.
