# Phiếu Chấm Tay Thủ Công Đã Chốt (Manual Audit — Phương án 1)

> Tài liệu này lưu **chỉ tiêu chấm chuẩn**, **bảng tổng kết đã chốt**, **văn bản chunk / Top-3 nguyên văn**, **đáp án chuẩn**, và **nhãn chấm tay cuối cùng** cho cả 4 chiến lược (`A, B, C, D`). Quá trình chấm do sinh viên thực hiện và rà soát đối chiếu thủ công toàn bộ các ca biên (chú ý công khai giới hạn tự chấm ở phần *Thiên lệch*).

## Bảng tổng kết nhãn thủ công đã chốt (Phương án 1)

| Tiêu chí chấm tay | Chiến lược A (`fixed_500_50`) | Chiến lược B (`paragraph_500`) | Chiến lược C (`paragraph_500 + filter`) | Chiến lược D (`recursive_650_100 + filter`) |
| --- | :---: | :---: | :---: | :---: |
| **1. Chunk Coherence** *(10 trang cố định, tối đa 20)* | **10 / 20** (TB `1.00`) | **17 / 20** (TB `1.70`) | **17 / 20** (TB `1.70`) | **18 / 20** (TB `1.80`) |
| **2. Metadata Accuracy** *(21 hit tập `test`)* | **21 / 21** (`100%`) | **21 / 21** (`100%`) | **21 / 21** (`100%`) | **21 / 21** (`100%`) |
| **3. Filter Compliance** *(câu có filter)* | Không dùng (`N/A`; trùng ngẫu nhiên `6/6` test, `3/5` all) | Không dùng (`N/A`; trùng ngẫu nhiên `6/6` test, `4/5` all) | **`100%`** (`6/6` hit test, `5/5` câu = `15/15` all) | **`100%`** (`6/6` hit test, `5/5` câu = `15/15` all) |
| **4. Answer Grounding** *(7 câu `test`, tối đa 14)* | **14 / 14** (TB `2.00` · `0/0/7`) | **11 / 14** (TB `1.57` · `1/1/5`) | **11 / 14** (TB `1.57` · `1/1/5`) | **14 / 14** (TB `2.00` · `0/0/7`) |

---
## Phần 0 — Chỉ tiêu & Cách chấm chuẩn (`GUIDE.md` & `BENCHMARK.md`)
### 1. Chunk Coherence (Chấm độ mạch lạc của từng đoạn cắt — thang `0 / 1 / 2`)
- **Mục tiêu:** Kiểm tra xem chiến lược chia nhỏ (`A = fixed 500`, `B/C = paragraph 500`, `D = recursive 650`) có cắt vụn câu chữ hay giữ nguyên ý nghĩa tự thân của đoạn văn/bảng không.
- **Cách chấm:** Trên cùng **10 trang cố định** (`18, 25, 27, 32, 35, 49, 56, 64, 68, 72`), đọc đoạn text của chunk ở A, B/C, D rồi cho điểm:
  - **`2` điểm:** Đọc tự hiểu trọn vẹn ý chính trong chunk; không bị cắt ngang giữa chữ/giữa câu/giữa hàng bảng; không bị cụt mất đề bài hoặc đáp án.
  - **`1` điểm:** Vẫn hiểu được phần lớn ý chính ở thân đoạn, **nhưng** bị lỗi ranh giới: cắt giữa từ, cụt đầu/đuôi câu, kéo thiếu đáp án câu hỏi, hoặc vướng mảnh câu từ trang trước.
  - **`0` điểm:** Bị cắt quá nát hoặc thiếu chủ thể đến mức không hiểu chunk đang nói về gì.

### 2. Metadata Usefulness (Kiểm tra tính đúng & ích lợi của metadata trên 7 câu `test` × Top-3 = 21 records/chiến lược)
- **Chỉ tiêu:**
  1. **Độ chính xác (`Accuracy`):** Kiểm tra `source`, `page` (PDF), `book_page`, `chapter`, `section` trên cả 21 hit Top-3 xem có khớp 100% với trang gốc trong sách không.
  2. **Tuân thủ Filter (`Filter Compliance`):** Với câu có `filter` (vd `chapter = ch2_expressions` ở `q20, q24`), cả 3/3 chunk trả về có nằm đúng phạm vi filter không. Với câu `filter = None`, ghi `N/A`.
  3. **Hữu ích & Hạn chế:** Chỉ ra ít nhất **1 trường metadata hữu ích** cho truy vết/lọc và **1 hạn chế** còn thiếu.

### 3. Answer Grounding Quality (Chấm độ đủ bằng chứng trả lời câu hỏi — thang `0 / 1 / 2`)
> **Lưu ý rất quan trọng:** Tiêu chí này **KHÔNG** chấm xem LLM viết hay hay dở, mà chấm xem **nếu đưa 3 chunk Top-3 này cho LLM đọc, trong 3 chunk đó đã có ĐỦ dữ kiện để trả lời đúng Đáp án chuẩn hay chưa**.

- **Cách chấm:** Với mỗi câu `test` (`q16–q20, q24–q25`), chia **Đáp án chuẩn** thành các ý bắt buộc (Ý 1, Ý 2, ...), rồi đọc **Top-3 chunks ghép lại** của từng chiến lược:
  - **`2` điểm (Đủ hoàn toàn):** Ghép cả 3 chunk trong Top-3 tìm thấy **đầy đủ mọi ý** của Đáp án chuẩn (kể cả điều kiện/ngoại lệ) và có thông tin trang nguồn để trích dẫn. *(Lưu ý: máy chấm `Evidence Hit@3` có thể báo `False` nếu câu bằng chứng bị tách sang 2 chunk khác nhau, nhưng nếu cả 2 chunk đều nằm trong Top-3 thì chấm tay vẫn cho **`2` điểm**!)*
  - **`1` điểm (Đủ một phần):** Trong Top-3 chỉ tìm thấy **1 phần đáp án** (ví dụ trả lời được vế 2 nhưng sót mất vế 1 hoặc thiếu điều kiện quan trọng).
  - **`0` điểm (Không có bằng chứng):** Trong Top-3 **không chứa dữ kiện nào** dùng để trả lời được câu hỏi (ví dụ chỉ trúng dòng tiêu đề bảng trống không hoặc câu trắc nghiệm nhiễu).

---

## Phần 1 — Phiếu chấm Chunk Coherence (10 trang cố định)
*(Lưu ý: **B** và **C** dùng chung một bộ chunk `paragraph_500`, nên hai chiến lược này có cùng văn bản và cùng điểm Coherence.)*

### Trang PDF 18 (Sách: 8, `ch1_statements`, mục `1.1`)
- **A (`openstax-python-2024_p018_c02`, 500 chars):**
  ```text
r can run. Programs help people accomplish everyday tasks, create new technology, and have fun.

The goal of this book is to teach introductory programming and problem solving. Writing programs is a creative activity, inherently useful, and rewarding! No prior background in computer science is necessary to read this book. Many different types of programs exist, as shown in the illustration below. This book will focus on general purpose programs that typically run "behind the scenes."

CHECKPOINT
  ```
- **B (`openstax-python-2024_p018_c02`, 320 chars):**
  ```text
A computer is an electronic device that stores and processes information. Examples of computers include smartphones, tablets, laptops, desktops, and servers. Technically, a program is a sequence of instructions that a computer can run. Programs help people accomplish everyday tasks, create new technology, and have fun.
  ```
- **D (`openstax-python-2024_p018_c02`, 639 chars):**
  ```text
The goal of this book is to teach introductory programming and problem solving.

Writing programs is a creative activity, inherently useful, and rewarding! No prior background in computer science is necessary to read this book.

Many different types of programs exist, as shown in the illustration below. This book will focus on general purpose programs that typically run "behind the scenes."

CHECKPOINT

Online music streaming

Online music streaming; ch 1, video 1 (https://www.openstax.org/r/music-streaming)

CONCEPTS IN PRACTICE

Computers and programs

1 . How many types of programs were described in the animation?
a. 3
b. 4
c. 5
  ```

**Hướng dẫn soi lỗi & Gợi ý chấm trang này:**
- **A:** A (`1`): Mở đầu bị cắt giữa từ `"r can run."` và kết thúc cụt ở chữ `"CHECKPOINT"` (thiếu nội dung checkpoint), nhưng giữ được đoạn giải thích chính. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **B/C:** B/C (`2`): Trọn vẹn 2 câu hoàn chỉnh định nghĩa *computer* và *computer program*, không cắt từ hay câu. -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`
- **D:** D (`2`): Gồm trọn đoạn mục tiêu sách + `CHECKPOINT` + trọn câu hỏi `1.` và 3 đáp án `a, b, c`. -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`

---

### Trang PDF 25 (Sách: 15, `ch1_statements`, mục `1.3`)
- **A (`openstax-python-2024_p025_c01`, 500 chars):**
  ```text
a. temperature = 98.5
b. 98.5 = temperature
c. temperature - 23.2

Variable naming rules

A variable name can consist of letters, digits, and underscores and be of any length. The name cannot start with a digit. Ex: 101class is invalid. Also, letter case matters. Ex: Total is different from total. Python's style guide recommends writing variable names in snake case, which is all lowercase with underscores in between each word, such as first_name or total_price.

A name should be short and descri
  ```
- **B (`openstax-python-2024_p025_c01`, 465 chars):**
  ```text
a. temperature = 98.5
b. 98.5 = temperature
c. temperature - 23.2

Variable naming rules

A variable name can consist of letters, digits, and underscores and be of any length. The name cannot start with a digit. Ex: 101class is invalid. Also, letter case matters. Ex: Total is different from total. Python's style guide recommends writing variable names in snake case, which is all lowercase with underscores in between each word, such as first_name or total_price.
  ```
- **D (`openstax-python-2024_p025_c01`, 466 chars):**
  ```text
a. temperature = 98.5
b. 98.5 = temperature
c. temperature - 23.2

Variable naming rules

A variable name can consist of letters, digits, and underscores and be of any length. The name cannot start with a digit. Ex: 101class is invalid. Also, letter case matters. Ex: Total is different from total.

Python's style guide recommends writing variable names in snake case, which is all lowercase with underscores in between each word, such as first_name or total_price.
  ```

**Hướng dẫn soi lỗi & Gợi ý chấm trang này:**
- **A:** A (`1`): Mở đầu từ phương án `a. temperature = 98.5` và kết thúc cắt ngang giữa từ `"descri"` (thiếu phần sau của nguyên tắc đặt tên biến). -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **B/C:** B/C (`2`): Kết thúc sạch tại cuối câu `"...total_price."` (lưu ý mở đầu từ `a. temperature...` do ranh giới đầu trang PDF 25). -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`
- **D:** D (`2`): Tương tự B/C, kết thúc sạch tại `"...total_price."`, không cắt câu hay cắt từ. -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`

---

### Trang PDF 27 (Sách: 17, `ch1_statements`, mục `1.4`)
- **A (`openstax-python-2024_p027_c01`, 500 chars):**
  ```text
| Valid string | Invalid string |
| --- | --- |
| "I hope you aren't sad." | 'I hope you aren't sad.' |
| 'The teacher said "Correct!" ' | "The teacher said "Correct!" " |

Table 1.3 Rules for strings.

CONCEPTS IN PRACTICE

Valid and invalid strings

1 . Which of the following is a string?
a. Hello!
b. 29
c. "7 days"

2 . Which line of code assigns a string to the variable email?
a. "fred78@gmail.com"
b. "email = fred78@gmail.com"
c. email = "fred78@gmail.com"

3 . Which is a valid string?
a. I
  ```
- **B (`openstax-python-2024_p027_c01`, 465 chars):**
  ```text
| Valid string | Invalid string |
| --- | --- |
| "I hope you aren't sad." | 'I hope you aren't sad.' |
| 'The teacher said "Correct!" ' | "The teacher said "Correct!" " |

Table 1.3 Rules for strings.

CONCEPTS IN PRACTICE

Valid and invalid strings

1 . Which of the following is a string?
a. Hello!
b. 29
c. "7 days"

2 . Which line of code assigns a string to the variable email?
a. "fred78@gmail.com"
b. "email = fred78@gmail.com"
c. email = "fred78@gmail.com"
  ```
- **D (`openstax-python-2024_p027_c01`, 604 chars):**
  ```text
| Valid string | Invalid string |
| --- | --- |
| "I hope you aren't sad." | 'I hope you aren't sad.' |
| 'The teacher said "Correct!" ' | "The teacher said "Correct!" " |

Table 1.3 Rules for strings.

CONCEPTS IN PRACTICE

Valid and invalid strings

1 . Which of the following is a string?
a. Hello!
b. 29
c. "7 days"

2 . Which line of code assigns a string to the variable email?
a. "fred78@gmail.com"
b. "email = fred78@gmail.com"
c. email = "fred78@gmail.com"

3 . Which is a valid string?
a. I know you'll answer correctly!
b. 'I know you'll answer correctly!'
c. "I know you'll answer correctly!"
  ```

**Hướng dẫn soi lỗi & Gợi ý chấm trang này:**
- **A:** A (`1`): Lấy đủ `Table 1.3`, câu `1`, câu `2`, nhưng cắt ngang câu `3` thành `"3 . Which is a valid string?\na. I"`. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **B/C:** B/C (`2`): Ngắt sạch ngay sau hết câu `2` (`c. email = "fred78@gmail.com"`), không kéo lửng câu `3`. -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`
- **D:** D (`2`): Gồm trọn cả `Table 1.3`, câu `1`, câu `2` và trọn vẹn câu `3` (`a, b, c`). -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`

