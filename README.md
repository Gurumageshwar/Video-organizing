# Video Organizer

A fast, intelligent, and highly customizable Python utility designed to automatically scan and organize chaotic directories of video files. It instantly categorizes your media into neatly structured "Movies" and "Series" libraries based on filename metadata.

## 🚀 Features

- **Smart Detection:** Uses pre-compiled regex to distinguish between TV Series (by Season/Episode) and standalone Movies.
- **Multi-Language Support:** Detects regional sub-labels in filenames (English, Tamil, Telugu, Hindi, Malayalam, Kannada, Spanish, French, German, Korean, Japanese, Chinese) and reorganizes them into localized folders.
- **Bypass Windows Limits:** Integrated `\\?\` pathing to safely handle massive filenames without crashing under Windows' 260-character `MAX_PATH` limit.
- **Blazing Fast I/O:** Powered by a recursive `os.scandir` loop to scan thousands of files across heavy drives in milliseconds.
- **Safe Duplicate Handling:** Interactively prompts for confirmation before overwriting identical files.

---

## 🛠️ Usage

**1. Prerequisites**
The core tool uses vanilla Python! Ensure you have Python 3.x installed. No massive third-party package dependencies like `pip install` are required to get moving.

**2. Run the Application**
Point the application to your source folder containing the jumbled videos, and give it a clean destination array:
```bash
python run.py --src "E:\Movies\Kollywood-Movies" --dest "E:\Movies"
```

---

## ⚙️ Configuration (`config.json`)

You can effortlessly customize how the script shapes your library by creating or editing the `config.json` file in the root directory.

```json
{
    "movies_folder_name": "Movies",
    "series_folder_name": "Series",
    "flatten_movies": false,
    "flatten_series": false
}
```

### Formatting Options:
- **`flatten_movies`:** Set to `true` to dump all standalone movies into the root `Movies/` folder. Set to `false` to cleanly nest them sequentially `(e.g., Movies/Language/Year/)`.
- **`flatten_series`:** Set to `true` to drop all series into one directory. Set to `false` to nest them structurally `(e.g., Series/Language/Show Name/Season XX/)`.

---

## 🧪 Testing

The platform ships with a testing suite to validate how the Regex engine interprets different filename structures. You can run trials against the parser by executing:

```bash
python -m unittest tests/test_metadata.py
```
