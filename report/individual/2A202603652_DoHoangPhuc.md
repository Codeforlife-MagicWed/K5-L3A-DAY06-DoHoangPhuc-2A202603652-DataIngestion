# Báo cáo cá nhân — Day 6

- **Họ và tên:** Đỗ Hoàng Phúc (`MSSV: 2A202603652`, lớp `L3A`)
- **Chủ đề & Corpus:** Lập trình Python cơ bản (*Introduction to Python Programming*, OpenStax, Chương 1–2)

---

## Dữ liệu và pipeline

- **Chủ đề, nguồn/quyền, số trang và quy tắc tính trang:**
  - Nguồn: Giáo trình mở *Introduction to Python Programming* (OpenStax, Rice University, phiên bản WEB PDF ©2026, tác giả Udayan Das et al., `isbn_13: 978-1-961584-45-7`, tải tại `https://openstax.org/details/books/introduction-python-programming`, đường dẫn local `data/Introduction_to_Python_Programming-WEB.pdf`, truy cập `2026-11-13`).
  - Giấy phép: **CC BY-NC-SA 4.0** (cho phép sử dụng, trích xuất và phân phối lại phi thương mại kèm ghi công OpenStax).
  - Phạm vi & quy tắc tính trang ([manifest.json](../../data/manifest.json)): Chọn **dải trang vật lý PDF `[17, 76]`** tương ứng Chương 1 (*1 Statements*, trang sách `7–35`) và Chương 2 (*2 Expressions*, trang sách `37–66`, quy tắc `book_page = pdf_page - 10`). Loại trang bìa/mục lục (`1–16`), các chương sau (`77–397`) và **trang trống `46`** (trang sách `36`, chỉ chứa `156` ký tự thô gồm running header `'36 1 • Statements'` và footer `'Access for free at openstax.org'`, sau chuẩn hóa còn `0` ký tự). Kết quả thu được **59 trang nội dung hợp lệ** (`29` trang Chương 1 + `30` trang Chương 2), tổng cộng **87.783 ký tự đã chuẩn hóa** (`ingest_seconds = 2.998s`).

- **Chuẩn hóa, lỗi và giới hạn:**
  - Bộ đọc [`starter/src/ingestion.py`](../../starter/src/ingestion.py) dùng `pypdf==6.21.4` với `extract_text(extraction_mode="layout")`, chuẩn hóa Unicode **NFC**, loại running header/footer ở đầu-cuối mỗi trang và tách lại thành đoạn văn / bảng Markdown (`| col | col |`).
  - Xử lý layout 2 cột / bảng trong sách OpenStax bằng thuật toán phát hiện khoảng trống cột (column-gutter) và khôi phục hàng bảng giúp `25/25` câu bằng chứng khớp nguyên văn sau chuẩn hóa.
  - **Giới hạn đã ghi nhận:** Bộ đọc xử lý độc lập từng trang PDF nên các câu nằm vắt qua ranh giới hai trang liên tiếp có thể bị đứt ở đầu trang mới (thấy rõ ở trang PDF `32` khi chunk mở bằng mảnh câu `"is 7 because..."`). Ngoài ra, bảng chú thích ngắn (`Table 2.8`, `Table 2.9`) đứng tách đoạn nên dễ bị chunk tách paragraph cắt thành chunk riêng 1 dòng nếu không gộp khối hoặc giới hạn độ dài tối thiểu.

