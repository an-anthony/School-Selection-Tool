import json
import datetime
import time
from urllib import parse
from urllib import request


subject = input("请输入专业名称(Enter)：")
subject = parse.quote(subject)

eolApi = "https://api.eol.cn/gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&f211=&f985=&is_dual_class=&keyword="+ subject + "&local_batch_id=&local_type_id=&page=1&province_id=&school_type=&signsafe=&size=20&type=&uri=apidata/api/gk/score/special&year=" + (str)(datetime.datetime.now().year - 1)
head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}

req = request.Request(eolApi, headers=head)
data = request.urlopen(req)
data = data.read().decode('UTF-8')

data = json.loads(data)

collegeNum = data["data"]["numFound"] # 专业数量
print("该专业共寻找到",collegeNum,"个招生院校。")

studentFrom = input("请输入生源地省份(请勿输入省字)(Enter)：")



pageHave = 20
if collegeNum % pageHave != 0:
    loadNeed = (int)(collegeNum / pageHave) + 1
else:
    loadNeed = (int)(collegeNum / pageHave)

loadCount = 0
n = 1

print("学院名称","院校类型","文理科","录取批次","专业名","分数线")

while loadCount <= loadNeed:
    loadCount = loadCount + 1
    data["code"]  = '233'
    n = 1
    while data["code"] != '0000':
        if n > 2:
            print("[debug]当前正在第", loadCount ,"页第 ",n ,"次循环")
        time.sleep(6 * n)
        eolApi = "https://api.eol.cn/gkcx/api/?access_token=&admissions=&central=&department=&dual_class=&f211=&f985=&is_dual_class=&keyword="+ subject + "&local_batch_id=&local_type_id=&page="+ (str)(loadCount) + "&province_id=&school_type=&signsafe=&size="+(str)(pageHave) + "&type=&uri=apidata/api/gk/score/special&year=" + (str)(datetime.datetime.now().year - 1)
        req = request.Request(eolApi, headers=head)
        data = request.urlopen(req)
        data = data.read().decode('UTF-8')
        data = json.loads(data)
        n = n + 1
   
    for college in data["data"]["item"]:
        if college["local_province_name"] == studentFrom:
            print(college["name"],college["level1_name"],college["local_type_name"],college["local_batch_name"],college["spname"],college["min"])
input("循环完成，请按回车键结束程序")