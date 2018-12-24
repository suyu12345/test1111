import allure


class TestLogin:
    def test_a(self):
        print("\n 111")
        assert 1
    @allure.step('测试登录的步骤')
    def test_b(self):
        print("\n 222")
        allure.attach('描述1账号',"请输入账号")
        print("\n 5555")
        allure.attach('描述2密码',"请输入密码")
        assert 1

