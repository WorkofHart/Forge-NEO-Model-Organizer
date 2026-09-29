import gradio as gr
import os
from scripts.forge_neo_mo.environment import env
from scripts.forge_neo_mo.data.model_manager import ModelManager
from scripts.forge_neo_mo.dl.download_manager import DownloadManager


def main_ui_block():
    """Main UI block for the Forge NEO Model Organizer"""
    with gr.Blocks() as main_block:
        gr.Markdown("# Forge NEO Model Organizer")
        gr.Markdown("Organize, manage, and download your AI models efficiently.")
        
        # Initialize managers
        model_manager = ModelManager()
        download_manager = DownloadManager()
        
        with gr.Tab("Home"):
            home_tab(model_manager)
            
        with gr.Tab("Download"):
            download_tab(download_manager)
            
        with gr.Tab("Settings"):
            settings_tab()
            
    return main_block


def home_tab(model_manager):
    """Home tab showing organized models"""
    gr.Markdown("## Your Models")
    
    # Layout selector
    with gr.Row():
        layout_choice = gr.Radio(
            choices=["Cards", "Table"],
            value="Cards",
            label="Display Layout"
        )
        refresh_btn = gr.Button("Refresh Models")
    
    # Model display area
    with gr.Column(visible=True) as card_layout:
        gr.Markdown("### Model Cards View")
        model_cards = gr.Gallery(
            label="Models",
            show_label=False,
            columns=4,
            height="auto"
        )
        
    with gr.Column(visible=False) as table_layout:
        gr.Markdown("### Model Table View")
        model_table = gr.Dataframe(
            headers=["Name", "Type", "Size", "Path"],
            datatype=["str", "str", "str", "str"],
            interactive=False
        )
    
    # Refresh button
    refresh_btn.click(
        fn=refresh_models,
        inputs=[],
        outputs=[model_cards, model_table]
    )
    
    # Layout change handler
    def change_layout(layout):
        return {
            card_layout: gr.update(visible=(layout == "Cards")),
            table_layout: gr.update(visible=(layout == "Table"))
        }
    
    layout_choice.change(
        fn=change_layout,
        inputs=[layout_choice],
        outputs=[card_layout, table_layout]
    )


def download_tab(download_manager):
    """Download tab for acquiring new models"""
    gr.Markdown("## Download Models")
    
    with gr.Row():
        with gr.Column():
            url_input = gr.Textbox(
                label="Model URL",
                placeholder="Enter URL to model file or repository..."
            )
            model_name = gr.Textbox(
                label="Model Name (Optional)",
                placeholder="Enter a name for the model..."
            )
            model_type = gr.Dropdown(
                choices=["Checkpoint", "LoRA", "VAE", "Embedding", "ControlNet"],
                value="Checkpoint",
                label="Model Type"
            )
            download_btn = gr.Button("Download")
            
        with gr.Column():
            gr.Markdown("### Download Status")
            status_output = gr.Textbox(label="Status", interactive=False, lines=5)
            
    download_btn.click(
        fn=download_model,
        inputs=[url_input, model_name, model_type],
        outputs=[status_output]
    )


def settings_tab():
    """Settings tab for configuration"""
    gr.Markdown("## Settings")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Display Settings")
            card_width = gr.Number(
                label="Card Width",
                value=250,
                precision=0
            )
            card_height = gr.Number(
                label="Card Height",
                value=350,
                precision=0
            )
            
        with gr.Column():
            gr.Markdown("### Download Settings")
            preview_toggle = gr.Checkbox(
                label="Download Previews",
                value=True
            )
            nsfw_toggle = gr.Checkbox(
                label="Blur NSFW Content",
                value=True
            )


def refresh_models():
    """Refresh the models display"""
    # This would contain logic to scan and update model listings
    model_manager = ModelManager()
    models = model_manager.scan_models()
    
    # Prepare data for gallery view
    gallery_data = []
    for model in models:
        gallery_data.append({
            "name": model["name"],
            "data": None,  # Would be image data in real implementation
            "caption": f"{model['name']} ({model['type']})"
        })
    
    # Prepare data for table view
    table_data = []
    for model in models:
        table_data.append([
            model["name"],
            model["type"],
            f"{model['size'] / (1024*1024):.2f} MB",
            model["path"]
        ])
    
    return gallery_data, table_data


def download_model(url, name, model_type):
    """Download a model from a URL"""
    # This would contain logic to download models
    if not url:
        return "Please enter a valid URL"
    
    try:
        download_manager = DownloadManager()
        result = download_manager.download_model(url, name, model_type)
        
        if result:
            return f"Model downloaded successfully!\nSaved to: {result}"
        else:
            return "Failed to download model. Please check the URL and try again."
            
    except Exception as e:
        return f"Error downloading model: {str(e)}"