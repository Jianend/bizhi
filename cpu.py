from multiprocessing import cpu_count
from multiprocessing import Process

def func():  # 死循环函数,让cpu满载
    while True:
         pass

if __name__ == '__main__':
    p_lst = []  # 定义一个列表
    core_count = cpu_count()  # CPU核心数
    for i in range(core_count):
        p = Process(target=func)  # 子进程调用函数
        p.start()  # 启动子进程
        p_lst.append(p)  # 将所有进程写入列表中
    for p in p_lst: p.join()  # 检测p是否结束,如果没有结束就阻塞直到结束,否则不阻塞
    print('结束')