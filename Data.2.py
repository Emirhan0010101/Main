f = open("data","w")
f.write("Name: Emirhan\nSurname: Erdogdu\nGender: Sek erkek\nUsername: Crazyboy_31\nJob: Playboy")
f.close()
f = open("data", "r")
curt = f.read().split("\n")
dict = {}
for cart in curt :
    key, value = cart.split(": ")
    dict[key] = value
print(dict) 
