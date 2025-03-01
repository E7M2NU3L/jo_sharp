from tokens import Integer, Float

class Intrepreter:
    def __init__(self, tree, base) -> None:
        self.tree = tree
        self.base = base

    def read_INT(self, value):
        return int(value)
    
    def read_FLT(self, value):
        return float(value)

    def compute_binary(self, left, op, right):
        left_type = str(left.type)
        right_type = str(right.type)

        if op.value == ":":
            left.type = f"VAR({right_type})"
            self.base.write(left, right)
            self.base.read_all()

        left = getattr(self, "read_{0}".format(left_type))(left.value)
        right = getattr(self, "read_{0}".format(right_type))(right.value)

        if op.value == "+":
            output = left + right
        elif op.value == "-":
            output = left - right
        elif op.value == "*":
            output = left * right
        elif op.value == "/":
            output = left / right

        return Integer(output) if (left_type == "INT" and right_type == "INT") else Float(output)
        
    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree

        left_node = tree[0]
        if isinstance(left_node, list):
            left_node = self.interpret(left_node)

        right_node = tree[2]
        if isinstance(right_node, list):
            right_node = self.interpret(right_node)

        operator = tree[1]

        root_node = self.compute_binary(left_node, operator, right_node)
        return root_node