espeaker = {}
espeaker = set(espeaker)
multispeaker = {}
multispeaker = set(multispeaker)


line = input("Line: ")

while line != '':
  if line.split(' ', 1)[0] == 'English':
    array = line.split()
    for x in array:
      if x != line.split(' ', 1)[0]:
        espeaker.add(x)
    line = input("Line: ")
  else:
    array = line.split()
    for x in array:
      if x != line.split(' ', 1)[0]:
        multispeaker.add(x)
    line = input("Line: ")


monolangual =  espeaker - multispeaker;

for x in monolangual:
  print(x + " is monolangual")
