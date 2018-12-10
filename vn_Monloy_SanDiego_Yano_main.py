#The Obscured: A Visual Novel

import pygame, sys

game_display = pygame.display.set_mode((1280, 720))
def game_init():
    """
    Initializes the game.
    Key press: Spacebar - starts the game
    """
    pygame.mixer.pre_init(44100,16,2,40996)
    pygame.init()
    pygame.mixer.music.load('Dark Piano - Null.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    pygame.display.set_caption('The Obscured')

    pygame.display.set_icon(pygame.image.load('icon.png'))

    bg = ['main_menu.png']
    run = True
    while run:
        game_display.blit(pygame.image.load(bg[0]),(0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fade(bg)
                    run = False
def new_game():
    """
    Stores the all images in a nested list.
    Updates the number of purchased items, states of all the items, score, chosen paths.
    Calls ending function after all information was collected.
    """
    ending, purchased_items, score = '', 0, 0
    item1, item2, item3 = False, False, False
    main = [
            ['MainSceneOne_1.jpg','MainSceneOne_2.jpg','MainSceneOne_3.jpg','MainSceneOne_4.jpg','MainSceneOne_5.jpg','MainSceneOne_6.jpg','MainSceneOne_7.jpg','DecisionSceneOne_1.jpg','DecisionSceneOne_2.jpg','DecisionSceneOne_3.jpg','DecisionSceneOne_4.jpg','DecisionSceneOne_5.jpg','DecisionSceneOne_6.jpg','DecisionSceneOne_7.jpg'],
            ['MainSceneTwo_1.jpg','MainSceneTwo_2.jpg','MainSceneTwo_3.jpg','MainSceneTwo_4.jpg','DecisionSceneTwo_1.jpg','DecisionSceneTwo_2.jpg','DecisionSceneTwo_3.jpg'],
            ['MainSceneThree_1.jpg','MainSceneThree_2.jpg','MainSceneThree_3.jpg','DecisionSceneThree_1.jpg','DecisionSceneThree_2.jpg'],
            ['MainSceneFour_1.jpg','MainSceneFour_2.jpg','MainSceneFour_3.jpg','MainSceneFour_4.jpg','DecisionSceneFour_1.jpg','DecisionSceneFour_2.jpg','DecisionSceneFour_3.jpg'],
            ['MainSceneFive_1.jpg','MainSceneFive_2.jpg','MainSceneFive_3.jpg','MainSceneFive_4.jpg','DecisionSceneFive_1.jpg','DecisionSceneFive_2.jpg','DecisionSceneFive_3.jpg'],
            ['MainSceneSix_1.jpg','MainSceneSix_2.jpg','MainSceneSix_3.jpg','DecisionSceneSix_1.jpg','DecisionSceneSix_2.jpg'],
            ['MainSceneSeven_1.jpg','MainSceneSeven_2.jpg','MainSceneSeven_3.jpg','DecisionSceneSeven_1.jpg','DecisionSceneSeven_2.jpg'],
            ['MainSceneEight_1.jpg','MainSceneEight_2.jpg','MainSceneEight_3.jpg','DecisionSceneEight_1.jpg','DecisionSceneEight_2.jpg'],
            ['MainSceneNine_1.jpg','MainSceneNine_2.jpg','MainSceneNine_3.jpg','DecisionSceneNine_1.jpg','DecisionSceneNine_2.jpg','DecisionSceneNine_3.jpg']
            ]
    dec = ['DecisionSceneOne_8.jpg','DecisionSceneTwo_4.jpg','DecisionSceneThree_3.jpg','DecisionSceneFour_4.jpg','DecisionSceneFive_4.jpg','DecisionSceneSix_3.jpg','DecisionSceneSeven_3.jpg','DecisionSceneEight_3.jpg','DecisionSceneNine_4.jpg']
    dec_a = [
            ['DecisionSceneOne-A_1.jpg','DecisionSceneOne-A_2.jpg','DecisionSceneOne-A_3.jpg','DecisionSceneOne-A_4.jpg','DecisionSceneOne-A_5.jpg','DecisionSceneOne-A_6.jpg'],
            ['DecisionSceneTwo-A_1.jpg','DecisionSceneTwo-A_2.jpg','DecisionSceneTwo-A_3.jpg','DecisionSceneTwo-A_4.jpg','DecisionSceneTwo-A_5.jpg','DecisionSceneTwo-A_6.jpg','DecisionSceneTwo-A_7.jpg'],
            ['DecisionSceneThree-A_1.jpg','DecisionSceneThree-A_2.jpg','DecisionSceneThree-A_3.jpg','DecisionSceneThree-A_4.jpg'],
            ['DecisionSceneFour-A_1.jpg','DecisionSceneFour-A_2.jpg','DecisionSceneFour-A_3.jpg','DecisionSceneFour-A_4.jpg','DecisionSceneFour-A_5.jpg','DecisionSceneFour-A_6.jpg'],
            ['DecisionSceneFiveA_1.jpg','DecisionSceneFiveA_2.jpg','DecisionSceneFiveA_3.jpg','DecisionSceneFiveA_4.jpg'],
            ['DecisionSceneSix-A_1.jpg','DecisionSceneSix-A_2.jpg','DecisionSceneSix-A_3.jpg','DecisionSceneSix-A_4.jpg','DecisionSceneSix-A_5.jpg','DecisionSceneSix-A_6.jpg'],
            ['DecisionSceneSeven-A_1.jpg','DecisionSceneSeven-A_2.jpg','DecisionSceneSeven-A_3.jpg','DecisionSceneSeven-A_4.jpg','DecisionSceneSeven-A_5.jpg'],
            ['DecisionSceneEight-A_1.jpg','DecisionSceneEight-A_2.jpg','DecisionSceneEight-A_3.jpg','DecisionSceneEight-A_4.jpg','DecisionSceneEight-A_5.jpg'],
            ['DecisionSceneNine-A_1.jpg','DecisionSceneNine-A_2.jpg','DecisionSceneNine-A_3.jpg','DecisionSceneNine-A_4.jpg','DecisionSceneNine-A_5.jpg','DecisionSceneNine-A_6.jpg','DecisionSceneNine-A_7.jpg','DecisionSceneNine-A_8.jpg']
            ]
    dec_b = [
            ['DecisionSceneOne-B_1.jpg','DecisionSceneOne-B_2.jpg','DecisionSceneOne-B_3.jpg','DecisionSceneOne-B_4.jpg','DecisionSceneOne-B_5.jpg'],
            ['DecisionSceneTwo-B_1.jpg','DecisionSceneTwo-B_2.jpg','DecisionSceneTwo-B_3.jpg','DecisionSceneTwo-B_4.jpg'],
            ['DecisionSceneThree-B_1.jpg','DecisionSceneThree-B_2.jpg','DecisionSceneThree-B_3.jpg','DecisionSceneThree-B_4.jpg','DecisionSceneThree-B_5.jpg','DecisionSceneThree-B_6.jpg','DecisionSceneThree-B_7.jpg'],
            ['DecisionSceneFour-B_1.jpg','DecisionSceneFour-B_2.jpg','DecisionSceneFour-B_3.jpg'],
            ['DecisionSceneFiveB_1.jpg','DecisionSceneFiveB_2.jpg','DecisionSceneFiveB_3.jpg'],
            ['DecisionSceneSix-B_1.jpg','DecisionSceneSix-B_2.jpg','DecisionSceneSix-B_3.jpg','DecisionSceneSix-B_4.jpg','DecisionSceneSix-B_5.jpg'],
            ['DecisionSceneSeven-B_1.jpg','DecisionSceneSeven-B_2.jpg','DecisionSceneSeven-B_3.jpg','DecisionSceneSeven-B_4.jpg','DecisionSceneSeven-B_5.jpg','DecisionSceneSeven-B_6.jpg','DecisionSceneSeven-B_7.jpg','DecisionSceneSeven-B_8.jpg'],
            ['DecisionSceneEight-B_1.jpg','DecisionSceneEight-B_2.jpg','DecisionSceneEight-B_3.jpg','DecisionSceneEight-B_4.jpg','DecisionSceneEight-B_5.jpg','DecisionSceneEight-B_6.jpg','DecisionSceneEight-B_7.jpg'],
            ['DecisionSceneNine-B_1.jpg','DecisionSceneNine-B_2.jpg','DecisionSceneNine-B_3.jpg','DecisionSceneNine-B_4.jpg']]
    
    purchased_items, item1, item2, item3, score, ending = main_scene(purchased_items, item1, item2, item3, score, ending, main[0], dec[0], dec_a[0], dec_b[0], False, True)
    purchased_items, item1, item2, item3, score, ending = main_scene(purchased_items, item1, item2, item3, score, ending, main[1], dec[1], dec_a[1], dec_b[1], True, False)
    purchased_items, item1, item2, item3, score, ending = main_scene(purchased_items, item1, item2, item3, score, ending, main[2], dec[2], dec_a[2], dec_b[2], False, True)
    purchased_items, item1, item2, item3, score, ending = main_scene(purchased_items, item1, item2, item3, score, ending, main[3], dec[3], dec_a[3], dec_b[3], True, False)
    purchased_items, item1, item2, item3, score, ending = main_scene(purchased_items, item1, item2, item3, score, ending, main[4], dec[4], dec_a[4], dec_b[4], True, False)
    purchased_items, item1, item2, item3, score, ending = main_scene(purchased_items, item1, item2, item3, score, ending, main[5], dec[5], dec_a[5], dec_b[5], True, False)
    purchased_items, item1, item2, item3, score, ending = main_scene(purchased_items, item1, item2, item3, score, ending, main[6], dec[6], dec_a[6], dec_b[6], True, False)
    purchased_items, item1, item2, item3, score, ending = main_scene(purchased_items, item1, item2, item3, score, ending, main[7], dec[7], dec_a[7], dec_b[7], True, False)
    purchased_items, item1, item2, item3, score, ending = main_scene(purchased_items, item1, item2, item3, score, ending, main[8], dec[8], dec_a[8], dec_b[8], True, False)

    #print(purchased_items, item1, item2, item3, score, ending)

    ending_scene(ending, purchased_items)
def main_scene(purchased_items, item1, item2, item3, score, ending, scene, dec, dec_1, dec_2, d1, d2):
    """
    Displays the main scene.
    After the main scene, it calls the "decision_making" function to proceed to the decision scene.
    """
    run = True
    cnt = 0
    game_display.blit(pygame.image.load(scene[cnt]), (0,0))
    text_score = display_text(score)
    game_display.blit(text_score, (51, 23))
    pygame.display.update()
    while run:
        try:
            purchased_items, item1, item2, item3, score, cnt= scene_play_with_store(scene, cnt, purchased_items, item1, item2, item3, score)
        except:
            score, ending = decision_making(score, ending,dec, dec_1, dec_2, d1, d2)
            run = False
    return purchased_items, item1, item2, item3, score, ending
def decision_making(score, ending, dec, dec_1, dec_2, d1, d2):
    """
    Displays the decision scene and the scenes of the chosen path.
    Keeps track of the decision made (which will then be used for determining the ending).
    Adds point (depends on the chosen path) to the player's score. 
    Key presses: 1 - Decision 1; 2 - Decision 2
    """
    run = True
    game_display.blit(pygame.image.load(dec), (0, 0))
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    ending += '1'
                    scene_play_without_store(dec_1)
                    score += scoring(d1)
                    run = False
                if event.key == pygame.K_2:
                    ending += '2'
                    scene_play_without_store(dec_2)
                    score += scoring(d2)
                    run = False
    return score, ending
def ending_scene(end, purchased_items):
    last = ['MainSceneTen_1.jpg','MainSceneTen_2.jpg','MainSceneTen_3.jpg']
    endings = [
                ['EndingOne_1.jpg','EndingOne_2.jpg','EndingOne_3.jpg','EndingOne_4.jpg','EndingOne_5.jpg','EndingOne_6.jpg','EndingOne_7.jpg','EndingOne_8.jpg','EndingOne_9.jpg','EndingOne_10.jpg','EndingOne_11.jpg','EndingOne_12.jpg','EndingOne_13.jpg','EndingOne_14.jpg','EndingOne_15.jpg','EndingOne_16.jpg','EndingOne_17.jpg','EndingOne_18.jpg','EndingOne_19.jpg','EndingOne_20.jpg','EndingOne_21.jpg','EndingOne_22.jpg'],
                ['EndingTwo_1.jpg','EndingTwo_2.jpg','EndingTwo_3.jpg','EndingTwo_4.jpg','EndingTwo_5.jpg','EndingTwo_6.jpg','EndingTwo_7.jpg','EndingTwo_8.jpg','EndingTwo_9.jpg','EndingTwo_10.jpg'],
                ['EndingThree_1.jpg','EndingThree_2.jpg','EndingThree_3.jpg','EndingThree_4.jpg','EndingThree_5.jpg','EndingThree_6.jpg','EndingThree_7.jpg','EndingThree_8.jpg','EndingThree_9.jpg','EndingThree_10.jpg','EndingThree_11.jpg','EndingThree_12.jpg','EndingThree_13.jpg','EndingThree_14.jpg','EndingThree_15.jpg','EndingThree_16.jpg','EndingThree_17.jpg','EndingThree_18.jpg','EndingThree_19.jpg','EndingThree_20.jpg','EndingThree_21.jpg','EndingThree_22.jpg','EndingThree_23.jpg'],
                ['EndingFour_1.jpg','EndingFour_2.jpg','EndingFour_3.jpg','EndingFour_4.jpg','EndingFour_5.jpg','EndingFour_6.jpg','EndingFour_7.jpg','EndingFour_8.jpg','EndingFour_9.jpg','EndingFour_10.jpg','EndingFour_11.jpg','EndingFour_12.jpg','EndingFour_13.jpg','EndingFour_14.jpg','EndingFour_15.jpg','EndingFour_16.jpg','EndingFour_17.jpg','EndingFour_18.jpg','EndingFour_19.jpg','EndingFour_20.jpg'],
                ['EndingFive_1.jpg','EndingFive_2.jpg','EndingFive_3.jpg','EndingFive_4.jpg','EndingFive_5.jpg','EndingFive_6.jpg','EndingFive_7.jpg','EndingFive_8.jpg','EndingFive_9.jpg','EndingFive_10.jpg','EndingFive_11.jpg','EndingFive_12.jpg','EndingFive_13.jpg','EndingFive_14.jpg','EndingFive_15.jpg','EndingFive_16.jpg','EndingFive_17.jpg','EndingFive_18.jpg','EndingFive_19.jpg','EndingFive_20.jpg','EndingFive_21.jpg'],
                ['EndingSix_1.jpg','EndingSix_2.jpg','EndingSix_3.jpg','EndingSix_4.jpg','EndingSix_5.jpg','EndingSix_6.jpg','EndingSix_7.jpg','EndingSix_8.jpg','EndingSix_9.jpg','EndingSix_10.jpg','EndingSix_11.jpg','EndingSix_12.jpg','EndingSix_13.jpg','EndingSix_14.jpg','EndingSix_15.jpg','EndingSix_16.jpg','EndingSix_17.jpg','EndingSix_18.jpg','EndingSix_19.jpg','EndingSix_20.jpg'],
                ['EndingSeven_1.jpg','EndingSeven_2.jpg','EndingSeven_3.jpg','EndingSeven_4.jpg','EndingSeven_5.jpg','EndingSeven_6.jpg','EndingSeven_7.jpg','EndingSeven_8.jpg','EndingSeven_9.jpg','EndingSeven_10.jpg','EndingSeven_11.jpg','EndingSeven_12.jpg','EndingSeven_13.jpg','EndingSeven_14.jpg','EndingSeven_15.jpg','EndingSeven_16.jpg','EndingSeven_17.jpg','EndingSeven_18.jpg','EndingSeven_19.jpg','EndingSeven_20.jpg','EndingSeven_21.jpg','EndingSeven_22.jpg', 'EndingSeven_23.jpg', 'EndingSeven_24.jpg', 'EndingSeven_25.jpg', 'EndingSeven_26.jpg', 'EndingSeven_27.jpg']
            ]
    scene_play_without_store(last)
    if end == '212111221' or end == '212121221':
        if purchased_items == 3:
            scene_play_without_store(endings[6])
        else:
            scene_play_without_store(endings[0])
    elif end == '111112121' or end == '111122121':
        scene_play_without_store(endings[2])
    elif end == '111111221' or end == '111121221':
        scene_play_without_store(endings[3])
    elif end == '211211211' or end == '211221211':
        scene_play_without_store(endings[4])
    elif end == '222212222' or end == '222222222':
        scene_play_without_store(endings[5])
    else:
        scene_play_without_store(endings[1])
def credits():
    """
    Displays the credits page.
    Allows the user to choose to play another game.
    """
    run = True
    game_display.blit(pygame.image.load('CreditsOne.png'), (0, 0))
    pygame.display.update()
    pygame.time.delay(1500)
    game_display.blit(pygame.image.load('CreditsThree.png'), (0, 0))
    pygame.display.update()
    pygame.time.delay(1500)
    while run:
        game_display.blit(pygame.image.load('CreditsFour.png'), (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    new_game()

def scene_play_with_store(scene, cnt, purchased_items, item1, item2, item3, score):
    """
    Displays images of a scene. The store can be accessed in the scenes given to this function.
    Key presses: (1) Right arrow key - next image, (2) S - store, (3) H - help
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                fade(scene,cnt)
                cnt += 1
                game_display.blit(pygame.image.load(scene[cnt]), (0, 0))
                text_score = display_text(score)
                game_display.blit(text_score, (51, 23))
                pygame.display.update()
            if event.key == pygame.K_s:
                purchased_items, item1, item2, item3, score = store(purchased_items, item1, item2, item3, score)
                game_display.blit(pygame.image.load(scene[cnt]), (0, 0))
                text_score = display_text(score)
                game_display.blit(text_score, (51, 23))
                pygame.display.update()
            if event.key == pygame.K_h:
                help()
                game_display.blit(pygame.image.load(scene[cnt]), (0, 0))
                text_score = display_text(score)
                game_display.blit(text_score, (51, 23))
                pygame.display.update()
    return purchased_items, item1, item2, item3, score, cnt
def scene_play_without_store(scene):
    """
    Displays images of a scene. However, the store can't be accessed in the given scene.
    Example scenes: Decision scene, chosen path scene
    """
    cnt = 0
    game_display.blit(pygame.image.load(scene[cnt]), (0, 0))
    pygame.display.update()
    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        fade(scene, cnt)
                        cnt += 1
                        game_display.blit(pygame.image.load(scene[cnt]), (0, 0))
                        pygame.display.update() 
                    if event.key == pygame.K_h:
                        help()
                        game_display.blit(pygame.image.load(scene[cnt]), (0, 0))
                        pygame.display.update()
        except:
            break

def help():
    """
    Displays help guide for the player. The guide includes all the necessary key presses in the game.
    """
    run = True
    while run:
        game_display.blit(pygame.image.load('HelpMenu.png'), (250, 125))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    run = False
def store(purchased_items, item1, item2, item3, score):
    """
    Allows the player to access the store to purchase items.
    Key presses: (1) Q - first item, (2) W - second item, (3) E - third item, (4) Left arrow key - return to previous scene
    """
    store_bg = 'Store(Background).jpg'
    item = [
            ['StoreItemOne.png','StoreItemOneBought.png'],
            ['StoreItemThree.png','StoreItemThreeBought.png'],
            ['StoreItemTwo.png','StoreItemTwoBought.png']
            ]
    scenes = [
            ['StoreSceneOne_1.jpg','StoreSceneOne_2.jpg','StoreSceneOne_3.jpg','StoreSceneOne_4.jpg','StoreSceneOne_5.jpg','StoreSceneOne_6.jpg','StoreSceneOne_7.jpg','StoreSceneOne_8.jpg','StoreSceneOne_9.jpg','StoreSceneOne_10.jpg','StoreSceneOne_11.jpg'], 
            ['StoreSceneTwo_1.jpg','StoreSceneTwo_2.jpg','StoreSceneTwo_3.jpg','StoreSceneTwo_4.jpg','StoreSceneTwo_5.jpg','StoreSceneTwo_6.jpg','StoreSceneTwo_7.jpg','StoreSceneTwo_8.jpg','StoreSceneTwo_9.jpg','StoreSceneTwo_10.jpg','StoreSceneTwo_11.jpg'], 
            ['StoreSceneThree_1.jpg','StoreSceneThree_2.jpg','StoreSceneThree_3.jpg','StoreSceneThree_4.jpg','StoreSceneThree_5.jpg','StoreSceneThree_6.jpg','StoreSceneThree_7.jpg','StoreSceneThree_8.jpg','StoreSceneThree_9.jpg','StoreSceneThree_10.jpg','StoreSceneThree_11.jpg', 'StoreSceneThree_12.jpg', 'StoreSceneThree_13.jpg', 'StoreSceneThree_14.jpg', 'StoreSceneThree_15.jpg', 'StoreSceneThree_16.jpg', 'StoreSceneThree_17.jpg']
            ]
    run = True
    while run:
        game_display.blit(pygame.image.load(store_bg), (0, 0))
        text_score = display_text(score)
        game_display.blit(text_score, (51, 23))
        if not item1:
            game_display.blit(pygame.image.load(item[0][0]), (300, 225))
        else:
            game_display.blit(pygame.image.load(item[0][1]), (300, 225))

        if not item2:
            game_display.blit(pygame.image.load(item[1][0]), (540, 225))
        else:
            game_display.blit(pygame.image.load(item[1][1]), (540, 225))
        
        if not item3:
            game_display.blit(pygame.image.load(item[2][0]), (770, 225))
        else:
            game_display.blit(pygame.image.load(item[2][1]), (770, 225))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    purchased_items, item1, score = buy_items(purchased_items, item1, score, scenes[0], 400)
                if event.key == pygame.K_w:
                    purchased_items, item2, score = buy_items(purchased_items, item2, score, scenes[1], 150)
                if event.key == pygame.K_e:
                    purchased_items, item3, score = buy_items(purchased_items, item3, score, scenes[2], 350)
                if event.key == pygame.K_LEFT:
                    run = False
                
    return purchased_items, item1, item2, item3, score
def buy_items(purchased_items, item, score, scene, price):
    """
    Determines if the chosen item can be purchased or was already purchased.

    """
    if item:
        game_display.blit(pygame.image.load('StoreBought.png'), (310, 150))
        pygame.display.update()
        pygame.time.delay(1500)
    else:
        if score >= price:
            item = True
            score -= price
            purchased_items += 1
            scene_play_without_store(scene)
        else:
            game_display.blit(pygame.image.load('StoreInsufficient.png'), (250, 150))
            pygame.display.update()
            pygame.time.delay(1500)
    return purchased_items, item, score

def fade(scene, cnt = 0):
    """
    Puts a fading transition after each scene by adjusting the opacity of the surface.
    """
    fade = pygame.Surface((1280, 720))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300, 40):
        fade.set_alpha(alpha)
        game_display.blit(pygame.image.load(scene[cnt]), (0, 0))
        game_display.blit(fade, (0, 0))
        pygame.display.update()
def scoring(state):
    """
    Determines the corresponding point for the chosen path.
    """
    if state:
        return 125
    else:
        return 50     
def display_text(score):
    """
    Returns the player's earned memory points.
    """
    pygame.font.init()
    font = pygame.font.SysFont("timesnewroman", 45)
    text = font.render(str(score), True, (255, 255, 255))
    return text

def main():
    """
    Main function of the game
    """
    game_init()
    new_game()
    credits()

if __name__ == '__main__':
    main()
