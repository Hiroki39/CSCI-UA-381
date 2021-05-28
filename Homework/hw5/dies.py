import random


class Die:
    def roll(self):
        return random.randint(1, 6)


dies = [Die() for i in range(1000000)]

count = 0

while dies:
    dies = [curr_die for curr_die in dies if curr_die.roll() == 6]
    count += 1

print("Number of iteration taken:", count)

print("Probability that rolling a dice that many times would yield a 6 all of"
      " those times: 1 in", 6**count)

# That doesn't mean the next roll of this die is more likely than 1/6 to be a 6

# There are millions of pairs of features we could compare, so it is easy to
# find some relationships like the one mentioned in this question by chance
# even if there's no actual correlations at all. To prevent this, we need to
# pre-register our features of interest before we conduct the experiment and
# analyze the data
