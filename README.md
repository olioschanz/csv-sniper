# 🎯 CSV Sniper

A Streamlit web app that matches email addresses between two CSV files.

---

## What It Does

Upload two CSV files:
- **First file** (your primary contact list)
- **Second file** (reference list)

The app will:
- Identify and normalize the email column
- Match email addresses between the two files
- Display the matched rows from your first file
- Let you **download** the matched results as a CSV

---

## How to Use It

**Live app:**  
[https://olioschanz-csv-sniper.streamlit.app](https://csv-sniper.streamlit.app/)

**Local use:**
```bash
# Clone the repo
git clone https://github.com/olioschanz/csv-sniper.git
cd csv-sniper

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run csv_sniper.py