- **Embedding model/provider/version/số chiều, vector store/version, metric, lệnh chạy và chi phí:**
  - **Embedding:** Provider `google-genai==3.3.0` (Google AI Studio, `vertexai=False`), model **`gemini-embedding-001`**, số chiều **`3072`**, phân tách task type **`RETRIEVAL_DOCUMENT`** khi embed chunk và **`RETRIEVAL_QUERY`** khi embed câu hỏi (`batch_size=50`), kèm cache SHA-256 trên đĩa (`temp/embedding_cache.jsonl`) và backoff theo `retryDelay` khi gặp giới hạn rate limit free tier (`429`/`5xx`), không fallback mock.
  - **Vector Store:** **PostgreSQL `16.16` + `pgvector 0.8.7`** chạy local qua Docker Compose (`127.0.0.1:55433`, bảng `document_chunks`), thư viện **`psycopg==3.3.8`**, metric **`cosine_distance (<=>)`**, chế độ tìm kiếm **`exact`** (không dùng ANN để tránh sai số index trên tập ~200 chunk/chiến lược). `upsert()` chạy idempotent theo cặp `(strategy, chunk_id)` và xóa tự động chunk thừa nếu phiên bản dữ liệu thay đổi (đã kiểm chứng chạy lại `python -m src.run` lần thứ 2 trên cùng database: `stored_count` giữ nguyên `217 / 235 / 235 / 180`, không nhân đôi; cũng đã test xóa chunk thừa khi giảm tập đầu vào).
  - **Lệnh chạy (từ thư mục `starter/`):** `python -m src.run` (hoặc `.\.venv\Scripts\python.exe -m src.run` trên Windows).
  - **Chi phí:** **$0.00** (Free Tier Google AI Studio). Tổng `646` entry embedding duy nhất đã được pre-embed vào cache từ bước chuẩn bị trước; trong lần chạy benchmark cuối cùng (`results/metrics_summary.json`), `api_calls_this_run = 0`, `cache_hits_this_run = 892`, `query_embed_seconds = 0.0s`.

- **Metadata bắt buộc, trường lọc bổ sung, nguồn giá trị và lý do chọn:**
  - Bắt buộc: `document_id` (`openstax-python-2024`), `source` (`data/Introduction_to_Python_Programming-WEB.pdf`), `page` (số trang vật lý PDF `int`), `book_page` (số trang in trên sách `int`), `chunk_index`, `char_len`.
  - Trường lọc bổ sung: **`chapter`** (`"ch1_statements"` cho trang `17–45`; `"ch2_expressions"` cho trang `47–76`) và **`section`** (nhận diện từ tiêu đề mục trong trang gốc như `"1.5"`, `"2.7"`).
  - Nguồn giá trị & lý do chọn: Rút trích trực tiếp từ phân chương mục lục và tiêu đề trang PDF đã ghi trong [manifest.json](../../data/manifest.json) (không suy đoán ngoài nguồn). Chọn `chapter` làm trường SQL pre-filter (`WHERE metadata->>'chapter' = ...`) vì đây là cấp phân đoạn rõ ràng, tin cậy 100% và đại diện cho ngữ cảnh truy vấn theo từng chương học.

---

## Cấu hình và benchmark

- **A / B / C / D (tham số cụ thể, khác biệt duy nhất B–C):**
  - **A (`A_fixed_500_50`):** `fixed_size(size=500, overlap=50)`, lưu đủ metadata nguồn/trang/chương/mục, **không bật filter**.
  - **B (`B_paragraph_500`):** `by_paragraph(max_size=500)` — tách theo đoạn văn và giữ nguyên khối bảng Markdown `<= 500` ký tự, cùng metadata như A, **không bật filter**.
  - **C (`C_paragraph_500_filtered`):** **Giữ nguyên 100% tập 235 chunks và vector của B**, chỉ thay đổi **duy nhất 1 yếu tố là bật SQL metadata pre-filter** khi câu hỏi có trường `filter` (với câu `filter=null` thì truy xuất unfiltered như B).
  - **D (`D_recursive_650_100_filtered` — cấu hình bổ sung khắc phục hạn chế của B/C):** `recursive_split(chunk_size=650, overlap=100)` ưu tiên giữ bảng và biên câu/dòng, **bật metadata pre-filter** khi có `filter`.

