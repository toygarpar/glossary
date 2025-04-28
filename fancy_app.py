import json
import math
import os
from jinja2 import Environment, FileSystemLoader

# Base directory setup
base_dir = os.path.dirname(os.path.abspath(__file__))
ITEMS_PER_PAGE = 100

# Load glossary data
glossary_path = os.path.join(base_dir, './data/glossary.json')
try:
    with open(glossary_path, 'r', encoding='utf-8') as f:
        glossary = json.load(f)
except FileNotFoundError:
    raise FileNotFoundError("❌ Glossary file not found. Please check the path: ../data/glossary.json")

# Sort terms alphabetically
sorted_terms = sorted(glossary.items(), key=lambda x: x[0].lower())
total_pages = math.ceil(len(sorted_terms) / ITEMS_PER_PAGE)

# Set up Jinja2 environment
template_dir = os.path.join(base_dir, './glossary_web_app/fancy')
if not os.path.exists(template_dir):
    raise FileNotFoundError("❌ Template directory 'fancy' not found.")

env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('index.html')

# Ensure static folder exists
static_dir = os.path.join(base_dir, 'glossary_web_app', 'static')
os.makedirs(static_dir, exist_ok=True)

# Create CSS file if it doesn't exist
css_path = os.path.join(static_dir, 'fancystyle.css')
if not os.path.exists(css_path):
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write('''/* Modern Glossary Design */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f9f9f9;
    color: #333;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.header {
    text-align: center;
    margin-bottom: 40px;
}

.header h1 {
    font-size: 2.5rem;
    margin-bottom: 20px;
    color: #2c3e50;
}

.search-bar {
    width: 100%;
    padding: 10px;
    font-size: 1rem;
    border: 2px solid #ddd;
    border-radius: 5px;
    outline: none;
    transition: border-color 0.3s ease;
}

.search-bar:focus {
    border-color: #2c3e50;
}

.glossary {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.glossary-item {
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.glossary-item:hover {
    transform: translateY(-5px);
}

.glossary-item h2 {
    font-size: 1.5rem;
    margin-bottom: 10px;
    color: #2c3e50;
}

.glossary-item p {
    font-size: 1rem;
    margin-bottom: 5px;
}

.glossary-item p strong {
    color: #34495e;
}

.pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin-top: 40px;
}

.pagination-link {
    display: inline-block;
    padding: 10px 15px;
    background: #2c3e50;
    color: #fff;
    text-decoration: none;
    border-radius: 5px;
    transition: background 0.3s ease;
}

.pagination-link:hover {
    background: #34495e;
}

.pagination-current {
    display: inline-block;
    padding: 10px 15px;
    background: #ecf0f1;
    color: #2c3e50;
    border: 1px solid #2c3e50;
    border-radius: 5px;
    font-weight: bold;
}
''')







# Generate HTML pages
for page in range(1, total_pages + 1):
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    terms_on_page = sorted_terms[start:end]

    output_filename = 'index.html' if page == 1 else f'page{page}.html'
    output_path = os.path.join(base_dir, output_filename)

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            html_content = template.render(
                terms=terms_on_page,
                page=page,
                total_pages=total_pages
            )
            f.write(html_content)
    except Exception as e:
        print(f"❌ Error generating {output_filename}: {e}")

print("✅ Site generation complete!")



