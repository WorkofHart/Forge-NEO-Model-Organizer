# Forge NEO Model Organizer

A model organization and management extension for Stable Diffusion WebUI Forge NEO.

## Features

- **Model Organization**: Browse your AI models in a clean, intuitive interface with card or table views
- **Download Manager**: Download models directly from URLs with progress tracking
- **Model Categorization**: Automatically categorize models by type (Checkpoints, LoRA, VAE, etc.)
- **Preview Management**: Download and display model preview images
- **NSFW Filtering**: Optional blurring of NSFW content
- **Customizable Display**: Adjustable card sizes and layout options
- **Model Information**: View detailed information about each model

## Installation

### Automatic Installation (Recommended)

1. Open Forge NEO WebUI
2. Go to the "Extensions" tab
3. Click "Install from URL"
4. Enter this URL: `https://github.com/WorkofHart/Forge-NEO-Model-Organizer`
5. Click "Install"
6. Restart Forge NEO

### Manual Installation

1. Clone this repository to your Forge NEO extensions directory:
   ```bash
   cd /path/to/forge-neo/extensions
   git clone https://github.com/WorkofHart/Forge-NEO-Model-Organizer.git
   ```

2. Restart Forge NEO to load the extension

3. The "Model Organizer" tab will appear in the WebUI

## Usage

### Home Tab
- View all your models organized by type
- Switch between card view and table view
- See model details like file size and modification date
- Refresh to scan for new models

### Download Tab
- Enter a URL to download models directly
- Specify model name and type
- Track download progress
- Models are automatically saved to the appropriate directory

### Settings Tab
- Configure display options (card size, layout)
- Enable/disable preview downloads
- Toggle NSFW content filtering
- Set custom models directory

## Supported Model Types

- **Checkpoints**: Main Stable Diffusion models (.ckpt, .safetensors)
- **LoRA**: Low-Rank Adaptation models
- **VAE**: Variational Autoencoder models
- **Embeddings**: Textual inversion embeddings
- **ControlNet**: ControlNet models
- **Hypernetworks**: Hypernetwork models
- **LyCORIS**: LyCORIS models

## Requirements

- Forge NEO WebUI
- Python 3.7+
- Required Python packages (automatically installed):
  - requests
  - beautifulsoup4
  - pillow

## Configuration

The extension can be configured through Forge NEO's settings panel under "Forge NEO Model Organizer".

Options include:
- Layout type (Cards or Table)
- Card dimensions
- Preview download settings
- NSFW content filtering
- Custom models directory

## Development

To contribute to this extension:

1. Fork this repository
2. Create a feature branch
3. Commit your changes
4. Push to your fork
5. Create a pull request

### Project Structure

```
Forge-NEO-Model-Organizer/
├── install.py              # Dependency installation
├── preload.py              # Command line arguments
├── manifest.json           # Extension metadata
├── README.md               # This file
├── styles/                 # CSS styling
│   └── main.css
├── javascript/             # Frontend JavaScript
│   └── main.js
└── scripts/
    └── forge_neo_mo/       # Main extension code
        ├── environment.py   # Configuration and settings
        ├── utils.py         # Utility functions
        ├── ui/              # User interface components
        │   └── main_ui.py
        ├── data/            # Data management
        │   └── model_manager.py
        └── dl/              # Download management
            └── download_manager.py
```

## Troubleshooting

### Extension not appearing
- Ensure Forge NEO is restarted after installation
- Check that the extension is in the correct `extensions` directory
- Verify there are no error messages in the console

### Download issues
- Check that the URL is accessible
- Ensure there is sufficient disk space
- Verify network connectivity

### Models not showing
- Click "Refresh Models" to rescan the models directory
- Check that models are in the correct subdirectories
- Verify file permissions

## License

MIT License

## Acknowledgments

This extension was designed specifically for Forge NEO and takes inspiration from various model management tools in the Stable Diffusion community.