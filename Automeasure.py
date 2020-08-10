import requests
import pprint
import datetime

def get_workspace_id():
    r = requests.get(url, auth=(API_TOKEN, "api_token"))
    data = r.json()
    Data = data[0]
    return Data['id']


def get_month_total():
    r = requests.get(report_url, auth=(API_TOKEN, "api_token"), params=params)
    data = r.json()
    #1ヶ月分の時間を(days(日数) と seconds（秒)で返す
    return datetime.timedelta(milliseconds=data["total_grand"])

def get_h_m_s(td):
    m, s = divmod(td.seconds, 60)
    h, m = divmod(m, 60)
    h += 24 * td.days
    return h, m, s

def get_month_total_project():
    project_name = []
    total_project_time = []
    r = requests.get(report_url, auth=(API_TOKEN, "api_token"), params=params)
    data = r.json()
    for i in range(len(data["data"])):
        project_name.append(data["data"][i]["title"]["project"])
        total_project_time.append(data["data"][i]["time"])
    return project_name, total_project_time

report_url = "https://toggl.com/reports/api/v2/summary"
url = "https://www.toggl.com/api/v8/workspaces"

#個人のAPIを設置
API_TOKEN = ""

params = {
    "user_agent": "",
    "workspace_id": get_workspace_id(),
    "since": "2020-07-01T00:00:00",
    "until": "2020-07-31T23:59:59"
}


total_month_seconds = get_month_total()
cov_datime = get_h_m_s(total_month_seconds)
print(cov_datime)
#プロジェクト別で集計を行う
project_name_list, prohect_time_list = get_month_total_project()