- **≥20 câu: phân chia ≥15 dev / ≥5 test, câu metadata filter và cách kiểm chứng evidence:**
  - Tổng **25 câu hỏi tiếng Việt** ([questions.json](../../benchmark/questions.json)), tách cố định trước khi thử nghiệm thành **`18` câu `dev`** (`q01–q15, q21–q23`) và **`7` câu `test`** (`q16–q20, q24–q25`).
  - Gồm câu hỏi trực tiếp (`direct`), diễn đạt lại (`paraphrase`), tổng hợp/điều kiện ngoại lệ (`synthesis`), đọc bảng (`q21–q25`) và **5 câu kiểm tra metadata filter** (`q13, q14, q15` trên `dev`; `q20, q24` trên `test` — giá trị filter `chapter` được cung cấp từ ngữ cảnh câu hỏi như `"Trong chương Expressions..."`).
  - Cách kiểm chứng evidence: Mỗi câu ghi rõ `gold_page`, `valid_pages` (nếu bảng tóm tắt cuối chương lặp lại cùng nội dung như trang `44`, `74`) và nguyên văn `evidence_quote` (cho phép nhiều mảnh `...` khi thông tin trải nhiều dòng bảng/đoạn). Toàn bộ `25/25` câu đều đã kiểm chứng tồn tại chính xác trên `59` trang đã chuẩn hóa (`Evidence match: 25/25`, `misses=[]`).

- **Tiêu chí chọn chiến lược đã chốt trước khi xem test:**
  1. Ưu tiên cao nhất: **Evidence Hit@3** (và tỷ lệ hợp nhất đủ bằng chứng trong Top-3) trên tập `dev`, kết hợp **Filter Compliance = 100%** đối với các cấu hình bật filter.
  2. Ưu tiên thứ hai: Chất lượng thủ công **Chunk Coherence** và **Answer Grounding** đạt mức cao (`>= 1.70/2`) để tránh cung cấp đoạn cắt nát cho LLM.
  3. Ưu tiên thứ ba: Số chunk gọn (`<= 240`), thời gian ingest/truy xuất và chi phí thấp.

---

## Kết quả

### 1. Chỉ số truy xuất tự động & tài nguyên

| Strategy | Split | Hit@1 (n/N) | Evidence Hit@3 (n/N) | Chunk count | Thời gian chạy (ingest + chunk/embed/upsert/search) | Chi phí |
|---|---|---|---|---|---|---|
| A (`fixed_500_50`) | dev | 7/18 (38.9%) | 10/18 (55.6%) | 217 | 2.998s + 2.992s (cache hit) | \$0.00 |
| A (`fixed_500_50`) | test | 4/7 (57.1%) | 4/7 (57.1%) | 217 | *(chung tập chạy trên)* | \$0.00 |
| B (`paragraph_500`) | dev | 9/18 (50.0%) | 13/18 (72.2%) | 235 | 2.998s + 2.425s (cache hit) | \$0.00 |
| B (`paragraph_500`) | test | 2/7 (28.6%) | 2/7 (28.6%) | 235 | *(chung tập chạy trên)* | \$0.00 |
| C (`paragraph_500 + filter`) | dev | 9/18 (50.0%) | 13/18 (72.2%) | 235 | 2.998s + 2.352s (cache hit) | \$0.00 |
| C (`paragraph_500 + filter`) | test | 2/7 (28.6%) | 2/7 (28.6%) | 235 | *(chung tập chạy trên)* | \$0.00 |
| D (`recursive_650_100 + filter`) | dev | 10/18 (55.6%) | 13/18 (72.2%) | 180 | 2.998s + 2.022s (cache hit) | \$0.00 |
| D (`recursive_650_100 + filter`) | test | 3/7 (42.9%) | 3/7 (42.9%) | 180 | *(chung tập chạy trên)* | \$0.00 |

*(Ghi chú chỉ số bổ trợ: xét tổng `25` câu dev+test, `source_page_hit@3` đạt `25/25` ở A, B, C và `24/25` ở D; tỷ lệ bao phủ đủ nhiều mảnh evidence trong Top-3 `multi_chunk_top3_covered` đạt `19/25` ở A và `21/25` ở B, C, D.)*

### 2. Chỉ số chấm thủ công (Manual Audit — đã chốt theo Phương án 1)

