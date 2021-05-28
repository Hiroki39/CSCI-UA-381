import sys

N = int(input("Enter the number of people answering the questionare: "))

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

with open(sys.argv[2], 'w') as f:
    f.write('\t'.join(lines) + '\n')
    for i in range(N):
        print("------------------------------------------")
        print(f"Filling the questionare for person #{i+1}...")
        answers = []
        for line in lines:
            print(line)
            answers.append(input())
        f.write('\t'.join(answers) + '\n')
