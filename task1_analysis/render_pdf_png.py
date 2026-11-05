import subprocess

html_url = "file:///C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/task1_analysis/infographic_gaming_impact.html"
png_out = "C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/task1_analysis/infographic_gaming_impact.png"
pdf_out = "C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/task1_analysis/infographic_gaming_impact.pdf"

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

cmd_pdf = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_out}",
    html_url
]

res = subprocess.run(cmd_pdf, capture_output=True, text=True)
print("PDF exit code:", res.returncode)
print("PDF stdout:", res.stdout)
print("PDF stderr:", res.stderr)

cmd_png = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=1260,1900",
    f"--screenshot={png_out}",
    html_url
]

res_png = subprocess.run(cmd_png, capture_output=True, text=True)
print("PNG exit code:", res_png.returncode)
print("PNG stdout:", res_png.stdout)
print("PNG stderr:", res_png.stderr)