| Strategy | Coherence trung bình /2 (n) | Metadata đủ và đúng (n/N) | Filter tuân thủ (n/N hoặc N/A) | Grounding 0/1/2 (số câu) và trung bình /2 |
|---|---|---|---|---|
| A (`fixed_500_50`) | **1.00 / 2** (`10/20`, n=10) | 21/21 (100%) | N/A *(không lọc; trùng ngẫu nhiên 6/6 hit test, 3/5 toàn tập)* | `0 / 0 / 7` -> **2.00 / 2** (`14/14`) |
| B (`paragraph_500`) | **1.70 / 2** (`17/20`, n=10) | 21/21 (100%) | N/A *(không lọc; trùng ngẫu nhiên 6/6 hit test, 4/5 toàn tập)* | `1 / 1 / 5` -> **1.57 / 2** (`11/14`) |
| C (`paragraph_500 + filter`) | **1.70 / 2** (`17/20`, n=10) | 21/21 (100%) | **100%** (6/6 hit test; 5/5 câu = 15/15 hit toàn tập) | `1 / 1 / 5` -> **1.57 / 2** (`11/14`) |
| D (`recursive_650_100 + filter`) | **1.80 / 2** (`18/20`, n=10) | 21/21 (100%) | **100%** (6/6 hit test; 5/5 câu = 15/15 hit toàn tập) | `0 / 0 / 7` -> **2.00 / 2** (`14/14`) |

- **Đường dẫn trace, nhãn thủ công và cách chọn mẫu:**
  - Chỉ số tự động: [metrics_summary.json](../../results/metrics_summary.json)
  - Toàn bộ trace Top-3 các chiến lược: [traces_all_strategies.json](../../results/traces_all_strategies.json)
  - Gói mẫu thô xuất từ pipeline: [manual_audit_packets.md](../../results/manual_audit_packets.md)
  - **Phiếu chấm thủ công hoàn chỉnh (tiêu chí, đáp án đối chiếu, nhãn `0/1/2` và giải trình):** [manual_audit_workbook.md](../../results/manual_audit_workbook.md)
  - **Cách chọn mẫu Coherence:** Cố định danh sách `10` trang trước khi chạy benchmark: `COHERENCE_SAMPLE_PAGES = (18, 25, 27, 32, 35, 49, 56, 64, 68, 72)` (trải đều Chương 1 và Chương 2, bao gồm cả đoạn văn, bài tập và bảng), lấy cùng vị trí chunk trên cả `A`, `B/C` và `D`. Người chấm là tác giả bài làm (tự chấm kèm rà soát đối chiếu nguyên văn từng đoạn).

---

## Phân tích và kết luận

