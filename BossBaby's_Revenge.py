def kind_of_boy(bullets):
    if bullets[0] == 'R':
        return "Bad boy"

    count_shoot = 0
    for i in range(len(bullets)):
        if bullets[i] == 'S':
            count_shoot += 1
        else:
            count_shoot -= 1
            if count_shoot < 0:
                count_shoot = 0

    return "Good boy" if count_shoot == 0 else "Bad boy"


print(kind_of_boy("SSRSRRR"))
