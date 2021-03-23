# [exert-nmap](https://github.com/chaosanals/exert-nmap)

## 命令

```bash
# 扫描
# -sV 得到版本信息
# -p80 指定80端口
# --script <script-name> [--script-args <arg_key>=<arg_val>,<arg_key>=<arg_val>,...] 使用脚本
nmap <target>
```

### vulners.nse

```bash
nmap -sV --script vulners [--script-args mincvss=<arg_val>] <target>
```
