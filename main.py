import random

class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self, other):
        damage = random.randint(10, 30)  # Случайный урон от 10 до 30
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def heal(self):
        heal_amount = random.randint(5, 20)  # Случайное восстановление от 5 до 20
        self.health += heal_amount
        print(f"{self.name} пропускает ход и восстанавливает {heal_amount} здоровья.")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health} здоровья"

class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(name=player_name)
        self.computer = Hero(name="Компьютерный герой")
        print(f"Добро пожаловать в игру, {self.player.name}!")

    def start(self):
        print(f"\nНачало игры: {self.player.name} против {self.computer.name}!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                break
            self.computer_turn()
        self.declare_winner()

    def player_turn(self):
        print("\n--- Ваш ход ---")
        self.show_health()
        action = self.choose_action()
        if action == '1':
            self.player.attack(self.computer)
        elif action == '2':
            self.player.heal()
        else:
            print("Неверный выбор. Вы пропустили ход.")
        self.show_health()

    def computer_turn(self):
        print("\n--- Ход компьютера ---")
        self.computer.attack(self.player)
        self.show_health()

    def choose_action(self):
        print("Выберите действие:")
        print("1. Атаковать")
        print("2. Пропустить ход (восстановить здоровье)")
        return input("Ваш выбор: ")

    def show_health(self):
        print(f"{self.player}")
        print(f"{self.computer}")
        print("-" * 30)

    def declare_winner(self):
        if self.player.is_alive():
            print(f"\nПоздравляем, {self.player.name} победил!")
        else:
            print(f"\n{self.computer.name} победил. Удачи в следующий раз, {self.player.name}!")

# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.start()
