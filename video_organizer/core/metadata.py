import os
import re
from dataclasses import dataclass

@dataclass
class VideoMetadata:
    video_type: str  # 'Movie' or 'Series'
    language: str
    year: str
    series_name: str = ""
    season: str = ""

# Pre-compiled Regex patterns for performance
TV_PATTERN = re.compile(r'(?P<title>.*?)[ ._-]*(?:s(?P<season>\d{1,2})e(?P<episode>\d{1,2})|(?P<season_alt>\d{1,2})x(?P<episode_alt>\d{1,2}))', re.IGNORECASE)
YEAR_PATTERN = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_metadata(file_path):
    filename = os.path.basename(file_path)
    
    # Check if it's a TV Series using pre-compiled pattern
    tv_match = TV_PATTERN.search(filename)
    
    video_type = "Movie"
    series_name = ""
    season = ""
    
    if tv_match:
        video_type = "Series"
        extracted_title = tv_match.group('title')
        if extracted_title:
            series_name = extracted_title.replace('.', ' ').strip().title()
        else:
            series_name = "Unknown Show"
            
        season_num = tv_match.group('season') or tv_match.group('season_alt')
        if season_num:
            season = f"Season {int(season_num):02d}"
        else:
            season = "Unknown Season"

    # Try to find a 4-digit year in the filename using pre-compiled pattern
    year_match = YEAR_PATTERN.search(filename)
    year = year_match.group(1) if year_match else "Unknown"
    
    # In a real implementation we could use ffprobe or specific naming conventions
    # For now, default to English unless some clue is found.
    filename_lower = filename.lower()
    
    # Comprehensive dictionary of languages
    supported_langs = [
        "hindi", "tamil", "telugu", "malayalam", "kannada", 
        "spanish", "french", "german", "korean", "japanese", 
        "chinese"
    ]
    
    language = "English"
    for lang in supported_langs:
        if lang in filename_lower:
            language = lang.capitalize()
            break

    return VideoMetadata(
        video_type=video_type, 
        language=language, 
        year=year,
        series_name=series_name,
        season=season
    )

def rename_file(file_path, metadata):
    # Simply keep original name for now
    return os.path.basename(file_path)
