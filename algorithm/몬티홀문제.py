import random
game_num = 0
change_correct = 0
not_change_correct = 0
for _ in range(10000):
    game_num += 1
    num_list = [1, 2, 3]
    choice_num = random.randint(1, 3)
    correct_num = random.randint(1, 3)
    num_list.remove(choice_num)
    if num_list[1] != correct_num:
        num_list.pop()
    else:
        num_list.pop(0)

    for i in ['do_change','do_not_change']:
        if i == 'do_change':            
            final_choice_num = num_list[0]
            if final_choice_num == correct_num:
                change_correct += 1
        else:
            final_choice_num = choice_num
            if final_choice_num == correct_num:
                not_change_correct += 1
    if game_num % 1000 == 0:
        print('game_num :', game_num )
        print('바꿨을 때 맞출 확률   :', change_correct/game_num, 'correct_num / game_num :', f'{change_correct}/{game_num}')
        print('안바꿨을 때 맞출 확률 :', not_change_correct/game_num, 'correct_num / game_num :', f'{not_change_correct}/{game_num}')

