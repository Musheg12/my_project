from My_project import generate_mat, generate_inst


def deal(qwerty, inst, discount_value=10):
    print(qwerty)
    print(inst)
    if inst.price >= 5_000:
        inst.work_Install()
        inst.discount(discount_value)
    if qwerty.Cable in range(50, 100) and qwerty.Point in range(1, 40) and qwerty.Box in range(1, 3):
        qwerty.name = "garage"
        return qwerty.name
    elif qwerty.Cable in range(100, 500) and qwerty.Point in range(40, 100) and qwerty.Box in range(3, 6):
        qwerty.name = "apartment"
        return qwerty.name
    elif qwerty.Cable in range(500, 5_000) and qwerty.Point in range(100, 200) and qwerty.Box in range(6, 10):
        qwerty.name = "house"
        return qwerty.name
    elif qwerty.Cable in range(5_000, 50_000) and qwerty.Point in range(200, 500) and qwerty.Box in range(10, 30):
        qwerty.name = "office"
        return qwerty.name
    elif qwerty.Cable in range(50_000, 100_000) and qwerty.Point in range(500, 1_000) and qwerty.Box in range(30, 50):
        qwerty.name = "factory"
        return qwerty.name
    else:
        return "another building"


print(deal(generate_mat(), generate_inst()))