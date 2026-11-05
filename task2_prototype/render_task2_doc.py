import os
import subprocess
import html
import shutil

base_dir = os.path.dirname(os.path.abspath(__file__))
md_path = os.path.join(base_dir, 'Task2_AI_Product_Prototype_Document.md')

# Humanize and clean wording in MD
with open(md_path, 'r', encoding='utf-8') as f:
    md_text = f.read()

md_text = md_text.replace(
    "YourDOST operates on a model where employees can book any expert",
    "YourDOST operates on a delivery structure where employees can book any expert"
)
md_text = md_text.replace(
    "- **Deterministic Crisis Gating vs. LLM Freedom:**",
    "- **Deterministic Crisis Gating vs. Unconstrained Generative Chat:**"
)
md_text = md_text.replace(
    "- **Rule-Based Hybrid Classifier vs. Pure Black-Box LLM:**",
    "- **Rule-Based Hybrid Classifier vs. Pure Black-Box Generative Algorithms:**"
)
md_text = md_text.replace(
    "Utilize structured clinical domain heuristics coupled with sentiment embeddings rather than an unconstrained generative chatbot.",
    "Utilize structured clinical domain heuristics coupled with sentiment classification rather than an unconstrained generative chatbot."
)
md_text = md_text.replace(
    "Guarantees predictable, auditable clinical outcomes and eliminates hallucinations.",
    "Guarantees predictable, auditable clinical outcomes and eliminates conversational hallucinations."
)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(md_text)

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
        html_body.append(f'<h1 style="color:#2F2663; font-size:24px; border-bottom:2px solid #e2e8f0; padding-bottom:8px; margin-top:20px;">{html.escape(l[2:])}</h1>')
    elif l.startswith('## '):
        html_body.append(f'<h2 style="color:#0f172a; font-size:18px; margin-top:16px; margin-bottom:8px;">{html.escape(l[3:])}</h2>')
    elif l.startswith('### '):
        html_body.append(f'<h3 style="color:#F47920; font-size:15px; margin-top:14px; margin-bottom:6px;">{html.escape(l[4:])}</h3>')
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
<title>Task 2: Product Strategy & Decisions Document</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
  @page {{
    margin: 15mm 20mm;
    size: A4;
  }}
  body {{
    font-family: 'Plus Jakarta Sans', Arial, sans-serif;
    color: #1e293b;
    padding: 10px 20px;
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
  th {{
    background-color: #f1f5f9;
    font-weight: 700;
  }}
</style>
</head>
<body>
{content_html}
</body>
</html>
"""

html_out = os.path.join(base_dir, 'Task2_Document.html')
pdf_out = os.path.join(base_dir, 'Task2_AI_Product_Prototype_Document.pdf')

with open(html_out, 'w', encoding='utf-8') as f:
    f.write(full_html)

chrome_candidates = [
    shutil.which('google-chrome'),
    shutil.which('chrome'),
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
]
chrome_bin = next((c for c in chrome_candidates if c and os.path.exists(c)), 'chrome')

cmd_pdf = [
    chrome_bin,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_out}",
    f"file:///{html_out}"
]
subprocess.run(cmd_pdf, capture_output=True)
print("Rendered Task 2 Document PDF at:", pdf_out)
