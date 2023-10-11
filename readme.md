# [exert-nmap](https://github.com/chaosanals/exert-nmap)

## Zenmap（GUI 界面）

### 常用命令

```bash
# 嗅探内网
# -A 深入服务枚举
nmap -T4 -A -v 192.168.0.1-254

# 扫描服务信息
# -sV 显示服务版本
# -O 显示系统信息
nmap -sV -p 8080  -O 192.168.0.123

# PING 网段
# -sP 旧命令，新版是 -sn 
nmap -sn 192.168.0.0/24
```

### 输出文件

```bash
# -oN <path>  输出文本格式
# -oX <path>  输出 XML 格式

```

## 细微操作指令

```bash
# TCP 全连接扫描，仅验证 TCP 是否可以链接
nmap -sT -p 8080 192.168.0.123

# TCP 半连接扫描，仅验证 对方是否返回 ACK
nmap -sS -p 8080 192.168.0.123
```

## 命令

```bash
# 扫描
# -sV 得到版本信息
# -p80 指定80端口
# --script <script-name> [--script-args <arg_key>=<arg_val>,<arg_key>=<arg_val>,...] 使用脚本
nmap <target>

# -sS 隐秘 TCP 扫描
# -Pn 不以 ping 命令预先判断
# -A 深入服务枚举
# -oX <path/to/output.xml> 输入 XML 文件
nmap -sS -Pn -A <target>
```

### vulners.nse

```bash
nmap -sV --script vulners [--script-args mincvss=<arg_val>] <target>
```
