from lexer import Lexer
from parse import Parser
from intrepreter import Intrepreter
from data import Data

base = Data()

while True:
    text = input("Jo# Community Version 1: ")
    if text == "exit":
        break

    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    interpretor = Intrepreter(tree, base)
    result = interpretor.interpret()

    print(tree)