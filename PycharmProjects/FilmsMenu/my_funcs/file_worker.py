def read_from_file(filepath):
    with open(filepath, "r") as f:
        return f.readlines()


print(read_from_file("prodfile.txt"))

