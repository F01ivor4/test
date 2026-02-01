import subprocess

def solve():
    print("--- SOLVER START ---")
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
        print(f"Expression: {expression_line}")
    
        if not expression_line:
            print("Error: Empty expression")
            return
        result = eval(expression_line)
        print(f"Result: {result}")
        
        p.stdin.write(f"{result}\n")
        p.stdin.flush()
        
        flag = p.stdout.read()
        print(flag)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    solve()