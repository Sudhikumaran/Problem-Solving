"""inner class
inner class in python is a class defined inside another class.
"""
class OuterClass:
    class InnerClass:
        def inner_method(self):
            return "This is a method inside the InnerClass."

    def outer_method(self):
        inner_instance = self.InnerClass()
        return inner_instance.inner_method()
outer_instance = OuterClass()
print(outer_instance.outer_method())    
# Output: This is a method inside the InnerClass.
# Creating an instance of InnerClass directly
inner_instance = OuterClass.InnerClass()    
print(inner_instance.inner_method())
# Output: This is a method inside the InnerClass.   
# Accessing InnerClass from an instance of OuterClass
inner_instance_via_outer = outer_instance.InnerClass()
print(inner_instance_via_outer.inner_method())
# Output: This is a method inside the InnerClass.
# Note: Inner classes can be useful for logically grouping classes that are only used in one place,
# and they can also help to encapsulate functionality within the outer class.
# However, they are not commonly used in everyday Python programming.
# Inner classes do not have special access to the outer class's members.
# They behave like regular classes defined at the top level.
# Example of InnerClass accessing OuterClass attribute
class OuterWithAttribute:
    def __init__(self, value):
        self.value = value

    class InnerClass:
        def display_outer_value(self, outer_instance):
            return f"Outer class value is: {outer_instance.value}"
outer_with_attr = OuterWithAttribute(42)
inner_instance = outer_with_attr.InnerClass()
print(inner_instance.display_outer_value(outer_with_attr))
# Output: Outer class value is: 42
# Note: The inner class method 'display_outer_value' requires an instance of the outer class to access its attributes.
# This demonstrates that inner classes do not have implicit access to the outer class's instance variables.
# They need to be explicitly passed an instance of the outer class to access its members.
# Inner classes can also be used to create more complex data structures.
class Tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_rec(node.left, value)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_rec(node.right, value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)
tree = Tree()
tree.insert(5) 
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
tree.inorder_traversal(tree.root)
# Output: 2 3 4 5 6 7 8
