import pygame #importar e instalar pygame
import os
from pygame import mixer #reproductor de música
pygame.init()#iniciar el juego


screen = pygame.display.set_mode((900, 600)) #pantalla de inicio
pygame.display.set_caption ("Music Box")#titulo
estado_menu = "principal"
font = pygame.font.Font("freesansbold.ttf", 24)

#colores

#cargar archivo de imagen
MissMysterious_imagen= pygame.image.load(os.path.join("MusicBox", "MissMysterious.jpeg"))
BadLiar_imagen= pygame.image.load(os.path.join("MusicBox", "BadLiar.jpeg"))
TheScientist_imagen= pygame.image.load(os.path.join("MusicBox", "TheScientist.jpeg"))
MyUniverse_imagen= pygame.image.load(os.path.join("MusicBox", "MyUniverse.jpeg"))


class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (160, 40))
    def draw(self):
        pygame.draw.rect(screen, "light gray", self.button, 0, 5)
        pygame.draw.rect(screen, "dark gray", self.button, 3, 5)
        text = font.render(self.text, True, "black")
        screen.blit(text, (self.pos[0] + 15, self.pos[1] + 7))


class Cancion_Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (420, 40))
    def draw(self):
        pygame.draw.rect(screen, "light gray", self.button, 0, 5)
        pygame.draw.rect(screen, "dark gray", self.button, 3, 5)
        text = font.render(self.text, True, "black")
        screen.blit(text, (self.pos[0] + 15, self.pos[1] + 7))       

#despliegue de botones 
def menu():
    canciones_boton.draw()
    ayuda_boton.draw()
    salir_boton.draw() 
    return
                
#botones
canciones_boton = Button("Canciones", (10, 10))
ayuda_boton= Button("Ayuda", (190, 10))
salir_boton= Button("Salir", (720, 10))
volverMenu_boton= Button("Volver", (10,500))
regresarCanciones_boton= Button ("Regresar", (330 ,450))
MissMysterious= Cancion_Button("Miss Mysterious - Set It Off", (10,100))
TheScientist= Cancion_Button("The Scientist - Coldplay", (10,150))
BadLiar= Cancion_Button("Bad Liar - Imagine Dragons", (10,200))
MyUniverse= Cancion_Button("My Universe - Coldplay (feat. BTS)", (10,250))
reproducir= Button("Reproducir", (330, 400))
pausa= Button("pausa", (400, 800))

#loop
run = True

while run: #pantalla se abre y se mantiene
    screen.fill("light blue")
    if  estado_menu == "principal":
        menu()       
    if canciones_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "lista"
    if volverMenu_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "principal"
    if estado_menu == "instrucciones":###ventana con instrucciones con saltos
        screen.fill(pygame.Color("white"))
        volverMenu_boton.draw()
        texto ="Guia de uso\n1. Para desplegar la lista de canciones, da click sobre el boton "
        def render_multi_line(text, x, y, fsize):
            lines = text.splitlines()
            for i, l in enumerate(lines):
                font = pygame.font.SysFont('freesansbold.ttf', fsize)
                screen.blit(font.render(l, 0, 0), (x, y + fsize*i))
        texto ="Guia de uso\n1. Para desplegar la lista de canciones, da click sobre el boton ""Canciones""\n2. Para reproducir tu canción favorita, da click sobre el nombre de la canción. Ingresa la cantidad de veces\n que la quieres reproducir y da clic en ""Reproducir"""
        render_multi_line(texto, 10, 10, 24)
        pygame.display.update()
    if estado_menu == "lista": #abre la lista de canciones
        menu()
        MissMysterious.draw()
        TheScientist.draw()
        BadLiar.draw()
        MyUniverse.draw()
        volverMenu_boton.draw()
    if volverMenu_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "principal"
    if ayuda_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "instrucciones"
    
    #canciones disponibles
    if MissMysterious.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "missSelect"
    if estado_menu == "missSelect":
        screen.fill((133, 180, 181))
        MissMysterious_imagen = pygame.transform.scale(MissMysterious_imagen, (300, 300))
        screen.blit(MissMysterious_imagen, (520, 150))
        reproducir.draw()
        if reproducir.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            MissMysterious_imagen= pygame.image.load(os.path.join("MusicBox", "MissMysterious.jpeg"))
            MissMysterious_cancion= pygame.mixer.music.load(os.path.join("MusicBox","MissMysterious.mp3"))
            MissMysterious_volumen= pygame.mixer.music.set_volume(0.5)
            MissMysterious_reproducir = pygame.mixer.music.play (1)
        menu()
        regresarCanciones_boton.draw()
    if regresarCanciones_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "lista"

            
    if BadLiar.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "liarSelect"
    if estado_menu == "liarSelect":
        screen.fill((109, 196, 189))
        BadLiar_imagen = pygame.transform.scale(BadLiar_imagen, (300, 300))
        screen.blit(BadLiar_imagen, (520, 150))
        reproducir.draw()
        if reproducir.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            BadLiar_cancion= pygame.mixer.music.load(os.path.join("MusicBox","BadLiar.mp3"))
            BadLiar_volumen= pygame.mixer.music.set_volume(0.5)
            BadLiar_reproducir = pygame.mixer.music.play (1)                
        menu()
        regresarCanciones_boton.draw()
    if regresarCanciones_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "lista"

    if TheScientist.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "scienSelect"
    if estado_menu == "scienSelect":
        screen.fill((217, 231, 244))
        TheScientist_imagen = pygame.transform.scale(TheScientist_imagen, (300, 300))
        screen.blit(TheScientist_imagen, (520, 150))
        reproducir.draw()
        if reproducir.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            TheScientist_cancion= pygame.mixer.music.load(os.path.join("MusicBox","TheScientist.mp3"))
            TheScientist_volumen= pygame.mixer.music.set_volume(0.5)
            TheScientist_reproducir = pygame.mixer.music.play (1)
        menu()
        regresarCanciones_boton.draw()
    if regresarCanciones_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            estado_menu = "lista"

                
    if MyUniverse.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "univSelect"
    if estado_menu == "univSelect":
        screen.fill((116, 201, 232))
        MyUniverse_imagen = pygame.transform.scale(MyUniverse_imagen, (300, 300))
        screen.blit(MyUniverse_imagen, (520, 150))
        reproducir.draw()
        menu()
        if reproducir.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            MyUniverse_cancion= pygame.mixer.music.load(os.path.join("MusicBox","MyUniverse.mp3"))
            MyUniverse_volumen= pygame.mixer.music.set_volume(0.5)
            MyUniverse_reproducir = pygame.mixer.music.play (1)
            
        regresarCanciones_boton.draw()
    if regresarCanciones_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            estado_menu = "lista"

            

            
    if salir_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        run = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()
  
