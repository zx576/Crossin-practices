
nice = lambda x:'silence'

rat = lambda x :'betray'


def tit_for_tat(last_turn):
    if last_turn == 'betray':
        return 'betray'
    else:
        return 'silence'

def prison_delimma(n,s1,s2):

    p1_years,p2_years = 0
    p1_last_turn,p2_last_turn = ''

    for i in range(n):

        p1_choice = s1(p2_last_turn)
        p2_choice = s2(p1_last_turn)

        if p1_choice == p2_choice == 'betray':
            p1_years += 2
            p2_years += 2


        elif p1_choice == p2_choice == 'silence':
            p1_years += 1
            p2_years += 1

        elif p1_choice == 'betray' != p2_choice:
            # p1_years += 0
            p2_years += 5
        else:
            p1_years += 5

        p1_last_turn,p2_last_turn = p1_choice,p2_choice

    return p1_years,p2_years

res = prison_delimma(5,rat,tit_for_tat)

print(res)
