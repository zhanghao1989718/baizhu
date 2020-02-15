# coding:utf-8
import time, os, pymysql, datetime, base64, requests, json
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from sys import version_info

class GetReturnNum(object):

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_desktop():
        get_desktop = os.path.join(os.path.expanduser('~'), "Desktop")
        return get_desktop

    def make_dir(self):
        try:
            os.makedirs(os.path.join(self.get_desktop()) + '\\screen')
        except:
            pass

    def base64_api(self, uname, pwd, img):
        img = img.convert('RGB')
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        if version_info.major >= 3:
            b64 = str(base64.b64encode(buffered.getvalue()), encoding='utf-8')
        else:
            b64 = str(base64.b64encode(buffered.getvalue()))
        data = {"username": uname, "password": pwd, "image": b64}
        result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]

    def get_verification_code_shitu(self, left, top, right, bottom):
        screenshot = self.driver.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        captcha = screenshot.crop((left, top, right, bottom))
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        img_path = self.get_desktop() + "\\" + "screen" + "\\" + rq + ".png"
        captcha.save(img_path)
        img = Image.open(img_path)
        result = self.base64_api(uname='zhanghao1989718', pwd='1989718', img=img)
        print(result)
        return result

    def write_data(self, write_list, sql):
        # 创建一个person表
        db = pymysql.Connect(
            host='testbaizhu.mysql.rds.aliyuncs.com', port=3307,
            user='root', passwd='Baizhu7958', database='intelsys_test')
        # 创建一个游标
        cursor = db.cursor()
        # 创建表
        # sql = '''
        # CREATE TABLE `test_get_data` (
        #   `id` int(15) NOT NULL AUTO_INCREMENT,
        #   `date` date NOT NULL,
        #   `sid` char(20) NOT NULL,
        #   `soft_name` char(20) NOT NULL,
        #   `num` int(11) NULL,
        #   `return_point` double(14,3) NULL,
        #   `price` double(14,3) NULL,
        #   PRIMARY KEY (`id`),
        #   UNIQUE KEY `id` (`id`),
        #   UNIQUE INDEX (`date`,`sid`,`soft_name`)
        # )
        # '''
        try:
            # 执行sql
            cursor.executemany(sql, write_list)
            db.commit()
            print("插入数据成功")
        except Exception as e:
            print(e)
            # 数据回滚
            db.rollback()
            print("插入数据失败")
        finally:
            # 关闭游标连接
            cursor.close()
            # 关闭数据库连接
            db.close()

    def get_sjmnds(self):

        url = "http://mgamehl.monidashi.cn/user/login?destUrl=/index/index"
        username = "15215551632"
        passwd = "A123456"

        self.driver.get(url)
        self.get_verification_code_shitu(932, 387, 1121, 466)
        time.sleep(3)
        self.driver.find_element_by_id("id_tel").send_keys(username)
        self.driver.find_element_by_id("id_passwd").send_keys(passwd)

        # 验证码循环验证
        while True:
            try:
                self.driver.find_element_by_id("validate_code").send_keys(
                    self.get_verification_code_shitu(932, 387, 1121, 466))
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="formLogin"]/a/div').click()
                time.sleep(2)
                try:
                    self.driver.find_element_by_id("validate_code").clear()
                    self.driver.find_element_by_xpath('//*[@id="img_validate_code"]').click()
                    time.sleep(2)
                except:
                    break
            except:
                print("页面跳转错误")
                break

        # 获取页面信息
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "cont_statement")))
        soup = BeautifulSoup(self.driver.page_source, "lxml")
        table = soup.table
        tr_all = table.find_all("tr")
        result = []
        for tr in tr_all:
            # //查询所有td
            tds = tr.find_all('td')
            for td in tds:
                td_str = str(td)
                value = td_str.split(">")[1].split("<")[0]
                result.append(value)

        # 将信息转换格式
        result_num = len(result)
        list_all = []
        for x in range(result_num // 6):
            list_single = []
            for i in [0 + 6 * x, 1 + 6 * x, 2 + 6 * x, 3 + 6 * x, 4 + 6 * x, 5 + 6 * x]:
                list_single.append(result[i])
                i += 1
            tuple_single = tuple(list_single)
            list_all.append(tuple_single)

        sql = "replace into test_get_data (date,sid,soft_name,num,return_point,price) values (%s, %s, %s, %s, %s, %s)"
        # 写入数据
        self.write_data(list_all, sql)

    def get_iqy(self):

        url = "http://p.ppstream.com"
        username = "baizhu_stat"
        passwd = "baizhu12345678"

        self.driver.get(url)
        time.sleep(2)
        self.get_verification_code_shitu(980, 400, 1160, 450)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="loginWrap"]/input[1]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="loginWrap"]/input[2]').send_keys(passwd)

        # 验证码循环验证
        while True:
            try:
                self.driver.find_element_by_xpath('//*[@id="loginWrap"]/div[1]/div[1]/input').send_keys(
                    self.get_verification_code_shitu(980, 400, 1160, 450))
                time.sleep(2)
                self.driver.find_element_by_xpath('//*[@id="loginWrap"]/div[2]/div[2]/a').click()
                time.sleep(2)
                while True:
                    try:
                        self.driver.find_element_by_xpath('//*[@id="loginWrap"]/div[2]/div[1]/input').clear()
                        self.driver.find_element_by_xpath('//*[@id="loginWrap"]/div[2]/div[3]/img').click()
                        time.sleep(2)
                        self.driver.find_element_by_xpath('//*[@id="loginWrap"]/div[2]/div[1]/input').send_keys(
                            self.get_verification_code_shitu(980, 430, 1160, 480))
                        self.driver.find_element_by_xpath('//*[@id="loginWrap"]/div[3]/div[2]/a').click()
                        time.sleep(2)
                    except:
                        break
            except:
                break

        # 查询前一周的数据
        now_time = datetime.date.today()
        fromDate = now_time - datetime.timedelta(days=15)
        toDate = now_time - datetime.timedelta(days=8)
        from_date = str(fromDate)
        to_date = str(toDate)
        js_fromdate = "$('input[id=txt_from_date]').attr('readonly',false)"
        js_todate = "$('input[id=txt_to_date]').attr('readonly',false)"
        self.driver.execute_script(js_fromdate)
        time.sleep(1)
        for i in range(11):
            self.driver.find_element_by_id('txt_from_date').send_keys(Keys.BACK_SPACE)
            i += 1
        self.driver.find_element_by_id('txt_from_date').send_keys(from_date)
        self.driver.execute_script(js_todate)
        time.sleep(1)
        for i in range(11):
            self.driver.find_element_by_id('txt_to_date').send_keys(Keys.BACK_SPACE)
            i += 1
        self.driver.find_element_by_id('txt_to_date').send_keys(to_date)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div/button').click()
        time.sleep(3)

        # 获取页面信息
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "navbar-brand")))
        soup = BeautifulSoup(self.driver.page_source, "lxml")
        tbody = soup.find_all("tbody")
        tbody_need = tbody[1]
        tr_all = tbody_need.find_all("tr")
        result = []
        for tr in tr_all:
            # //查询所有td
            tds = tr.find_all('td')
            for td in tds:
                td_str = str(td)
                value = td_str.split(">")[1].split("<")[0]
                result.append(value)

        # 将信息转换格式
        result_num = len(result)
        list_all = []
        for x in range(result_num // 3):
            list_single = []
            for i in [0 + 3 * x, 1 + 3 * x, 2 + 3 * x]:
                if i < 2 + 3 * x:
                    list_single.append(result[i])
                else:
                    list_single.append("爱奇艺-阿拉丁")
                    list_single.append(result[i])
                i += 1
            tuple_single = tuple(list_single)
            list_all.append(tuple_single)
        sql = "replace into test_get_data (date,sid,soft_name,num) values (%s, %s, %s, %s)"
        # 写入数据
        self.write_data(list_all, sql)

    def main(self):
        self.make_dir()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.get_sjmnds()
        print("手机模拟大师数据拉取成功")
        time.sleep(2)
        self.get_iqy()
        print("爱奇艺-阿拉丁数据拉取成功")
        self.driver.quit()


if __name__ == "__main__":
    grn = GetReturnNum(webdriver.Chrome())
    grn.main()

