import random


def test_school(test):
    for number in range(len(test)):

        with open('test_country%s.txt' % (number + 1), 'w', encoding='utf-8') as question:
            question.write('ФИО:\nГруппа:\n')
            question.write('Тест Вариант №%s\n' % (number + 1))
            country = list(test.keys())
            random.shuffle(country)

            with open('test_answer%s.txt' % (number + 1), 'w', encoding='utf-8') as answer:

                for quest in range(len(test)):
                    correct_answer = test[country[quest]]
                    wrong_answer = list(test.values())
                    del wrong_answer[wrong_answer.index(correct_answer)]
                    wrong_answer = random.sample(wrong_answer, 3)
                    test_answer = wrong_answer + [correct_answer]
                    random.shuffle(test_answer)
                    question.write('%s) Столица страны %s:\n' % (quest + 1, country[quest]))

                    for answer_point in range(4):
                        question.write('%s) %s\n' % ('abcd'[answer_point], test_answer[answer_point]))

                    answer.write('%s) %s\n' % (quest + 1, 'abcd'[test_answer.index(correct_answer)]))


if __name__ == '__main__':
    ans = {
        'Россия': 'Москва',
        'Беларусь': 'Минск',
        'Сша': 'Вашингтон',
        'Украина': 'Киев'
        }
    test_school(ans)
