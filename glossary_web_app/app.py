from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'
app.config['DATA_FOLDER'] = 'data'
app.config['GLOSSARY_FILE'] = os.path.join(app.config['DATA_FOLDER'], 'glossary.json')
app.config['BACKUP_FOLDER'] = os.path.join(app.config['DATA_FOLDER'], 'backups')

# Ensure data directories exist
os.makedirs(app.config['DATA_FOLDER'], exist_ok=True)
os.makedirs(app.config['BACKUP_FOLDER'], exist_ok=True)

def load_glossary():
    """Load glossary from JSON file with error handling"""
    try:
        if not os.path.exists(app.config['GLOSSARY_FILE']):
            with open(app.config['GLOSSARY_FILE'], 'w', encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=False, indent=4)
            return {}
        
        with open(app.config['GLOSSARY_FILE'], 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        flash(f"Error loading glossary: {str(e)}", 'error')
        return {}

def save_glossary(data):
    """Save glossary to JSON file with backup"""
    try:
        # Create backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(app.config['BACKUP_FOLDER'], f"glossary_backup_{timestamp}.json")
        
        if os.path.exists(app.config['GLOSSARY_FILE']):
            with open(app.config['GLOSSARY_FILE'], 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
            with open(backup_file, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, ensure_ascii=False, indent=4)
        
        # Save new data
        with open(app.config['GLOSSARY_FILE'], 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
    except (json.JSONDecodeError, IOError) as e:
        flash(f"Error saving glossary: {str(e)}", 'error')
        raise

@app.route('/')
def index():
    glossary = load_glossary()
    return render_template('index.html', glossary=glossary)

@app.route('/add', methods=['GET', 'POST'])
def add_term():
    if request.method == 'POST':
        glossary = load_glossary()
        english_term = request.form['english_term'].strip().lower()
        
        if not english_term:
            flash("Terim boş olamaz", 'error')
            return redirect(url_for('add_term'))
            
        glossary[english_term] = {
            'english_definition': request.form['english_definition'].strip(),
            'turkish_definition': request.form['turkish_definition'].strip(),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        try:
            save_glossary(glossary)
            flash(f"'{english_term}' başarıyla eklendi", 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Kayıt hatası: {str(e)}", 'error')
            return redirect(url_for('add_term'))
            
    return render_template('add_term.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        glossary = load_glossary()
        term = request.form.get('term', '').strip().lower()
        result = glossary.get(term)
        return render_template('search.html', result=result, term=term)
    return render_template('search.html')

@app.route('/edit/<term>', methods=['GET', 'POST'])
def edit_term(term):
    glossary = load_glossary()
    
    if term not in glossary:
        flash(f"'{term}' bulunamadı", 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        glossary[term] = {
            'english_definition': request.form['english_definition'].strip(),
            'turkish_definition': request.form['turkish_definition'].strip(),
            'created_at': glossary[term].get('created_at', datetime.now().isoformat()),
            'updated_at': datetime.now().isoformat()
        }
        
        try:
            save_glossary(glossary)
            flash(f"'{term}' başarıyla güncellendi", 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Güncelleme hatası: {str(e)}", 'error')
    
    return render_template('edit_term.html', term=term, definitions=glossary[term])

@app.route('/delete/<term>', methods=['GET', 'POST'])
def delete_term(term):
    glossary = load_glossary()
    
    if term not in glossary:
        flash(f"'{term}' bulunamadı", 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        del glossary[term]
        try:
            save_glossary(glossary)
            flash(f"'{term}' başarıyla silindi", 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Silme hatası: {str(e)}", 'error')
    
    return render_template('delete_confirm.html', term=term)

@app.route('/export')
def export():
    glossary = load_glossary()
    if request.args.get('download'):
        response = make_response(render_template(
            'export_plain.html', 
            glossary=sorted(glossary.items()),
            now=datetime.now()
        ))
        response.headers['Content-Disposition'] = 'attachment; filename=glossary_export.html'
        return response
    return render_template('export.html', glossary=sorted(glossary.items()))

@app.route('/backup')
def backup():
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(app.config['BACKUP_FOLDER'], f"manual_backup_{timestamp}.json")
        
        glossary = load_glossary()
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(glossary, f, ensure_ascii=False, indent=4)
            
        flash(f"Yedek başarıyla oluşturuldu: {backup_file}", 'success')
    except Exception as e:
        flash(f"Yedekleme hatası: {str(e)}", 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)