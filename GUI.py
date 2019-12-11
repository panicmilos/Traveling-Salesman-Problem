import pygame

display_w = 1000
display_h = 800
max_x = 0
max_y = 0
printed = False
window = pygame.display.set_mode((display_w, display_h))
font = None

def init(ga):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("TSP - genetic algorithm")
    global font
    font = pygame.font.SysFont('Comic Sans MS', 20)
    global ga_gui
    ga_gui = ga
    global max_x
    global max_y
    # maksimalno x i y (zbog skaliranja)
    for city in ga_gui.cities:
        if max_x < city.x:
            max_x = city.x
        if max_y < city.y:
            max_y = city.y
    _draw_dots()
    _draw_best_path()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        _update_window()


def _draw_dots():
    for city in ga_gui.cities:
        pygame.draw.circle(window, pygame.Color("black"), _scale_coordinates(city), 4, 1)

    pygame.draw.circle(window, pygame.Color("purple"), _scale_coordinates(ga_gui.best_path[0]), 7, 1)



def _draw_best_path():
    for i in range(-1, len(ga_gui.population[1]) - 1):
        pygame.draw.line(window, pygame.Color("red"), _scale_coordinates(ga_gui.best_path[i]),
                         _scale_coordinates(ga_gui.best_path[i + 1]), 3)


# prikaz kako se dolazi do najboljeg(sporo)
def _draw_paths():
    for path in ga_gui.population:
        window.fill((100, 100, 100))
        _draw_dots()
        _draw_best_path()
        for i in range(-1, len(ga_gui.population[1]) - 1):
            pygame.draw.line(window, pygame.Color("white"), _scale_coordinates(path[i]),
                             _scale_coordinates(path[i + 1]), 1)

    _write_text("Current best: ")



def _scale_coordinates(city):
    x = 50 + int(city.x * (display_w - 100) / max_x)
    y = 50 + int(city.y * (display_h - 100) / max_y)
    return x, y


def _write_text(message):
    text = message + str(ga_gui.current_best)
    text2 = "Iteration: " + str(ga_gui.current_iter)
    text = font.render(text, True, (200, 200, 200))
    text2 = font.render(text2, True, (200, 200, 200))
    window.blit(text, (10, 10))
    window.blit(text2, (10, 30))



def _update_window():
    # window.fill((100, 100, 100))
    # _draw_dots()
    # _draw_best_path()
    _draw_paths()
    if not ga_gui.next_iter():
        window.fill((130, 130, 90))
        _draw_best_path()
        _draw_dots()
        _write_text("Best: ")
        global printed
        if not printed:
            print("Predjeni put >> ", ga_gui.current_best)
            print("Redosled gradova >> ", ga_gui.best_path)
            printed = True
    pygame.display.update()
