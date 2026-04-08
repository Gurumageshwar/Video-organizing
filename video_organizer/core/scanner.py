import os

VIDEO_EXTENSIONS = {'.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v'}

def scan_files(path):
    files = []
    
    def _scan(current_path):
        try:
            with os.scandir(current_path) as it:
                for entry in it:
                    if entry.is_dir(follow_symlinks=False):
                        _scan(entry.path)
                    elif entry.is_file(follow_symlinks=False):
                        ext = os.path.splitext(entry.name)[1].lower()
                        if ext in VIDEO_EXTENSIONS:
                            files.append(entry.path)
        except PermissionError:
            pass  # Skip directories we don't have access to
            
    if os.path.exists(path):
        _scan(path)
        
    return files