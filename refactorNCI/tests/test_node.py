import sys
sys.path.append("./refactornci/")
from main import Node

def test_add():
    node = Node(1)
    assert str(node) == "(1, None)"