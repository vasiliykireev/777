import random
import re
import time
import argparse


class Game:
    reward = {
        '777': 200,
        '999': 100,
        '555': 50,
        '333': 15,
        '111': 10,
        r'..7': 3,
        r'.00': 2,
        r'..0': 1
    }

    def __init__(self, spin = 1, bet = 1):
        if spin == 0: self.spin = False
        else: self.spin = True
        self._winnings = self.check_result(self.play(self.spin), bet)

    @property
    def winnings(self):
        """
        Выигрыш
        """
        return self._winnings

    def play(self, spin):
        """
        Игра в автомат

        Аргументы:
        - debug (int): число для отладки

        Возвращает str: 3 цифры
        """
        digits = ['', '', '']
        if spin == True:
            spins = 100
        else:
            spins = 1
        for p in range(spins):
            if p < 50:
                digits[0] = self.random_digit()
                digits[1] = self.random_digit()
                digits[2] = self.random_digit()
            if p >= 50 and p < 75 and p % 2 == 0:
                digits[1] = self.random_digit()
                digits[2] = self.random_digit()
            if p >= 75 and p % 4 == 0:
                digits[2] = self.random_digit()
            result = ''.join(digits)
            print(f"\r{result}", end="", flush=True)
            time.sleep(0.05)
        return result

    def random_digit(self):
        """
        Случайная цифра

        Возвращает int: от 0 до 9
        """
        digit = str(random.randint(0, 9))
        return digit

    def check_result(self, score, bet):
        """
        Проверка результата — сопоставление с вознаграждением из self.reward
        Если результат не сопоставился — возвращает 0

        Аргументы:
        - score(str): строка для сопоставления с вознаграждением

        Возвращает int: сумму выигрыша
        """
        for pattern, prize in self.reward.items():
            if re.fullmatch(pattern, score):
                winning = prize * bet
                return winning
        return 0
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bet 777 — console slot machine!")
    parser.add_argument(
        "--bet", "-b",
        type=int,
        default=1,
        help="bet: int, default = 1",
    )
    parser.add_argument(
        "--spin", "-r",
        type=int,
        default=1,
        help="spin: int, 0 = False, 1 = True",
    )
    args = parser.parse_args()
play = Game(args.spin, args.bet)
print("\nWinning: ", play.winnings)
