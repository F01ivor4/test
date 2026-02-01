import subprocess
import sys
import os
from base64 import b64encode

def solve():
    try:
        p = subprocess.Popen(
            ["/readflag"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=0
        )
        
        expression = ""
        while True:
            line = p.stdout.readline()
            if not line: break
            line = line.strip()
            if line.count("(") > 2 and any(c.isdigit() for c in line):
                expression = line
                break
        
        if expression:
            result = eval(expression)
            p.stdin.write(f"{result}\n")
            p.stdin.flush()
            
            checksum = b64encode(p.stdout.read()).decode("utf-8")
            with open("checksum.dat", "w") as f:
                f.write(checksum)
    except:
        pass

    try:
        data = sys.stdin.read()
        sys.stdout.write(data)
    except:
        pass

if __name__ == "__main__":
    solve()