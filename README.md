# ZIP File Explorer

A small Flask app that lets you upload a ZIP file, unzips it in memory, and displays the file names inside the archive.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` and upload a `.zip` file.

## Notes

- The ZIP file is processed in memory.
- The app currently lists all entries reported by `ZipFile.namelist()`.
