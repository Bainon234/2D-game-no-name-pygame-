 
import pygame, os

class Game:
    def objects_draw(range, x=0,y=0):
        def pause():
            background = pygame.image.load(os.path.join('sprites', 'menu_background.png'))
            if not background in Game.stats.objects_in_game:
                Game.stats.objects_in_game.append(background)
        def player():
            player = pygame.image.load(os.path.join('sprites', 'player.png'))
        recorces = [pause,player]
        recorces[range]()
    #drawing a image into the screen

    class stage:
        def pause():
            Game.objects_draw(1)
        #This helps the game knows where the player is
    class stats:
        playing_state = False
        failed_state = False
        game_stage = 0
        player_paused = False
        objects_in_game = []
        #I sould wish if theres a better way to do this to not ruin the read-ablity of this code

    def __init__():
        return f'playing state = {Game.stats.playing_state} | ', f'failed_state = {Game.stats.failed_state} | ', f'game_stage = {Game.stats.game_stage} | ', f'objects = {Game.stats.objects_in_game} |'
        #Easy debugging

    def window_objects(state, tick, host_window_clock):
        #This handles the events.
        while state:
            host_window_clock.tick(tick)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return False
                if Game.stats.game_stage == 0 or Game.stats.player_paused:
                    Game.objects_draw(0)
                    pygame.display.update()
                print(Game.__init__())
            pygame.display.update()


    def window(width, height, name, frames):
        #A window which is a list? Fancy!
        WIN = [pygame.display.set_mode((width, height)),pygame.display.set_caption(str(name)), pygame.time.Clock()]
        if not Game.window_objects(True, frames, WIN[2]):
            pygame.quit()
            return 'Window quited!'

if __name__ == '__main__':
    #Checks if this script is not a imported script thank you.
    Game.window(900,500,"Test",60)
    if Game.stats.failed_state:
        print('cmd')
        ''' If the game ran into a error or a bug that crashes the game. 

            Then the game should pop up a cmd that acts like console
            When a console is opened, then it should tell the player
            can choose to type help for console commands and debugging
            commands.

        '''