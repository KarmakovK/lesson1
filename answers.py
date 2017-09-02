def get_answer(question):
    answers = {'привет': 'И тебе привет!', 'как дела?': 'Лучше всех!', 'пока!': 'Увидимся'}
    answer = answers.get(question.lower(),'хм... не понимаю')
    return answer

question = input('Говорите: ')

print(get_answer(question))