List = []
while True:
    try:
        List.append(input("Name: "))

    except EOFError:
        new="Adieu, adieu, to "
        for i in range(len(List)-1):
            new += f"{List[i]}, "
        if len(List) == 1:
            new += f"{List[0]}"
        else:
            new+= f"and {List[len(List)-1]}"
        print(new)
        break