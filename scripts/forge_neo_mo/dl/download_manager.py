import os
import requests
from pathlib import Path
from typing import Optional, Callable
from urllib.parse import urlparse


class DownloadManager:
    """Manage downloading of AI models"""
    
    def __init__(self, download_dir: str = None):
        self.download_dir = download_dir or self._get_default_download_dir()
        self._ensure_directory_exists(self.download_dir)
    
    def _get_default_download_dir(self) -> str:
        """Get the default download directory"""
        # Try to find Forge NEO models directory
        base_path = Path(__file__).parent.parent.parent.parent
        models_path = base_path / "models"
        
        if models_path.exists():
            return str(models_path)
        
        # Fallback to downloads subdirectory
        downloads_path = base_path / "downloads"
        return str(downloads_path)
    
    def _ensure_directory_exists(self, directory: str):
        """Ensure a directory exists"""
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    def download_file(self, url: str, filename: str = None, progress_callback: Callable = None) -> Optional[str]:
        """
        Download a file from a URL
        
        Args:
            url: URL to download from
            filename: Optional filename to save as
            progress_callback: Optional callback function to report progress
            
        Returns:
            Path to downloaded file or None if failed
        """
        try:
            # Parse filename from URL if not provided
            if not filename:
                parsed_url = urlparse(url)
                filename = os.path.basename(parsed_url.path)
                if not filename:
                    filename = "downloaded_file"
            
            # Full path to save file
            file_path = os.path.join(self.download_dir, filename)
            
            # Stream download
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            # Get total file size if available
            total_size = int(response.headers.get('content-length', 0))
            downloaded_size = 0
            
            # Write file in chunks
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        
                        # Report progress if callback provided
                        if progress_callback and total_size > 0:
                            progress = (downloaded_size / total_size) * 100
                            progress_callback(progress)
            
            return file_path
            
        except Exception as e:
            print(f"Error downloading file: {e}")
            return None
    
    def download_model(self, url: str, model_name: str = None, model_type: str = "Checkpoint") -> Optional[str]:
        """
        Download an AI model from a URL
        
        Args:
            url: URL to download from
            model_name: Optional name for the model
            model_type: Type of model (Checkpoint, LoRA, VAE, etc.)
            
        Returns:
            Path to downloaded model or None if failed
        """
        try:
            # Determine appropriate filename
            if not model_name:
                parsed_url = urlparse(url)
                model_name = os.path.basename(parsed_url.path)
                if not model_name:
                    model_name = f"{model_type.lower()}_model"
            
            # Add appropriate extension if missing
            if not any(model_name.endswith(ext) for ext in ['.ckpt', '.safetensors', '.pt', '.bin']):
                model_name += ".safetensors"
            
            # Download the file
            file_path = self.download_file(url, model_name)
            
            if file_path:
                print(f"Model downloaded successfully to: {file_path}")
                return file_path
            else:
                print("Failed to download model")
                return None
                
        except Exception as e:
            print(f"Error downloading model: {e}")
            return None
    
    def get_download_dir(self) -> str:
        """Get the current download directory"""
        return self.download_dir
    
    def set_download_dir(self, directory: str):
        """Set a new download directory"""
        self._ensure_directory_exists(directory)
        self.download_dir = directory