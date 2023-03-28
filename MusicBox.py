import pygame #importar e instalar pygame
from pygame import mixer #reproductor de música
pygame.init()#iniciar el juego


screen = pygame.display.set_mode((900, 600)) #pantalla de inicio
pygame.display.set_caption ("Music Box")#titulo
fps = 60
timer = pygame.time.Clock()
estado_menu = "principal"
font = pygame.font.Font("freesansbold.ttf", 24)

#cargar archivo de imagen
def cargar_imagen(imagen, escala=1):
    imagen = pygame.image.load(imagen)
    imagen = pygame.transform.scale(imagen, (300, 300))
    screen.blit(imagen, (520, 150))
    return imagen

#cargar archivo de sonido
def cargar_sonido(cancion):
    pygame.mixer.init()
    cancion = pygame.mixer.music.load(cancion)
    pygame.mixer.music.set_volume(0.5)
    cancion = pygame.mixer.music.play (1) #remember to change to n+1 cuz esto define cuanto se loopea
    return cancion

class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (160, 40))
        self.clicked = False
    def draw(self):
        pygame.draw.rect(screen, "light gray", self.button, 0, 5)
        pygame.draw.rect(screen, "dark gray", self.button, 3, 5)
        text = font.render(self.text, True, "black")
        screen.blit(text, (self.pos[0] + 15, self.pos[1] + 7))        
    def verificar_click(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
           self.clicked = True
        else:
           self.clicked = False

#despliegue de botones 
def menu():
    canciones_boton.draw()
    ayuda_boton.draw()
    salir_boton.draw()
    if estado_menu != "principal":
        if estado_menu != "instrucciones":
            MissMysterious.draw()
            TheScientist.draw()
            BadLiar.draw()
            MyUniverse.draw()  
    return
                
#botones
canciones_boton = Button("Canciones", (10, 10))
ayuda_boton= Button("Ayuda", (190, 10))
salir_boton= Button("Salir", (720, 10))
volverMenu_boton= Button("Volver", (230,450))
volverCanciones_boton= Button ("Volver", (230 ,450))
MissMysterious= Button("Miss Mysterious - Set It Off", (10,100))
TheScientist= Button("The Scientist - Coldplay", (10,150))
BadLiar= Button("Bad Liar - Imagine Dragons", (10,200))
MyUniverse= Button("My Universe - Coldplay (feat. BTS)", (10,250))
reproducir= Button("repro", (400, 400))
pausa= Button("pausa", (400, 800))

#loop
run = True

while run: #pantalla se abre y se mantiene
    screen.fill("light blue")
    timer.tick(fps)
    if  estado_menu == "principal":
        menu()
        
    if canciones_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "lista"
    if estado_menu == "instrucciones": #despliega ayuda para el usuario
        menu()
        volverMenu_boton.draw()
        instrucciones = pygame.draw.rect(screen, "purple", [220, 100, 200, 200], 0) #se despliega cuadro de instrucciones
        fuente = pygame.font.Font("freesansbold.ttf", 24)
        texto = fuente.render("Guia de uso", True, "Black")
        screen.blit(texto,(220,100))
        if volverMenu_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            estado_menu = "principal"
    if estado_menu == "lista": #abre la lista de canciones
        menu()
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
        cargar_imagen("MissMysterious.jpeg", 1)
        reproducir.draw()
        menu()
        volverCanciones_boton.draw()
        if volverCanciones_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            estado_menu = "lista"
        if reproducir.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                cargar_sonido("MissMysterious.mp3")
            
    if BadLiar.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "liarSelect"
    if estado_menu == "liarSelect":
        screen.fill((109, 196, 189))
        cargar_imagen("BadLiar.jpeg", 1)
        reproducir.draw()
        menu()
        volverCanciones_boton.draw()
        if volverCanciones_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            estado_menu = "lista"
        if reproducir.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                cargar_sonido("BadLiar.mp3")
                
    if TheScientist.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "scienSelect"
    if estado_menu == "scienSelect":
        screen.fill((217, 231, 244))
        cargar_imagen("TheScientist.jpeg", 1)
        reproducir.draw()
        menu()
        volverCanciones_boton.draw()
        if volverCanciones_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            estado_menu = "lista"
        if reproducir.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                cargar_sonido("TheScientist.mp3")
                
    if MyUniverse.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        estado_menu = "univSelect"
    if estado_menu == "univSelect":
        screen.fill((116, 201, 232))
        cargar_imagen("MyUniverse.jpeg", 1)
        reproducir.draw()
        menu()
        volverCanciones_boton.draw()
        if volverCanciones_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            estado_menu = "lista"
        if reproducir.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            cargar_sonido("MyUniverse.mp3")
            
            

            
    if salir_boton.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        run = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()
  
