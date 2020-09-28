import random
import time

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class mymiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(2222)
        print(request.path)
        if request.path == '/two/hello':
            # if random.randrange(100) > 50:
            #     print('ok')
            # timeout = cache.get(ip)
            # if timeout:
            #     return HttpResponse('稍后再试')
            # cache.set(ip, ip, timeout=10)
            # count = cache.get(ip, [])

            '''
            两层判断，一个是cache超时时间
            一个是个数，每次写入超时时间开始重新计数
            '''
            count = cache.get(ip)
            count = [] if count is None else count
            print(count)
            while count and time.time() - count[-1] > 60:
                count.pop()
                # 列表顺序为最新的时间index为0，所以最后一个元素距离现在超过60秒时，删除最后一个元素，遍历判断，直到每个元素距离现在都小于60秒
            if count:
                # 删除超过60秒的元素后，count数量仍大于3，说明60秒内访问次数超过3
                if len(count) >= 3:
                    return HttpResponse('60秒内访问过多，稍后再试')
            # 不论上面判断，每次访问都会增加一个当前时间，即使已经返回 访问过多
            count.insert(0, time.time())
            # 覆写缓存，把当前最新的访问时间次数列表写入缓存
            # cache.set(ip, count, timeout=60)
            cache.set(ip, count)

    def process_exception(self, request, exception):
        print(type(exception))
        print(dir(exception))
        print(11111)
        print(exception.__class__.__name__)
        if exception.__class__.__name__ == 'ZeroDivisionError':
            res = redirect(reverse('two:hello'))
        return res

    def process_view(self, request,view_func, view_args, view_kwargs):
        if request.path == '/two/hello':
            print("process_view")
            # return HttpResponse("return process_view")

