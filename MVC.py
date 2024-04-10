import pygame
import sys

class Model:
    def __init__(self):
        pass  # Add initialization logic here if needed

class View:
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

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view



if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.run()
