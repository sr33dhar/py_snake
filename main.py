import pygame
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.orientation = "RIGHT"
        self.paused = False
        self.playing = True
        self.score = 0
        self.high_score = self.get_high_score()

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.head = Snake(self, 5, 5)
        self.snake_body = []
        self.snake_body.append(Snake(self, 4, 5))
        self.snake_body.append(Snake(self, 3, 5))
        self.all_sprites.add(self.head)
        self.all_sprites.add(*self.snake_body)

        self.reward = Reward(self, 20, 5)
        self.all_sprites.add(self.reward)

        self.run()

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):

        if not self.paused:            
            # check for body collisions
            for body_part in self.snake_body:
                if body_part.body_collision():
                    self.playing = False

            # Check for Reward collision
            if self.reward.reward_collision():
                self.reward.get_new_position()
                self.snake_body.append(Snake(self, self.snake_body[-1].x, self.snake_body[-1].y))
                self.score += 1

            self.all_sprites.update()

            # Store the current head position
            head_x, head_y = self.head.x, self.head.y
            # Update body positions
            prev_x, prev_y = head_x, head_y
            for part in self.snake_body:
                # Swap the current part's position with the previous one
                part.x, part.y, prev_x, prev_y = prev_x, prev_y, part.x, part.y

            # Move the head in the current direction
            if self.orientation == "UP":
                self.head.y -= 1
            elif self.orientation == "DOWN":
                self.head.y += 1
            elif self.orientation == "LEFT":
                self.head.x -= 1
            elif self.orientation == "RIGHT":
                self.head.x += 1

            # Check for collisions with the walls

            # if self.head.x < 0 or self.head.x >= GRIDWIDTH or self.head.y < 0 or self.head.y >= GRIDHEIGHT:
            #     self.playing = False

            if self.head.x < 0:
                self.head.x = GRIDWIDTH - 1
            elif self.head.x > GRIDWIDTH - 1:
                self.head.x = 0

            if self.head.y < 0:
                self.head.y = GRIDHEIGHT - 1
            elif self.head.y > GRIDHEIGHT - 1:
                self.head.y = 0

            # Update all sprites
            self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if not self.paused:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if not self.orientation == "DOWN":
                            self.orientation = "UP"
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if not self.orientation == "UP":
                            self.orientation = "DOWN"
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if not self.orientation == "RIGHT":
                            self.orientation = "LEFT"
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if not self.orientation == "LEFT":
                            self.orientation = "RIGHT"
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused

    def quit(self):
        pygame.quit()
        quit(0)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.all_sprites.draw(self.screen)
        self.draw_grid()

        # Display current score and high score
        high_score_digits = len(str(self.high_score))
        score_text = f"S: {self.score:0{high_score_digits}d}"
        high_score_text = f"H: {self.high_score:0{high_score_digits}d}"
        
        # Create UIElement instances
        score_element = UIElement(GRIDWIDTH - 2, 1, score_text)
        high_score_element = UIElement(GRIDWIDTH - 2, 2, high_score_text)
        
        # Draw the score and high score
        score_element.draw(self.screen, 20)
        high_score_element.draw(self.screen, 20)

        if self.paused:
            UIElement(GRIDWIDTH//2 - 6, GRIDHEIGHT//2 - 1, "PAUSED").draw(self.screen, 100)
        pygame.display.flip()

    def get_high_score(self):
        with open("high_score.txt", "r") as file:
            try:
                high_score = int(file.read())
            except:
                high_score = 0
        return high_score

    def set_high_score(self):
        with open("high_score.txt", "w") as file:
            if self.score > self.high_score:
                file.write(str(self.score))
            else:
                file.write(str(self.high_score))

    def main_screen(self):
        self.set_high_score()
        self.screen.fill(BLACK)

        if not self.playing:
            title_element = UIElement(0, 6, "GAME OVER!")
            title_element.x = (WIDTH - title_element.get_text_width(100)) // 2
            title_element.draw(self.screen, 100)

            title_element = UIElement(0, 15, f"Score: {self.score}")
            title_element.x = (WIDTH - title_element.get_text_width(50)) // 2
            title_element.draw(self.screen, 50)

        else:

            title_element = UIElement(0, 6, "SNAKE GAME")
            title_element.x = (WIDTH - title_element.get_text_width(100)) // 2
            title_element.draw(self.screen, 100)

        title_element = UIElement(0, 12, f"High Score: {self.high_score if self.high_score > self.score else self.score}")
        title_element.x = (WIDTH - title_element.get_text_width(50)) // 2
        title_element.draw(self.screen, 50)

        self.start_button = Button(self, BLACK, WHITE, WIDTH//2 - 100, 600, 200, 80, "START")        
        self.autoplay_button = Button(self, BLACK, WHITE, WIDTH//2 - 150, 700, 300, 80, "AUTOPLAY")        
        self.quit_button = Button(self, BLACK, WHITE, WIDTH//2 - 100, 800, 200, 80, "QUIT")

        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.autoplay_button.draw(self.screen, 50)
            self.start_button.draw(self.screen, 50)
            self.quit_button.draw(self.screen, 50)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    if self.start_button.is_mouse_over(mouse_x, mouse_y):
                        self.start_button.color = LIGHTGREY
                    else:
                        self.start_button.color = BLACK

                    if self.autoplay_button.is_mouse_over(mouse_x, mouse_y):
                        self.autoplay_button.color = LIGHTGREY
                    else:
                        self.autoplay_button.color = BLACK

                if event.type == pygame.MOUSEMOTION:
                    if self.quit_button.is_mouse_over(mouse_x, mouse_y):
                        self.quit_button.color = LIGHTGREY
                    else:
                        self.quit_button.color = BLACK
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_mouse_over(mouse_x, mouse_y):
                        waiting = False
                    if self.quit_button.is_mouse_over(mouse_x, mouse_y):
                        self.quit()


game  = Game()
while True:
    game.main_screen()
    game.new()
    game.run()