- **So sánh A–B và B–C (kèm D); 2 ví dụ sai thực tế có ID câu và nguồn:**
  - **A -> B (đổi cách chunk từ `fixed_500_50` sang `by_paragraph_500`):** Trên tập `dev`, `Hit@1` tăng từ `38.9% (7/18)` lên `50.0% (9/18)`, `Hit@3` tăng mạnh từ `55.6% (10/18)` lên `72.2% (13/18)`, và điểm **Coherence** tăng vượt bậc từ `1.00/2` (10/10 mẫu ở A đều bị cắt ngang chữ/bảng) lên `1.70/2`. Tuy nhiên trên `test`, strict `Hit@3` của B lại giảm từ `57.1%` (A) xuống `28.6%` và Grounding giảm xuống `1.57/2` vì `paragraph_500` tạo ra các chunk rất ngắn (`min_len = 38` ký tự) không có overlap, làm tách rời tiêu đề bảng khỏi thân bảng hoặc tách 2 câu liền nhau sang 2 chunk riêng.
  - **B -> C (giữ nguyên chunk B, chỉ bật SQL metadata filter):** Trên `dev` và `test`, `Hit@1`/`Hit@3` giữ nguyên (`13/18` và `2/7`), **nhưng tỷ lệ tuân thủ phạm vi chương tăng lên `100%` (`5/5` câu = `15/15` hit)** so với A (`3/5`) và B (`4/5`), ngăn chặn hoàn toàn tình trạng hit ngoài chương lọt vào Top-3 khi ngữ cảnh đã chỉ định rõ chương.
  - **C -> D (`recursive_650_100 + filter`):** Tăng `chunk_size` lên `650` và khôi phục `overlap=100` giúp giảm số chunk từ `235` xuống `180`, đạt `Dev Hit@1 = 55.6%` (cao nhất), `Overall Hit@3 = 64.0%` (`16/25`), `Coherence = 1.80/2`, `Filter Compliance = 100%` và khôi phục **`Answer Grounding = 2.00/2`** (`14/14`, ngang A nhưng giữ nguyên khối bảng/đoạn tốt hơn hẳn).
  - **Ví dụ sai 1 — `q25` (tập `test`, `gold_page = 72`, sách trang `62`, mục `2.8`):** B & C đều đạt **`0/2` Grounding** (`ev_hit3 = False`, `multi_chunk_top3 = False`). Nguyên nhân: `by_paragraph` cắt dòng chú thích bảng thành hai chunk độc lập 1 dòng chỉ `38–39` ký tự (`openstax-python-2024_p072_c08`: `"Table 2.9 Applications built with Python."` và `p072_c06`: `"Table 2.8 Python outside of CS and IT."`). Hai chunk caption mồ côi này đạt cosine score cao nhất (`0.7682` và `0.7544`), chiếm Top-2 và đẩy toàn bộ nội dung bảng `Science/biologist` và `Data visualization/Matplotlib` ra khỏi Top-3. Chiến lược A và D nhờ gộp kích thước/overlap lớn hơn nên giữ được caption gắn cùng các hàng bảng -> đều đạt `2/2` Grounding.
  - **Ví dụ sai 2 — `q13` (tập `dev`, `filter = {'chapter': 'ch1_statements'}`, `gold_page = 28`, mục `1.4`):** Chiến lược **A (`unfiltered`)** thất bại hoàn toàn (`ev_hit3 = False`, `filter_compliant = False`) vì Rank 1 (`p069_c04`, score `0.7486`) và Rank 3 (`p070_c04`, `0.7322`) nhảy sang Chương 2 (`ch2_expressions`); chiến lược **B (`unfiltered`)** dù lấy được chunk đúng ở Rank 1 (`p028_c02`) nhưng Rank 2 (`p069_c05`) và Rank 3 (`p054_c03`) vẫn rò sang `ch2_expressions`. Khi bật SQL pre-filter ở **C** và **D**, cả 3/3 hit đều nằm trọn trong `ch1_statements` (`p028_c02, p028_c03, p028_c01` ở C; `p028_c02, p028_c01, p029_c01` ở D).
  - *(Ví dụ bổ trợ — `q18` trên tập `test`, `gold_page = 54`, mục `2.3`: B/C chỉ đạt `1/2` Grounding vì câu trả lời gồm 2 đoạn văn kế tiếp `p054_c02` và `p054_c03`; Rank 1 của B/C chỉ lấy được `p054_c03` về toán tử `*` còn `p054_c02` về `+`, `-`, `/` không tương thích bị rớt khỏi Top-3 nhường chỗ cho câu trắc nghiệm trang `55` và bảng trang `44`. D gom cả hai đoạn vào `p054_c02` -> đạt `2/2`.)*

- **Chiến lược chọn, đánh đổi, điều kiện áp dụng:**
  - Theo đúng tiêu chí ưu tiên đã chốt trước khi xem `test`, nếu chỉ xét ba cấu hình chuẩn A–B–C thì **C (`by_paragraph + metadata filter`)** vượt trội A trên `dev` (`Hit@3 72.2% vs 55.6%`, Coherence `1.70 vs 1.00`, Filter `100%`), nhưng khi đối chiếu sâu sang `D` (`recursive_650_100 + filter`), **D là cấu hình cân bằng nhất để đưa vào sử dụng** nhờ giữ nguyên khối bảng + tăng cửa sổ lên `650` ký tự có `overlap=100`, vừa đạt `Dev Hit@1 = 55.6%` cao nhất, vừa loại bỏ lỗi caption mồ côi (`Grounding 2.00/2`, `Coherence 1.80/2`, `Filter 100%`) và giảm 23% số chunk so với B/C (`180` vs `235`).
  - **Đánh đổi & điều kiện áp dụng:** `D` chấp nhận kích thước chunk lớn hơn (`avg = 502.9` chars, tồn tại trùng lặp overlap ~100 ký tự khiến tổng ký tự lưu trữ là `90.523` so với `87.447` của B/C) để đổi lấy ngữ cảnh đầy đủ hơn khi nạp cho LLM. Điều kiện áp dụng tốt nhất là tài liệu giáo trình/kỹ thuật có bảng, danh sách và phân mục chương rõ ràng để filter theo `chapter`.

