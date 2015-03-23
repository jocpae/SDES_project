import matplotlib.pyplot as plt
import numpy as np
import pygame
import math as mat


#class board():
#	data # saves the state of the board
#	row_num
#	col_num 
#	color
#	
#	player1
#	player2
#
#	mode # mode can be either human with human or human with the computer
#	
#	def check_winner(self):
#		# check if any condition of winning is satisfying or not
#		print "In the check winner"
class button():
	def __init__(self, cx, cy, h, l, label):
		self.cx = cx
		self.cy = cy
		self.h = h
		self.l = l
		self.label = label
	
	def draw(self):
		pygame.draw.rect(screen, WHITE, [self.cx-self.l/2, self.cy-self.h/2 , self.l , self.h ])
		label_text = font_big.render(self.label , True , BLACK)
		screen.blit(label_text, [self.cx-15, self.cy-10])
	
	def is_clicked(self, m_pos):
		if m_pos[0] > self.cx-self.l/2 and m_pos[0] < self.cx+self.l/2 and m_pos[1]>self.cy-self.h/2 and m_pos[1]<self.cy+self.h/2:
			print "clicked"
			flag = 1
		else:
			flag = 0
		return flag
		
	
def default_canvas():
	screen.fill(GREY)
	
	
	for i in range(num_col+1):
		# draw horizontal lines
		pygame.draw.line(screen, BLACK, [0, w_height/num_rows+i*w_height/num_rows], [w_length , w_height/num_rows+i*w_height/num_rows], 2)
	for i in range(num_rows+1):
		# draw vertical lines
		pygame.draw.line(screen, BLACK, [ w_length/num_col + i* w_length/num_col, 0], [ w_length/num_col +i * w_length/num_col, w_height], 2)

	pygame.draw.rect(screen, BLACK, [0, w_height-w_height/num_rows, w_length, w_height]) # The top panel
	reset_button.draw()
	if disks!=[]:
		for d in disks:
			cd_x = (d[0]+0.5)*w_height/num_rows
			cd_y = (d[1]+0.5)* w_length/num_col
			pygame.draw.circle(screen, BLACK, [cd_x, cd_y],15)

		
#		
#def make_matrix_to_check(disks):
#	
#	
#	
#	
#def check_winner(m):
#	
	
	
	
	
	
# Initialize the game engine
pygame.init()
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
GREY =  	(205,201, 201)
PEACH =  	(255, 218, 185)
pi = mat.pi

num_col = 12
num_rows = 10

w_length = 400
w_height = 400
size = [w_length, w_height]
done = False
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font_big = pygame.font.SysFont('Calibri', 20, True, False)
reset_button = button(w_length/2, w_height- 0.5*w_height/num_rows, 20, 60, "Reset")

disks = []

while not done:
	# This limits the while loop to a max of 10 times per second.
	clock.tick(10)
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done=True # Flag that we are done so we exit this loop
		elif event.type == pygame.KEYDOWN:
			print("User pressed a key.")
		elif event.type == pygame.KEYUP:
			print("User let go of a key.")
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# check if the reset button is clicked
			mouse_pos = pygame.mouse.get_pos()
			flag = reset_button.is_clicked(pygame.mouse.get_pos() )
			if flag ==0:
				print "use have not clicked on the reset button clicked at",mouse_pos 
				if mouse_pos[1]>w_height-0.5*w_height/num_rows:
					# clicked on the empy space
					print "clicked on empty space"
					pass
				else:
					# Clicked on the road, get the indexes of the square and make the impression
					i = mouse_pos[0]*num_col/w_length
					j = mouse_pos[1]*num_rows/w_height+1
					if [i, j] in disks:
						print i , j
						pass
					else:
						print i , j
						disks.append([i, j])
					
#				 reset the game
			print disks
			# check if any of the box is clicked
			
			
			print("User pressed a mouse button")
			print 
#	m = make_matrix_to_check(disks)
#	winner = check_winner(m)
	default_canvas()
	pygame.display.flip()
	#print discrete_pts
# Be IDLE friendly
pygame.quit()	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


