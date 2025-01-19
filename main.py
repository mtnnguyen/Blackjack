import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (80, 73, 73)
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("BLACKJACK!")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Images and sounds
intro_Clover = pygame.image.load("blackredclover.png").convert()
intro_Clover.set_colorkey(WHITE)
background_image = pygame.image.load("blackjack.png").convert()
introduction_image = pygame.image.load("introduction.png").convert()
card_image = pygame.image.load("card.png").convert()
cardA = pygame.image.load("A.png").convert()
card2 = pygame.image.load("2.png").convert()
card3 = pygame.image.load("3.png").convert()
card4 = pygame.image.load("4.png").convert()
card5 = pygame.image.load("5.png").convert()
card6 = pygame.image.load("6.png").convert()
card7 = pygame.image.load("7.png").convert()
card8 = pygame.image.load("8.png").convert()
card9 = pygame.image.load("9.png").convert()
card10 = pygame.image.load("10.png").convert()
cardK = pygame.image.load("king.png").convert()
cardQ = pygame.image.load("queen.png").convert()
cardJ = pygame.image.load("jack.png").convert()
instruction_image = pygame.image.load("howto.png").convert()
instruction_image.set_colorkey(BLACK)
card_sound = pygame.mixer.Sound("shuffle.wav")
theme_sound = pygame.mixer.Sound("theme.wav")
theme_sound.play()

# Defining a function that determines the card image
def printcard(card):
  cards = [cardA, card2, card3, card4, card5, card6, card7, card8, card9, card10, cardJ, cardQ, cardK]
  return cards[card]

# Making a list of all possible cards in Blackjack
my_Cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Defining a function that determines the card value
def calculate_score(card,score): 
  if card == 0 and score <= 21:
    return 11 # The A card becomes 11 points 
  elif card == 0 and score+11 > 21:
    return 1 # The A card becomes 1 point
  elif card in [9, 10, 11, 12]:
    return 10 # The jack, queen, and king become 10 points
  else:
    return card + 1 # The rest become their int value + 1
      
# Determines player's score and card image
pscore = 0
p_ace = 0
pscorelist = []
p_imagelist = []
while pscore <= 21:
  pcard = random.randrange(len(my_Cards))
  p_imagelist.append(printcard(pcard))
  if pcard == 0:
    p_ace = p_ace + 1
  pscore = pscore + calculate_score(pcard,pscore)
  if pscore > 21 and p_ace > 0:
    pscore = pscore - 10
    p_ace = p_ace - 1
  pscorelist.append(pscore)
  
# Determines dealer's score and card image
dscore = 0
dscoretem = 0
d_ace = 0
dscorelist = []
d_imagelist = []
while dscoretem <= 21:
  dcard = random.randrange(len(my_Cards))
  if dcard == 0:
    d_ace = d_ace + 1
  dscoretem = dscoretem + calculate_score(dcard,dscoretem)
  if dscoretem > 21 and d_ace > 0:
    dscoretem = dscoretem - 10
    d_ace = d_ace - 1
  if dscoretem < 22 and dscore < 17:
    dscore = dscoretem
    dscorelist.append(dscore)
    d_imagelist.append(printcard(dcard))
  if dscoretem > 21 and dscore < 17:
    dscore = dscoretem
    dscorelist.append(dscore)
    d_imagelist.append(printcard(dcard))
    
# Initial value of dealer score, player score, hit number, cards, wins,
# loses, and draws
p_total = pscorelist[1]
d_total = dscorelist[0]
hit_Num = 0

# Boolean values for the introduction
introduction = True
instructions = False
# Boolean values for the actual game
play_Game = False
hit_or_stand = False
hit = False
hit1 = False
hit2 = False
hit3 = False
hit4 = False
hit5 = False
stand = False
# Boolean values for the end of the game
game_Over = False
won_Game = False
lost_Game = False
drew_Game = False
main_menu = False

