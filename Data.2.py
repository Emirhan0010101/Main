f = open("data", "r")
curt = f.read().split("\n")
dict = {}
for cart in curt :
    key, value = cart.split(": ")
    dict[key] = value
print(dict) 
