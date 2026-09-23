import random
import os

class Hero:
    def __init__(self,name,armor,health,damage,weapon):
        self.name = name #string
        self.armor = armor #int
        self.health = health #int
        self.damage = damage #int
        self.armor_crushed = False
        self.weapon = weapon

    def show_info(self):
        print(f"Nome: {self.name}\nArmadura:{self.armor}\nVida:{self.health}\nForça de Ataque:{self.damage}")

    def death(self):
        if self.health <= 0:
            print(f"{self.name} morreu.")
            del self

    def check_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def broken_armor(self):
        if self.armor_crushed == False and self.armor == 0:
            print(f"A armadura de {self.name} foi destruída!")
            self.armor_crushed = True

    def armor_status(self):
        print(f'{self.name} - Armadura atual: {self.armor}')

    def health_status(self):
        print(f'Vida atual:{self.health} ')

    def take_damage(self,damage):
        if self.armor >= damage:
            if type(heroi):
                print('Um ataque poderoso, mas foi parado pela sua armadura!')
                self.armor -= damage
            else:
                print('Um ataque poderoso, mas foi parado pela armadura do inimigo!')
                self.armor -= damage
                
            print(f'Dano causado a armadura: {damage}')
            if self. armor == 0:
                self.broken_armor()
            else:
                self.armor_status()
        else:
            if self.armor <= 0:
                self.health -= damage
                if self.health <= 0:
                    print(f'{self.name} sofreu um golpe brutal! Dano {damage}')
                    self.death()
                else:
                    print(f'Dano causado: {damage}')
                    self.health_status()
            else:
                print(f'Dano causado a armadura: {self.armor}')
                damage -= self.armor
                self.armor = 0
                self.broken_armor()
                print(f'Dano causado: {damage}')
                self.health -= damage
                if self.health <= 0:
                    print(f'{self.name} sofreu um golpe letal!')
                    self.death()     

    def roll_a_dice(self):
        return random.randint(1, 6)
    
    # def attack(self,enemy,damage):
    #     if enemy.health <= 0:
    #         if enemy.name != 'Arthur':
    #             print(f'Mantenha a calma aventureiro, {enemy.name} já está morto.')
    #         else:
    #             print(f'O nosso heroi {enemy.name}, foi abatido D:')
    #         return
    #     print(f"{self.name} atacou {enemy.name}")
    #     enemy.take_damage(damage)
    
    def perform_attack(self,target,damage):
        if self.health > 0:
            if target.health <= 0:
                if type(heroi):
                    print(f'Mantenha a calma aventureiro, {target.name} já está morto.')
                else:
                    print(f'O nosso heroi {target.name}, foi abatido D:')
                return
            else:
                dice = self.roll_a_dice() 
                if dice == 6:
                    if self.weapon == 'Arco Longo':
                        print(f"{self.name} encaixa duas flechas de uma só vez e dispara!")
                        target.take_damage(damage * 2)
                else:
                    print(f"{self.name} atacou {target.name}")
                    target.take_damage(damage)
        input('Enter para continuar...\n')
        
    def combat(self,target):
        while self.health > 0 or target.health > 0:
            if type(heroi):
                action = input('1 - Atacar\n2 - Curar\n3 - Fugir\n-> ')
                if action == '1' or action.lower() =='atacar':
                    self.perform_attack(target,self.damage)
                    target.perform_attack(self,target.damage)
                elif action == '2' or action.lower() == 'curar':
                    print('Curar!') #ainda a implementar
                    target.perform_attack(self,target.damage)
                elif action == '3' or action.lower() == 'fugir':
                    print('Cocoricó') #ainda a implementar
                    target.perform_attack(self,target.damage)
                else:
                    print('Opção inválida! Tente novamente.')
            else:
                print('Ação inválida')

class Knight(Hero):
    def __init__(self,name,armor,health,damage,weapon):
        super().__init__(name,armor,health,damage,weapon)
        self.armor = armor + (armor * 10) / 100 #heavy armor bonus + 10%

class Rogue(Hero):
    def __init__(self,name,armor,health,damage,weapon):
        super().__init__(name,armor,health,damage,weapon)


    def dodge(self):
        dice = self.roll_a_dice() 
        if dice == 6:
            print(f"{self.name} esquivou do ataque!")
            return True
        else:
            return False
    def take_damage(self, damage):
        if self.dodge() == False:
            super().take_damage(damage)

class Archer(Hero):
    def __init__(self,name,armor,health,damage,weapon):
        super().__init__(name,armor,health,damage,weapon)
    
    # def attack(self,enemy):
    #     dice = self.roll_a_dice() 
    #     if dice == 6:
    #         print(f"{self.name} encaixa duas flechas de uma só vez e dispara!")
    #         critical_damage = self.damage *2 # Dobra o dano
    #         super().attack(enemy,critical_damage) 
    #     else:
    #         super().attack(enemy,self.damage)

class Mage(Hero):
    pass

class Dragon(Hero):
    pass


##Game Start
input(
    "\nBem-vindo ao Reino de Mythralis, uma terra outrora pacífica, agora assolada por perigos inimagináveis.\n"
    "Criaturas malignas emergem das profundezas da floresta sombria, saqueando vilarejos e espalhando caos.\n"
    "Os aldeões estão desesperados, buscando um herói capaz de enfrentar essas ameaças.\n"
    "Você, um forasteiro misterioso, chega em um momento crítico. Será você o salvador que Mythralis tanto precisa?\n"
    "Prepare-se para uma jornada repleta de desafios, onde suas decisões moldarão o destino deste reino.\n"
    "\nPressione enter para continuar..."
)
os.system('cls')
heroi = Hero(input('\nAldeão: Saudações forasteiro, qual o seu nome?\n-> '),30,50,30,'Espada Bastarda')
enemy = Archer('Bandit',20,20,20,'Arco Longo')

playing = True

# heroi.show_info()
# enemy.show_info()

while playing:
    answer = input(f'Aldeão: Bem vindo {heroi.name}, vieste para ajudar-nos a lidar com os monstros na floresta?\n1 - sim\n2 - não\n-> ')
    if answer == '1' or answer == 'sim':
        heroi.combat(enemy)
        # heroi.attack(enemy)
        # heroi.attack(enemy)

        if heroi.health <= 0:
            playing = False
            print('Fim de Jogo!')
    elif answer == '2' or answer =='nao' or answer =='não':
        answer = input('Não tens mesmo a cara de um herói, parece estar com medo... queres voltar para casa?\n1 - sim\n2 - não\n-> ')
        if answer == '1' or 'sim':
            print('O Aldeão exibe uma expressão que mistura tristeza e desprezo...')
            print('Fim de jogo! Você abandonou a aventura.')
            playing = False
        else:
            print('Você diz ao Aldeão que não é nenhum covarde e que está pronto para enfrentar os desafios da floresta')
    else:
        answer = input('Opção Inválida.')