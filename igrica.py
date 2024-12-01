import pygame
import math

# Inicializacija Pygame
pygame.init()

# Barve
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (0, 128, 0)  # Zeleni tank
RED = (255, 0, 0)  # Rdeča barva
GRAY = (150, 150, 150)  # Siva barva za izstrelke
SKY_BLUE = (135, 206, 235)
BROWN_GROUND = (139, 69, 19)
BLACK = (0, 0, 0)  # Črna barva

# Nastavitve zaslona
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Stars")


# Risanje ozadja
def draw_background():
    # Nariši nebo
    screen.fill(SKY_BLUE)
    # Nariši tla (spustimo še nižje)
    pygame.draw.rect(screen, BROWN_GROUND, (0, HEIGHT - 180, WIDTH, 180))

# Tank razred

class Tank:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.angle = 45
        self.power = 50
        self.health = 100  # Dodano zdravje
        self.max_health = self.health  # Maksimalno zdravje
        self.fuel = 100  # Omejeno gorivo, ki se porablja za premike
        self.max_fuel = 100  # Maksimalno gorivo
        self.has_shot = False  # Zastavica za izstrelitev

    def draw(self):
        # Risanje tanke oblike
        pygame.draw.rect(screen, self.color, (self.x, self.y, 40, 20))

        # Risanje pravokotnika na levi za modri tank
        pygame.draw.rect(screen, BLACK, (self.x - 5, self.y + 20, 50, 10))  # Velik pravokotnik na levi

        # Risanje kupole (sedaj nižje)
        pygame.draw.rect(screen, self.color, (self.x + 10, self.y - 10, 20, 15))  # Kupola je nižje
        pygame.draw.line(screen, self.color, (self.x + 20, self.y - 10), 
                         (self.x + 20 + 30 * math.cos(math.radians(self.angle)), 
                          self.y - 10 - 35 * math.sin(math.radians(self.angle))), 5)  # Cev je višje

        # Prikaz zdravja
        health_bar_length = 40 * (self.health / self.max_health)
        health_bar = pygame.Rect(self.x, self.y - 10, health_bar_length, 5)
        pygame.draw.rect(screen, GREEN, health_bar)
        pygame.draw.rect(screen, WHITE, (self.x, self.y - 10, 40, 5), 1)

        # Rdeče črte za izgubljeno zdravje
        for i in range(self.max_health // 10):
            if i >= self.health // 10:
                pygame.draw.line(screen, RED, (self.x + i * 4, self.y - 9), (self.x + i * 4 + 4, self.y - 9), 3)

        # Prikaz goriva
        fuel_bar_length = 40 * (self.fuel / self.max_fuel)
        fuel_bar = pygame.Rect(self.x, self.y - 20, fuel_bar_length, 5)
        pygame.draw.rect(screen, BLUE, fuel_bar)
        pygame.draw.rect(screen, WHITE, (self.x, self.y - 20, 40, 5), 1)

    def shoot(self):
        return Bullet(self.x + 20, self.y - 15, self.angle, self.power)

    def move(self, direction):
        if self.fuel >= 10:  # 1 cm premika = 10 pikslov
            if direction == "left" and self.x > 0:  # Omejitev gibanja levo
                self.x -= 10  # Premik za 10 pikslov
                self.fuel -= 10  # Porabi gorivo
            elif direction == "right" and self.x < WIDTH - 40:  # Omejitev gibanja desno
                self.x += 10  # Premik za 10 pikslov
                self.fuel -= 10  # Porabi gorivo

# Kroglica razred

class Bullet:
    def __init__(self, x, y, angle, power):
        self.x = x
        self.y = y
        self.angle = angle
        self.power = power
        self.gravity = 0.5
        self.time = 0

    def update(self):
        self.x += self.power * math.cos(math.radians(self.angle))
        self.y -= self.power * math.sin(math.radians(self.angle)) - (self.gravity * self.time)
        self.time += 1

    def draw(self):
        pygame.draw.circle(screen, GRAY, (int(self.x), int(self.y)), 5)  # Izstrelki so zdaj sivi

# Glavna zanka
tank1 = Tank(100, HEIGHT - 150, BLUE)  # Spustimo tank nekoliko višje
tank2 = Tank(600, HEIGHT - 150, DARK_GREEN)  # Zeleni tank
bullets = []

running = True
turn = 1  # 1 for tank1, 2 for tank2
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Tank 1 controls
    if turn == 1:
        if keys[pygame.K_LEFT] and tank1.fuel >= 10:
            tank1.move("left")
        if keys[pygame.K_RIGHT] and tank1.fuel >= 10:
            tank1.move("right")
        if keys[pygame.K_UP]:
            tank1.angle += 1
        if keys[pygame.K_DOWN]:
            tank1.angle -= 1
        if keys[pygame.K_SPACE] and not tank1.has_shot:  # En strel na potezo
            bullet = tank1.shoot()
            bullets.append(bullet)
            tank1.has_shot = True  # Označi, da je tank streljal
            turn = 2  # Preklopi na tank 2

    # Tank 2 controls
    if turn == 2:
        if keys[pygame.K_a] and tank2.fuel >= 10:
            tank2.move("left")
        if keys[pygame.K_d] and tank2.fuel >= 10:
            tank2.move("right")
        if keys[pygame.K_w]:
            tank2.angle += 1
        if keys[pygame.K_s]:
            tank2.angle -= 1
        if keys[pygame.K_RETURN] and not tank2.has_shot:  # En strel na potezo
            bullet = tank2.shoot()
            bullets.append(bullet)
            tank2.has_shot = True  # Označi, da je tank streljal
            turn = 1  # Preklopi na tank 1

    # Risanje
    draw_background()
    tank1.draw()
    tank2.draw()

    for bullet in bullets:
        bullet.update()
        bullet.draw()
        
        # Preverjanje trkov
        if (tank1.x < bullet.x < tank1.x + 40 and tank1.y < bullet.y < tank1.y + 20):
            tank1.health -= 10
            bullets.remove(bullet)
        elif (tank2.x < bullet.x < tank2.x + 40 and tank2.y < bullet.y < tank2.y + 20):
            tank2.health -= 10
            bullets.remove(bullet)

    # Preverjanje, ali je tank izgubil
    if tank1.health <= 0:
        print("Tank 1 je izgubil!")
        game_over = True
    if tank2.health <= 0:
        print("Tank 2 je izgubil!")
        game_over = True

    # Izpis konca igre
    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render("Konec igre!", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        pygame.display.flip()
        pygame.time.wait(2000)  # Čakanje pred zaprtjem
        running = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
