import ast
import tokenize
from io import BytesIO
class CodeAnalyzer:
    def __init__(self, code: str):
        self.code = code
        self.ast_tree = ast.parse(code)
        self.tokens = list(tokenize.tokenize(BytesIO(code.encode()).readline))
        def print_ast_summary(self):
        print("AST Nodes:")
        for node in ast.walk(self.ast_tree):
            print(type(node).__name__)
        def print_tokens(self):
        print("Tokens:")
        for tok in self.tokens:
            print(tok)