# Text font
font = pygame.font.SysFont('Century', 30, True, False)
# Rendered text
play_Text = font.render("PLAY",True,RED)
instruction_Text = font.render("HOW TO PLAY",True,RED)
exit_Text = font.render("EXIT",True,RED)
dealer_Text = font.render("DEALER: ",True,RED)
user_Text = font.render("YOUR CARDS: ",True,RED)
hit_Text = font.render("HIT ME",True,RED)
stand_Text = font.render("STAND",True,RED)
win_Text = font.render("YOU WON!",True,RED)
lose_Text = font.render("YOU LOST!",True,RED)
draw_Text = font.render("YOU DREW!",True,RED)
menu_Text = font.render("MAIN MENU",True,RED)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        if event.type == pygame.MOUSEBUTTONDOWN: # Used when player presses button with left click
          mouse_Position = pygame.mouse.get_pos()
          x_mouse = mouse_Position[0]
          y_mouse = mouse_Position[1]
          
          if introduction: # User clicks to play or to read instructions
            if x_mouse >= 245 and x_mouse <= 420 and y_mouse >= 285 and y_mouse <= 335: 
              introduction = False
              play_Game = True
              hit_or_stand = True
            if x_mouse >= 245 and x_mouse <= 420 and y_mouse >= 336 and y_mouse <= 385:
              instructions = True
              introduction = False
              
          if instructions: # User clicks to exit the instructions
            if x_mouse >= 245 and x_mouse <= 345 and y_mouse >= 450 and y_mouse <= 485:
              introduction = True
              instructions = False

          if play_Game: # User clicks the "hit me", "stand", or "main menu"
            if x_mouse >= 375 and x_mouse <= 500 and y_mouse >= 215 and y_mouse <= 265:
              stand = True
              card_sound.play()
            elif x_mouse >= 175 and x_mouse <= 300 and y_mouse >= 215 and y_mouse <= 265:
              card_sound.play()
              p_total = pscorelist[hit_Num + 2]
              if not hit:
                hit = True
              elif hit and not hit1:
                hit1 = True
              elif hit1 and not hit2:
                hit2 = True
              elif hit2 and not hit3:
                hit3 = True
              elif hit3 and not hit4:
                hit4 = True
              elif hit4 and not hit5:
                hit5 = True
              hit_Num = hit_Num + 1
            if x_mouse >= 535 and x_mouse <= 660 and y_mouse >= 440 and y_mouse <= 490:
              main_menu = True 
              
    # --- Game logic    
              
    if p_total > 21 or stand: # Game is over when cards over 21 or stands
      game_Over = True 
      hit_or_stand = False
      
    if game_Over: # Determines dealer's score and if player won, lost, or drew
      hit_or_stand = False
      d_total = dscorelist[-2]
      if d_total < 17:
        d_total = dscorelist[-1]
      if p_total > d_total and p_total <= 21 and d_total < 21:
        won_Game = True
      elif d_total > 21 and p_total <= 21:
        won_Game = True
      elif p_total > 21:
        lost_Game = True
      elif d_total > p_total and d_total <= 21 and p_total <= 21:
        lost_Game = True
      elif d_total == p_total and p_total <= 21 and d_total <= 21:
        drew_Game = True

    if main_menu: # User goes back to the very beginning (Resets)
      pscore = 0
      p_ace = 0
      pscorelist = []
      p_imagelist = []
      while pscore <= 21:
        pcard = random.randrange(len(my_Cards))
        p_imagelist.append(printcard(pcard))
        if pcard == 0:
          p_ace = p_ace + 1
        pscore = pscore + calculate_score(pcard,pscore)
        if pscore > 21 and p_ace > 0:
          pscore = pscore - 10
          p_ace = p_ace - 1
        pscorelist.append(pscore)
      dscore = 0
      dscoretem = 0
      d_ace = 0
      dscorelist = []
      d_imagelist = []
      while dscoretem <= 21:
        dcard = random.randrange(len(my_Cards))
        if dcard == 0:
          d_ace = d_ace + 1
        dscoretem = dscoretem + calculate_score(dcard,dscoretem)
        if dscoretem > 21 and d_ace > 0:
          dscoretem = dscoretem - 10
          d_ace = d_ace - 1
        if dscoretem < 22 and dscore < 17:
          dscore = dscoretem
          dscorelist.append(dscore)
          d_imagelist.append(printcard(dcard))
        if dscoretem > 21 and dscore < 17:
          dscore = dscoretem
          dscorelist.append(dscore)
          d_imagelist.append(printcard(dcard))
      p_total = pscorelist[1]
      d_total = dscorelist[0]
      hit_Num = 0
      introduction = True
      instructions = False
      play_Game = False
      hit_or_stand = False
      hit = False
      hit1 = False
      hit2 = False
      hit3 = False
      hit4 = False
      hit5 = False
      stand = False
      game_Over = False
      won_Game = False
      lost_Game = False
      drew_Game = False
      main_menu = False
      
    # Buttons become grey when user mouse position hovers over a button          
    hover_Position = pygame.mouse.get_pos()
    x_hover = hover_Position[0]
    y_hover = hover_Position[1]
  
    # Background image
    screen.blit(background_image, [0, 0])
    # --- Drawing code should go here
  
    if introduction: # Every image/text in the introduction
      screen.blit(introduction_image, [0,0])
      pygame.draw.ellipse(screen, BLACK, [40,75,600,350], 0)
      screen.blit(intro_Clover, [95, 200])
      if x_hover >= 245 and x_hover <= 420 and y_hover >= 285 and y_hover <= 335: 
        pygame.draw.rect(screen, GREY, [245,285,175,50])
      if x_hover >= 245 and x_hover <= 420 and y_hover >= 336 and y_hover <= 385:
        pygame.draw.rect(screen, GREY, [245,336,175,50])
      screen.blit(play_Text, [300,300])
      screen.blit(instruction_Text, [250,350])
      
    if instructions: # Every image/text in the instructions
      screen.blit(instruction_image, [10,50])
      pygame.draw.rect(screen, BLACK, [245,450,100,35])
      if x_hover >= 245 and x_hover <= 345 and y_hover >= 450 and y_hover <= 485:
        pygame.draw.rect(screen, GREY, [245,450,100,35])
      screen.blit(exit_Text,[265,460])

    if play_Game: # Every image/text in the actual game
      screen.blit(dealer_Text, [150,75])
      screen.blit(user_Text, [125,350])
      screen.blit(p_imagelist[0], [300,350])
      screen.blit(p_imagelist[1], [330,350])
      screen.blit(card_image, [330,75])
      screen.blit(d_imagelist[0], [300,75])
      pscore_Text = font.render("Score: " + str(p_total),True,RED)
      screen.blit(pscore_Text, [300, 450])
      dscore_Text = font.render("Score: " + str(d_total),True,RED)
      screen.blit(dscore_Text, [150, 115]) 
      pygame.draw.rect(screen,BLACK,[535,440,150,50],0)
      if x_hover >= 535 and x_hover <= 660 and y_hover >= 440 and y_hover <= 490:
        pygame.draw.rect(screen, GREY, [535,440,150,50])
      screen.blit(menu_Text, [540,455])
      if hit: # Every image when user clicks
        screen.blit(p_imagelist[2], [360,350])
        if hit1: 
          screen.blit(p_imagelist[3], [390,350])
          if hit2: 
            screen.blit(p_imagelist[4], [420,350])
            if hit3:
              screen.blit(p_imagelist[5], [450,350])
              if hit4:
                screen.blit(p_imagelist[6], [480,350])
                if hit5:
                  screen.blit(p_imagelist[7], [510,350])
      
      
    if hit_or_stand: # Every image/text for the stand or hit option
      pygame.draw.rect(screen,BLACK,[175,215,125,50],0)
      pygame.draw.rect(screen,BLACK,[375,215,125,50],0)
      if x_hover >= 375 and x_hover <= 500 and y_hover >= 215 and y_hover <= 265:
        pygame.draw.rect(screen, GREY, [375,215,125,50])
      if x_hover >= 175 and x_hover <= 300 and y_hover >= 215 and y_hover <= 265:
        pygame.draw.rect(screen, GREY, [175,215,125,50])
      screen.blit(hit_Text, [195, 230])
      screen.blit(stand_Text, [395, 230])
                
    if game_Over: # Every image/text when game finishes
      hitostand_Game = False
      for i in range(len(d_imagelist)-1):
          screen.blit(d_imagelist[i+1],[330+30*i,75])
      if won_Game:
        screen.blit(win_Text,[265,230])
      if lost_Game:
        screen.blit(lose_Text,[265,230])
      if drew_Game:
        screen.blit(draw_Text,[265,230])

    # --- Reset when user presses "main menu" or "play again"
      
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()