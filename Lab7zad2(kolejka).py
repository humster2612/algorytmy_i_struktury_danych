def ziemniaczka(num):
    register = Queue()
    ludzi= ["Oleg", "Matwij", "Kola", "Ania", "Olha", "Misza"]
    for lud in ludzi:
        register.enqueue(lud)

    while register.size() > 1:
        for i in range(num):
            register.enqueue(register.dequeue())

        liczby= rd.randint(0, 35)
        if liczby == 5:
            register.dequeue()


    return register.dequeue()
