# Day 06 · Data Ingestion Engineering

**Lab cá nhân** · **4 giờ** · **Dữ liệu tự chọn**

Biến tài liệu thành kho tri thức có thể truy xuất cho AI agent, rồi đo xem cách chuẩn bị dữ liệu nào hiệu quả nhất.

| 📄 Dữ liệu | 🧩 Chiến lược | 🎯 Benchmark |
|---|---|---|
| Tối thiểu **30 trang nội dung** | Tối thiểu **3 cấu hình** | Tối thiểu **20 câu hỏi** |

## Hướng dẫn setup & chạy pipeline (Bài nộp Đỗ Hoàng Phúc — 2A202603652)

### 1. Dữ liệu & cấu trúc chính
- **Corpus:** `data/Introduction_to_Python_Programming-WEB.pdf` (*Introduction to Python Programming*, OpenStax, Chương 1–2, `59` trang PDF nội dung hợp lệ `[17–45, 47–76]`, giấy phép CC BY-NC-SA 4.0) — chi tiết tại [data/manifest.json](data/manifest.json).
- **Benchmark:** `25` câu hỏi (`18 dev` / `7 test`, trong đó `5` câu kiểm tra metadata filter) tại [benchmark/questions.json](benchmark/questions.json).
- **Mã nguồn pipeline:** nằm trong [starter/src/](starter/src/) (`ingestion.py`, `chunking.py`, `embeddings.py`, `store.py`, `evaluation.py`, `run.py`).
- **Kết quả, nhãn audit & báo cáo:**
  - Nhật ký cấu hình & chỉ số: [artifacts/experiment_log.csv](artifacts/experiment_log.csv)
  - Kết quả đo tự động & trace Top-3: [results/metrics_summary.json](results/metrics_summary.json), [results/traces_all_strategies.json](results/traces_all_strategies.json)
  - Nhãn chấm thủ công đã chốt: [results/manual_audit_workbook.md](results/manual_audit_workbook.md)
  - Báo cáo cá nhân: [report/individual/2A202603652_DoHoangPhuc.md](report/individual/2A202603652_DoHoangPhuc.md)

### 2. Yêu cầu môi trường & cài đặt
Cần **Python 3.11+**, **Docker Desktop** (cho PostgreSQL 16 + pgvector 0.8.7) và API key **Google AI Studio (`GEMINI_API_KEY`)** để gọi model `gemini-embedding-001` (`3072` chiều).

Chạy các lệnh sau từ thư mục `starter/`:

```powershell
cd starter
python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
pip install google-genai==3.3.0

Copy-Item .env.example .env
# Mở starter/.env, kiểm tra DATABASE_URL (mặc định 127.0.0.1:55433) và điền GEMINI_API_KEY=...
```

*(Trên macOS/Linux dùng `source .venv/bin/activate` và `cp .env.example .env`.)*

### 3. Khởi động database & chạy toàn bộ pipeline
```powershell
docker compose -p day6_student_starter up -d --wait
python scripts/check_setup.py

python -m src.run
```

Lệnh `python -m src.run` thực hiện tuần tự: đọc và chuẩn hóa `59` trang PDF -> chạy 4 chiến lược (`A_fixed_500_50`, `B_paragraph_500`, `C_paragraph_500_filtered`, `D_recursive_650_100_filtered`) -> tạo/lấy vector từ cache SHA-256 (`temp/embedding_cache.jsonl`) hoặc gọi Gemini API -> upsert idempotent vào PostgreSQL + `pgvector` -> truy vấn Top-3 và xuất lại `results/metrics_summary.json`, `results/traces_all_strategies.json`, `results/manual_audit_packets.md`.

Để dừng container khi xong việc (vẫn giữ dữ liệu DB):
```powershell
docker compose -p day6_student_starter stop
```

---

## Bắt đầu nhanh (Đề bài gốc)

Dùng [starter PostgreSQL + pgvector](starter/README.md) để dựng database và hoàn thiện các hàm TODO, hoặc tự chọn vector store tương đương. Starter chỉ là khung: **bạn tự hiện thực pipeline và benchmark**.

## 1. Xây pipeline

![Đọc tài liệu, chuẩn hóa, chia chunk, tạo vector, lưu và kiểm tra](assets/ingestion-pipeline.svg)

Chọn tài liệu được phép sử dụng; giữ **ID tài liệu, nguồn, trang/vị trí** và metadata phù hợp. Dùng embedding model thật qua API hoặc chạy local; lưu và truy xuất bằng pgvector, Qdrant, Chroma hoặc một store tương đương.

## 2. So sánh và đánh giá

![Ba chiến lược được đánh giá trên cùng corpus và benchmark dev/test](assets/benchmark-workflow.svg)

Dùng cùng dữ liệu, model và câu hỏi cho cả ba cấu hình. Tách **15 câu dev / 5 câu test** trước khi chạy; chọn cấu hình trên dev, rồi đánh giá test sau khi cố định. Mỗi câu hỏi cần có đoạn bằng chứng và trang nguồn; thiết kế bộ câu hỏi và đánh giá theo [BENCHMARK.md](BENCHMARK.md).

Đánh giá theo năm khía cạnh: **độ chính xác truy xuất**, **tính mạch lạc của chunk**, **tính hữu dụng của metadata**, **chất lượng grounding** và **tác động của chiến lược dữ liệu**. Giải thích lựa chọn bằng kết quả, ví dụ lỗi và các đánh đổi.

## 3. Chuẩn bị bài nộp

1. Chạy pipeline và lưu cấu hình, kết quả top-3, trace cùng nhãn đánh giá thủ công.
2. Điền [thông tin học viên](STUDENT.md), [nhật ký thí nghiệm](artifacts/experiment_log.csv) và bản sao [mẫu báo cáo cá nhân](report/individual/MSSV_HoTen.md).
3. Kiểm tra mã nguồn, cách chạy, manifest dữ liệu và checklist trong [SUBMISSION.md](SUBMISSION.md).

## Tài liệu hướng dẫn

| Bạn cần tìm | Tài liệu |
|---|---|
| Setup baseline PostgreSQL + pgvector | [starter/README.md](starter/README.md) |
| Các bước làm và cách tính chỉ số | [GUIDE.md](GUIDE.md) |
| Tiến độ trong 4 giờ | [CHECKPOINTS.md](CHECKPOINTS.md) |
| Năm tiêu chí benchmark và bộ câu hỏi | [BENCHMARK.md](BENCHMARK.md) |
| Tiêu chí chấm điểm | [RUBRIC.md](RUBRIC.md) |
| Quy tắc sử dụng dữ liệu, AI và API | [RULES.md](RULES.md) |
| Cách nộp bài | [SUBMISSION.md](SUBMISSION.md) |

[data/format-example.json](data/format-example.json) chỉ minh họa định dạng, không phải corpus đủ điều kiện. Phần xử lý và benchmark do bạn tự hiện thực; không bắt buộc xây chatbot.
