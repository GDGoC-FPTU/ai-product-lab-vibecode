import os
from PIL import Image, ImageDraw, ImageFont

# Create a clean workflow diagram image for Xanh SM Current-State Workflow
width, height = 1200, 650
image = Image.new("RGB", (width, height), color=(248, 249, 250))
draw = ImageDraw.Draw(image)

# Draw Title Header
draw.rectangle([(0, 0), (width, 80)], fill=(13, 110, 253))
draw.text((30, 25), "XANH SM (GSM) — CURRENT-STATE WORKFLOW DIAGRAM", fill=(255, 255, 255))
draw.text((780, 25), "Vin Smart Future Lab 02", fill=(220, 240, 255))

# Subtitle
draw.text((30, 95), "Quy trinh xu ly su co sac pin thuc dia cua Dieu phoi vien Xanh SM (Tong thoi gian: 15 phut/luot)", fill=(50, 50, 50))

# Workflow Boxes Data
boxes = [
    {"title": "Buc 1: Nhan Call", "sub": "Tài xế gọi báo hết pin", "who": "Dispatcher | ⏱ 2 min", "color": (230, 240, 255), "border": (13, 110, 253), "x": 40, "y": 160},
    {"title": "Buc 2: Tra GPS 🔄", "sub": "Handoff: Tra vị trí xe", "who": "Dispatcher | ⏱ 2 min", "color": (230, 240, 255), "border": (13, 110, 253), "x": 270, "y": 160},
    {"title": "Buc 3: Tra Tram Sac 🔴", "sub": "Bottleneck: Tra trụ trống", "who": "Dispatcher | ⏱ 5 min", "color": (255, 235, 235), "border": (220, 53, 69), "x": 500, "y": 160},
    {"title": "Buc 4: Soan Draft SMS 🔴", "sub": "Bottleneck: Gõ tin nhắn", "who": "Dispatcher | ⏱ 5 min", "color": (255, 235, 235), "border": (220, 53, 69), "x": 730, "y": 160},
    {"title": "Buc 5: Goi Cuu Ho", "sub": "Điều xe cứu hộ pin (<5%)", "who": "Dispatcher | ⏱ 1 min", "color": (230, 240, 255), "border": (13, 110, 253), "x": 960, "y": 160},
]

bw, bh = 190, 140

for b in boxes:
    x, y = b["x"], b["y"]
    # Draw box container
    draw.rectangle([(x, y), (x + bw, y + bh)], fill=b["color"], outline=b["border"], width=3)
    # Header text
    draw.text((x + 10, y + 15), b["title"], fill=(0, 0, 0))
    draw.line([(x + 5, y + 45), (x + bw - 5, y + 45)], fill=b["border"], width=1)
    # Sub & Who
    draw.text((x + 10, y + 55), b["sub"], fill=(60, 60, 60))
    draw.text((x + 10, y + 95), b["who"], fill=(100, 100, 100))

# Draw Arrows connecting boxes
for i in range(len(boxes) - 1):
    x1 = boxes[i]["x"] + bw
    y1 = boxes[i]["y"] + bh // 2
    x2 = boxes[i+1]["x"]
    y2 = boxes[i+1]["y"] + bh // 2
    draw.line([(x1, y1), (x2, y2)], fill=(100, 100, 100), width=3)
    # Arrow head
    draw.polygon([(x2, y2), (x2 - 10, y2 - 6), (x2 - 10, y2 + 6)], fill=(100, 100, 100))

# Legend & Metrics Box at bottom
draw.rectangle([(40, 340), (1150, 600)], fill=(255, 255, 255), outline=(200, 200, 200), width=2)
draw.text((60, 360), "GHI CHU & METRICS DIEM NGHEN (BOTTLENECKS):", fill=(0, 0, 0))

draw.rectangle([(60, 400), (80, 420)], fill=(255, 235, 235), outline=(220, 53, 69), width=2)
draw.text((95, 403), "🔴 Bottlenecks: Buoc 3 & Buoc 4 ngon 10/15 phut do tra cuu tru sac thu cong & go tay tin nhan.", fill=(180, 0, 0))

draw.rectangle([(60, 440), (80, 460)], fill=(230, 240, 255), outline=(13, 110, 253), width=2)
draw.text((95, 443), "🔄 Handoff: Chuyen giao thong tin giua Tai xe - Tong dai Dieu van - Dashboard Tram sac VinFast.", fill=(0, 80, 180))

draw.text((60, 490), "KPI HIEN TAI: 15 phut/luot xu ly su co | 80 su co/ngay | Lang phi 20 gio dieu van/ngay", fill=(50, 50, 50))
draw.text((60, 520), "MUC TIEU FUTURE-STATE AI: Giam thoi gian xu ly xuong < 3 phut/luot (Tiet kiem 80% thoi gian)", fill=(40, 147, 86))

# Save image
output_path = "04-workflow-diagram.png"
image.save(output_path)
print(f"Diagram successfully generated at: {output_path}")
