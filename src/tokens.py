class Token:
    def __init__(self, type : str, value) -> None:
        self.type  = type
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)

class Integer(Token):
    def __init__(self, value) -> None:
        super().__init__('INT', value)

class String(Token):
    def __init__(self, value) -> None:
        super().__init__('STR', value)
    
class Float(Token):
    def __init__(self, value) -> None:
        super().__init__('FLT', value)
       
class Boolean(Token):
    def __init__(self, value) -> None:
        super().__init__('BOOL', value)

class Operation(Token):
    def __init__(self, value) -> None:
        super().__init__('OP', value)

class Declaration(Token):
    def __init__(self, value) -> None:
        super().__init__("DECL", value)

class Variable(Token):
    def __init__(self, value) -> None:
        super().__init__("VAR(?)", value)