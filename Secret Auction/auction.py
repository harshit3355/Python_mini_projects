import art

empty_dict={}
loop=True

print("Welcome to the Auction:")
print(art.logo)


while loop==True:
    name=input("Enter your Name:\n")
    bid=int(input("Enter your bid:\n"))

    empty_dict[name]=bid
    repeat=input("If there is any other person to Bid 'y/n':\n")

    if repeat=="n":
        loop=False


id=""
max=0
for data in empty_dict:
    if empty_dict[data]>max:
        max=empty_dict[data]
        id=data

print("*****************************************************")
print("*****************************************************")
print("*****************************************************")

print(f"Highest Bid is from {id} i.e. {max}\n")
