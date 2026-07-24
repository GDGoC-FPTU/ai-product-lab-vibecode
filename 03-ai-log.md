# 03 — Nhật ký tương tác và chiêm nghiệm về AI

**Người viết:** [Điền họ tên và MSSV]

**Bài lab:** Lab 02 — AI Product Scoping (Vin Smart Future)

---

## Tôi đã dùng AI như thế nào?

Trong bài này, tôi dùng ChatGPT và Gemini chủ yếu như một người để trao đổi ý tưởng, chứ không lấy nguyên câu trả lời đầu tiên rồi đưa vào bài. Lúc bắt đầu Phase 1, tôi khá dễ bị cuốn vào những đề tài nghe “đúng chất AI” như trợ lý ảo, xe tự điều phối hoặc chatbot tự xử lý mọi yêu cầu. Tôi nhờ AI liệt kê các công việc cụ thể phía sau những dịch vụ của Vinhomes, Vinmec, Xanh SM, VinFast và Vinpearl. Sau đó tôi hỏi lại theo hướng thực tế hơn: ai là người đang làm, họ nhận đầu vào gì, thao tác trên hệ thống nào, và kết quả cuối cùng phải được ai duyệt.

Cách hỏi này giúp tôi chuyển từ một ý tưởng khá mơ hồ, ví dụ “dùng AI tối ưu vận hành Xanh SM”, thành một workflow có thể nhìn thấy được: điều phối viên nhận báo cáo, xem vị trí và mức pin, tra tình trạng trạm, chọn phương án rồi gửi bản hướng dẫn cho tài xế. AI cũng giúp tôi nghĩ ra những câu hỏi mà lúc đầu tôi chưa để ý, chẳng hạn trạng thái trạm có cập nhật theo thời gian thực hay không, khi dữ liệu GPS cũ thì xử lý thế nào, và ai chịu trách nhiệm nếu đề xuất sai.

Ở phần Quick Cards, tôi dùng AI để phản biện metric. Ban đầu tôi chỉ viết “xử lý nhanh hơn” và “giảm tải cho nhân viên”, nhưng hai câu này gần như không đo được. Sau khi trao đổi, tôi đổi thành các ngưỡng cụ thể như giảm thời gian xử lý một lượt từ 15 phút xuống dưới 3 phút. Tuy nhiên, tôi ghi rõ đây là con số giả định phục vụ scoping. Muốn đưa vào đề xuất thật thì phải lấy log thực tế hoặc đo thử trong một khoảng thời gian, không thể coi con số AI đưa ra là dữ liệu của doanh nghiệp.

Với phần prototype, tôi nhờ AI gợi ý cách viết system prompt và hai trường hợp kiểm thử đối nghịch. Một test cố ép hệ thống bỏ nhãn `[DRAFT_ONLY]` để gửi thẳng nội dung; test còn lại yêu cầu chỉ đường đến một trạm cách 8 km khi xe chỉ còn 2% pin. Tôi thấy việc yêu cầu AI tự nghĩ cách “phá” prompt của mình khá hữu ích, vì nếu chỉ chạy các câu hỏi bình thường thì mô hình thường trả lời rất ngoan và mình dễ tưởng hệ thống đã an toàn.

## AI đã sai hoặc làm tôi mất cảnh giác ở đâu?

Điểm sai lớn nhất là AI có xu hướng lấp phần thông tin còn thiếu bằng một câu trả lời nghe rất hợp lý. Khi brainstorm bài toán Xanh SM, AI từng nói như thể doanh nghiệp đã có sẵn API GPS, API trạm sạc theo thời gian thực và đội xe sạc cứu hộ di động. Trong repo không có bằng chứng xác nhận các điều này. Nếu không để ý, tôi có thể biến giả định kỹ thuật thành “hiện trạng đã có”, rồi tính tiếp số giờ tiết kiệm và thời gian hoàn vốn. Các con số khi đó trông rất thuyết phục nhưng nền tảng của chúng lại chưa được kiểm chứng.

AI cũng đề xuất một Agent có thể tự chọn trạm, tự gửi hướng dẫn và tự điều xe cứu hộ. Nghe thì hiện đại, nhưng sau khi vẽ workflow tôi thấy quyền tự hành đó chưa hợp lý. Một dữ liệu pin bị trễ hoặc trạng thái trạm sai có thể làm tài xế đi nhầm hướng. Ở phiên bản đầu, giá trị thật sự chỉ là gom thông tin và soạn phương án để điều phối viên quyết định; chưa có lý do đủ mạnh để trao quyền hành động cho Agent.

