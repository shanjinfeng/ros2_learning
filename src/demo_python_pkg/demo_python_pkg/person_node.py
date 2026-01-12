import rclpy
from rclpy.node import Node

class PersonNode(Node):
    def __init__(self,name:str,age:int)-> None:
        super().__init__("node_name")
        self.name = name
        self.age = age  

    def eat(self,food_name:str):
       self.get_logger().info(f"我叫{self.name},我今年{self.age}岁,我正在吃{food_name}  ")

def main():
    rclpy.init()
    node = PersonNode("小明",18)
    node.eat("苹果")
    rclpy.spin(node)
    rclpy.shutdown()