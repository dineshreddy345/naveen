from django.http import HttpResponse
class executionofflow(object):
    def __init__(self,x):
        self.x=x
    def __call__(self,b):
        print('this line is printed before processing the request')
        response=self.x(b)
        print('this line is printed after post processing')
        return response
    def process_exception(self,request,v):
        return HttpResponse('<h1>currently we are facing somwe tchincakl problems pls try after sometime')
