import gradio as gr
import modules.scripts as scripts
from modules import script_callbacks, shared
from modules.shared import OptionInfo

from scripts.forge_neo_mo.environment import env
from scripts.forge_neo_mo.ui.main_ui import main_ui_block


def on_ui_tabs():
    """Add the Model Organizer tab to Forge NEO"""
    try:
        return [(main_ui_block(), "Model Organizer", "forge_neo_model_organizer")]
    except Exception as e:
        print(f"Error creating Model Organizer tab: {e}")
        return []


def on_ui_settings():
    """Add Model Organizer settings to Forge NEO settings"""
    section = ('forge_neo_model_organizer', "Forge NEO Model Organizer")
    
    opts = {
        "forge_neo_mo_layout": OptionInfo(
            env.layout(),
            "Layout Type:",
            gr.Radio,
            {"choices": ["Cards", "Table"]},
        ),
        "forge_neo_mo_card_width": OptionInfo(
            env.card_width(), 
            'Card width (250 default value):'
        ),
        "forge_neo_mo_card_height": OptionInfo(
            env.card_height(), 
            'Card height (350 default value):'
        ),
        "forge_neo_mo_download_preview": OptionInfo(
            env.download_preview(), 
            'Download Preview'
        ),
        "forge_neo_mo_resize_preview": OptionInfo(
            env.resize_preview(), 
            'Resize Preview'
        ),
        "forge_neo_mo_nsfw_blur": OptionInfo(
            env.nsfw_blur(), 
            'Blur NSFW Previews (models with "nsfw" tag)'
        ),
    }

    dir_opts = {
        "forge_neo_mo_models_dir": OptionInfo(
            env.models_dir(),
            "Models directory (If empty uses default Forge NEO models directory):"
        ),
    }

    # Add options to settings
    for key, opt in opts.items():
        opt.section = section
        shared.opts.add_option(key, opt)

    for key, opt in dir_opts.items():
        opt.section = section
        shared.opts.add_option(key, opt)


# Register callbacks
script_callbacks.on_ui_tabs(on_ui_tabs)
script_callbacks.on_ui_settings(on_ui_settings)