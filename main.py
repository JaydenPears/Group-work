import os
import sys

import pygame
import requests

address_x = 37.260653
address_y = 55.675709
address = str(address_x) + ',' + str(address_y)
spn_x, spn_y = 0.003, 0.003
spn = str(spn_x) + ',' + str(spn_y)

pygame.init()
screen = pygame.display.set_mode((600, 450))
running = True
clock = pygame.time.Clock()

map_file = "map.png"

def draw_map():
    global map_file, address, spn
    map_request = "http://static-maps.yandex.ru/1.x/?ll=" + address + "&spn=" + spn + "&l=map"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    with open(map_file, "wb") as file:
        file.write(response.content)
    
    screen.blit(pygame.image.load(map_file), (0, 0))

draw_map()

while running:
    clock.tick(60)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEDOWN:
                if spn_x + 0.01 < 1:
                    spn_x += 0.01
                if spn_y + 0.01 < 1:
                    spn_y += 0.01
                spn = str(spn_x) + ',' + str(spn_y)
                draw_map()
            if event.key == pygame.K_PAGEUP:
                if spn_x - 0.01 > 0:
                    spn_x -= 0.01
                if spn_y - 0.01 > 0:
                    spn_y -= 0.01
                spn = str(spn_x) + ',' + str(spn_y)
                draw_map()

os.remove(map_file)