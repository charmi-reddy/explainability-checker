from scorer import CodeAnalyzer
from heuristics import compute_explainability_score

def load_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()

if __name__ == "__main__":
    code = load_file("sample.py")
    analyzer = CodeAnalyzer(code)

    score, issues = compute_explainability_score(analyzer.ast_tree)
    print(f"Explainability Score: {score}/100")

    if issues:
        print("Issues found:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("No explainability issues found.")
