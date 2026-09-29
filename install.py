import launch

# Install required dependencies for Forge NEO Model Organizer
if not launch.is_installed("requests"):
    launch.run_pip("install requests", "requests requirement for Forge NEO Model Organizer")

if not launch.is_installed("beautifulsoup4"):
    launch.run_pip("install beautifulsoup4", "beautifulsoup4 requirement for Forge NEO Model Organizer")

if not launch.is_installed("pillow"):
    launch.run_pip("install pillow", "pillow requirement for Forge NEO Model Organizer")

# Optional: Uncomment if you want to use database features
# if not launch.is_installed("sqlite3"):
#     launch.run_pip("install sqlite3", "sqlite3 requirement for Forge NEO Model Organizer")