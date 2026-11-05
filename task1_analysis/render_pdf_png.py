import os
import subprocess

base_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(base_dir, "infographic_gaming_impact.html")
png_out = os.path.join(base_dir, "infographic_gaming_impact.png")
pdf_out = os.path.join(base_dir, "infographic_gaming_impact.pdf")

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

subprocess.run([
    chrome_path, "--headless", "--disable-gpu", "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_out}", f"file:///{html_path}"
], capture_output=True)

subprocess.run([
    chrome_path, "--headless", "--disable-gpu", "--window-size=1260,1900",
    f"--screenshot={png_out}", f"file:///{html_path}"
], capture_output=True)

print("Rendered PNG and PDF.")
