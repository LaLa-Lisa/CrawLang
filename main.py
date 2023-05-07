from antlr4 import *
from grammar.CrawLangLexer import CrawLangLexer
from grammar.CrawLangParser import CrawLangParser
from MyCrawLangVistor import MyCrawLangVisitor

def main():
    input_stream = FileStream("code_sample.txt")
    lexer = CrawLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CrawLangParser(stream)
    tree = parser.funclist()
    # evaluator
    visitor = MyCrawLangVisitor()
    output = visitor.visit(tree)
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    print("start")
    main()
    print("done")
