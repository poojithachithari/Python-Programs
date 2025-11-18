
try:
    with open("Assignment-4/sample.txt", "rt") as fh:
        #contents = fh.read()
        lines = fh.readlines()
        print("Reading file content:")
        count = 1
        for line in lines:
            print(f"Line {count}: {line.strip()}")
            count += 1
except FileNotFoundError:
    print(f"Error: The file 'sample.txt' was not found")

