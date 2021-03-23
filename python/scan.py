import nmap3
nmap = nmap3.Nmap()
result = nmap.scan_top_ports("baidu.com")
for k, v in result.items():
    print(k)
    for i in v:
        print(v)