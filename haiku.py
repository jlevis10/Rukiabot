import random
class Haiku():
    def __init__(self):
        self.name = 'Rukia'

    def grab_word(self,s):
        if s == 1:
            if 0 == 0:
                with open('one_syl.txt','r') as f:
                    words = f.read().split()
                    index = random.randint(0,len(words)-1)
                    return words[index]
            else:
                with open('one_adj.txt','r') as f:
                    words = f.read().split()
                    index = random.randint(0,len(words)-1)
                    return words[index]
        elif s== 4:
            with open('four_syl.txt', 'r') as f:
                words = f.read().split()
                index = random.randint(0, len(words) - 1)
                return words[index]
        elif s== 3:
            with open('three_syl.txt', 'r') as f:
                words = f.read().split()
                index = random.randint(0, len(words) - 1)
                return words[index]
        elif s==5:
            with open('five_syl.txt', 'r') as f:
                words = f.read().split()
                index = random.randint(0, len(words) - 1)
                return words[index]
        else:
            with open('two_syl.txt', 'r') as f:
                words = f.read().split()
                index = random.randint(0, len(words) - 1)
                return words[index]

    def sequence(self):
        l1 = []
        l2 = []
        l3 = []
        while sum(l1) < 5:
            num = random.randint(1,5)
            if sum(l1) + num <= 5:
                l1.append(num)
        while sum(l3) < 5:
            num = random.randint(1,5)
            if sum(l3) + num <= 5:
                l3.append(num)
        while sum(l2) < 7:
            num = random.randint(1,5)
            if sum(l2) + num <= 7:
                l2.append(num)
        return [l1,l2,l3]

    def generate(self):
        seq = self.sequence()
        line1,line2,line3 = "","",""
        for e in seq[0]:
            line1 += " " + self.grab_word(e)
        for e in seq[1]:
            line2 += " " + self.grab_word(e)
        for e in seq[2]:
            line3 += " " + self.grab_word(e)
        return line1 + '\n' + line2 + '\n' + line3


