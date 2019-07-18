class Myrange:
    def __init__(self):
        self.list01 = []
    def add_skill(self, skill):
        self.list01.append(skill)
    def __iter__(self):
        print(self.list01)
        return SkillIterator(self.list01)
class SkillIterator:
    def __init__(self,target):
        self.target = target
        self.a = 0
    def __next__(self):
        if self.a > len(self.target)-1:
            raise StopIteration
        ne = self.target[self.a]
        self.a += 1
        return ne

Myrange().add_skill(1)
Myrange().add_skill(2)
Myrange().add_skill(3)
Myrange().add_skill(4)
Myrange().add_skill(5)
Myrange().add_skill(6)

range01 = Myrange().__iter__()
while True:
    try:
        range02 = range01.__next__()
        print(range02)
    except StopIteration:
        break



