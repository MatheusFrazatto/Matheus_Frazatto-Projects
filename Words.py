import random
import os


def words_loader(file=r'D:\Estudos\Projetos\Words_Repository.txt'):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            word_list = [line.strip() for line in f if line.strip()]
        return word_list
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo '{file}' Não Encontrado ❌")
        return []


def hint_process(secret_word, correct_letters):
    secret_word_letters = set(secret_word)
    possible_letters_hints = []
    for letter in secret_word_letters:
        if letter not in correct_letters:
            possible_letters_hints.append(letter)
    return random.choice(possible_letters_hints)


def game_loop(word_list, points):
    secret_word = random.choice(word_list).lower()
    correct_letters = set()
    attempted_letters = set()
    attempts = len(secret_word) + 5

    print(f'|🔸 Letras: {len(secret_word)}\n'
          f'|🔸 Tentativas: {len(secret_word) + 5}\n'
          f'|🔸 Pontos: {points}\n\n',
          '◽️ ', '➖ '*len(secret_word), '\n')

    while attempts > 0:
        user_input = input(' ➜  ').strip().lower()

        if user_input == 'sair':
            return False, points
        elif user_input == 'dica':
            hint = hint_process(secret_word, correct_letters)
            correct_letters.add(hint)
            attempted_letters.add(hint)
            attempts -= 4
        elif len(user_input) == 1:
            if user_input in secret_word:
                correct_letters.add(user_input)
                attempted_letters.add(user_input)
                points += 3
            else:
                attempted_letters.add(user_input)
                points -= 1
                attempts -= 1
        elif user_input != secret_word:
            for i in user_input:
                if i in secret_word:
                    correct_letters.add(i)
                    attempted_letters.add(i)
                    points += 1
                else:
                    attempted_letters.add(i)
                    points -= 3
                    attempts -= 2

            print('🔵 Palavra Errada!')

        print(f'\n🔸Letras Jogadas: {', '.join(sorted(attempted_letters)).upper()}🔹\n'
              f'🔸Tentativas Restantes: {attempts}\n')

        formed_word_visible = ' ◽️  '
        formed_word_invisible = ''
        for letter in secret_word:
            if letter in correct_letters:
                formed_word_visible += letter.upper() + ' '
                formed_word_invisible += letter
            else:
                formed_word_visible += '➖ '
        print(formed_word_visible, '\n')

        if correct_letters == set(secret_word) or user_input == secret_word:
            extra_points = 0
            if user_input == secret_word:
                extra_points += (len(secret_word) - len(correct_letters)) * 5
            points += 10 + extra_points
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'🔵 Você Acertou a Palavra!')
            print(f'🔸 Pontos extras por completar direto: {extra_points}')
            print(f'🔸Pontuação final: {points} pontos.🔸')
            return True, points

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'🔵 Você PerdeU... A Palavra Era: {secret_word.upper()}')
        print(f'🔸Pontuação final: {points} pontos.🔸')
        return False, points


def main():
    word_list = words_loader()
    points = 0

    print('______________________________________________________\n'
          '|             📝 Bem-vindo Ao Words! 📝              |\n'
          '|❗️Digite [SAIR] a Qualquer Momento Para Encerrar.❗️ |\n'
          '|____________________________________________________|\n')

    while True:
        result, points = game_loop(word_list, points)
        if not result:
            print('🔻Saindo...🔻\n')
            break

        play_again = input(
            '🔵 Deseja Jogar Novamente? [S]im ou [N]ão:\n ➜ ').strip().lower()

        if play_again == 's' or play_again == 'sim':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif play_again == 'n' or play_again == 'não':
            print('🔻Saindo...🔻\n')
            break
        else:
            print('‼️ Opção Inválida. Saindo... ‼️\n')
            break


if __name__ == '__main__':
    main()
