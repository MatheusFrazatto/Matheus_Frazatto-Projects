import random
import re


def cpf_validator():
    while True:
        cpf_input = input('\n🔵 Digite seu CPF:\n'
                          ' ➜  ')
        if cpf_input.lower() == 'sair':
            print("🔻Voltando...🔻")
            break

        cpf_only_digits = re.sub(r'[^0-9]', '', cpf_input)

        if len(cpf_only_digits) != 11:
            print("\n🔴 O CPF deve conter 11 dígitos!\n")
        elif cpf_only_digits == cpf_only_digits[0] * 11:
            print("\n🔴 O CPF é inválido!\n")
            return
        else:
            cpf_calc(cpf_only_digits, False)


def cpf_calc(cpf, generation,):
    if generation:
        nine_digits = cpf
    else:
        nine_digits = cpf[:9]

    result_sum_d1 = 0
    countdown_timer_d1 = 10
    for digit in cpf[:9]:
        result_sum_d1 += int(digit) * countdown_timer_d1
        countdown_timer_d1 -= 1
    first_digit = (result_sum_d1 * 10) % 11
    first_digit = first_digit if first_digit <= 9 else 0
    ten_digits = nine_digits + str(first_digit)

    result_sum_d2 = 0
    countdown_timer_d2 = 11
    for digit in ten_digits:
        result_sum_d2 += int(digit) * countdown_timer_d2
        countdown_timer_d2 -= 1
    second_digit = (result_sum_d2 * 10) % 11
    second_digit = second_digit if second_digit <= 9 else 0

    cpf_generated = nine_digits + str(first_digit) + str(second_digit)

    if generation is False:
        if cpf == cpf_generated:
            print(f"\n🔵 O CPF {format_cpf(cpf)} é válido!\n")
            return cpf_generated
        else:
            print(f"\n🔴 O CPF {format_cpf(cpf)} é inválido!\n")
            return cpf_generated
    else:
        return cpf_generated


def cpf_generator(loop):
    generated_cpfs = set()
    count = 0
    while count < loop:
        random_nine_digits = ''
        for _ in range(9):
            random_nine_digits += str(random.randint(0, 9))
        if random_nine_digits == random_nine_digits[0] * 9:
            continue

        cpf_generated = cpf_calc(random_nine_digits, True)

        if cpf_generated not in generated_cpfs:
            generated_cpfs.add(cpf_generated)
            count += 1
            print(f"\n🔵 {count} - CPF Gerado: {format_cpf(cpf_generated)}")


def format_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def main():
    while True:
        print('______________________________________________________\n'
              '|          📝 CPF Validator & Generator! 📝          |\n'
              '|❗️Digite [S]air a Qualquer Momento Para Encerrar.❗️ |\n'
              '|____________________________________________________|\n')

        user_input = input(
            '🔵 Deseja [V]alidar ou [G]erar um CPF?\n'
            ' ➜  ').strip().lower()
        if user_input == 'v' or user_input == 'validar':
            cpf_validator()
        elif user_input == 'g' or user_input == 'gerar':
            try:
                times = int(input('Quantos CPFs deseja gerar?\n'
                                  '➜  '))
                cpf_generator(times)
            except ValueError:
                print("🔴 Valor inválido. Tente novamente.")
        elif user_input == 's' or user_input == 'sair':
            print("🔻Saindo...🔻")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
