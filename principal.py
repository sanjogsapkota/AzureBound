import pygame
import sys
from boton import Boton

pygame.init()

pantalla = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Azure Stranded")
pygame.mixer.music.load("assets_menu/musica_incio.wav")
pygame.mixer.music.play()
fondo_pantalla = pygame.image.load("assets_menu/Planeta.png")


def obtener_fuente(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets_menu/GloriousChristmas-BLWWB.ttf", size)
    def __init__(self):
        self.pantalla = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Azure Stranded")
        self.fondo_pantalla = pygame.image.load("assets_menu/Planeta.png")
        self.font = pygame.font.Font("assets_menu/GloriousChristmas-BLWWB.ttf", 45)

    def update_jugar_screen(self):
        jugar_texto = self.font.render("Pantalla Jugar.", True, "White")
        jugar_rect = jugar_texto.get_rect(center=(640, 260))
        self.pantalla.blit(jugar_texto, jugar_rect)

    def update_opciones_screen(self):
        opciones_texto = self.font.render("Pantalla opciones", True, "White")
        opciones_rect = opciones_texto.get_rect(center=(640, 260))
        self.pantalla.blit(opciones_texto, opciones_rect)

    def update_principal_screen(self):
        self.pantalla.blit(self.fondo_pantalla, (0, 0))
        menu_texto = self.font.render("Azure Stranded", True, "blue")
        menu_rect = menu_texto.get_rect(center=(640, 100))
        self.pantalla.blit(menu_texto, menu_rect)


def opciones():
    while True:
        Opciones_Ration_Pos = pygame.mouse.get_pos()

        pantalla.fill("black")

        opciones_texto = obtener_fuente(45).render("Pantalla opciones", True, "White")
        opciones_rect = opciones_texto.get_rect(center=(640, 260))
        pantalla.blit(opciones_texto, opciones_rect)

        opciones_atras = Boton(imagen=None, pos=(640, 460),
                               texto_entrada="ATRAS", fuente=obtener_fuente(75), color_base="White",
                               color_flotante="Green")

        opciones_atras.cambiar_color(Opciones_Ration_Pos)
        opciones_atras.actualizar(pantalla)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if opciones_atras.verificar_entrada(Opciones_Ration_Pos):
                    pantalla_principal()

        pygame.display.update()


def pantalla_principal():
    while True:
        pantalla.fill("black")
        pantalla.blit(fondo_pantalla, (0, 0))

        menu_raton_pos = pygame.mouse.get_pos()

        menu_texto = obtener_fuente(140).render("Azure Stranded", True, "blue")
        menu_rect = menu_texto.get_rect(center=(640, 100))

        boton_jugar = Boton(imagen=pygame.image.load("assets_menu/Jugar Rect.png"), pos=(640, 250),
                            texto_entrada="JUGAR", fuente=obtener_fuente(75), color_base="green", color_flotante="red")
        boton_opciones = Boton(imagen=pygame.image.load("assets_menu/Opciones Rect.png"), pos=(640, 400),
                               texto_entrada="OPCIONES", fuente=obtener_fuente(75), color_base="orange",
                               color_flotante="red")
        boton_salir = Boton(imagen=pygame.image.load("assets_menu/Salir Rect.png"), pos=(640, 550),
                            texto_entrada="SALIR", fuente=obtener_fuente(75), color_base="grey", color_flotante="red")

        pantalla.blit(menu_texto, menu_rect)

        for boton in [boton_jugar, boton_opciones, boton_salir]:
            boton.cambiar_color(menu_raton_pos)
            boton.actualizar(pantalla)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.verificar_entrada(menu_raton_pos):
                    jugar()
                if boton_opciones.verificar_entrada(menu_raton_pos):
                    opciones()
                if boton_salir.verificar_entrada(menu_raton_pos):
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


pantalla_principal()
