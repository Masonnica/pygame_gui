import pygame, threading

import document, style, script
import storage

def __init__(title: str, logo: pygame.Surface, mode_display: str = 'resizable', size: tuple[int, int] = (0,0)):
	pygame.init()
	pygame.display.set_caption(title)
	pygame.display.set_icon(logo)
	
	mode_display = mode_display.lower()
	if mode_display == 'resizable':
		pygame.display.set_mode(size, pygame.RESIZABLE)
	elif mode_display == 'fullscreen':
		pygame.display.set_mode(size, pygame.FULLSCREEN)
	elif mode_display == 'noframe':
		pygame.display.set_mode(size, pygame.NOFRAME)
	else:
		pygame.display.set_mode(size, pygame.SHOWN)
	return None
