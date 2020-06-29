import json

array = []
arr_POST = []
arr_GET = []
arr_IP = []
arr_4xx = []
arr_5xx = []
long_inquiries = []


file = open('access.log', 'r')
lines = file.readlines()

number_of_requests = sum(1 for line in open('access.log', 'r'))

for i in lines:

    method = "POST"
    if method in i:
        if len(arr_POST) < 10:
            arr_POST.append(i)

    method = "GET"
    if method in i:
        if len(arr_GET) < 20:
            arr_GET.append(i)

    if len(arr_IP) < 10:
        adrr = i.partition('-')[0]
        if adrr not in arr_IP:
            arr_IP.append(adrr)

    if len(arr_4xx) < 10:
        if '404' in i and '200' not in i:
            i = i.split('"-"')[0]
            arr_4xx.append(i)

    if len(arr_5xx) < 10:
        if '500' in i:
            i = i.split('"-"')[0]
            arr_4xx.append(i)

    if '200' in i:
        item = i.split('200')[1]
        request_time = item.split('"')[0]
        if int(request_time) > int('500'):
            long_inquiries.append(i.partition('"Mozilla')[0])

data = {
    "number_of_requests": number_of_requests,
    "requests": {
        "top10_POST": arr_POST,
        "top20_GET": arr_GET
    },
    "ip_addr": arr_IP,
    "err_4xx": arr_4xx,
    "err_5xx": arr_5xx,
    "long_inquiries": long_inquiries
}

if not array:
    array = [data]
else:
    array.append(data)

log = {"log": array}

with open("access_log.json", "a") as file:
    access_log = json.dumps(log, indent=4)
    file.write(access_log)
