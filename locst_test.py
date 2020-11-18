'''
任务集合；分层的方式，按模块或者子系统来管理
'''
from locust import TaskSet, HttpUser, between
from locust.user import task


class System(TaskSet):
    @task
    def task1(self):

        self.client.get("http://127.0.0.1:8080/carRental/user/loadAllUser.action?page=1&limit=10")

    @task
    def task2(self):
        self.client.get("http://127.0.0.1:8080/carRental/sys/toMenuLeft.action")

    @task
    def task3(self):
        self.client.get("http://127.0.0.1:8080/carRental/sys/toUserManager.action")

#基础管理模块
class BasicMnaage(TaskSet):
    @task
    def task1(self):
        self.client.get("http://127.0.0.1:8080/carRental/stat/toCustomerAreaSexStat.action")

    @task
    def task2(self):
        self.client.get("http://127.0.0.1:8080/carRental/stat/toCustomerAreaStat.action")

class CarRentalTest(HttpUser):
    wait_time = between(1,3)
    tasks = {BasicMnaage:4,System:1}

    # 测试前置
    def on_start(self):
        user = {"loginname":"admin","pwd":"123456"}
        self.client.post("http://127.0.0.1:8080/carRental/login/login.action",data=user)

    #测试后置
    def on_stop(self):
        self.client.post("http://127.0.0.1:8080/carRental/login/logoutlocust.action")