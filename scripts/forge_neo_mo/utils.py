import os
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Any


def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format"""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024.0 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.2f} {size_names[i]}"


def calculate_md5(file_path: str) -> str:
    """Calculate MD5 hash of a file"""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"Error calculating MD5 for {file_path}: {e}")
        return ""


def get_file_info(file_path: str) -> Dict[str, Any]:
    """Get information about a file"""
    try:
        stat = os.stat(file_path)
        return {
            "size": stat.st_size,
            "modified": stat.st_mtime,
            "created": stat.st_ctime,
            "md5": calculate_md5(file_path)
        }
    except Exception as e:
        print(f"Error getting file info for {file_path}: {e}")
        return {}


def sanitize_filename(filename: str) -> str:
    """Sanitize filename to remove invalid characters"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename.strip()


def create_thumbnail(image_path: str, thumbnail_path: str, size: tuple = (256, 256)) -> bool:
    """Create a thumbnail of an image"""
    try:
        from PIL import Image
        
        with Image.open(image_path) as img:
            img.thumbnail(size)
            img.save(thumbnail_path)
        return True
    except Exception as e:
        print(f"Error creating thumbnail: {e}")
        return False


def load_json_file(file_path: str) -> Dict:
    """Load JSON data from a file"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON file {file_path}: {e}")
        return {}


def save_json_file(file_path: str, data: Dict) -> bool:
    """Save data to a JSON file"""
    try:
        # Create directory if it doesn't exist
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving JSON file {file_path}: {e}")
        return False


def find_files_by_extension(directory: str, extensions: List[str]) -> List[str]:
    """Find all files with specified extensions in a directory"""
    found_files = []
    
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.lower().endswith(ext.lower()) for ext in extensions):
                    found_files.append(os.path.join(root, file))
    except Exception as e:
        print(f"Error scanning directory {directory}: {e}")
    
    return found_files