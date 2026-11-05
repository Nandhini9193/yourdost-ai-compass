import subprocess
import html

md_path = 'C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/task2_prototype/Task2_AI_Product_Prototype_Document.md'
with open(md_path, 'r', encoding='utf-8') as f:
    md_text = f.read()

html_body = []
in_code = False

for line in md_text.split('\n'):
    l = line.strip()
    if l.startswith('```'):
        in_code = not in_code
        if in_code:
            html_body.append('<pre style="background:#f1f5f9; padding:12px; border-radius:8px; font-size:11px; overflow-x:auto; font-family:monospace; line-height:1.4; border:1px solid #cbd5e1;">')
        else:
            html_body.append('</pre>')
        continue
    if in_code:
        html_body.append(html.escape(line))
        continue
    if l.startswith('# '):
        html_body.append(f'<h1 style="color:#1e3a8a; font-size:24px; border-bottom:2px solid #e2e8f0; padding-bottom:8px; margin-top:20px;">{html.escape(l[2:])}</h1>')
    elif l.startswith('## '):
        html_body.append(f'<h2 style="color:#0f172a; font-size:18px; margin-top:16px; margin-bottom:8px;">{html.escape(l[3:])}</h2>')
    elif l.startswith('### '):
        html_body.append(f'<h3 style="color:#1e40af; font-size:15px; margin-top:14px; margin-bottom:6px;">{html.escape(l[4:])}</h3>')
    elif l.startswith('#### '):
        html_body.append(f'<h4 style="color:#334155; font-size:13px; margin-top:12px; margin-bottom:4px;">{html.escape(l[5:])}</h4>')
    elif l.startswith('|') and l.endswith('|'):
        if '---' in l:
            continue
        cells = [c.strip() for c in l[1:-1].split('|')]
        row = ''.join([f'<td style="border:1px solid #cbd5e1; padding:6px 10px; font-size:11.5px;">{html.escape(c)}</td>' for c in cells])
        html_body.append(f'<table style="border-collapse:collapse; width:100%; margin:8px 0;"><tr>{row}</tr></table>')
    elif l.startswith('- '):
        html_body.append(f'<li style="margin-left:20px; font-size:12px; line-height:1.5; color:#334155; margin-bottom:4px;">{html.escape(l[2:])}</li>')
    elif l.startswith('1. ') or l.startswith('2. ') or l.startswith('3. ') or l.startswith('4. ') or l.startswith('5. '):
        html_body.append(f'<li style="margin-left:20px; font-size:12px; line-height:1.5; color:#334155; margin-bottom:4px;"><strong>{html.escape(l[:3])}</strong>{html.escape(l[3:])}</li>')
    elif l == '---':
        html_body.append('<hr style="border:none; border-top:1px solid #e2e8f0; margin:16px 0;">')
    elif l:
        html_body.append(f'<p style="font-size:12px; line-height:1.5; color:#334155; margin-bottom:8px;">{html.escape(l)}</p>')

content_html = '\n'.join(html_body)

full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Task 2: AI Product Strategy & Decisions</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
  body {{
    font-family: 'Plus Jakarta Sans', Arial, sans-serif;
    color: #1e293b;
    padding: 30px 40px;
    line-height: 1.5;
  }}
  table {{
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 12px;
  }}
  td, th {{
    border: 1px solid #cbd5e1;
    padding: 6px 10px;
    font-size: 11px;
  }}
</style>
</head>
<body>
{content_html}
</body>
</html>
"""

html_out = 'C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/task2_prototype/Task2_Document.html'
pdf_out = 'C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/task2_prototype/Task2_AI_Product_Prototype_Document.pdf'

with open(html_out, 'w', encoding='utf-8') as f:
    f.write(full_html)

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
cmd_pdf = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    f"--print-to-pdf={pdf_out}",
    f"file:///{html_out}"
]
subprocess.run(cmd_pdf, capture_output=True)
print("Rendered Task 2 Document PDF at:", pdf_out)
