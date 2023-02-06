List = []
while True:
    try:
        List.append(input("Name: "))

    except EOFError:
        new="Adieu, adieu, to "
        if len(List) == 1:
            new += f"{List[0]}"
        elif len(List) == 2:
            new+= f"{List[0]} and {List[1]}"
        else:
            for i in range(len(List)-1):
                new += f"{List[i]}, "
            new+= f"and {List[len(List)-1]}"
        print(new)
        break