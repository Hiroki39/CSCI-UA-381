with open("sample_input.csv") as f:
    lines = f.read().splitlines()

with open("sample_output.csv", "w") as f:
    f.write("Student,Code\n")
    for i in range(1, len(lines)):
        line = lines[i]
        entries = line.split(",")
        phone_pieces = entries[2].split("-")
        product = float(entries[1]) * float(phone_pieces[0]) * \
            float(phone_pieces[1]) * float(phone_pieces[2])
        f.write(entries[0] + "," + str(product) + "\n")
