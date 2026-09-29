// Forge NEO Model Organizer JavaScript

function initializeModelOrganizer() {
    console.log("Initializing Forge NEO Model Organizer");
    
    // Add any initialization code here
    setupThemeListener();
}

function setupThemeListener() {
    // Listen for theme changes and update UI accordingly
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === "attributes" && mutation.attributeName === "class") {
                updateThemeClasses();
            }
        });
    });
    
    const config = { attributes: true, childList: false, subtree: false };
    observer.observe(document.body, config);
}

function updateThemeClasses() {
    // Update any theme-specific classes
    const isDark = document.body.classList.contains('dark');
    
    // Apply theme to our components
    const moElements = document.querySelectorAll('[class*="mo-"]');
    moElements.forEach(el => {
        if (isDark) {
            el.classList.add('dark-theme');
        } else {
            el.classList.remove('dark-theme');
        }
    });
}

function handleModelDownload(url) {
    if (!url) {
        showMessage("Please enter a valid URL", "error");
        return;
    }
    
    showMessage("Starting download...", "info");
    
    // This would typically call a backend API
    // For now, we'll simulate the process
    setTimeout(() => {
        showMessage("Download completed successfully!", "success");
    }, 2000);
}

function showMessage(message, type) {
    const statusDiv = document.getElementById('download-status');
    if (statusDiv) {
        statusDiv.textContent = message;
        statusDiv.className = `mo-message mo-${type}`;
    }
}

// Initialize when the page loads
document.addEventListener('DOMContentLoaded', function() {
    initializeModelOrganizer();
});