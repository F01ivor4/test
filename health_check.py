import subprocess

def solve():
    p = subprocess.Popen(
        ["/readflag"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=0
    )

    try:
        expression_line = p.stdout.readline().strip()
    
        if not expression_line:
            print("Error: Empty expression")
            return
        result = eval(expression_line)
        
        p.stdin.write(f"{result}\n")
        p.stdin.flush()
        
        flag = p.stdout.read()
        print(flag)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    solve()