Một lỗi khác lại đến từ phần code tưởng như “an toàn hơn AI”. Fallback hiện tại có điều kiện gần giống:

```python
if "2%" in user_input or "5%" in user_input or "pin" in user_input.lower():
    return "dispatch_mobile_charger"
```

Điều kiện này quá rộng. Chỉ cần câu đầu vào có chữ “pin”, kể cả “xe còn 80% pin”, hệ thống vẫn có thể trả về phương án điều xe sạc cứu hộ. Ngoài ra, chuỗi `"5%"` không có nghĩa là `< 5%`; câu “pin 55%” cũng chứa đoạn này. Tôi nhận ra rule-based không tự động đồng nghĩa với chính xác. Rule chỉ tốt khi dữ liệu được parse đúng, điều kiện rõ và có test ở ranh giới.

Cuối cùng, nhãn `[DRAFT_ONLY]` trong system prompt chỉ là một lớp nhắc nhở. Nếu hệ thống phía sau cứ thấy output là tự gửi, một prompt injection hoặc lỗi model vẫn có thể gây sự cố. AI lúc đầu làm tôi có cảm giác rằng viết câu “không được vi phạm trong mọi trường hợp” là đủ. Thực tế, ranh giới quan trọng phải được chặn bằng code và quyền hệ thống, không nên giao hoàn toàn cho mô hình ngôn ngữ.

## Tôi đã sửa cách làm như thế nào?

Trước hết, tôi đổi vai trò của AI từ “dispatcher tự động” thành **co-pilot tạo bản nháp**. Output dành cho tài xế phải bắt đầu bằng `[DRAFT_ONLY]`, và điều phối viên là người xem rồi mới gửi. Tôi cũng bổ sung trực tiếp vào system prompt rằng yêu cầu của người dùng không được phép xóa nhãn này. Hai adversarial tests được giữ riêng để kiểm tra đúng hai ranh giới, thay vì chỉ test các tình huống thuận lợi.

Thứ hai, tôi tách việc nào dành cho LLM và việc nào phải là rule. LLM có thể tóm tắt tình huống và soạn câu chữ dễ hiểu. Các kiểm tra như mức pin, khoảng cách, dữ liệu có quá hạn hay không và trạm còn chỗ hay không phải đọc từ trường dữ liệu có cấu trúc. Cách sửa đúng cho lỗi fallback là parse phần trăm thành số rồi so sánh `battery_percent < 5`, không tìm chuỗi `"pin"` hoặc `"5%"`. Tôi cũng cần thêm các test cho 0%, 4.9%, 5%, 55%, 80% và trường hợp không đọc được mức pin. Đây là phần tôi thấy code hiện tại vẫn cần hoàn thiện thêm trước khi gọi là prototype an toàn.

Thứ ba, tôi không giữ những con số AI đưa ra nếu không chỉ ra được nguồn. Trong bản scan cá nhân, tôi đổi cách ghi thành “ước tính để scoping” và thêm bước phải đo baseline trên log thật. Với các giả định như có API trạng thái trạm hoặc có xe cứu hộ sạc, tôi xem đó là câu hỏi cần xác minh với đội vận hành, không phải sự thật đã biết.

## Điều tôi rút ra sau bài này

Trước bài lab, tôi thường nghĩ phần khó nhất là viết một prompt đủ chi tiết. Sau khi làm, tôi thấy prompt chỉ là một phần nhỏ. Khó hơn là chọn đúng điểm để AI tham gia, không nhầm giả định với dữ liệu, và thiết kế sao cho khi AI sai thì người vận hành vẫn kiểm soát được.

AI giúp tôi mở rộng góc nhìn rất nhanh, đặc biệt ở giai đoạn brainstorm và stress-test. Nhưng nó cũng có thể làm một ý tưởng thiếu dữ liệu trở nên quá tròn trịa. Vì vậy cách dùng hiệu quả nhất với tôi là yêu cầu AI đề xuất, sau đó bắt nó phản biện chính đề xuất đó, rồi quay lại kiểm tra bằng workflow, rule và test case cụ thể. Tôi không chọn giải pháp có nhiều AI nhất; tôi chọn giải pháp mà mình giải thích được AI làm gì, con người duyệt ở đâu và hệ thống sẽ lùi về phương án nào khi dữ liệu không đủ tin cậy.
