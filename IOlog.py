
import os
import time

class IOlog():

    #初始化IO日志对象
    def __init__(self, O_out=True,flush_size=100,clear_old=False):
        """
        O_out: bool(after loged, still print out to system)
        flush_size: int(after calling print or input for this number of times, execute the flush_cache)
        clear_old: bool(clear screen when initializing a object)
        """
        load_time=str( time.strftime("%y%m%d_%H%M%S",time.localtime()) )
        #文件目录创建
        self.folder_name="logs"
        self.logs_filename=load_time
        os.makedirs(self.folder_name,exist_ok=True)
        with open(f"{self.folder_name}/{self.logs_filename}.txt","w",encoding="utf-8") as f:    pass

        self.flush_size=flush_size
        self.O_out=O_out
        self.cache=[]

        #清屏
        if clear_old:    os.system('cls' if os.name=='nt' else 'clear')


    #输出逻辑
    def log_print(self,string,out=False,end="\n",):
        """
        out: bool(after loged, still print out to system)
            if out or self.O_out:    print(string,end=end)
        """
        self.cache.append(string+end)
        if len(self.cache) >= self.flush_size:
            self.flush_cache()
        if out or self.O_out:    print(string,end=end)

    #输入逻辑
    def log_input(self,string):
        self.cache.append(string)
        if len(self.cache) >= self.flush_size:
            self.flush_cache()
        return input(string)

    #刷新缓存,写入文件逻辑
    def flush_cache(self):
        with open(f"{self.folder_name}/{self.logs_filename}.txt","w",encoding="utf-8") as f:
            f.write("".join(self.cache))
        self.cache.clear()


    #结束时刷新缓存
    def __del__(self):
        self.flush_cache()
        self.log_print("log is over, final cache has been saved")



if __name__=="__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system('cls' if os.name=='nt' else 'clear')
    print("Perhaps this module should not be run directly")



