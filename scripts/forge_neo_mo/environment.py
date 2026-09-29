import hashlib
import logging
import os.path
from typing import Callable
from modules import shared
from modules.paths import models_path


# Constants
STORAGE_SQLITE = 'SQLite'
STORAGE_NONE = 'None'

LAYOUT_CARDS = 'Cards'
LAYOUT_TABLE = 'Table'

DEFAULT_CARD_WIDTH = 250
DEFAULT_CARD_HEIGHT = 350

# Logging configuration
class CustomFormatter(logging.Formatter):
    light_green = '\033[92m'
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "[%(levelname)s] %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: light_green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        _formatter = logging.Formatter(log_fmt)
        return _formatter.format(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
handler.setFormatter(CustomFormatter())

logger.addHandler(handler)


class Environment:
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    def storage_type(self):
        """Get storage type from settings"""
        if hasattr(shared.opts, 'forge_neo_mo_storage_type'):
            return shared.opts.forge_neo_mo_storage_type
        return STORAGE_NONE

    def download_preview(self):
        """Check if preview download is enabled"""
        if hasattr(shared.opts, 'forge_neo_mo_download_preview'):
            return shared.opts.forge_neo_mo_download_preview
        return True

    def resize_preview(self):
        """Check if preview resizing is enabled"""
        if hasattr(shared.opts, 'forge_neo_mo_resize_preview'):
            return shared.opts.forge_neo_mo_resize_preview
        return True

    def nsfw_blur(self):
        """Check if NSFW blur is enabled"""
        if hasattr(shared.opts, 'forge_neo_mo_nsfw_blur'):
            return shared.opts.forge_neo_mo_nsfw_blur
        return True

    def models_dir(self):
        """Get models directory from settings or default"""
        if hasattr(shared.opts, 'forge_neo_mo_models_dir') and shared.opts.forge_neo_mo_models_dir:
            return shared.opts.forge_neo_mo_models_dir
        # Default to Forge NEO models directory
        return models_path

    def layout(self):
        """Get layout preference"""
        if hasattr(shared.opts, 'forge_neo_mo_layout'):
            return shared.opts.forge_neo_mo_layout
        return LAYOUT_CARDS

    def card_width(self):
        """Get card width preference"""
        if hasattr(shared.opts, 'forge_neo_mo_card_width') and shared.opts.forge_neo_mo_card_width:
            return shared.opts.forge_neo_mo_card_width
        return DEFAULT_CARD_WIDTH

    def card_height(self):
        """Get card height preference"""
        if hasattr(shared.opts, 'forge_neo_mo_card_height') and shared.opts.forge_neo_mo_card_height:
            return shared.opts.forge_neo_mo_card_height
        return DEFAULT_CARD_HEIGHT

    def is_debug_mode_enabled(self):
        """Check if debug mode is enabled"""
        if hasattr(shared.cmd_opts, 'forge_neo_mo_debug'):
            return shared.cmd_opts.forge_neo_mo_debug
        return False

    def get_model_path(self, model_type="Checkpoint"):
        """Get path for specific model type"""
        base_path = self.models_dir()
        
        # Map model types to directories
        type_map = {
            "Checkpoint": "Stable-diffusion",
            "LoRA": "Lora",
            "VAE": "VAE",
            "Embedding": "embeddings",
            "ControlNet": "ControlNet",
            "Hypernetwork": "hypernetworks",
            "LyCORIS": "LyCORIS"
        }
        
        subdir = type_map.get(model_type, "")
        return os.path.join(base_path, subdir) if subdir else base_path

    def is_storage_initialized(self):
        """Check if storage is initialized"""
        return True  # For now, we're not using database storage

    def is_storage_has_errors(self):
        """Check if storage has errors"""
        return False  # For now, no storage errors


# Global environment instance
env = Environment()