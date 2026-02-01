with open("checksum.dat", "r") as f:
    checksum = f.read()

if checksum:
    print(checksum)
else:
    print("Authentication failed")