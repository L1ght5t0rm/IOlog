# IOlog

用于python的print和input的记录留存的脚本模块

    This is a script
    This is a script
    This is a script
















## 深入理解IOlog类的实现与内部使用逻辑

### IOlog类

#### 初始化

    在当前执行路径生成logs文件夹,文件名为当前时间.txt
    位置参数: -
    关键字参数:
        O_out=True: bool（记录日志后，仍实时打印）
        flush_size=100：int（在调用print或input达到此次数后，执行flush_cache）
        clear_old=Flase：bool（初始化对象时清除屏幕）

#### self.log_print

    打印字符串
    位置参数:
        string: 打印的字符串
    关键字参数:
        out：bool（记录后，仍打印到系统）
            无论是外出还是自我。O_out：print(输入的字符串，end=end)


#### self.log_input

    输入字符串
    位置参数:
        string: 打印的字符串


#### self.flush_cache

    将缓存保存到log文件
        位置参数: -
        关键字参数: -






















































Thank you for reading
