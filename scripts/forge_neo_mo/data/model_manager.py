import os
import json
from pathlib import Path
from typing import List, Dict, Optional


class ModelManager:
    """Manage AI models for Forge NEO"""
    
    def __init__(self, models_dir: str = None):
        self.models_dir = models_dir or self._get_default_models_dir()
        self.models_db = os.path.join(self.models_dir, "models.json")
        self.models = self._load_models()
    
    def _get_default_models_dir(self) -> str:
        """Get the default models directory"""
        # Try to find Forge NEO models directory
        base_path = Path(__file__).parent.parent.parent
        models_path = base_path / "models"
        
        if models_path.exists():
            return str(models_path)
        
        # Fallback to current directory
        return str(base_path / "models")
    
    def _load_models(self) -> List[Dict]:
        """Load models from the database file"""
        if os.path.exists(self.models_db):
            try:
                with open(self.models_db, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading models: {e}")
                return []
        return []
    
    def _save_models(self):
        """Save models to the database file"""
        try:
            with open(self.models_db, 'w') as f:
                json.dump(self.models, f, indent=2)
        except Exception as e:
            print(f"Error saving models: {e}")
    
    def scan_models(self) -> List[Dict]:
        """Scan the models directory and return a list of models"""
        models = []
        
        if not os.path.exists(self.models_dir):
            return models
        
        # Common model file extensions
        model_extensions = {'.ckpt', '.safetensors', '.pt', '.bin', '.onnx'}
        
        for root, dirs, files in os.walk(self.models_dir):
            for file in files:
                if any(file.endswith(ext) for ext in model_extensions):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.models_dir)
                    
                    model_info = {
                        "name": os.path.splitext(file)[0],
                        "path": rel_path,
                        "size": os.path.getsize(file_path),
                        "modified": os.path.getmtime(file_path),
                        "type": self._get_model_type(file)
                    }
                    
                    models.append(model_info)
        
        return models
    
    def _get_model_type(self, filename: str) -> str:
        """Determine model type from filename"""
        filename_lower = filename.lower()
        
        if 'lora' in filename_lower:
            return "LoRA"
        elif 'vae' in filename_lower:
            return "VAE"
        elif 'embedding' in filename_lower or 'embed' in filename_lower:
            return "Embedding"
        elif 'control' in filename_lower:
            return "ControlNet"
        else:
            return "Checkpoint"
    
    def add_model(self, name: str, path: str, model_type: str = "Unknown") -> bool:
        """Add a new model to the database"""
        model = {
            "id": len(self.models) + 1,
            "name": name,
            "path": path,
            "type": model_type,
            "tags": [],
            "description": "",
            "preview": ""
        }
        
        self.models.append(model)
        self._save_models()
        return True
    
    def get_models(self) -> List[Dict]:
        """Get all models"""
        return self.models
    
    def get_model_by_id(self, model_id: int) -> Optional[Dict]:
        """Get a model by its ID"""
        for model in self.models:
            if model.get("id") == model_id:
                return model
        return None
    
    def update_model(self, model_id: int, **kwargs) -> bool:
        """Update a model's information"""
        for i, model in enumerate(self.models):
            if model.get("id") == model_id:
                self.models[i].update(kwargs)
                self._save_models()
                return True
        return False
    
    def delete_model(self, model_id: int) -> bool:
        """Delete a model from the database"""
        for i, model in enumerate(self.models):
            if model.get("id") == model_id:
                del self.models[i]
                self._save_models()
                return True
        return False