- **Hạn chế của dữ liệu, nhãn, test nhỏ, đo thời gian/chi phí:**
  - **Quy mô corpus & test nhỏ:** `59` trang PDF thuộc 2 chương đầu của cùng 1 sách, tập `test` chỉ có `7` câu hỏi (trong đó `2` câu có filter) nên mỗi 1 câu trượt làm tỷ lệ % nhảy `14.3%` — không thể suy rộng kết luận tổng quát cho mọi miền tài liệu hay mọi mô hình embedding.
  - **Thiên lệch tự chấm (Self-grading bias):** Tác giả đồng thời thiết kế benchmark, viết pipeline và chấm thủ công `Coherence`/`Grounding`; dù đã khóa bộ test và giữ nguyên không chỉnh tham số sau khi đọc trace `test`, vẫn cần có đánh giá độc lập hoặc chấm chéo để loại bỏ thiên lệch chủ quan ở các ca biên.
  - **Đo thời gian/chi phí trên cache:** Các mốc `embed_s` (`0.001–0.002s`) trong `metrics_summary.json` đo trên trạng thái **đã pre-warm cache SHA-256** để tiết kiệm quota Free Tier Gemini API (`892` cache hits trong lần chạy tổng hợp); tốc độ thực nếu embed mới từ đầu qua mạng sẽ bị chi phối bởi latency API và rate limit batch theo phút/ngày.

- **Nếu làm lại hoặc mở rộng, cải tiến gì?**
  1. **Chunking xuyên ranh giới trang (cross-page chunking):** Gộp văn bản liên tục theo từng chương (`chapter`) trước khi chia đoạn để xóa lỗi mở đầu cụt câu như ở trang PDF `32`.
  2. **Gắn thêm metadata cấu trúc khối (`content_type`: `prose` / `table` / `mcq_exercise`) và `prev_chunk_id` / `next_chunk_id`:** Giúp lọc hoặc giảm trọng số câu hỏi trắc nghiệm `CONCEPTS IN PRACTICE` khi người dùng hỏi lý thuyết (giảm nhiễu như ở `q10`, `q18`) và tự động kéo thêm tiêu đề/đoạn liền kề khi gặp bảng lớn.
  3. **Gắn liền caption bảng với bảng gốc trong tiền xử lý** (thay vì tách thành chunk riêng ở mức đoạn), đồng thời thử **Hybrid Retrieval (Dense Cosine + BM25 / Postgres FTS với RRF)** để bắt chính xác tên hàm, ký hiệu toán tử (`round()`, `//`, `%`, `Table 2.7`) vốn dễ bị embedding ngữ nghĩa làm mờ.

- **Nhật ký lỗi đã gặp, cách khắc phục & công cụ hỗ trợ (`RULES.md`):**
  - *Lỗi đọc PDF & tách bảng ban đầu:* `pypdf` ở chế độ mặc định trộn cột và vỡ hàng bảng; khắc phục bằng `extraction_mode="layout"`, phát hiện column-gutter và khôi phục bảng Markdown (kiểm chứng `25/25` evidence khớp sau chuẩn hóa), đồng thời loại trang trống `46` (`0` ký tự chuẩn hóa).
  - *Lỗi rate limit Free Tier API (`429 RESOURCE_EXHAUSTED`):* Khi gửi nhiều batch liên tiếp tới `gemini-embedding-001` dễ vượt giới hạn request/token theo phút của Free Tier; khắc phục bằng tự động đọc `retryDelay` để backoff (`embeddings.py`) kết hợp pre-embed một lần và lưu cache SHA-256 trên đĩa (`temp/embedding_cache.jsonl`) — không fallback sang vector giả.
  - *Công cụ AI hỗ trợ & kiểm chứng:* Có sử dụng trợ lý AI trong IDE để hỗ trợ lập trình hoàn thiện khung `starter/src/`, chuẩn hóa script trích bảng Markdown và tạo phiếu đối chiếu `manual_audit_workbook.md`. Học viên trực tiếp đọc rà soát lại toàn bộ phiếu chấm, tự bắt và hiệu đính 3 lỗi trích dẫn/chốt ca biên/thuật ngữ filter, kiểm chứng file output thực tế và chịu trách nhiệm toàn bộ số liệu báo cáo.
