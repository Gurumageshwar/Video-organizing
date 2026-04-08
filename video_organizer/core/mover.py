import os
import shutil
import sys

def _get_long_path(path):
    """Bypass Windows 260 character path limit."""
    if sys.platform == 'win32':
        path = os.path.abspath(path)
        if not path.startswith('\\\\?\\'):
            path = '\\\\?\\' + path
    return path

def move_file(src, metadata, new_name, dest_root):
    if metadata.video_type == "Series":
        if metadata.series_name:
            dest_path = os.path.join(dest_root, "Series", metadata.language, metadata.series_name, metadata.season)
        else:
            dest_path = os.path.join(dest_root, "Series", metadata.language, "Unknown Show")
    else:
        dest_path = os.path.join(dest_root, "Movies", metadata.language, str(metadata.year))

    # Safely handle creation of deep paths
    safe_dest_path = _get_long_path(dest_path)
    os.makedirs(safe_dest_path, exist_ok=True)

    dest_file = os.path.join(dest_path, new_name)
    safe_src = _get_long_path(src)
    safe_dest_file = _get_long_path(dest_file)
    
    if os.path.exists(safe_dest_file):
        response = input(f"Duplicate found: '{new_name}' already exists at destination. Overwrite? [y/N]: ")
        if response.strip().lower() != 'y':
            print(f"  -> Skipped '{new_name}'")
            return
            
    try:
        os.replace(safe_src, safe_dest_file)
        print(f"  -> Moved '{new_name}'")
    except OSError:
        shutil.move(safe_src, safe_dest_file)
        print(f"  -> Moved '{new_name}'")