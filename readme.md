# [exert-nmap](https://github.com/chaosanals/exert-nmap)

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
