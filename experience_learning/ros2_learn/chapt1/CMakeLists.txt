# 构建当前文件最低的cmake版本
cmake_minimum_required(VERSION 3.8)
#声明工程的名字
project(hello_world)
#添加一个可执行文件
add_executable(learn_cmake hello_world.cpp)