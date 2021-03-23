'''
扫描内网段
'''

from ipaddress import ip_address, ip_network
from asyncio import wait, get_event_loop
from icmplib import ping
from time import time

async def ping_ip(ip):
    start = time()
    print('start ping {}'.format(ip))
    r = ping(ip)
    end = time()
    print('end ping {} : {}s : {}'.format(ip, end - start, r.is_alive))

ips = [str(ip) for ip in ip_network('192.168.0.0/24')]

loop = get_event_loop()
tasks = [ping_ip(ip) for ip in ips]
loop.run_until_complete(wait(tasks))
loop.close()
