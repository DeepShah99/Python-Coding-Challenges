num = 4


def four_season(num):
    match num:
        case 1:
            return "Spring"
        case 404:
            return "Summer"
        case 418:
            return "Fall"
        case _:
            return "Winter"

season = four_season(num)
print(season)
