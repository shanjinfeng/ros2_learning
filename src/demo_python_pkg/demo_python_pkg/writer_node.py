from demo_python_pkg.person_node import PersonNode
import rclpy

class WriterNode(PersonNode):
    def __init__(self,name:str,age:int,book:str)-> None:
        super().__init__(name,age)
        self.get_logger().info("WriterNode::__init__")
        self.book = book

def main():
    rclpy.init()
    node = WriterNode('小红',25,'Python编程')
    node.eat("香蕉")
    rclpy.spin(node)
    rclpy.shutdown()
