import subprocess as sp
ip = ("172.16.0.1", "172.16.8.3", "115.231.50.254", "115.231.50.249",
      "60.12.218.186", "60.12.218.129", "www.baidu.com", "172.16.8.2",
      "172.16.8.4", "172.16.8.5", "172.16.0.220", "172.16.0.221",
      "172.16.0.222", "172.16.0.192")
bad = 0
count = 0
badIp = []
for url in ip:
    status, result = sp.getstatusoutput("ping " + url + " -w 2000")
    count += 1
    if "请求超时" in result:
        bad += 1
        badIp.append(url)
print("总共ping了%d个ip,"%(count) + "其中%d个IP无法Ping通"%(bad))
if len(badIp) != 0:
    print("网络不通的ip如下:")
    print(badIp)