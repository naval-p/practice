'''

性能测试
'''
import math

from locust import HttpUser, between, task, LoadTestShape

'''
1.为要模拟的用户模拟一个类，继承于httpuser
'''
class CarRental(HttpUser):
    '''
    between是user类中的一个方法
    wait—time是user定义的一个属性
    '''
    wait_time = between(3,8)
    @task
    def carManage(self):
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")
    @task
    def loadAllMenu(self):
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")
class DoubleWave(LoadTestShape):
    """
    A shape to immitate some specific user behaviour. In this example, midday
    and evening meal times.

    Settings:
        min_users -- minimum users
        peak_one_users -- users in first peak
        peak_two_users -- users in second peak
        time_limit -- total length of test
    """

    min_users = 20
    peak_one_users = 60
    peak_two_users = 40
    time_limit = 600

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_limit:
            user_count = (
                (self.peak_one_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
                + (self.peak_two_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
                + self.min_users
            )
            return (round(user_count), round(user_count))
        else:
            return None

