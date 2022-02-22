import os
import sys

import pygame
import requests

address_x = 37.260653
address_y = 55.675709
address = str(address_x) + ',' + str(address_y)
spn_x, spn_y = 0.003, 0.003
spn = str(spn_x) + ',' + str(spn_y)

map_request = "http://static-maps.yandex.ru/1.x/?ll=" + address + "&spn=" + spn + "&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))

screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)