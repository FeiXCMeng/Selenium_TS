#-*-coding:utf-8-*- 

'''
供root log使用，子log可直接使用logging.getLogger('XXX')
日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别
'''
import logging
import logging.handlers

class MyLogger():
    '''
    目的：整合系统所有模块的日志处理，将使得一个系统的所有子模块使用同样的level、handler等设置。
    实现的原理为：1.logger实例的唯一性，即只要name相同，返回的logger实例都是同一个而且只有一个，name和logger实例是
                一一对应的。这意味着，无需把logger实例在各个模块中传递。只要知道name，就能得到同一个logger实例
                2.root logger就是处于最顶层的logger， 它是所有logger的祖先,也是单实例的;如果一个logger没有显示地设置level，那么它就
                用父亲的level。如果父亲也没有显示地设置level， 就用父亲的父亲的level，以此推....最后到达root logger。
                3.child loggers得到消息后，既把消息分发给它的handler处理，也会传递给所有祖先logger处理,如果孩子logger没有任何handler，对消息不做处理。
                但是它把消息转发给了它的父亲以及root logger
    使用方式：1）本类应该仅在程序入口（main）处调用
            2）系统子模块可以使用该类的getlogger方法也可以使用logging.getLogger('XXX')获取logger，logger的其他都不用设置
            日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
    '''

    def __init__(self, level=logging.DEBUG):
        self.handler_format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        self.date_format = '%a, %d %b %Y %H:%M:%S'
        self.level = logging.INFO
        self.root = logging.getLogger()
        self.root.setLevel(self.level)


    def getlogger(self, logname):
        '''
        直接调用logging.getLogger([name])，返回一个logger实例，如果没有指定name，返回root logger。
        只要name相同，返回的logger实例都是同一个而且只有一个，即name和logger实例是一一对应的。
        默认子logger没有设置handler，所以调试可以增加下面语句使其打印log
        import logging
        logging.basicConfig(level=logging.INFO) 
        '''
        logger = logging.getLogger(logname)
        #stream_handler = logging.StreamHandler()  
        #stream_handler.setLevel(self.level)
        #formatter = logging.Formatter(self.handler_format)
        #stream_handler.setFormatter(formatter)
        #if not logger.handlers:
            #logger.addHandler(stream_handler)
        return logger

    def log_to_stream(self):
        '''
        输出到屏幕,默认存在
        '''
        stream_handler = logging.StreamHandler()  
        stream_handler.setLevel(self.level)
        formatter = logging.Formatter(self.handler_format)
        stream_handler.setFormatter(formatter)
        self.root.addHandler(stream_handler)
        return self.root

    def log_to_onefile(self, filename): 
        '''
        输出到一个日志文件
        '''
        self.log_to_stream()
        file_handler = logging.FileHandler(filename) 
        file_handler.setLevel(self.level)
        formatter = logging.Formatter(self.handler_format)
        file_handler.setFormatter(formatter)
        self.root.addHandler(file_handler)
        return self.root
        
    def log_to_RotatingFile(self, filename,  maxbytes=10*1024*1024, backupcount=5):
        '''
        输出到一个大小回滚的日志文件，默认10M，最多保存5个
        '''
        self.log_to_stream()
        Rthandler = logging.handlers.RotatingFileHandler(filename,maxBytes=maxbytes, backupCount=backupcount)
        Rthandler.setLevel(self.level)
        formatter = logging.Formatter(self.handler_format)
        Rthandler.setFormatter(formatter)
        self.root.addHandler(Rthandler)
        return self.root

    def log_to_TimedRotatingFile(self, filename, when='D', interval=1, backupCount=5):
        '''
        输出到一个时间回滚的日志文件，默认1天，最多保存5个
        '''
        self.log_to_stream()
        Trthandler = logging.handlers.TimedRotatingFileHandler(filename, when=when, interval=interval, backupCount=backupCount)
        Trthandler.setLevel(self.level)
        formatter = logging.Formatter(self.handler_format)
        Trthandler.setFormatter(formatter)
        self.root.addHandler(Trthandler)
        return self.root
    #----------------------------------------------------------------------
    def set_print_level(self, print_level="INFO"):
        """CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET"""        
        if print_level.upper() == "NOTSET":
            self.level = logging.NOTSET
        elif print_level.upper() == "DEBUG":
            self.level = logging.DEBUG
        elif print_level.upper() == "INFO":
            self.level = logging.INFO
        elif print_level.upper() == "WARNING":
            self.level = logging.WARNING
        elif print_level.upper() == "ERROR":
            self.level = logging.ERROR
        elif print_level.upper() == "CRITICAL":
            self.level = logging.CRITICAL
        else:
            self.level = logging.INFO

mylogger =  MyLogger() 

if __name__ == "__main__":
    pass
