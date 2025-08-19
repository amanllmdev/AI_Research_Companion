
# 📝 Document Comparator

This is a lightweight Python tool designed to compare two text documents and highlight their differences using advanced natural language processing techniques.

## 🔍 Features

- Compare two `.txt` documents and identify:
  - Exact differences
  - Semantic (meaning-based) changes
- Provides a similarity score between documents
- Outputs side-by-side comparison
- Simple CLI interface — ideal for developers and content reviewers

## 📁 File Structure

```
document-comparator/
│
├── main.py                 # Main comparison script
├── requirements.txt        # Python dependencies
├── test_files/             # Demo documents for testing
│   ├── demo_doc1.txt
│   └── demo_doc2.txt
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/amanllmdev/document-comparator.git
cd document-comparator
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Script

```bash
python main.py
```

The program will compare the two sample files located in the `test_files/` directory.

## 🧪 Example Output

```
Similarity Score: 85%
➖ Differences:
- Line 3 differs in wording but retains similar meaning.
- Line 5 removed from doc2.
```

## 📄 Demo Files

Two demo documents (`demo_doc1.txt` and `demo_doc2.txt`) are provided inside the `test_files/` folder to help you quickly test the functionality.

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or submit PRs to improve document handling, add GUI, or improve comparison logic.

## 📜 License

This project is open-source and available under the MIT License.

## ✨ Future Scope

- Add support for `.pdf` and `.docx`
- Visual web-based diff viewer
- Streamlit UI for interactive comparison