---

### Trang PDF 32 (Sách: 22, `ch1_statements`, mục `1.5`)
- **A (`openstax-python-2024_p032_c01`, 500 chars):**
  ```text
is 7 because multiplication takes precedence over addition. However, (1 + 2) * 3 is 9 because parentheses take precedence over multiplication.

| Operator | Description | Example | Result |
| --- | --- | --- | --- |
| () | Parentheses | (1 + 2) * 3 | 9 |
| ** | Exponentiation | 2 ** 4 | 16 |
| +, - | Positive, negative | -math.pi | -3.14159 |
| *, / | Multiplication, division | 2 * 3 | 6 |
| +, - | Addition, subtraction | 1 + 2 | 3 |

Table 1.4 Operator precedence from highest to lowest.

CHECKP
  ```
- **B (`openstax-python-2024_p032_c01`, 492 chars):**
  ```text
is 7 because multiplication takes precedence over addition. However, (1 + 2) * 3 is 9 because parentheses take precedence over multiplication.

| Operator | Description | Example | Result |
| --- | --- | --- | --- |
| () | Parentheses | (1 + 2) * 3 | 9 |
| ** | Exponentiation | 2 ** 4 | 16 |
| +, - | Positive, negative | -math.pi | -3.14159 |
| *, / | Multiplication, division | 2 * 3 | 6 |
| +, - | Addition, subtraction | 1 + 2 | 3 |

Table 1.4 Operator precedence from highest to lowest.
  ```
- **D (`openstax-python-2024_p032_c01`, 553 chars):**
  ```text
is 7 because multiplication takes precedence over addition. However, (1 + 2) * 3 is 9 because parentheses take precedence over multiplication.

| Operator | Description | Example | Result |
| --- | --- | --- | --- |
| () | Parentheses | (1 + 2) * 3 | 9 |
| ** | Exponentiation | 2 ** 4 | 16 |
| +, - | Positive, negative | -math.pi | -3.14159 |
| *, / | Multiplication, division | 2 * 3 | 6 |
| +, - | Addition, subtraction | 1 + 2 | 3 |

Table 1.4 Operator precedence from highest to lowest.

CHECKPOINT

Order of operations in an arithmetic expression
  ```

**Hướng dẫn soi lỗi & Gợi ý chấm trang này:**
- **A:** A (`1`): Bắt đầu bằng mảnh câu vắt từ trang 31 (`"is 7 because..."`), lấy đủ `Table 1.4`, nhưng cuối chunk cắt ngang chữ `"CHECKP"`. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **B/C:** B/C (`1`): Giữ nguyên vẹn `Table 1.4` và không cắt từ ở cuối, nhưng đầu chunk vẫn vướng mảnh câu `"is 7 because..."` do chunking theo từng trang PDF. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **D:** D (`1`): Tương tự B/C, vướng mảnh câu `"is 7 because..."` ở đầu trang (và kèm tiêu đề `CHECKPOINT` ở cuối). -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`

---

### Trang PDF 35 (Sách: 25, `ch1_statements`, mục `1.6`)
- **A (`openstax-python-2024_p035_c01`, 500 chars):**
  ```text
Common types of errors

Different types of errors may occur when running Python programs. When an error occurs, knowing the type of error gives insight about how to correct the error. The following table shows examples of mistakes that anyone could make when programming.

