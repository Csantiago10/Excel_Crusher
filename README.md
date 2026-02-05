# 📊 Excel Crusher

> **"Stop copying and pasting rows. Reclaim your time."**

![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![Built With](https://img.shields.io/badge/Built%20With-Python-yellow)

## 🧐 The Problem
Is your **data scattered across dozens of spreadsheets**?
We've all been there. You lose valuable time opening file after file, copying rows, and pasting them into a master document. It's boring, prone to human error, and kills your productivity.

## 💡 The Solution
**Excel Crusher** is an intelligent automation engine designed to detect, read, and consolidate massive amounts of data instantly. It takes a folder full of disconnected Excel files and merges them into a single, structured **Master Report** with just one command.

### ✨ Key Features
* **Smart Detection:** Automatically scans the `input_data` directory and targets only `.xlsx` files, ignoring temporary or irrelevant files.
* **Data Traceability:** Adds a customized column (`Source_File`) to every row, so you always know exactly which file the data came from.
* **Lightning Fast:** Processes and merges multiple workbooks in seconds using the power of the **Pandas** library.
* **Safe Execution:** Uses robust error handling to skip corrupt files without crashing the entire process.

---

## 🚀 How to Use

### Running from Source (For Developers)
If you want to inspect the code or run it directly:

```bash
# 1. Clone the repository
git clone [https://github.com/Csantiago10/Excel_Crusher.git](https://github.com/Csantiago10/Excel_Crusher.git)

# 2. Navigate to the folder
cd Excel_Crusher

# 3. Create virtual environment (Optional but recommended)
python -m venv venv
source venv/Scripts/activate # On Windows Git Bash

# 4. Install dependencies
pip install pandas openpyxl

# 5. Run the script
python src/consolidator.py