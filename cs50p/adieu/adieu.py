while True:
    List = []
    try:
        List.append(input("Name: "))

    except EOFError:
        new="Adieu, adieu, to "
        for i in range(len(List)-1):
            new += f"{List[i]}, "
        new+= f" and {List[len(List)-1]}"
        break