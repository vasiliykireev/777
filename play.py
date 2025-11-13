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

    def __init__(self, speed = 5, bet = 1):
        self._winnings = self.check_result(self.play(speed), bet)

    @property
    def winnings(self):
        """
        Выигрыш
        """
        return self._winnings

    def play(self, speed):
        """
        Игра в автомат

        Аргументы:
        - debug (int): число для отладки

        Возвращает str: 3 цифры
        """
        digits = ['', '', '']
        time_sleep = 0
        if speed == 0:
            spins = 1
        else:
            time_sleep = 0.1 - (max(1, min(speed, 9)) - 1) * (0.1 - 0.01) / 8
            spins = 100
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
            time.sleep(time_sleep)
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
        "--speed", "-s",
        type=int,
        default=5,
        help="speed: int, 1 (slow) to 9 (fast), 0 = no animation, default = 5",
    )
    args = parser.parse_args()
play = Game(args.speed, args.bet)
print("\nWinning: ", play.winnings)
