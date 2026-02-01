import subprocess
import sys

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
        
        if not expression:
            print("Error: Could not find equation line.")
            return


        result = eval(expression)
        
        p.stdin.write(f"{result}\n")
        p.stdin.flush()
        
        flag_output = p.stdout.read()
        if "ali" not in flag_output:
            print("Error: sandbox failed")
            return
        print("".join(flag_output.split()))

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    solve()