| Mistake | Error message | Explanation |
| --- | --- | --- |
| print("Have a nice day!" | SyntaxError: unexpected EOF while parsing | The closing parenthesis is missing. Python is surprised to reach the end of file (EOF) befor
  ```
- **B (`openstax-python-2024_p035_c01`, 271 chars):**
  ```text
Common types of errors

Different types of errors may occur when running Python programs. When an error occurs, knowing the type of error gives insight about how to correct the error. The following table shows examples of mistakes that anyone could make when programming.
  ```
- **D (`openstax-python-2024_p035_c01`, 272 chars):**
  ```text
Common types of errors

Different types of errors may occur when running Python programs. When an error occurs, knowing the type of error gives insight about how to correct the error.

The following table shows examples of mistakes that anyone could make when programming.
  ```

**Hướng dẫn soi lỗi & Gợi ý chấm trang này:**
- **A:** A (`1`): Lấy đoạn mở đầu + header `Table 1.5`, nhưng cắt ngang hàng 1 giữa từ `"befor"`. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **B/C:** B/C (`2`): Trọn vẹn phần dẫn nhập `Common types of errors` (ngắt sạch trước bảng `Table 1.5`). -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`
- **D:** D (`2`): Giống B/C, trọn vẹn phần dẫn nhập trước bảng. -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`

---

### Trang PDF 49 (Sách: 39, `ch2_expressions`, mục `2.1`)
- **A (`openstax-python-2024_p049_c02`, 499 chars):**
  ```text
down arrow displays the next line. That way, the user can repeat a line without having to type the line again.

CHECKPOINT

Correcting a typo

Correcting a typo; ch 2, video 2 (https://www.openstax.org/r/correcting-typo)

CONCEPTS IN PRACTICE

Using the arrow keys

4 . Which arrow keys were needed to edit the typo?
a. only the up arrow key
b. the up and down arrows
c. the up and left arrows

5 . What keys would the user press to go back two lines?
a. press the up arrow twice
b. press the down a
  ```
- **B (`openstax-python-2024_p049_c02`, 450 chars):**
  ```text
Most shells maintain a history of every line of code the user types. Pressing the up or down arrow key on the keyboard displays the history. The up arrow displays the previous line; the down arrow displays the next line. That way, the user can repeat a line without having to type the line again.

CHECKPOINT

Correcting a typo

Correcting a typo; ch 2, video 2 (https://www.openstax.org/r/correcting-typo)

CONCEPTS IN PRACTICE

Using the arrow keys
  ```
- **D (`openstax-python-2024_p049_c02`, 640 chars):**
  ```text
CHECKPOINT

Correcting a typo

Correcting a typo; ch 2, video 2 (https://www.openstax.org/r/correcting-typo)

CONCEPTS IN PRACTICE

Using the arrow keys

4 . Which arrow keys were needed to edit the typo?
a. only the up arrow key
b. the up and down arrows
c. the up and left arrows

5 . What keys would the user press to go back two lines?
a. press the up arrow twice
b. press the down arrow twice
c. press the left arrow twice

TRY IT

Exploring the shell

Running code interactively is a great way to learn how Python works. Open a Python shell on your computer, or use the one at python.org/shell (https://openstax.org/r/100pythonshell).
  ```

**Hướng dẫn soi lỗi & Gợi ý chấm trang này:**
- **A:** A (`1`): Cụt cả hai đầu — mở bằng `"down arrow..."` và kết thúc cắt ngang `"b. press the down a"`. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **B/C:** B/C (`1`): Đoạn văn + `CHECKPOINT` sạch, nhưng cuối chunk kéo theo tiêu đề mồ côi `CONCEPTS IN PRACTICE / Using the arrow keys` mà toàn bộ câu hỏi bên dưới lại rơi sang chunk sau. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **D:** D (`1`, chốt ca biên nhất quán): Trọn vẹn `CHECKPOINT`, câu `4` (`a, b, c`) và câu `5` (`a, b, c`), nhưng cuối chunk kéo theo phần mở đầu `TRY IT / Exploring the shell` (thiếu nội dung thực hành bên dưới ở chunk sau). -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`

---

### Trang PDF 56 (Sách: 46, `ch2_expressions`, mục `2.4`)
- **A (`openstax-python-2024_p056_c02`, 499 chars):**
  ```text
n numerical inaccuracies related to floating-point representation.
• Use the round() function to mitigate floating-point errors in output. Floating-point errors

Computers store information using 0's and 1's. All information must be converted to a string of 0's and 1's. Ex: 5 is converted to 101. Since only two values, 0 or 1, are allowed the format is called binary.

Floating-point values are stored as binary by Python. The conversion of a floating point number to the underlying binary results
  ```
- **B (`openstax-python-2024_p056_c02`, 377 chars):**
  ```text
• Explain numerical inaccuracies related to floating-point representation.
• Use the round() function to mitigate floating-point errors in output. Floating-point errors

Computers store information using 0's and 1's. All information must be converted to a string of 0's and 1's. Ex: 5 is converted to 101. Since only two values, 0 or 1, are allowed the format is called binary.
  ```
- **D (`openstax-python-2024_p056_c02`, 608 chars):**
  ```text
Computers store information using 0's and 1's. All information must be converted to a string of 0's and 1's. Ex: 5 is converted to 101. Since only two values, 0 or 1, are allowed the format is called binary.

Floating-point values are stored as binary by Python. The conversion of a floating point number to the underlying binary results in specific types of floating-point errors.

A round-off error occurs when floating-point values are stored erroneously as an approximation.

The difference between an approximation of a value used in computation and the correct (true) value is called a round-off error.
  ```

**Hướng dẫn soi lỗi & Gợi ý chấm trang này:**
- **A:** A (`1`): Cụt cả hai đầu — mở giữa từ `"n numerical inaccuracies..."` và cắt giữa câu ở cuối `"results"`. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **B/C:** B/C (`2`): Trọn vẹn 2 `Learning objectives` và đoạn giải thích hệ nhị phân (`binary`). -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`
- **D:** D (`2`): Trọn vẹn đoạn `binary`, lưu trữ `floating-point` và định nghĩa `round-off error`. -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`

---

### Trang PDF 64 (Sách: 54, `ch2_expressions`, mục `2.6`)
- **A (`openstax-python-2024_p064_c01`, 500 chars):**
  ```text
| Function | Description | Examples |
| --- | --- | --- |
| **Number-theoretic** |  |  |
| math.ceil(x) | The ceiling of x: the smallest integer greater than or equal to x. | math.ceil(7.4) 8 math.ceil(-7.4) -7 |
| math.floor(x) | The floor of x: the largest integer less than or equal to x. | math.floor(7.4) 7 math.floor(-7.4) -8 |
| **Power and logarithmic** |  |  |
| math.log(x) | The natural logarithm of x (to base e). | math.log(math.e) 1.0 math.log(0) ValueError: math domain error |
| math.
  ```
- **B (`openstax-python-2024_p064_c01`, 492 chars):**
  ```text
| Function | Description | Examples |
| --- | --- | --- |
| **Number-theoretic** |  |  |
| math.ceil(x) | The ceiling of x: the smallest integer greater than or equal to x. | math.ceil(7.4) 8 math.ceil(-7.4) -7 |
| math.floor(x) | The floor of x: the largest integer less than or equal to x. | math.floor(7.4) 7 math.floor(-7.4) -8 |
| **Power and logarithmic** |  |  |
| math.log(x) | The natural logarithm of x (to base e). | math.log(math.e) 1.0 math.log(0) ValueError: math domain error |
  ```
- **D (`openstax-python-2024_p064_c01`, 599 chars):**
  ```text
| Function | Description | Examples |
| --- | --- | --- |
| **Number-theoretic** |  |  |
| math.ceil(x) | The ceiling of x: the smallest integer greater than or equal to x. | math.ceil(7.4) 8 math.ceil(-7.4) -7 |
| math.floor(x) | The floor of x: the largest integer less than or equal to x. | math.floor(7.4) 7 math.floor(-7.4) -8 |
| **Power and logarithmic** |  |  |
| math.log(x) | The natural logarithm of x (to base e). | math.log(math.e) 1.0 math.log(0) ValueError: math domain error |
| math.log(x, base) | The logarithm of x to the given base. | math.log(8, 2) 3.0 math.log(10000, 10) 4.0 |
  ```

**Hướng dẫn soi lỗi & Gợi ý chấm trang này:**
- **A:** A (`1`): Có `Table 2.4` (`ceil`, `floor`, `math.log`) nhưng cắt cụt giữa lệnh ở cuối `"math."`. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **B/C:** B/C (`2`): Giữ trọn vẹn header `Table 2.4` và 3 hàng hoàn chỉnh (`ceil`, `floor`, `math.log(x)`). -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`
- **D:** D (`2`): Giữ trọn vẹn header `Table 2.4` và 4 hàng hoàn chỉnh (thêm `math.log(x, base)`). -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`

---

### Trang PDF 68 (Sách: 58, `ch2_expressions`, mục `2.7`)
- **A (`openstax-python-2024_p068_c01`, 500 chars):**
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
| Concatenation: one space before and after the +. | print(
  ```
- **B (`openstax-python-2024_p068_c01`, 440 chars):**
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
  ```
- **D (`openstax-python-2024_p068_c01`, 589 chars):**
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
| Concatenation: one space before and after the +. | print("Hi", name + "!") | print("Hi", name+"!") print("Hi", name+ "!") print("Hi", name +"!") |
  ```

**Hướng dẫn soi lỗi & Gợi ý chấm trang này:**
- **A:** A (`1`): Có `Table 2.7` 3 hàng đầu, nhưng cắt ngang ở hàng `Concatenation` tại `"print("`. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **B/C:** B/C (`2`): Trọn vẹn 3 hàng (`Parentheses`, `Commas`, `Assignment`), không cắt giữa hàng hay từ. -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`
- **D:** D (`2`): Trọn vẹn 4 hàng (`Parentheses`, `Commas`, `Assignment`, `Concatenation`). -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`

---

### Trang PDF 72 (Sách: 62, `ch2_expressions`, mục `2.8`)
- **A (`openstax-python-2024_p072_c01`, 500 chars):**
  ```text
2.8 Python careers

Learning objectives

By the end of this section you should be able to

• Summarize how Python is used in fields other than CS and IT.
• Describe two different kinds of applications made with Python. Fields and applications

Learning Python opens the door to many programming-related careers. Example job titles include software engineer, data scientist, web developer, and systems analyst. These jobs often require a degree in computer science (CS), information technology (IT), o
  ```
- **B (`openstax-python-2024_p072_c01`, 242 chars):**
  ```text
2.8 Python careers

Learning objectives

By the end of this section you should be able to

• Summarize how Python is used in fields other than CS and IT.
• Describe two different kinds of applications made with Python. Fields and applications
  ```
- **D (`openstax-python-2024_p072_c01`, 584 chars):**
  ```text
2.8 Python careers

Learning objectives

By the end of this section you should be able to

• Summarize how Python is used in fields other than CS and IT.
• Describe two different kinds of applications made with Python. Fields and applications

Learning Python opens the door to many programming-related careers. Example job titles include software engineer, data scientist, web developer, and systems analyst.

These jobs often require a degree in computer science (CS), information technology (IT), or a related field. However, programming is not limited to these fields and careers.
  ```

**Hướng dẫn soi lỗi & Gợi ý chấm trang này:**
- **A:** A (`1`): Có tiêu đề `2.8 Python careers`, `Learning objectives` và đoạn mở đầu, nhưng cắt giữa từ ở cuối `"(IT), o"`. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **B/C:** B/C (`1`, chốt ca biên nhất quán): Trọn khối `2.8` + 2 `Learning objectives` (242 ký tự), nhưng cuối bullet thứ 2 bị dính cụm tiêu đề phụ `"Fields and applications"` mà nội dung mục đó nằm ở chunk sau. -> Điểm chốt: **`1`** | `[ ] 0  [x] 1  [ ] 2`
- **D:** D (`2`): Trọn khối `2.8` + `Learning objectives` + 2 câu hoàn chỉnh giới thiệu nghề nghiệp Python. -> Điểm chốt: **`2`** | `[ ] 0  [ ] 1  [x] 2`

---

## Phần 2 — Phiếu kiểm tra Metadata Usefulness (7 câu `test` × Top-3 = 21 records/chiến lược)

Bảng dưới đây liệt kê **từng hit Top-3** và kết quả đối chiếu từng trường metadata với trang gốc trong `temp/ingestion_pages.json`:

### Chiến lược A

| Câu hỏi | Rank | Chunk ID | `page` (sách) | `chapter` / `section` | Khớp gốc (`source,page,book,ch,sec`) | Yêu cầu Filter & Tuân thủ |
| --- | :-: | --- | :-: | --- | :-: | --- |
| `q16` | 1 | `openstax-python-2024_p030_c01` | p.30 (b.20) | `ch1_statements` / `1.5` | **ĐÚNG** | N/A (không filter) |
| `q16` | 2 | `openstax-python-2024_p056_c04` | p.56 (b.46) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q16` | 3 | `openstax-python-2024_p047_c04` | p.47 (b.37) | `ch2_expressions` / `2.0` | **ĐÚNG** | N/A (không filter) |
| `q17` | 1 | `openstax-python-2024_p039_c01` | p.39 (b.29) | `ch1_statements` / `1.7` | **ĐÚNG** | N/A (không filter) |
| `q17` | 2 | `openstax-python-2024_p044_c03` | p.44 (b.34) | `ch1_statements` / `1.9` | **ĐÚNG** | N/A (không filter) |
| `q17` | 3 | `openstax-python-2024_p039_c02` | p.39 (b.29) | `ch1_statements` / `1.7` | **ĐÚNG** | N/A (không filter) |
| `q18` | 1 | `openstax-python-2024_p054_c02` | p.54 (b.44) | `ch2_expressions` / `2.3` | **ĐÚNG** | N/A (không filter) |
| `q18` | 2 | `openstax-python-2024_p054_c03` | p.54 (b.44) | `ch2_expressions` / `2.3` | **ĐÚNG** | N/A (không filter) |
| `q18` | 3 | `openstax-python-2024_p055_c01` | p.55 (b.45) | `ch2_expressions` / `2.3` | **ĐÚNG** | N/A (không filter) |
| `q19` | 1 | `openstax-python-2024_p057_c03` | p.57 (b.47) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q19` | 2 | `openstax-python-2024_p057_c04` | p.57 (b.47) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q19` | 3 | `openstax-python-2024_p058_c01` | p.58 (b.48) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q20` | 1 | `openstax-python-2024_p070_c02` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q20` | 2 | `openstax-python-2024_p070_c03` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q20` | 3 | `openstax-python-2024_p070_c01` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q24` | 1 | `openstax-python-2024_p068_c02` | p.68 (b.58) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q24` | 2 | `openstax-python-2024_p068_c01` | p.68 (b.58) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q24` | 3 | `openstax-python-2024_p067_c04` | p.67 (b.57) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q25` | 1 | `openstax-python-2024_p072_c05` | p.72 (b.62) | `ch2_expressions` / `2.8` | **ĐÚNG** | N/A (không filter) |
| `q25` | 2 | `openstax-python-2024_p072_c04` | p.72 (b.62) | `ch2_expressions` / `2.8` | **ĐÚNG** | N/A (không filter) |
| `q25` | 3 | `openstax-python-2024_p072_c03` | p.72 (b.62) | `ch2_expressions` / `2.8` | **ĐÚNG** | N/A (không filter) |

- **Tổng hợp chiến lược A:** Khớp nguồn gốc **`21/21` (100%)** | **Filter Compliance:** **Không áp dụng (`unfiltered`)** *(tỷ lệ hit trùng chương ngẫu nhiên nhờ tương đồng ngữ nghĩa: `6/6` trên 2 câu `test` có nhãn filter `q20, q24`; trên toàn tập 5 câu có nhãn filter `dev+test` chỉ trúng `3/5` câu)*.

### Chiến lược B

| Câu hỏi | Rank | Chunk ID | `page` (sách) | `chapter` / `section` | Khớp gốc (`source,page,book,ch,sec`) | Yêu cầu Filter & Tuân thủ |
| --- | :-: | --- | :-: | --- | :-: | --- |
| `q16` | 1 | `openstax-python-2024_p030_c01` | p.30 (b.20) | `ch1_statements` / `1.5` | **ĐÚNG** | N/A (không filter) |
| `q16` | 2 | `openstax-python-2024_p030_c03` | p.30 (b.20) | `ch1_statements` / `1.5` | **ĐÚNG** | N/A (không filter) |
| `q16` | 3 | `openstax-python-2024_p056_c03` | p.56 (b.46) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q17` | 1 | `openstax-python-2024_p039_c01` | p.39 (b.29) | `ch1_statements` / `1.7` | **ĐÚNG** | N/A (không filter) |
| `q17` | 2 | `openstax-python-2024_p039_c02` | p.39 (b.29) | `ch1_statements` / `1.7` | **ĐÚNG** | N/A (không filter) |
| `q17` | 3 | `openstax-python-2024_p040_c02` | p.40 (b.30) | `ch1_statements` / `1.8` | **ĐÚNG** | N/A (không filter) |
| `q18` | 1 | `openstax-python-2024_p054_c03` | p.54 (b.44) | `ch2_expressions` / `2.3` | **ĐÚNG** | N/A (không filter) |
| `q18` | 2 | `openstax-python-2024_p055_c01` | p.55 (b.45) | `ch2_expressions` / `2.3` | **ĐÚNG** | N/A (không filter) |
| `q18` | 3 | `openstax-python-2024_p044_c01` | p.44 (b.34) | `ch1_statements` / `1.9` | **ĐÚNG** | N/A (không filter) |
| `q19` | 1 | `openstax-python-2024_p057_c04` | p.57 (b.47) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q19` | 2 | `openstax-python-2024_p058_c01` | p.58 (b.48) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q19` | 3 | `openstax-python-2024_p074_c02` | p.74 (b.64) | `ch2_expressions` / `2.9` | **ĐÚNG** | N/A (không filter) |
| `q20` | 1 | `openstax-python-2024_p070_c03` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q20` | 2 | `openstax-python-2024_p070_c02` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q20` | 3 | `openstax-python-2024_p070_c01` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q24` | 1 | `openstax-python-2024_p068_c02` | p.68 (b.58) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q24` | 2 | `openstax-python-2024_p068_c01` | p.68 (b.58) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q24` | 3 | `openstax-python-2024_p067_c05` | p.67 (b.57) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> Trùng chương ngẫu nhiên (không bật filter) |
| `q25` | 1 | `openstax-python-2024_p072_c08` | p.72 (b.62) | `ch2_expressions` / `2.8` | **ĐÚNG** | N/A (không filter) |
| `q25` | 2 | `openstax-python-2024_p072_c06` | p.72 (b.62) | `ch2_expressions` / `2.8` | **ĐÚNG** | N/A (không filter) |
| `q25` | 3 | `openstax-python-2024_p072_c04` | p.72 (b.62) | `ch2_expressions` / `2.8` | **ĐÚNG** | N/A (không filter) |

- **Tổng hợp chiến lược B:** Khớp nguồn gốc **`21/21` (100%)** | **Filter Compliance:** **Không áp dụng (`unfiltered`)** *(tỷ lệ hit trùng chương ngẫu nhiên nhờ tương đồng ngữ nghĩa: `6/6` trên 2 câu `test` có nhãn filter `q20, q24`; trên toàn tập 5 câu có nhãn filter `dev+test` chỉ trúng `4/5` câu)*.

### Chiến lược C

| Câu hỏi | Rank | Chunk ID | `page` (sách) | `chapter` / `section` | Khớp gốc (`source,page,book,ch,sec`) | Yêu cầu Filter & Tuân thủ |
| --- | :-: | --- | :-: | --- | :-: | --- |
| `q16` | 1 | `openstax-python-2024_p030_c01` | p.30 (b.20) | `ch1_statements` / `1.5` | **ĐÚNG** | N/A (không filter) |
| `q16` | 2 | `openstax-python-2024_p030_c03` | p.30 (b.20) | `ch1_statements` / `1.5` | **ĐÚNG** | N/A (không filter) |
| `q16` | 3 | `openstax-python-2024_p056_c03` | p.56 (b.46) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q17` | 1 | `openstax-python-2024_p039_c01` | p.39 (b.29) | `ch1_statements` / `1.7` | **ĐÚNG** | N/A (không filter) |
| `q17` | 2 | `openstax-python-2024_p039_c02` | p.39 (b.29) | `ch1_statements` / `1.7` | **ĐÚNG** | N/A (không filter) |
| `q17` | 3 | `openstax-python-2024_p040_c02` | p.40 (b.30) | `ch1_statements` / `1.8` | **ĐÚNG** | N/A (không filter) |
| `q18` | 1 | `openstax-python-2024_p054_c03` | p.54 (b.44) | `ch2_expressions` / `2.3` | **ĐÚNG** | N/A (không filter) |
| `q18` | 2 | `openstax-python-2024_p055_c01` | p.55 (b.45) | `ch2_expressions` / `2.3` | **ĐÚNG** | N/A (không filter) |
| `q18` | 3 | `openstax-python-2024_p044_c01` | p.44 (b.34) | `ch1_statements` / `1.9` | **ĐÚNG** | N/A (không filter) |
| `q19` | 1 | `openstax-python-2024_p057_c04` | p.57 (b.47) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q19` | 2 | `openstax-python-2024_p058_c01` | p.58 (b.48) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q19` | 3 | `openstax-python-2024_p074_c02` | p.74 (b.64) | `ch2_expressions` / `2.9` | **ĐÚNG** | N/A (không filter) |
| `q20` | 1 | `openstax-python-2024_p070_c03` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q20` | 2 | `openstax-python-2024_p070_c02` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q20` | 3 | `openstax-python-2024_p070_c01` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q24` | 1 | `openstax-python-2024_p068_c02` | p.68 (b.58) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q24` | 2 | `openstax-python-2024_p068_c01` | p.68 (b.58) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q24` | 3 | `openstax-python-2024_p067_c05` | p.67 (b.57) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q25` | 1 | `openstax-python-2024_p072_c08` | p.72 (b.62) | `ch2_expressions` / `2.8` | **ĐÚNG** | N/A (không filter) |
| `q25` | 2 | `openstax-python-2024_p072_c06` | p.72 (b.62) | `ch2_expressions` / `2.8` | **ĐÚNG** | N/A (không filter) |
| `q25` | 3 | `openstax-python-2024_p072_c04` | p.72 (b.62) | `ch2_expressions` / `2.8` | **ĐÚNG** | N/A (không filter) |

- **Tổng hợp chiến lược C:** Khớp nguồn gốc **`21/21` (100%)** | **Filter Compliance (có bật SQL pre-filter):** **`100%`** (`6/6` hit trên 2 câu `test` có filter `q20, q24`; `5/5` câu = `15/15` hit trên toàn tập `dev+test`).

### Chiến lược D

| Câu hỏi | Rank | Chunk ID | `page` (sách) | `chapter` / `section` | Khớp gốc (`source,page,book,ch,sec`) | Yêu cầu Filter & Tuân thủ |
| --- | :-: | --- | :-: | --- | :-: | --- |
| `q16` | 1 | `openstax-python-2024_p030_c01` | p.30 (b.20) | `ch1_statements` / `1.5` | **ĐÚNG** | N/A (không filter) |
| `q16` | 2 | `openstax-python-2024_p056_c03` | p.56 (b.46) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q16` | 3 | `openstax-python-2024_p056_c02` | p.56 (b.46) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q17` | 1 | `openstax-python-2024_p039_c01` | p.39 (b.29) | `ch1_statements` / `1.7` | **ĐÚNG** | N/A (không filter) |
| `q17` | 2 | `openstax-python-2024_p039_c03` | p.39 (b.29) | `ch1_statements` / `1.7` | **ĐÚNG** | N/A (không filter) |
| `q17` | 3 | `openstax-python-2024_p037_c01` | p.37 (b.27) | `ch1_statements` / `1.7` | **ĐÚNG** | N/A (không filter) |
| `q18` | 1 | `openstax-python-2024_p054_c02` | p.54 (b.44) | `ch2_expressions` / `2.3` | **ĐÚNG** | N/A (không filter) |
| `q18` | 2 | `openstax-python-2024_p055_c01` | p.55 (b.45) | `ch2_expressions` / `2.3` | **ĐÚNG** | N/A (không filter) |
| `q18` | 3 | `openstax-python-2024_p044_c01` | p.44 (b.34) | `ch1_statements` / `1.9` | **ĐÚNG** | N/A (không filter) |
| `q19` | 1 | `openstax-python-2024_p057_c03` | p.57 (b.47) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q19` | 2 | `openstax-python-2024_p058_c01` | p.58 (b.48) | `ch2_expressions` / `2.4` | **ĐÚNG** | N/A (không filter) |
| `q19` | 3 | `openstax-python-2024_p074_c02` | p.74 (b.64) | `ch2_expressions` / `2.9` | **ĐÚNG** | N/A (không filter) |
| `q20` | 1 | `openstax-python-2024_p070_c02` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q20` | 2 | `openstax-python-2024_p070_c03` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q20` | 3 | `openstax-python-2024_p070_c01` | p.70 (b.60) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q24` | 1 | `openstax-python-2024_p068_c02` | p.68 (b.58) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q24` | 2 | `openstax-python-2024_p068_c01` | p.68 (b.58) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q24` | 3 | `openstax-python-2024_p067_c03` | p.67 (b.57) | `ch2_expressions` / `2.7` | **ĐÚNG** | `{'chapter': 'ch2_expressions'}` -> **Đúng** |
| `q25` | 1 | `openstax-python-2024_p072_c04` | p.72 (b.62) | `ch2_expressions` / `2.8` | **ĐÚNG** | N/A (không filter) |
| `q25` | 2 | `openstax-python-2024_p072_c03` | p.72 (b.62) | `ch2_expressions` / `2.8` | **ĐÚNG** | N/A (không filter) |
| `q25` | 3 | `openstax-python-2024_p073_c02` | p.73 (b.63) | `ch2_expressions` / `2.9` | **ĐÚNG** | N/A (không filter) |

- **Tổng hợp chiến lược D:** Khớp nguồn gốc **`21/21` (100%)** | **Filter Compliance (có bật SQL pre-filter):** **`100%`** (`6/6` hit trên 2 câu `test` có filter `q20, q24`; `5/5` câu = `15/15` hit trên toàn tập `dev+test`).

### Nhận xét Metadata Usefulness (cho cả hệ thống)
- **Trường hữu ích:** `chapter` và `section` giúp pre-filter chính xác theo phạm vi chương (`C`, `D` đạt `5/5` toàn tập); `source`, `page`, `book_page` giúp trích dẫn nguồn đến từng trang.
- **Hạn chế:** Thiếu trường phân loại khối `content_type` (`prose` / `table` / `table_caption` / `mcq_exercise`) nên chú thích bảng ngắn và câu hỏi trắc nghiệm vẫn chen vào Top-3; thiếu `prev_chunk_id`/`next_chunk_id` để tự nối đoạn bảng bị tách.

---

## Phần 3 — Phiếu chấm Answer Grounding Quality (7 câu `test` × 4 chiến lược)

*(Mỗi câu dưới đây gồm: **Câu hỏi -> Đáp án chuẩn & Checklist ý bắt buộc -> Nội dung Top-3 thực tế của A, B, C, D -> Gợi ý & Ô bạn tick điểm**.)*

### Câu `q16` (`direct` | trang chuẩn: `30` | các trang hợp lệ: `[30]` | filter: `None`)

- **Câu hỏi:** Python hỗ trợ hai định dạng số cơ bản (basic number formats) nào, và mỗi định dạng biểu diễn loại số gì?
- **Đáp án chuẩn:** Python hỗ trợ hai định dạng số cơ bản là số nguyên (integer) biểu diễn số nguyên tròn (whole number) và số thực dấu phẩy động (floating-point) biểu diễn số thập phân (decimal number).
- **Câu bằng chứng gốc trong sách:** `Python supports two basic number formats, integer and floating-point. An integer represents a whole number, and a floating-point format represents a decimal number.`
- **Cách chấm (Checklist các ý cần tìm thấy trong Top-3 chunks ghép lại):**
  - **Ý 1:** Nêu đúng hai định dạng số cơ bản là `integer` (số nguyên) và `floating-point` (số thực dấu phẩy động).
  - **Ý 2:** Nêu đúng ý nghĩa: `integer` biểu diễn số nguyên tròn (`whole number`), `floating-point` biểu diễn số thập phân (`decimal number`).
  - *Quy ước:* Đủ hết các ý = **`2`** | Thiếu 1 ý hoặc thiếu điều kiện = **`1`** | Không có thông tin trả lời = **`0`**.

#### Chiến lược A
- *Chỉ số máy đo (tham khảo):* `Hit@1=True` | `Evidence Hit@3 (1 chunk)=True` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p030_c01` | `score=0.7161` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
• Explain the precedence of arithmetic operators. Numeric data types

Python supports two basic number formats, integer and floating-point. An integer represents a whole number, and a floating-point format represents a decimal number. The format a language uses to represent data is called a data type. In addition to integer and floating-point types, programming languages typically have a string type for representing text.

CHECKPOINT

Integer and floating-point

Integer and floating point; ch 1,
  ```
- **Rank 2** | `openstax-python-2024_p056_c04` | `score=0.6828` | `page=56` (`book=46`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
015625)10 when converted back, which is not exactly equal to (0.1)10.

| Col 1 | Col 2 |
| --- | --- |
| # Print floats with 30 decimal places print(f'{0.1:.30f}') # prints 0.1 print(f'{0.2:.30f}') # prints 0.2 print(f'{0.4:.30f}') # prints 0.4 | 0.100000000000000005551115123126 0.200000000000000011102230246252 0.400000000000000022204460492503 |

Table 2.1 Round-off error. (The example above shows a formatted string or f-string, which are introduced in the Objects chapter.)

An overflow error oc
  ```
- **Rank 3** | `openstax-python-2024_p047_c04` | `score=0.6824` | `page=47` (`book=37`, `chapter=ch2_expressions`, `section=2.0`)
  ```text
details about integers and floating-point numbers, explain how to import and use the math module, and show how to make long lines of code easier to read.
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Rank 1 (`p030_c01`) chứa nguyên văn cả Ý 1 và Ý 2.
- **Điểm bạn chốt cho A (`q16`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược B
- *Chỉ số máy đo (tham khảo):* `Hit@1=True` | `Evidence Hit@3 (1 chunk)=True` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p030_c01` | `score=0.7179` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
• Explain the precedence of arithmetic operators. Numeric data types

Python supports two basic number formats, integer and floating-point. An integer represents a whole number, and a floating-point format represents a decimal number. The format a language uses to represent data is called a data type. In addition to integer and floating-point types, programming languages typically have a string type for representing text.

CHECKPOINT

Integer and floating-point
  ```
- **Rank 2** | `openstax-python-2024_p030_c03` | `score=0.6844` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
a. string
b. int
c. float

Basic arithmetic

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.

Four basic arithmetic operators exist in Python:

1. Addition (+)
2. Subtraction (-)
  ```
- **Rank 3** | `openstax-python-2024_p056_c03` | `score=0.6819` | `page=56` (`book=46`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Floating-point values are stored as binary by Python. The conversion of a floating point number to the underlying binary results in specific types of floating-point errors.

A round-off error occurs when floating-point values are stored erroneously as an approximation. The difference between an approximation of a value used in computation and the correct (true) value is called a round-off error.
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Rank 1 (`p030_c01`) chứa nguyên văn cả Ý 1 và Ý 2.
- **Điểm bạn chốt cho B (`q16`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược C *(Lưu ý: câu này `filter=None` nên C chạy giống hệt B)*
- *Chỉ số máy đo (tham khảo):* `Hit@1=True` | `Evidence Hit@3 (1 chunk)=True` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p030_c01` | `score=0.7179` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
• Explain the precedence of arithmetic operators. Numeric data types

Python supports two basic number formats, integer and floating-point. An integer represents a whole number, and a floating-point format represents a decimal number. The format a language uses to represent data is called a data type. In addition to integer and floating-point types, programming languages typically have a string type for representing text.

CHECKPOINT

Integer and floating-point
  ```
- **Rank 2** | `openstax-python-2024_p030_c03` | `score=0.6844` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
a. string
b. int
c. float

Basic arithmetic

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.

Four basic arithmetic operators exist in Python:

1. Addition (+)
2. Subtraction (-)
  ```
- **Rank 3** | `openstax-python-2024_p056_c03` | `score=0.6819` | `page=56` (`book=46`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Floating-point values are stored as binary by Python. The conversion of a floating point number to the underlying binary results in specific types of floating-point errors.

A round-off error occurs when floating-point values are stored erroneously as an approximation. The difference between an approximation of a value used in computation and the correct (true) value is called a round-off error.
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Giống B (`filter=None`), Rank 1 (`p030_c01`) đủ cả Ý 1 và Ý 2.
- **Điểm bạn chốt cho C (`q16`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược D
- *Chỉ số máy đo (tham khảo):* `Hit@1=True` | `Evidence Hit@3 (1 chunk)=True` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p030_c01` | `score=0.7079` | `page=30` (`book=20`, `chapter=ch1_statements`, `section=1.5`)
  ```text
• Explain the precedence of arithmetic operators. Numeric data types

Python supports two basic number formats, integer and floating-point. An integer represents a whole number, and a floating-point format represents a decimal number.

The format a language uses to represent data is called a data type. In addition to integer and floating-point types, programming languages typically have a string type for representing text.

CHECKPOINT

Integer and floating-point

Integer and floating point; ch 1, video 8 (https://www.openstax.org/r/integer-and-floating-point)

CONCEPTS IN PRACTICE

Integers, floats, and strings
  ```
- **Rank 2** | `openstax-python-2024_p056_c03` | `score=0.6878` | `page=56` (`book=46`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Ex: Storing the float (0.1)10 results in binary values that actually produce (0.1000000000000000055511151231257827021181583404541015625)10 when converted back, which is not exactly equal to (0.1)10.

| Col 1 | Col 2 |
| --- | --- |
| # Print floats with 30 decimal places print(f'{0.1:.30f}') # prints 0.1 print(f'{0.2:.30f}') # prints 0.2 print(f'{0.4:.30f}') # prints 0.4 | 0.100000000000000005551115123126 0.200000000000000011102230246252 0.400000000000000022204460492503 |

Table 2.1 Round-off error. (The example above shows a formatted string or f-string, which are introduced in the Objects chapter.)
  ```
- **Rank 3** | `openstax-python-2024_p056_c02` | `score=0.6831` | `page=56` (`book=46`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Computers store information using 0's and 1's. All information must be converted to a string of 0's and 1's. Ex: 5 is converted to 101. Since only two values, 0 or 1, are allowed the format is called binary.

Floating-point values are stored as binary by Python. The conversion of a floating point number to the underlying binary results in specific types of floating-point errors.

A round-off error occurs when floating-point values are stored erroneously as an approximation.

The difference between an approximation of a value used in computation and the correct (true) value is called a round-off error.
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Rank 1 (`p030_c01`) chứa nguyên văn cả Ý 1 và Ý 2.
- **Điểm bạn chốt cho D (`q16`):** `[ ] 0   [ ] 1   [x] 2`

---

### Câu `q17` (`paraphrase` | trang chuẩn: `39` | các trang hợp lệ: `[39, 44]` | filter: `None`)

- **Câu hỏi:** Chuỗi văn bản tùy chọn đặt ở đầu một chương trình Python dùng để làm tài liệu mô tả được gọi là gì, và thường được viết bằng cú pháp nào khi nội dung dài?
- **Đáp án chuẩn:** Chuỗi đó được gọi là docstring, và vì tài liệu mô tả có thể dài nên docstring thường được viết dưới dạng chuỗi nhiều dòng (multi-line strings) sử dụng cặp 3 dấu nháy kép (""").
- **Câu bằng chứng gốc trong sách:** `Python programs may optionally begin with a string known as a docstring. ... Documentation can be long, so docstrings are generally written as multi-line strings (""").`
- **Cách chấm (Checklist các ý cần tìm thấy trong Top-3 chunks ghép lại):**
  - **Ý 1:** Gọi tên đúng chuỗi tài liệu ở đầu chương trình là `docstring`.
  - **Ý 2:** Nêu đúng cú pháp thường dùng khi nội dung dài là chuỗi nhiều dòng (`multi-line strings`) dùng `"""`.
  - *Quy ước:* Đủ hết các ý = **`2`** | Thiếu 1 ý hoặc thiếu điều kiện = **`1`** | Không có thông tin trả lời = **`0`**.

#### Chiến lược A
- *Chỉ số máy đo (tham khảo):* `Hit@1=True` | `Evidence Hit@3 (1 chunk)=True` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p039_c01` | `score=0.7397` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
c. insert a # at the beginning of the line.

Documentation

Python programs may optionally begin with a string known as a docstring. A docstring is documentation written for others who will use the program but not necessarily read the source code. Most of the official documentation at docs.python.org (https://openstax.org/r/100docstrings) is generated from docstrings.

Documentation can be long, so docstrings are generally written as multi-line strings ("""). Common elements of a docstring inclu
  ```
- **Rank 2** | `openstax-python-2024_p044_c03` | `score=0.7337` | `page=44` (`book=34`, `chapter=ch1_statements`, `section=1.9`)
  ```text
Used for documentation, often in multi-line strings, to summarize a program's purpose or usage. |

Table 1.6 Chapter 1 reference.

TRY IT

Fun facts

Write a program that assigns a variable named number to any integer of your choice. Ex: number = 74. Then, use this variable to calculate and output the following results:
  ```
- **Rank 3** | `openstax-python-2024_p039_c02` | `score=0.7257` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
trings ("""). Common elements of a docstring include a one-line summary, a blank line, and a longer description.

CHECKPOINT

Vacations docstring

Vacations docstring; ch 1, video 13 (https://www.openstax.org/r/docstring)

CONCEPTS IN PRACTICE

Documentation

7 . The main purpose of writing docstrings is to . . .
a. summarize the program's purpose or usage.
b. explain how each part of the code works.
c. maintain a list of ideas for new features.

8 . Which of the following is NOT a docstring?
a.
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Rank 1 (`p039_c01`) có đủ cả Ý 1 (`known as a docstring`) và Ý 2 (`multi-line strings (""")`).
- **Điểm bạn chốt cho A (`q17`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược B
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p039_c01` | `score=0.7381` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
c. insert a # at the beginning of the line.

Documentation

Python programs may optionally begin with a string known as a docstring. A docstring is documentation written for others who will use the program but not necessarily read the source code. Most of the official documentation at docs.python.org (https://openstax.org/r/100docstrings) is generated from docstrings.
  ```
- **Rank 2** | `openstax-python-2024_p039_c02` | `score=0.7348` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
Documentation can be long, so docstrings are generally written as multi-line strings ("""). Common elements of a docstring include a one-line summary, a blank line, and a longer description.

CHECKPOINT

Vacations docstring

Vacations docstring; ch 1, video 13 (https://www.openstax.org/r/docstring)

CONCEPTS IN PRACTICE

Documentation
  ```
- **Rank 3** | `openstax-python-2024_p040_c02` | `score=0.7229` | `page=40` (`book=30`, `chapter=ch1_statements`, `section=1.8`)
  ```text
Write a docstring for the following program. The first line of the docstring should explain, in one short sentence, what the program is. The second line of the docstring should be blank. The third and subsequent lines should include a longer explanation of what the program does. At the end of the docstring, add a line that says "Author: " followed by your name.

Access multimedia content (http://openstax.org/books/introduction-python-programming/pages/1-7-comments)

1.8 Why Python?
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — **Hợp nhất Top-3 đủ 100%**: Rank 1 (`p039_c01`) có Ý 1; Rank 2 (`p039_c02`) có Ý 2. *(Máy chấm strict báo `ev_hit3=False` do tách 2 chunk, nhưng LLM đọc cả Top-3 vẫn trả lời đủ -> `2/2`)*.
- **Điểm bạn chốt cho B (`q17`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược C *(Lưu ý: câu này `filter=None` nên C chạy giống hệt B)*
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p039_c01` | `score=0.7381` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
c. insert a # at the beginning of the line.

Documentation

Python programs may optionally begin with a string known as a docstring. A docstring is documentation written for others who will use the program but not necessarily read the source code. Most of the official documentation at docs.python.org (https://openstax.org/r/100docstrings) is generated from docstrings.
  ```
- **Rank 2** | `openstax-python-2024_p039_c02` | `score=0.7348` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
Documentation can be long, so docstrings are generally written as multi-line strings ("""). Common elements of a docstring include a one-line summary, a blank line, and a longer description.

CHECKPOINT

Vacations docstring

Vacations docstring; ch 1, video 13 (https://www.openstax.org/r/docstring)

CONCEPTS IN PRACTICE

Documentation
  ```
- **Rank 3** | `openstax-python-2024_p040_c02` | `score=0.7229` | `page=40` (`book=30`, `chapter=ch1_statements`, `section=1.8`)
  ```text
Write a docstring for the following program. The first line of the docstring should explain, in one short sentence, what the program is. The second line of the docstring should be blank. The third and subsequent lines should include a longer explanation of what the program does. At the end of the docstring, add a line that says "Author: " followed by your name.

Access multimedia content (http://openstax.org/books/introduction-python-programming/pages/1-7-comments)

1.8 Why Python?
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Giống B (`filter=None`): Rank 1 (Ý 1) + Rank 2 (Ý 2) ghép lại đủ 100% -> `2/2`.
- **Điểm bạn chốt cho C (`q17`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược D
- *Chỉ số máy đo (tham khảo):* `Hit@1=True` | `Evidence Hit@3 (1 chunk)=True` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p039_c01` | `score=0.7390` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
c. insert a # at the beginning of the line.

Documentation

Python programs may optionally begin with a string known as a docstring. A docstring is documentation written for others who will use the program but not necessarily read the source code.

Most of the official documentation at docs.python.org (https://openstax.org/r/100docstrings) is generated from docstrings.

Documentation can be long, so docstrings are generally written as multi-line strings ("""). Common elements of a docstring include a one-line summary, a blank line, and a longer description.

CHECKPOINT

Vacations docstring
  ```
- **Rank 2** | `openstax-python-2024_p039_c03` | `score=0.7189` | `page=39` (`book=29`, `chapter=ch1_statements`, `section=1.7`)
  ```text
c. # Vacations Madlib. # # This program asks the user for two adjectives # and two nouns, which are then used to print # a funny story about a vacation.

9 . Which docstring is most useful for this program?
a. """Vacations Madlib."""

b. """Vacations Madlib. This program asks the user for two adjectives and two nouns, which are then used to print a funny story about a vacation. """

c. """Vacations Madlib. This program asks the user for two adjectives and two nouns, which are then used to print a funny story about a vacation.
  ```
- **Rank 3** | `openstax-python-2024_p037_c01` | `score=0.7078` | `page=37` (`book=27`, `chapter=ch1_statements`, `section=1.7`)
  ```text
1.7 Comments

Learning objectives

By the end of this section you should be able to

• Write concise, meaningful comments that explain intended functionality of the code.
• Write a docstring (more verbose comment) that describes the program functionality. The hash character

Comments are short phrases that explain what the code is doing. Ex: Lines 1, 8, and 10 in the following program contain comments. Each comment begins with a hash character (#).

All text from the hash character to the end of the line is ignored when running the program. In contrast, hash characters inside of strings are treated as regular text.
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Rank 1 (`p039_c01`) chứa trọn cả Ý 1 và Ý 2 trong 1 chunk duy nhất.
- **Điểm bạn chốt cho D (`q17`):** `[ ] 0   [ ] 1   [x] 2`

---

### Câu `q18` (`conditional` | trang chuẩn: `54` | các trang hợp lệ: `[54]` | filter: `None`)

- **Câu hỏi:** Những phép toán số học nào không tương thích giữa kiểu chuỗi (string) và kiểu số (numeric), và toán tử * hoạt động thế nào khi dùng giữa một chuỗi và một số nguyên?
- **Đáp án chuẩn:** Kiểu chuỗi và kiểu số không tương thích trong các phép cộng, trừ và chia; tuy nhiên toán tử * đóng vai trò là toán tử lặp (repetition operator), nhận một toán hạng chuỗi và một toán hạng số nguyên để lặp lại chuỗi đó.
- **Câu bằng chứng gốc trong sách:** `Strings and numeric data types are incompatible for addition, subtraction, and division. ... The * operator also serves as the repetition operator, which accepts a string operand and an integer operand and repeats the string.`
- **Cách chấm (Checklist các ý cần tìm thấy trong Top-3 chunks ghép lại):**
  - **Ý 1:** Nêu rõ 3 phép toán không tương thích giữa chuỗi (`string`) và số (`numeric`): cộng (`addition`), trừ (`subtraction`), chia (`division`).
  - **Ý 2:** Nêu vai trò toán tử `*` là toán tử lặp (`repetition operator`), nhận 1 chuỗi và 1 số nguyên (`integer`) để lặp lại chuỗi.
  - *Quy ước:* Đủ hết các ý = **`2`** | Thiếu 1 ý hoặc thiếu điều kiện = **`1`** | Không có thông tin trả lời = **`0`**.

#### Chiến lược A
- *Chỉ số máy đo (tham khảo):* `Hit@1=True` | `Evidence Hit@3 (1 chunk)=True` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p054_c02` | `score=0.7794` | `page=54` (`book=44`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
s the number in a calculation. This results in an error in the program because the input() function by default stores the number as a string. Strings and numeric data types are incompatible for addition, subtraction, and division. One of the operands needs to be explicitly converted depending on the goal of arithmetic or string concatenation.

The * operator also serves as the repetition operator, which accepts a string operand and an integer operand and repeats the string. Ex: "banjo" * 3 produ
  ```
- **Rank 2** | `openstax-python-2024_p054_c03` | `score=0.7271` | `page=54` (`book=44`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
rand and repeats the string. Ex: "banjo" * 3 produces "banjobanjobanjo".

CHECKPOINT

Adding a string and an integer

Adding a string and an integer; ch 2, video 6 (https://www.openstax.org/r/adding-str-int)
  ```
- **Rank 3** | `openstax-python-2024_p055_c01` | `score=0.7232` | `page=55` (`book=45`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
CONCEPTS IN PRACTICE

Operations combining numeric types and strings

8 . int('34') + 56
a. '3456'
b. 90
c. '90'

9 . str(12) + ' red roses'
a. '12 red roses'
b. '12'
c. Error

10 . '50' * 3
a. '150'
b. 150
c. '505050'

11 . str(5.2) + 7
a. 12.2
b. '12.2'
c. Error

12 . 80.0 + int('100')
a. 180
b. 180.0
c. '180'

13 . str(3.14) + '159'
a. 162.14
b. '3.14159'
c. Error

14 . 2.0 * 'this'
a. 'this'
b. 'thisthis'
c. Error

TRY IT

After the point

Write a program that reads in a string of digits tha
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Rank 1 (`p054_c02`) chứa trọn cả Ý 1 lẫn Ý 2.
- **Điểm bạn chốt cho A (`q18`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược B
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=False` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p054_c03` | `score=0.7715` | `page=54` (`book=44`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
One of the operands needs to be explicitly converted depending on the goal of arithmetic or string concatenation.

The * operator also serves as the repetition operator, which accepts a string operand and an integer operand and repeats the string. Ex: "banjo" * 3 produces "banjobanjobanjo".

CHECKPOINT

Adding a string and an integer

Adding a string and an integer; ch 2, video 6 (https://www.openstax.org/r/adding-str-int)
  ```
- **Rank 2** | `openstax-python-2024_p055_c01` | `score=0.7214` | `page=55` (`book=45`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
CONCEPTS IN PRACTICE

Operations combining numeric types and strings

8 . int('34') + 56
a. '3456'
b. 90
c. '90'

9 . str(12) + ' red roses'
a. '12 red roses'
b. '12'
c. Error

10 . '50' * 3
a. '150'
b. 150
c. '505050'

11 . str(5.2) + 7
a. 12.2
b. '12.2'
c. Error

12 . 80.0 + int('100')
a. 180
b. 180.0
c. '180'

13 . str(3.14) + '159'
a. 162.14
b. '3.14159'
c. Error

14 . 2.0 * 'this'
a. 'this'
b. 'thisthis'
c. Error

TRY IT

After the point
  ```
- **Rank 3** | `openstax-python-2024_p044_c01` | `score=0.7198` | `page=44` (`book=34`, `chapter=ch1_statements`, `section=1.9`)
  ```text
| Function | Description |
| --- | --- |
| = (Assignment) | Assigns (or updates) the value of a variable. In Python, variables begin to exist when assigned for the first time. |
| + (Concatenation) | Appends the contents of two strings, resulting in a new string. |
| + (Addition) | Adds the values of two numbers. |
| - (Subtraction) | Subtracts the value of one number from another. |
| * (Multiplication) | Multiplies the values of two numbers. |
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`1 / 2`** — **Thiếu Ý 1**: Rank 1 (`p054_c03`) chỉ có Ý 2 (`*` repetition operator). Vế Ý 1 nằm ở `p054_c02` nhưng bị rớt khỏi Top-3; Rank 2 là bài tập trắc nghiệm và Rank 3 là bảng p.44 không nói tính tương thích cộng/trừ/chia -> chỉ được `1/2`.
- **Điểm bạn chốt cho B (`q18`):** `[ ] 0   [x] 1   [ ] 2`

#### Chiến lược C *(Lưu ý: câu này `filter=None` nên C chạy giống hệt B)*
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=False` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p054_c03` | `score=0.7715` | `page=54` (`book=44`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
One of the operands needs to be explicitly converted depending on the goal of arithmetic or string concatenation.

The * operator also serves as the repetition operator, which accepts a string operand and an integer operand and repeats the string. Ex: "banjo" * 3 produces "banjobanjobanjo".

CHECKPOINT

Adding a string and an integer

Adding a string and an integer; ch 2, video 6 (https://www.openstax.org/r/adding-str-int)
  ```
- **Rank 2** | `openstax-python-2024_p055_c01` | `score=0.7214` | `page=55` (`book=45`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
CONCEPTS IN PRACTICE

Operations combining numeric types and strings

8 . int('34') + 56
a. '3456'
b. 90
c. '90'

9 . str(12) + ' red roses'
a. '12 red roses'
b. '12'
c. Error

10 . '50' * 3
a. '150'
b. 150
c. '505050'

11 . str(5.2) + 7
a. 12.2
b. '12.2'
c. Error

12 . 80.0 + int('100')
a. 180
b. 180.0
c. '180'

13 . str(3.14) + '159'
a. 162.14
b. '3.14159'
c. Error

14 . 2.0 * 'this'
a. 'this'
b. 'thisthis'
c. Error

TRY IT

After the point
  ```
- **Rank 3** | `openstax-python-2024_p044_c01` | `score=0.7198` | `page=44` (`book=34`, `chapter=ch1_statements`, `section=1.9`)
  ```text
| Function | Description |
| --- | --- |
| = (Assignment) | Assigns (or updates) the value of a variable. In Python, variables begin to exist when assigned for the first time. |
| + (Concatenation) | Appends the contents of two strings, resulting in a new string. |
| + (Addition) | Adds the values of two numbers. |
| - (Subtraction) | Subtracts the value of one number from another. |
| * (Multiplication) | Multiplies the values of two numbers. |
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`1 / 2`** — Giống B (`filter=None`): có Ý 2 ở Rank 1, thiếu Ý 1 -> `1/2`.
- **Điểm bạn chốt cho C (`q18`):** `[ ] 0   [x] 1   [ ] 2`

#### Chiến lược D
- *Chỉ số máy đo (tham khảo):* `Hit@1=True` | `Evidence Hit@3 (1 chunk)=True` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p054_c02` | `score=0.7747` | `page=54` (`book=44`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
This results in an error in the program because the input() function by default stores the number as a string. Strings and numeric data types are incompatible for addition, subtraction, and division.

One of the operands needs to be explicitly converted depending on the goal of arithmetic or string concatenation.

The * operator also serves as the repetition operator, which accepts a string operand and an integer operand and repeats the string. Ex: "banjo" * 3 produces "banjobanjobanjo".

CHECKPOINT

Adding a string and an integer

Adding a string and an integer; ch 2, video 6 (https://www.openstax.org/r/adding-str-int)
  ```
- **Rank 2** | `openstax-python-2024_p055_c01` | `score=0.7215` | `page=55` (`book=45`, `chapter=ch2_expressions`, `section=2.3`)
  ```text
CONCEPTS IN PRACTICE

Operations combining numeric types and strings

8 . int('34') + 56
a. '3456'
b. 90
c. '90'

9 . str(12) + ' red roses'
a. '12 red roses'
b. '12'
c. Error

10 . '50' * 3
a. '150'
b. 150
c. '505050'

11 . str(5.2) + 7
a. 12.2
b. '12.2'
c. Error

12 . 80.0 + int('100')
a. 180
b. 180.0
c. '180'

13 . str(3.14) + '159'
a. 162.14
b. '3.14159'
c. Error

14 . 2.0 * 'this'
a. 'this'
b. 'thisthis'
c. Error

TRY IT

After the point

Write a program that reads in a string of digits that represents the digits after the decimal point of a number, num. Concatenate the input string together with '.' and num, and print the result.
  ```
- **Rank 3** | `openstax-python-2024_p044_c01` | `score=0.7060` | `page=44` (`book=34`, `chapter=ch1_statements`, `section=1.9`)
  ```text
| Function | Description |
| --- | --- |
| = (Assignment) | Assigns (or updates) the value of a variable. In Python, variables begin to exist when assigned for the first time. |
| + (Concatenation) | Appends the contents of two strings, resulting in a new string. |
| + (Addition) | Adds the values of two numbers. |
| - (Subtraction) | Subtracts the value of one number from another. |
| * (Multiplication) | Multiplies the values of two numbers. |
| /(Division) | Divides the value of one number by another. |
| ** (Exponentiation) | Raises a number to a power. Ex: 3**2 is three squared. |
| Syntax | Description |
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Rank 1 (`p054_c02`) chứa trọn cả Ý 1 và Ý 2 trong 1 chunk.
- **Điểm bạn chốt cho D (`q18`):** `[ ] 0   [ ] 1   [x] 2`

---

### Câu `q19` (`conditional` | trang chuẩn: `57` | các trang hợp lệ: `[57, 74]` | filter: `None`)

- **Câu hỏi:** Hàm round() trong Python dùng để làm gì, và điều gì xảy ra nếu đối số thứ hai không được truyền vào?
- **Đáp án chuẩn:** Hàm round() dùng để làm tròn một số thực dấu phẩy động đến một số chữ số thập phân nhất định. Nếu đối số thứ hai không được cung cấp, số đó sẽ được làm tròn đến số nguyên gần nhất (closest integer).
- **Câu bằng chứng gốc trong sách:** `Python's round() function is used to round a floating-point number to a given number of decimal places. The function requires two arguments. The first argument is the number to be rounded. The second argument decides the number of decimal places to which the number is rounded. If the second argument is not provided, the number will be rounded to the closest integer.`
- **Cách chấm (Checklist các ý cần tìm thấy trong Top-3 chunks ghép lại):**
  - **Ý 1:** Nêu đúng công dụng của `round()`: làm tròn một số thực (`floating-point`) đến một số chữ số thập phân nhất định.
  - **Ý 2:** Nêu đúng hành vi khi không truyền đối số thứ 2: làm tròn đến số nguyên gần nhất (`closest/nearest integer`).
  - *Quy ước:* Đủ hết các ý = **`2`** | Thiếu 1 ý hoặc thiếu điều kiện = **`1`** | Không có thông tin trả lời = **`0`**.

#### Chiến lược A
- *Chỉ số máy đo (tham khảo):* `Hit@1=True` | `Evidence Hit@3 (1 chunk)=True` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p057_c03` | `score=0.7285` | `page=57` (`book=47`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
b. overflow

Floating point round() function

Python's round() function is used to round a floating-point number to a given number of decimal places. The function requires two arguments. The first argument is the number to be rounded. The second argument decides the number of decimal places to which the number is rounded. If the second argument is not provided, the number will be rounded to the closest integer. The round() function can be used to mitigate floating-point errors.

Ex:

• round(2.
  ```
- **Rank 2** | `openstax-python-2024_p057_c04` | `score=0.7169` | `page=57` (`book=47`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
o mitigate floating-point errors.

Ex:

• round(2.451, 2) = 2.45
• round(2.451) = 2

CHECKPOINT

Examples of round() function

Examples of a round () function; ch 2, video 7 (https://www.openstax.org/r/round-function)
  ```
- **Rank 3** | `openstax-python-2024_p058_c01` | `score=0.7029` | `page=58` (`book=48`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
CONCEPTS IN PRACTICE

Examples of round() function

3 . What is the output of round(6.6)?
a. 6
b. 6.6
c. 7

4 . What is the output of round(3.5, 2)?
a. 3
b. 3.5
c. 3.50

5 . What is the output of round(12)?
a. 12.0
b. 12
c. 12.00

6 . What is the output of round(0.1, 1)?
a. 0.1
b. 0.10
c. 0.1000000000000000055511151231257827021181583404541015625

TRY IT

Inaccurate tips

The following code calculates the tip amount, given a bill amount and the tip ratio. Experiment with the following bill amount
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Rank 1 (`p057_c03`) chứa trọn vẹn đoạn giải thích cả Ý 1 và Ý 2.
- **Điểm bạn chốt cho A (`q19`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược B
- *Chỉ số máy đo (tham khảo):* `Hit@1=True` | `Evidence Hit@3 (1 chunk)=True` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p057_c04` | `score=0.7840` | `page=57` (`book=47`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Python's round() function is used to round a floating-point number to a given number of decimal places. The function requires two arguments. The first argument is the number to be rounded. The second argument decides the number of decimal places to which the number is rounded. If the second argument is not provided, the number will be rounded to the closest integer. The round() function can be used to mitigate floating-point errors.

Ex:

• round(2.451, 2) = 2.45
• round(2.451) = 2

CHECKPOINT
  ```
- **Rank 2** | `openstax-python-2024_p058_c01` | `score=0.7107` | `page=58` (`book=48`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
CONCEPTS IN PRACTICE

Examples of round() function

3 . What is the output of round(6.6)?
a. 6
b. 6.6
c. 7

4 . What is the output of round(3.5, 2)?
a. 3
b. 3.5
c. 3.50

5 . What is the output of round(12)?
a. 12.0
b. 12
c. 12.00

6 . What is the output of round(0.1, 1)?
a. 0.1
b. 0.10
c. 0.1000000000000000055511151231257827021181583404541015625

TRY IT

Inaccurate tips
  ```
- **Rank 3** | `openstax-python-2024_p074_c02` | `score=0.6861` | `page=74` (`book=64`, `chapter=ch2_expressions`, `section=2.9`)
  ```text
| Function | Description |
| --- | --- |
| abs(x) | Returns the absolute value of x. |
| int(x) | Converts x (a string or float) to an integer. |
| float(x) | Converts x (a string or integer) to a float. |
| str(x) | Converts x (a float or integer) to a string. |
| round(x, ndigits) | Rounds x to ndigits places after the decimal point. If ndigits is omitted, returns the nearest integer to x. |
| Operator | Description |
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Rank 1 (`p057_c04`) chứa trọn vẹn đoạn giải thích cả Ý 1 và Ý 2.
- **Điểm bạn chốt cho B (`q19`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược C *(Lưu ý: câu này `filter=None` nên C chạy giống hệt B)*
- *Chỉ số máy đo (tham khảo):* `Hit@1=True` | `Evidence Hit@3 (1 chunk)=True` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p057_c04` | `score=0.7840` | `page=57` (`book=47`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
Python's round() function is used to round a floating-point number to a given number of decimal places. The function requires two arguments. The first argument is the number to be rounded. The second argument decides the number of decimal places to which the number is rounded. If the second argument is not provided, the number will be rounded to the closest integer. The round() function can be used to mitigate floating-point errors.

Ex:

• round(2.451, 2) = 2.45
• round(2.451) = 2

CHECKPOINT
  ```
- **Rank 2** | `openstax-python-2024_p058_c01` | `score=0.7107` | `page=58` (`book=48`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
CONCEPTS IN PRACTICE

Examples of round() function

3 . What is the output of round(6.6)?
a. 6
b. 6.6
c. 7

4 . What is the output of round(3.5, 2)?
a. 3
b. 3.5
c. 3.50

5 . What is the output of round(12)?
a. 12.0
b. 12
c. 12.00

6 . What is the output of round(0.1, 1)?
a. 0.1
b. 0.10
c. 0.1000000000000000055511151231257827021181583404541015625

TRY IT

Inaccurate tips
  ```
- **Rank 3** | `openstax-python-2024_p074_c02` | `score=0.6861` | `page=74` (`book=64`, `chapter=ch2_expressions`, `section=2.9`)
  ```text
| Function | Description |
| --- | --- |
| abs(x) | Returns the absolute value of x. |
| int(x) | Converts x (a string or float) to an integer. |
| float(x) | Converts x (a string or integer) to a float. |
| str(x) | Converts x (a float or integer) to a string. |
| round(x, ndigits) | Rounds x to ndigits places after the decimal point. If ndigits is omitted, returns the nearest integer to x. |
| Operator | Description |
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Giống B (`filter=None`), Rank 1 (`p057_c04`) đủ cả Ý 1 và Ý 2.
- **Điểm bạn chốt cho C (`q19`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược D
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=False` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p057_c03` | `score=0.7370` | `page=57` (`book=47`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
The second argument decides the number of decimal places to which the number is rounded. If the second argument is not provided, the number will be rounded to the closest integer.

The round() function can be used to mitigate floating-point errors.

Ex:

• round(2.451, 2) = 2.45
• round(2.451) = 2

CHECKPOINT

Examples of round() function

Examples of a round () function; ch 2, video 7 (https://www.openstax.org/r/round-function)
  ```
- **Rank 2** | `openstax-python-2024_p058_c01` | `score=0.6993` | `page=58` (`book=48`, `chapter=ch2_expressions`, `section=2.4`)
  ```text
CONCEPTS IN PRACTICE

Examples of round() function

3 . What is the output of round(6.6)?
a. 6
b. 6.6
c. 7

4 . What is the output of round(3.5, 2)?
a. 3
b. 3.5
c. 3.50

5 . What is the output of round(12)?
a. 12.0
b. 12
c. 12.00

6 . What is the output of round(0.1, 1)?
a. 0.1
b. 0.10
c. 0.1000000000000000055511151231257827021181583404541015625

TRY IT

Inaccurate tips

The following code calculates the tip amount, given a bill amount and the tip ratio. Experiment with the following bill amounts and tip ratios and see if any inaccuracies may result in calculating the tip amount.
  ```
- **Rank 3** | `openstax-python-2024_p074_c02` | `score=0.6888` | `page=74` (`book=64`, `chapter=ch2_expressions`, `section=2.9`)
  ```text
| Function | Description |
| --- | --- |
| abs(x) | Returns the absolute value of x. |
| int(x) | Converts x (a string or float) to an integer. |
| float(x) | Converts x (a string or integer) to a float. |
| str(x) | Converts x (a float or integer) to a string. |
| round(x, ndigits) | Rounds x to ndigits places after the decimal point. If ndigits is omitted, returns the nearest integer to x. |
| Operator | Description |
| s * n (Repetition) | Creates a string with n copies of s. Ex: "Ha" * 3 is "HaHaHa". |
| x / y (Real division) | Divides x by y and returns the entire result as a float. Ex: 7 / 4 is 1.75. |
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — **Ca hay cần đối chiếu kỹ**: Rank 1 (`p057_c03`) bị cụt 2 câu đầu (chỉ còn Ý 2 `closest integer` + `mitigate floating-point errors`), nên máy chấm `ev_hit3=False`. Tuy nhiên **Rank 3 (`p074_c02`, bảng tóm tắt 2.9)** ghi rõ `round(x, ndigits) | Rounds x to ndigits places after the decimal point. If ndigits is omitted, returns the nearest integer to x.` -> **Ghép Rank 1 + Rank 3 đủ cả Ý 1 lẫn Ý 2 -> `2/2`**.
- **Điểm bạn chốt cho D (`q19`):** `[ ] 0   [ ] 1   [x] 2`

---

### Câu `q20` (`metadata_filter` | trang chuẩn: `70` | các trang hợp lệ: `[70]` | filter: `{'chapter': 'ch2_expressions'}`)

- **Câu hỏi:** Trong chương Expressions, Python cung cấp hai cách nào để viết câu lệnh trên nhiều dòng (multi-line statements), và chuẩn PEP 8 khuyên nên tránh dùng cách nào?
- **Đáp án chuẩn:** Python cung cấp hai cách là nối dòng tường minh (explicit line joining dùng ký tự \) và nối dòng ngầm định (implicit line joining dùng dấu ngoặc đơn). Chuẩn PEP 8 khuyến nghị tránh sử dụng nối dòng tường minh (explicit line joining) bất cứ khi nào có thể.
- **Câu bằng chứng gốc trong sách:** `Python provides two ways to write multi-line statements: ... Explicit line joining, using \ characters: ... Implicit line joining, using parentheses: ... PEP 8 recommends avoiding the use of explicit line joining whenever possible.`
- **Cách chấm (Checklist các ý cần tìm thấy trong Top-3 chunks ghép lại):**
  - **Ý 1:** Nêu đủ 2 cách viết multi-line: nối dòng tường minh (`explicit line joining` dùng `\`) và nối dòng ngầm định (`implicit line joining` dùng ngoặc đơn `parentheses`).
  - **Ý 2:** Nêu đúng khuyến nghị của PEP 8: tránh sử dụng `explicit line joining` bất cứ khi nào có thể.
  - *Quy ước:* Đủ hết các ý = **`2`** | Thiếu 1 ý hoặc thiếu điều kiện = **`1`** | Không có thông tin trả lời = **`0`**.

#### Chiến lược A
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=True`
- **Rank 1** | `openstax-python-2024_p070_c02` | `score=0.7816` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
eople to dissolve the political bands..."
• Implicit line joining, using parentheses:

decl = ("The unanimous Declaration of the thirteen united States of " "America, When in the Course of human events, it becomes " "necessary for one people to dissolve the political bands...")

Implicit line joining is more common, since many statements and expressions use parentheses anyway. PEP 8 recommends avoiding the use of explicit line joining whenever possible.

CONCEPTS IN PRACTICE

Multi-line statemen
  ```
- **Rank 2** | `openstax-python-2024_p070_c03` | `score=0.7577` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
ssible.

CONCEPTS IN PRACTICE

Multi-line statements

8 . Which character is used for explicit line joining?
a. /
b. \
c. |

9 . What is the best way to print a very long string?
a. Break up the string into multiple smaller strings. print("..." # first part of string "..." # next part of string "...")
b. Print the string using multiple print statements. print("...") # first part of string print("...") # next part of string print("...")
c. Assign the string to a variable and print the variable. t
  ```
- **Rank 3** | `openstax-python-2024_p070_c01` | `score=0.7401` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
a. Hello,Ada
b. Hello, Ada
c. SyntaxError

Multi-line statements

Most statements in a Python program need only one line of code. But occasionally longer statements need to span multiple lines. Python provides two ways to write multi-line statements:

• Explicit line joining, using \ characters:

decl = "The unanimous Declaration of the thirteen united States of " \ "America, When in the Course of human events, it becomes " \ "necessary for one people to dissolve the political bands..."
• Implic
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — **Hợp nhất Top-3 đủ 100%**: Rank 3 (`p070_c01`) có `explicit line joining (\)` + mở đầu `implicit`; Rank 1 (`p070_c02`) có tiếp `implicit (parentheses)` và khuyến nghị PEP 8 tránh `explicit line joining`.
- **Điểm bạn chốt cho A (`q20`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược B
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=True`
- **Rank 1** | `openstax-python-2024_p070_c03` | `score=0.7679` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
Implicit line joining is more common, since many statements and expressions use parentheses anyway. PEP 8 recommends avoiding the use of explicit line joining whenever possible.

CONCEPTS IN PRACTICE

Multi-line statements

8 . Which character is used for explicit line joining?
a. /
b. \
c. |
  ```
- **Rank 2** | `openstax-python-2024_p070_c02` | `score=0.7508` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
decl = "The unanimous Declaration of the thirteen united States of " \ "America, When in the Course of human events, it becomes " \ "necessary for one people to dissolve the political bands..."
• Implicit line joining, using parentheses:

decl = ("The unanimous Declaration of the thirteen united States of " "America, When in the Course of human events, it becomes " "necessary for one people to dissolve the political bands...")
  ```
- **Rank 3** | `openstax-python-2024_p070_c01` | `score=0.7442` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
a. Hello,Ada
b. Hello, Ada
c. SyntaxError

Multi-line statements

Most statements in a Python program need only one line of code. But occasionally longer statements need to span multiple lines. Python provides two ways to write multi-line statements:

• Explicit line joining, using \ characters:
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — **Hợp nhất Top-3 đủ 100%**: Rank 3 (`p070_c01`) có nhãn `Explicit line joining (\)`, Rank 2 (`p070_c02`) có `Implicit line joining (parentheses)`, Rank 1 (`p070_c03`) có khuyến nghị PEP 8.
- **Điểm bạn chốt cho B (`q20`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược C
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=True`
- **Rank 1** | `openstax-python-2024_p070_c03` | `score=0.7679` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
Implicit line joining is more common, since many statements and expressions use parentheses anyway. PEP 8 recommends avoiding the use of explicit line joining whenever possible.

CONCEPTS IN PRACTICE

Multi-line statements

8 . Which character is used for explicit line joining?
a. /
b. \
c. |
  ```
- **Rank 2** | `openstax-python-2024_p070_c02` | `score=0.7508` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
decl = "The unanimous Declaration of the thirteen united States of " \ "America, When in the Course of human events, it becomes " \ "necessary for one people to dissolve the political bands..."
• Implicit line joining, using parentheses:

decl = ("The unanimous Declaration of the thirteen united States of " "America, When in the Course of human events, it becomes " "necessary for one people to dissolve the political bands...")
  ```
- **Rank 3** | `openstax-python-2024_p070_c01` | `score=0.7442` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
a. Hello,Ada
b. Hello, Ada
c. SyntaxError

Multi-line statements

Most statements in a Python program need only one line of code. But occasionally longer statements need to span multiple lines. Python provides two ways to write multi-line statements:

• Explicit line joining, using \ characters:
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Cùng chiến lược chunk với B, filter `ch2_expressions` khớp 3/3; hợp nhất Top-3 đủ cả Ý 1 và Ý 2.
- **Điểm bạn chốt cho C (`q20`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược D
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=True`
- **Rank 1** | `openstax-python-2024_p070_c02` | `score=0.7718` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
• Implicit line joining, using parentheses:

decl = ("The unanimous Declaration of the thirteen united States of " "America, When in the Course of human events, it becomes " "necessary for one people to dissolve the political bands...")

Implicit line joining is more common, since many statements and expressions use parentheses anyway. PEP 8 recommends avoiding the use of explicit line joining whenever possible.

CONCEPTS IN PRACTICE

Multi-line statements

8 . Which character is used for explicit line joining?
a. /
b. \
c. |
  ```
- **Rank 2** | `openstax-python-2024_p070_c03` | `score=0.7633` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
Multi-line statements

8 . Which character is used for explicit line joining?
a. /
b. \
c. |

9 . What is the best way to print a very long string?
a. Break up the string into multiple smaller strings. print("..." # first part of string "..." # next part of string "...")

b. Print the string using multiple print statements. print("...") # first part of string print("...") # next part of string print("...")

c. Assign the string to a variable and print the variable. text = "..." # the entire string print(text)

10 . Which example consists of two statements?
a. print("Happy " "New Year")
b. saying = ("Happy " "New Year")
  ```
- **Rank 3** | `openstax-python-2024_p070_c01` | `score=0.7454` | `page=70` (`book=60`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
a. Hello,Ada
b. Hello, Ada
c. SyntaxError

Multi-line statements

Most statements in a Python program need only one line of code. But occasionally longer statements need to span multiple lines. Python provides two ways to write multi-line statements:

• Explicit line joining, using \ characters:

decl = "The unanimous Declaration of the thirteen united States of " \ "America, When in the Course of human events, it becomes " \ "necessary for one people to dissolve the political bands..."

• Implicit line joining, using parentheses:
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — **Hợp nhất Top-3 đủ 100%**: Rank 3 (`p070_c01`) có đủ `Explicit (\)` + `Implicit`; Rank 1 (`p070_c02`) có `Implicit (parentheses)` + khuyến nghị PEP 8.
- **Điểm bạn chốt cho D (`q20`):** `[ ] 0   [ ] 1   [x] 2`

---

### Câu `q24` (`table_lookup` | trang chuẩn: `68` | các trang hợp lệ: `[68]` | filter: `{'chapter': 'ch2_expressions'}`)

- **Câu hỏi:** Trong chương Expressions, theo bảng hướng dẫn dùng khoảng trắng (Table 2.7 Guidelines for spaces), quy tắc đặt khoảng trắng quanh dấu phẩy (,), dấu gán (=) và phép toán số học (Arithmetic) là gì?
- **Đáp án chuẩn:** Với dấu phẩy: không có khoảng trắng trước và có một khoảng trắng sau (ví dụ print("Hello", name)). Với phép gán (=): có một khoảng trắng trước và sau dấu = (ví dụ name = input("Your name? ")). Với biểu thức số học: dùng khoảng trắng để thể hiện phép toán có độ ưu tiên thấp hơn (ví dụ x**2 + 5*x - 8).
- **Câu bằng chứng gốc trong sách:** `| Commas: no space before, one space after. | print("Hello", name) | ... | Assignment: one space before and after the =. | name = input("Your name? ") | ... | Arithmetic: use space to show lower precedence. | x**2 + 5*x - 8 |`
- **Cách chấm (Checklist các ý cần tìm thấy trong Top-3 chunks ghép lại):**
  - **Ý 1:** Dấu phẩy (`,`): không có khoảng trắng trước, 1 khoảng trắng sau (`no space before, one space after`).
  - **Ý 2:** Dấu gán (`=`): 1 khoảng trắng trước và sau (`one space before and after the =`).
  - **Ý 3:** Phép toán số học (`Arithmetic`): dùng khoảng trắng để thể hiện phép toán có độ ưu tiên thấp hơn (`use space to show lower precedence`, ví dụ `x**2 + 5*x - 8`).
  - *Quy ước:* Đủ hết các ý = **`2`** | Thiếu 1 ý hoặc thiếu điều kiện = **`1`** | Không có thông tin trả lời = **`0`**.

#### Chiến lược A
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=True`
- **Rank 1** | `openstax-python-2024_p068_c02` | `score=0.7823` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
nation: one space before and after the +. | print("Hi", name + "!") | print("Hi", name+"!") print("Hi", name+ "!") print("Hi", name +"!") |
| Arithmetic: use space to show lower precedence. | x**2 + 5*x - 8 | x ** 2 + 5 * x - 8 x ** 2+5 * x-8 x**2+5*x-8 |

Table 2.7 Guidelines for spaces.

CONCEPTS IN PRACTICE

Recommended spacing

1 . Which statement is formatted properly?
a. name = input("What is your name? ")
b. name = input ("What is your name? ")
c. name = input( "What is your name? " )

2
  ```
- **Rank 2** | `openstax-python-2024_p068_c01` | `score=0.7584` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
| Concatenation: one space before and after the +. | print(
  ```
- **Rank 3** | `openstax-python-2024_p067_c04` | `score=0.7184` | `page=67` (`book=57`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
, how to break up long lines, and other important topics.

PYTHON STYLE GUIDE

PEP 8 (https://openstax.org/r/100PEP8) is the official style guide for Python. PEP stands for Python Enhancement Proposal. Members of the Python community write PEPs to document best practices and propose new features. The table below is based on guidelines from PEP 8 under the heading Whitespace in Expressions and Statements (https://openstax.org/r/100whitespace).
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — **Hợp nhất Rank 2 + Rank 1 đủ 3/3 quy tắc**: Rank 2 (`p068_c01`) có Ý 1 & Ý 2; Rank 1 (`p068_c02`) có Ý 3 + nhãn `Table 2.7`.
- **Điểm bạn chốt cho A (`q24`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược B
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=True`
- **Rank 1** | `openstax-python-2024_p068_c02` | `score=0.7978` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Concatenation: one space before and after the +. | print("Hi", name + "!") | print("Hi", name+"!") print("Hi", name+ "!") print("Hi", name +"!") |
| Arithmetic: use space to show lower precedence. | x**2 + 5*x - 8 | x ** 2 + 5 * x - 8 x ** 2+5 * x-8 x**2+5*x-8 |

Table 2.7 Guidelines for spaces.

CONCEPTS IN PRACTICE

Recommended spacing
  ```
- **Rank 2** | `openstax-python-2024_p068_c01` | `score=0.7555` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
  ```
- **Rank 3** | `openstax-python-2024_p067_c05` | `score=0.7397` | `page=67` (`book=57`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
PEP 8 (https://openstax.org/r/100PEP8) is the official style guide for Python. PEP stands for Python Enhancement Proposal. Members of the Python community write PEPs to document best practices and propose new features. The table below is based on guidelines from PEP 8 under the heading Whitespace in Expressions and Statements (https://openstax.org/r/100whitespace).
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — **Hợp nhất Rank 2 + Rank 1 đủ 3/3 quy tắc**: Rank 2 (`p068_c01`) có Ý 1 & Ý 2; Rank 1 (`p068_c02`) có Ý 3 + nhãn `Table 2.7`.
- **Điểm bạn chốt cho B (`q24`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược C
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=True`
- **Rank 1** | `openstax-python-2024_p068_c02` | `score=0.7978` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Concatenation: one space before and after the +. | print("Hi", name + "!") | print("Hi", name+"!") print("Hi", name+ "!") print("Hi", name +"!") |
| Arithmetic: use space to show lower precedence. | x**2 + 5*x - 8 | x ** 2 + 5 * x - 8 x ** 2+5 * x-8 x**2+5*x-8 |

Table 2.7 Guidelines for spaces.

CONCEPTS IN PRACTICE

Recommended spacing
  ```
- **Rank 2** | `openstax-python-2024_p068_c01` | `score=0.7555` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
  ```
- **Rank 3** | `openstax-python-2024_p067_c05` | `score=0.7397` | `page=67` (`book=57`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
PEP 8 (https://openstax.org/r/100PEP8) is the official style guide for Python. PEP stands for Python Enhancement Proposal. Members of the Python community write PEPs to document best practices and propose new features. The table below is based on guidelines from PEP 8 under the heading Whitespace in Expressions and Statements (https://openstax.org/r/100whitespace).
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Filter `ch2_expressions` khớp 3/3; Rank 2 (`p068_c01`) + Rank 1 (`p068_c02`) đủ 3/3 quy tắc.
- **Điểm bạn chốt cho C (`q24`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược D
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=True`
- **Rank 1** | `openstax-python-2024_p068_c02` | `score=0.7771` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Arithmetic: use space to show lower precedence. | x**2 + 5*x - 8 | x ** 2 + 5 * x - 8 x ** 2+5 * x-8 x**2+5*x-8 |

Table 2.7 Guidelines for spaces.

CONCEPTS IN PRACTICE

Recommended spacing

1 . Which statement is formatted properly?
a. name = input("What is your name? ")
b. name = input ("What is your name? ")
c. name = input( "What is your name? " )

2 . Which statement is formatted properly?
a. name=name+"!"
b. name = name+"!"
c. name = name + "!"

3 . Which statement is formatted properly?
a. print("Hello",name)
b. print("Hello", name)
c. print("Hello " , name)
  ```
- **Rank 2** | `openstax-python-2024_p068_c01` | `score=0.7549` | `page=68` (`book=58`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
| Guideline | Example | Common Mistakes |
| --- | --- | --- |
| Parentheses: no space before or after. | print("Go team!") | print ("Go team!") print( "Go team!" ) |
| Commas: no space before, one space after. | print("Hello", name) | print("Hello" , name) print("Hello",name) |
| Assignment: one space before and after the =. | name = input("Your name? ") | name=input("Your name? ") name= input("Your name? ") name =input("Your name? ") |
| Concatenation: one space before and after the +. | print("Hi", name + "!") | print("Hi", name+"!") print("Hi", name+ "!") print("Hi", name +"!") |
  ```
- **Rank 3** | `openstax-python-2024_p067_c03` | `score=0.7185` | `page=67` (`book=57`, `chapter=ch2_expressions`, `section=2.7`)
  ```text
To encourage consistency, the Python community has a set of guidelines about where to put spaces and blank lines, what to name variables, how to break up long lines, and other important topics.

PYTHON STYLE GUIDE

PEP 8 (https://openstax.org/r/100PEP8) is the official style guide for Python. PEP stands for Python Enhancement Proposal.

Members of the Python community write PEPs to document best practices and propose new features.

The table below is based on guidelines from PEP 8 under the heading Whitespace in Expressions and Statements (https://openstax.org/r/100whitespace).
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — Filter `ch2_expressions` khớp 3/3; Rank 2 (`p068_c01`) + Rank 1 (`p068_c02`) đủ 3/3 quy tắc.
- **Điểm bạn chốt cho D (`q24`):** `[ ] 0   [ ] 1   [x] 2`

---

### Câu `q25` (`table_lookup` | trang chuẩn: `72` | các trang hợp lệ: `[72]` | filter: `None`)

- **Câu hỏi:** Theo bảng ví dụ về Python ngoài lĩnh vực CNTT và các ứng dụng xây dựng bằng Python (Table 2.8 và Table 2.9), nhà sinh học (biologist) dùng Python để làm gì và thư viện Matplotlib dùng cho lĩnh vực ứng dụng nào?
- **Đáp án chuẩn:** Trong lĩnh vực Khoa học (Science), nhà sinh học dùng Python để phân tích chuỗi DNA tìm ung thư; còn thư viện Matplotlib được dùng trong ứng dụng trực quan hóa dữ liệu (Data visualization) giúp nhà thống kê tạo biểu đồ.
- **Câu bằng chứng gốc trong sách:** `| Science | A biologist writes a Python program to analyze DNA sequences for cancer. | ... | Data visualization | A statistician creates charts to make sense of large amounts of data. Ex: Matplotlib library (https://openstax.org/r/100matplotlib). |`
- **Cách chấm (Checklist các ý cần tìm thấy trong Top-3 chunks ghép lại):**
  - **Ý 1 (Table 2.8):** Nhà sinh học (`biologist`, ngành `Science`) dùng Python để phân tích chuỗi DNA tìm ung thư (`analyze DNA sequences for cancer`).
  - **Ý 2 (Table 2.9):** Thư viện `Matplotlib` dùng cho ứng dụng trực quan hóa dữ liệu (`Data visualization`) giúp nhà thống kê tạo biểu đồ (`statistician creates charts...`).
  - *Quy ước:* Đủ hết các ý = **`2`** | Thiếu 1 ý hoặc thiếu điều kiện = **`1`** | Không có thông tin trả lời = **`0`**.

#### Chiến lược A
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p072_c05` | `score=0.7728` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
age and voice recognition. Ex: TensorFlow library (https://openstax.org/r/100tensorflow). |
| Data visualization | A statistician creates charts to make sense of large amounts of data. Ex: Matplotlib library (https://openstax.org/r/100matplotlib). |
| General purpose | Most programs in this book are general. Ex: Read inputs, perform calculations, print results. |

Table 2.9 Applications built with Python.
  ```
- **Rank 2** | `openstax-python-2024_p072_c04` | `score=0.7686` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
rk submissions. |
| Fine arts | An artist writes a Python program to operate an interactive art display. |
| Humanities | A linguist writes a Python program to analyze changes in slang word usage. |
| Science | A biologist writes a Python program to analyze DNA sequences for cancer. |

Table 2.8 Python outside of CS and IT.

| Application | Example use of Python |
| --- | --- |
| Artificial intelligence | An engineer develops models to support image and voice recognition. Ex: TensorFlow library
  ```
- **Rank 3** | `openstax-python-2024_p072_c03` | `score=0.7427` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
nds of applications. Table 2.9 shows a few examples of programs that can be written in Python. Given Python's usefulness and popularity, Python is a great language to learn. A supportive community of professionals and enthusiasts is ready to help.

| Field | Example use of Python |
| --- | --- |
| Business | An accountant writes a Python program to generate custom sales reports. |
| Education | A teacher writes a Python program to organize homework submissions. |
| Fine arts | An artist writes a
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — **Hợp nhất Rank 2 + Rank 1 đủ cả 2 ý**: Rank 2 (`p072_c04`) có hàng `Science | biologist...` + nhãn `Table 2.8`; Rank 1 (`p072_c05`) có hàng `Data visualization | ... Matplotlib` + nhãn `Table 2.9`.
- **Điểm bạn chốt cho A (`q25`):** `[ ] 0   [ ] 1   [x] 2`

#### Chiến lược B
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=False` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p072_c08` | `score=0.7682` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Table 2.9 Applications built with Python.
  ```
- **Rank 2** | `openstax-python-2024_p072_c06` | `score=0.7544` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Table 2.8 Python outside of CS and IT.
  ```
- **Rank 3** | `openstax-python-2024_p072_c04` | `score=0.7390` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Python is a versatile language that supports many kinds of applications. Table 2.9 shows a few examples of programs that can be written in Python. Given Python's usefulness and popularity, Python is a great language to learn. A supportive community of professionals and enthusiasts is ready to help.
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`0 / 2`** — **Thất bại hoàn toàn (`0/2`) do chunk caption mồ côi**: Rank 1 (`p072_c08`) chỉ là 1 dòng `"Table 2.9 Applications built with Python."` (trống nội dung); Rank 2 (`p072_c06`) chỉ là 1 dòng `"Table 2.8 Python outside of CS and IT."`; Rank 3 (`p072_c04`) là đoạn dẫn chung, không nhắc tới `biologist` hay `Matplotlib`.
- **Điểm bạn chốt cho B (`q25`):** `[x] 0   [ ] 1   [ ] 2`

#### Chiến lược C *(Lưu ý: câu này `filter=None` nên C chạy giống hệt B)*
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=False` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p072_c08` | `score=0.7682` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Table 2.9 Applications built with Python.
  ```
- **Rank 2** | `openstax-python-2024_p072_c06` | `score=0.7544` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Table 2.8 Python outside of CS and IT.
  ```
- **Rank 3** | `openstax-python-2024_p072_c04` | `score=0.7390` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Python is a versatile language that supports many kinds of applications. Table 2.9 shows a few examples of programs that can be written in Python. Given Python's usefulness and popularity, Python is a great language to learn. A supportive community of professionals and enthusiasts is ready to help.
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`0 / 2`** — Giống B (`filter=None`): Rank 1 & Rank 2 là 2 caption trống không có bảng, Rank 3 không có thông tin -> `0/2`.
- **Điểm bạn chốt cho C (`q25`):** `[x] 0   [ ] 1   [ ] 2`

#### Chiến lược D
- *Chỉ số máy đo (tham khảo):* `Hit@1=False` | `Evidence Hit@3 (1 chunk)=False` | `Hợp nhiều chunk Top-3=True` | `Filter=None`
- **Rank 1** | `openstax-python-2024_p072_c04` | `score=0.7643` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
Table 2.8 Python outside of CS and IT.

| Application | Example use of Python |
| --- | --- |
| Artificial intelligence | An engineer develops models to support image and voice recognition. Ex: TensorFlow library (https://openstax.org/r/100tensorflow). |
| Data visualization | A statistician creates charts to make sense of large amounts of data. Ex: Matplotlib library (https://openstax.org/r/100matplotlib). |
| General purpose | Most programs in this book are general. Ex: Read inputs, perform calculations, print results. |

Table 2.9 Applications built with Python.
  ```
- **Rank 2** | `openstax-python-2024_p072_c03` | `score=0.7615` | `page=72` (`book=62`, `chapter=ch2_expressions`, `section=2.8`)
  ```text
| Field | Example use of Python |
| --- | --- |
| Business | An accountant writes a Python program to generate custom sales reports. |
| Education | A teacher writes a Python program to organize homework submissions. |
| Fine arts | An artist writes a Python program to operate an interactive art display. |
| Humanities | A linguist writes a Python program to analyze changes in slang word usage. |
| Science | A biologist writes a Python program to analyze DNA sequences for cancer. |

Table 2.8 Python outside of CS and IT.
  ```
- **Rank 3** | `openstax-python-2024_p073_c02` | `score=0.7589` | `page=73` (`book=63`, `chapter=ch2_expressions`, `section=2.9`)
  ```text
2 . Which of the following Python libraries creates charts and plots?
a. Matplotlib
b. SciPy
c. TensorFlow

3 . Which of the following applications were built with Python?
a. Facebook
b. Instagram
c. WhatsApp

EXPLORING FURTHER

For more examples of applications that can be built with Python, see "Top 12 Fascinating Python Applications in Real-World" (https://openstax.org/r/100top12apps) by Rohit Sharma.

For more information about Python related careers, see "What Does a Python Developer Do?" (https://openstax.org/r/100careers) in BrainStation's career guide.

2.9 Chapter summary

Highlights from this chapter include:
  ```
- **Lý giải & Điểm chốt:** Điểm chốt = **`2 / 2`** — **Hợp nhất Rank 2 + Rank 1 đủ cả 2 ý**: Rank 2 (`p072_c03`) có trọn hàng `Science | biologist...`; Rank 1 (`p072_c04`) có trọn hàng `Data visualization | ... Matplotlib`.
- **Điểm bạn chốt cho D (`q25`):** `[ ] 0   [ ] 1   [x] 2`

---

