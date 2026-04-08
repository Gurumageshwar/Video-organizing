from video_organizer.core.scanner import scan_files
from video_organizer.core.mover import move_file
from video_organizer.core.metadata import extract_metadata, rename_file

class Organizer:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def run(self):
        files = scan_files(self.src)

        if not files:
            print(f"No video files found in '{self.src}'. Skipping process.")
            return
            
        print(f"Found {len(files)} video file(s). Starting organization...")

        for file in files:
            metadata = extract_metadata(file)
            new_name = rename_file(file, metadata)
            move_file(file, metadata, new_name, self.dest)