import time

def timer(func):
    def wrapper(*args,**kwargs):
        t_start = time.time()
        result = func(*args,**kwargs)
        t_total = time.time() - t_start
        print('{} took {}s'.format(func.__name__,t_total))
        return result
    return wrapper


@timer 
def sleep_n_seconds(n):
    time.sleep(n)
    
sleep_n_seconds(5)