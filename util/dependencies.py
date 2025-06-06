import os
import subprocess

def check_dependencies():
    """Check and install necessary dependencies for Chromium"""
    try:
        print("Checking dependencies...")
        
        chromium_installed = False
        chromium_path = None
        
        try:
            if os.name == 'nt':
                chromium_paths = [
                    os.path.join(os.environ.get('PROGRAMFILES', 'C:\\Program Files'), 'Chromium\\Application\\chromium.exe'),
                    os.path.join(os.environ.get('PROGRAMFILES(X86)', 'C:\\Program Files (x86)'), 'Chromium\\Application\\chromium.exe')
                ]
                for path in chromium_paths:
                    if os.path.exists(path):
                        chromium_installed = True
                        chromium_path = path
                        break
            else:
                for cmd in ['chromium', 'chromium-browser']:
                    try:
                        result = subprocess.run(['which', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        if result.returncode == 0:
                            chromium_installed = True
                            chromium_path = result.stdout.strip()
                            print("chromium_path", chromium_path)
                            break
                    except:
                        pass
            
            if chromium_installed:
                print(f"Chromium found: {chromium_path}")
            else:
                print("WARNING: Chromium not found. Please install Chromium:")
                print("- Linux: sudo apt install chromium-browser")
                print("- Ubuntu/Debian: sudo apt install chromium-browser")
                print("- Fedora: sudo dnf install chromium")
                print("- Arch: sudo pacman -S chromium")
                print("- macOS: brew install --cask chromium")
                print("- Windows: Download from https://www.chromium.org/getting-involved/download-chromium/")
        except Exception as e:
            print(f"Could not check if Chromium is installed: {e}")
        
        try:
            result = subprocess.run(['chromedriver', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                print(f"ChromeDriver found: {result.stdout.strip()}")
            else:
                raise FileNotFoundError("ChromeDriver not found")
        except (subprocess.SubprocessError, FileNotFoundError):
            print("ChromeDriver not found in PATH.")
            print("Please install ChromeDriver manually:")
            print("1. Check your Chromium version (chromium --version)")
            print("2. Download the corresponding ChromeDriver from: https://chromedriver.chromium.org/downloads")
            print("3. Add the executable to your PATH:")
            print("   - Linux/macOS: sudo mv chromedriver /usr/local/bin/ && sudo chmod +x /usr/local/bin/chromedriver")
            print("   - Windows: Add the chromedriver directory to your PATH environment variables")
    
    except Exception as e:
        print(f"Error checking dependencies: {e}") 