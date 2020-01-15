import AgeName


anna = AgeName.AgeName()
sam = AgeName.AgeName('sam', 44)

print(anna.GetName())
anna.SetAge(33)

print(sam.GetName())
sam.SetName('ali')

print(anna)
print(sam)
