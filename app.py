from flask import Flask, request, render_template, redirect, url_for
import os
import ast
import tokenize
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Dummy explainability checker function (replace with your real logic)
def check_explainability(code):
    score = 100.0
    issues = []

    tree = ast.parse(code)
    funcs = [node for node in tree.body if isinstance(node, ast.FunctionDef)]

    for func in funcs:
        if ast.get_docstring(func) is None:
            score -= 33.3
            issues.append(f"Function '{func.name}' is missing a docstring at line {func.lineno}.")

    tokens = tokenize.tokenize(BytesIO(code.encode('utf-8')).readline)
    comments = [tok for tok in tokens if tok.type == tokenize.COMMENT]
    if len(comments) == 0:
        score -= 33.3
        issues.append("No comments found in the file.")

    if score < 100:
        issues.append("Consider adding docstrings, comments, and proper naming.")

    return round(max(score, 0), 2), issues

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.py'):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            with open(filepath, 'r') as f:
                code = f.read()
            score, issues = check_explainability(code)
            return render_template('result.html', score=score, issues=issues)
        else:
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

