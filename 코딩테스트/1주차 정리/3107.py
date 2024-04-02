import sys
input = sys.stdin.readline

ipv6 = input().rstrip()
ipList = list(map(str,ipv6.split(":")))
result = []
check = 0

if len(ipList) == 8:
    for ip in ipList:
        result.append(ip.zfill(4))
else:
    clean = len(ipList) - ipList.count('')
    for ip in ipList:
        if(ip != ''):
            result.append(ip.zfill(4))
        else:
            if(check == 0):
                for _ in range(8-clean):
                    result.append(ip.zfill(4))
                check = 1

print(":".join(result))