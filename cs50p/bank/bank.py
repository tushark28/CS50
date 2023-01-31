greet = input("Greeting: ").strip(" ").lower()
array = greet.split(" ")
first = array[0]
if "hello" == first :
    print("$0")
elif first[0] == 'h':
    print("$20")
else:
    print("$100")