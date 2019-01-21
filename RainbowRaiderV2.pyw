# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.
import sys
sys.path.append('C:/Python27')

import warnings
warnings.filterwarnings("ignore")

import pygame
import PIL
import simpleguitk as simplegui
import math
import time
import warnings
import json

###############
WIDTH = 550.0
HEIGHT = 550.0
status = "MainScreen"
code = ""
tile_size = 68.75
EXTRA_HEIGHT = 68.75
message = ""
playedLevls = []
movable_rock_list = []
worldCount = 4
character1_finish = False 
character2_finish = False
Ttime = 0
notice = False
uCanvas = None

def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

bounce_condition = False
controller = "available"
player = "main"

#sound = simplegui.load_sound("http://srv70.vidtomp3.com/download/1sTCeqpyzmewZHFtmJSTa21o5KWmqXBo4pSXbGlhm2dram60vMzHrKid2GU=/Let%20it%20Go%20%28Frozen%29-%20Piano%20Cover.mp3")
#sound.play()

class ImageInfo:
    def __init__(self, center, size, backup_centre = 0, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        self.backup_center = backup_centre
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan
    
    def change_centre(self):
        self.center[0] = self.center[0] - 4
        if self.center[0] <= 214:
            self.center[0] = self.backup_center[0]
    
    def get_animated(self):
        return self.animated

pause_image_info = ImageInfo([200, 200], [400, 400])
pause_image_image = simplegui.load_image("pause_image.png")

main_character_front_info = ImageInfo([240, 212], [480, 424])
main_character_front_image = simplegui.load_image("main_character_front.png")

main_character_back_info = ImageInfo([240, 212], [480, 424])
main_character_back_image = simplegui.load_image("main_character_back.png")

main_character_left_info = ImageInfo([240, 212], [480, 424])
main_character_left_image = simplegui.load_image("main_character_left.png")

main_character_right_info = ImageInfo([240, 212], [480, 424])
main_character_right_image = simplegui.load_image("main_character_right.png")

ice_tile_info = ImageInfo([800, 800], [1600 , 1600])
ice_tile_image = simplegui.load_image("ice_tile.png")

ice_rock_info = ImageInfo([111, 90], [170, 150])
ice_rock_image = simplegui.load_image("ice_rock.png")

star_info = ImageInfo([1277, 1215], [2554, 2430])
star_image = simplegui.load_image("star_image.png")

ice_snow_tile_info = ImageInfo([256, 256], [512, 512])
ice_snow_tile_image = simplegui.load_image("ice_snow_tile.jpg")

ice_water_info = ImageInfo([122, 122], [243, 243])
ice_water_image = simplegui.load_image("ice_water_tile.png")

play_button_info = ImageInfo([512, 512], [1024, 1024])
play_button_image = simplegui.load_image("play_button.png")

zero_stars_collected_info = ImageInfo([862, 328], [1724, 656])
zero_stars_collected_image = simplegui.load_image("0_stars_collected.png")

one_stars_collected_info = ImageInfo([887, 278], [1774, 556])
one_stars_collected_image = simplegui.load_image("1_stars_collected.png")

two_stars_collected_info = ImageInfo([952, 287], [1904, 574])
two_stars_collected_image = simplegui.load_image("2_stars_collected.png")

three_stars_collected_info = ImageInfo([873, 314], [1746, 628])
three_stars_collected_image = simplegui.load_image("3_stars_collected.png")

lava_level_passed_info = ImageInfo([683, 384], [1366, 768])
lava_level_passed_image = simplegui.load_image("lava_level_passed.png")

pause_sign_info = ImageInfo([683, 384], [1366, 768])
pause_sign_image = simplegui.load_image("pause_sign.png")

breakable_rock_info = ImageInfo([200, 200], [170, 170])
breakable_rock = simplegui.load_image("breakable_rock.png")

broken_rock_info = ImageInfo([200, 200], [400, 400])
broken_rock_image = simplegui.load_image("broken_rock.png")

ice_level_select_info = ImageInfo([683, 384], [1366, 768])
ice_level_select_image = simplegui.load_image("ice_title_screen.png")

ice_level_passed_info = ImageInfo([514, 384], [1028, 768])
ice_level_passed_image = simplegui.load_image("ice_level_passed.png")

lava_tile_info = ImageInfo([300, 300], [600, 600])
lava_tile_image = simplegui.load_image("lava_tile.jpg")

lava_rock_tile_info = ImageInfo([456, 456], [912, 912])
lava_rock_tile_image = simplegui.load_image("lava_rock.png")

lava_character_back_info = ImageInfo([200, 200], [400, 400])
lava_character_back_image = simplegui.load_image("lava_character_back.png")

lava_character_front_info = ImageInfo([200, 200], [400, 400])
lava_character_front_image = simplegui.load_image("lava_character_front.png")

lava_character_left_info = ImageInfo([200, 200], [400, 400])
lava_character_left_image = simplegui.load_image("lava_character_left.png")

lava_character_right_info = ImageInfo([200, 200], [400, 400])
lava_character_right_image = simplegui.load_image("lava_character_right.png")

lava_character_burning_info = ImageInfo([100, 113], [200, 226])
lava_character_burning_image = simplegui.load_image("lava_character_burning.png")

lava_level_passed_info = ImageInfo([516, 386], [1032, 772])
lava_level_passed_image = simplegui.load_image("lava_level_passed.png")

lava_title_screen_info = ImageInfo([512, 384], [1024, 768])
lava_title_screen_image = simplegui.load_image("lava_title_screen.png")

volcano_no_fire_info = ImageInfo([200, 200], [400, 400])
volcano_no_fire_image = simplegui.load_image("volcano_no_fire.png")

volcano_with_fire_info = ImageInfo([200, 200], [400, 400])
volcano_with_fire_image = simplegui.load_image("volcano_with_fire.png")

movable_rock_info = ImageInfo([150, 150], [300, 300])
movable_rock_image = simplegui.load_image("movable_rock.png")

water_current_info = ImageInfo([1070, 214], [428, 428], [1070, 214])
water_current_image = simplegui.load_image("water_current.png")

water_tile_info = ImageInfo([112, 112], [224, 224])
water_tile_image = simplegui.load_image("water_tile.jpg")

whirlpool_info = ImageInfo([64, 64], [110, 110])
whirlpool_image = simplegui.load_image("whirlpool.png")

metal_tile_info = ImageInfo([47, 47], [94, 94])
metal_tile_image = simplegui.load_image("metal_tile.jpg")

slime_tile_info = ImageInfo([46, 46], [92, 92])
slime_tile_image = simplegui.load_image("slime_tile.png")

alien_rock_info = ImageInfo([163, 224], [326, 448])
alien_rock_image = simplegui.load_image("alien_rock.png")

water_character_back_info = ImageInfo([240, 212], [480, 424])
water_character_back_image = simplegui.load_image("water_character_back.png")

water_character_front_info = ImageInfo([240, 212], [480, 424])
water_character_front_image = simplegui.load_image("water_character_front.png")

water_character_right_info = ImageInfo([250, 222], [500, 444])
water_character_right_image = simplegui.load_image("water_character_right.png")
    
water_character_left_info = ImageInfo([240, 212], [480, 424])
water_character_left_image = simplegui.load_image("water_character_left.png")

alien_character_back_info = ImageInfo([240, 212], [480, 424])
alien_character_back_image = simplegui.load_image("alien_character_back.png")

alien_character_front_info = ImageInfo([240, 212], [480, 424])
alien_character_front_image = simplegui.load_image("alien_character_front.png")

alien_character_left_info = ImageInfo([240, 212], [480, 424])
alien_character_left_image = simplegui.load_image("alien_character_left.png")

alien_character_right_info = ImageInfo([240, 212], [480, 424])
alien_character_right_image = simplegui.load_image("alien_character_right.png")

alien_back_info = ImageInfo([195, 328], [390, 656])
alien_back_image = simplegui.load_image("alien_back.png")

alien_right_info = ImageInfo([200, 200], [400, 400])
alien_right_image = simplegui.load_image("alien_right.png")
    
alien_front_info = ImageInfo([195, 328], [390, 656])
alien_front_image = simplegui.load_image("alien_front.png")

alien_left_info = ImageInfo([195, 328], [390, 656])
alien_left_image = simplegui.load_image("alien_left.png")

laser_vertical_info = ImageInfo([262, 350], [174, 700])
laser_vertical_image = simplegui.load_image("laser_vertical.png")

laser_horizontal_info = ImageInfo([350, 262], [700, 174])
laser_horizontal_image = simplegui.load_image("laser_horizontal.png")

technology_tile_info = ImageInfo([160, 160], [320, 320])
technology_tile_image = simplegui.load_image("tech_tile.jpg")

teleporter_tile_info = ImageInfo([447, 447], [894, 894])
teleporter_tile_image = simplegui.load_image("teleporter_tile.png")

building_info = ImageInfo([198, 112], [396, 224])
building_image = simplegui.load_image("building.png")

poison_gas_info = ImageInfo([120, 68], [240,136])
poison_gas_image = simplegui.load_image("poison_gas.png")

future_level_passed_info = ImageInfo([515, 382], [1030, 764])
future_level_passed_image = simplegui.load_image("future_level_passed.png")

future_stopper_tile_info = ImageInfo([47, 47], [94, 94])
future_stopper_tile_image = simplegui.load_image("future_stopper.jpg")

future_level_select_info = ImageInfo([683, 384], [1366, 768])
future_level_select_image = simplegui.load_image("future_level_select.png")

spaceship_level_select_info = ImageInfo([683, 384], [1366, 768])
spaceship_level_select_image = simplegui.load_image("spaceship_level_select.png")

spaceship_level_passed_info = ImageInfo([515, 385], [1030, 770])
spaceship_level_passed_image = simplegui.load_image("spaceship_level_passed.png")

water_level_select_info = ImageInfo([683, 384], [1366, 768])
water_level_select_image = simplegui.load_image("water_level_select.png")

water_level_passed_info = ImageInfo([514, 384], [1028, 768])
water_level_passed_image = simplegui.load_image("water_level_passed.png")

spaceship_alien_end_info = ImageInfo([127, 140], [254, 280])
spaceship_alien_end_image = simplegui.load_image("spaceship_alien_end.png")

spaceship_normal_end_info = ImageInfo([116, 108], [232, 216])
spaceship_normal_end_image = simplegui.load_image("spaceship_normal_end.png")

spaceship_instructions_info = ImageInfo([683, 384], [1366, 768])
spaceship_instructions_image = simplegui.load_image("spaceship_instructions.png")

spaceship_plot_info = ImageInfo([683, 384], [1366, 768])
spaceship_plot_image = simplegui.load_image("spaceship_plot.png")

try_again_info = ImageInfo([200, 200], [400, 400])
try_again_image = simplegui.load_image("try_again.png")

main_title_info = ImageInfo([683, 384], [1366, 768])
main_title_image = simplegui.load_image("main_title.png")
                                    
future_plot_info = ImageInfo([683, 384], [1366, 768])
future_plot_image = simplegui.load_image("future_plot.png")

final_plot_info = ImageInfo([683, 384], [1366, 768])
final_plot_image = simplegui.load_image("final_plot.png")

future_instructions_info = ImageInfo([683, 384], [1366, 768])
future_instructions_image = simplegui.load_image("future_instructions.png")

water_instructions_info = ImageInfo([683, 384], [1366, 768])
water_instructions_image = simplegui.load_image("water_instructions.png")

water_plot_info = ImageInfo([683, 384], [1366, 768])
water_plot_image = simplegui.load_image("water_plot.png")

ice_instructions_info = ImageInfo([683, 384], [1366, 768])
ice_instructions_image = simplegui.load_image("ice_instructions.png")

ice_plot_info = ImageInfo([683, 384], [1366, 768])
ice_plot_image = simplegui.load_image("ice_plot.png")

lava_instructions_info = ImageInfo([683, 384], [1366, 768])
lava_instructions_image = simplegui.load_image("lava_instructions.png")

lava_plot_info = ImageInfo([683, 384], [1366, 768])
lava_plot_image = simplegui.load_image("lava_plot.png")

ice_frozen_character_info = ImageInfo([200, 200], [400, 400])
ice_frozen_character_image = simplegui.load_image("ice_frozen_character.png")
                                     

class Character:
    def __init__(self, pos, vel, front_image, front_info, back_image, back_info, left_image, left_info, right_image, right_info):
        global EXTRA_HEIGHT, tile_size
        self.pos = pos
        self.vel = vel
        self.front = [front_image, front_info]
        self.back = [back_image, back_info]
        self.left = [left_image, left_info]
        self.right = [right_image, right_info]
        self.moving = False
        self.current_image = front_image
        self.image_info = front_info
        self.direction = [0, 0]
        self.location = [((self.pos[1] - EXTRA_HEIGHT) // tile_size), (self.pos[0] // tile_size)]
        self.turn = 0

    def get_moving(self):
        return self.moving

    def stop_if_last_tile(self,currentTile):
        dimension = game_field.get_current_level("dimension")
        global tile_size, EXTRA_HEIGHT, message, status, condition_right, condition_left, condition_up, condition_down

        if self.direction == [1,0]:#right
            location = self.location[1] + 1
            finalPosition = (self.location[1] )*tile_size + tile_size*3/4
            finalPosition2 = (self.location[1] )*tile_size + tile_size/2
            if location == dimension:# last tile
                 if self.pos[0] >= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2

        elif self.direction == [-1,0]:#left
            finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[1]+ 1)*tile_size - tile_size/2
            if self.location[1] == 0:
                 if self.pos[0] <= finalPosition: # last tile
                    self.stop_moving()
                    self.pos[0] = finalPosition2

        elif  self.direction == [0,-1]:#up
            finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[0] + 2)*tile_size - tile_size/2
            if self.location[0] == 0:
                if self.pos[1] <= finalPosition:# last tile
                    self.stop_moving()
                    self.pos[1] = finalPosition2

        elif  self.direction == [0,1]:#down
            finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4
            finalPosition2 = (self.location[0] + 1)*tile_size + tile_size/2
            location = self.location[0] + 1
            if location == dimension:
                if self.pos[1] >= finalPosition:# last tile
                    self.stop_moving()
                    self.pos[1] = finalPosition2


    def check_if_won(self,currentTile, winTile):

        global tile_size, EXTRA_HEIGHT, message, status, condition_right, condition_left, condition_up, condition_down
        if currentTile == winTile:
            lvl = game_field.get_current_level()
            if lvl.stars == 3:
                status = "LVL"



    def move_code(self):
        self.pos[0] += (self.vel[0] * self.direction[0])
        self.pos[1] += (self.vel[1] * self.direction[1])

    def move(self):
        if self.moving == True:
            self.move_code()

    def start_moving_code(self, direction):
        self.direction = direction
        self.moving = True
        if direction == [0, 1]:
            self.current_image = self.front[0]
            self.current_info = self.front[1]
        elif direction == [0, -1]:
            self.current_image = self.back[0]
            self.current_info = self.back[1]
        elif direction == [1, 0]:
            self.current_image = self.right[0]
            self.current_info = self.right[1]
        elif direction == [-1, 0]:
            self.current_image = self.left[0]
            self.current_info = self.left[1]

    def get_turn(self):
        return self.turn

    def start_moving(self, direction):
        if self.moving == False:
            self.start_moving_code(direction)


    def stop_moving(self):
        if self.moving == True:
            self.direction = [0, 0]
            self.moving = False

    def teleport(self):
        global tile_size, EXTRA_HEIGHT
        if worldCount == 0:
            starting = game_field.get_current_level("start",2)
        elif worldCount == 1:
            starting = game_field.get_current_level("start",[5])
        elif worldCount == 2:
            starting = game_field.get_current_level("start",4)
        elif worldCount == 3:
            starting = game_field.get_current_level("start")
        elif worldCount == 4:
            starting = game_field.get_current_level("start",2)
        tile_size = game_field.get_current_level("tile_size")
        EXTRA_HEIGHT = WIDTH / game_field.get_current_level("dimension")
        self.pos = [(tile_size * starting[1]) + tile_size / 2, (tile_size * starting[0]) + tile_size / 2 + (EXTRA_HEIGHT)]
        self.turn = 0
        self.current_image = self.front[0]
        self.current_info = self.front[1]
        self.stop_moving()

    def death_animation(self, canvas):
        return ""

    def check_moving(self):
        return self.moving

    def get_pos(self):
        return self.pos
    def get_location(self):
        return self.location
    

    def draw(self, canvas):
        if message == "DEAD":
            self.death_animation(canvas)
        else:
            canvas.draw_image(self.current_image, self.image_info.get_center(), self.image_info.get_size(), self.pos, [tile_size * 0.6, tile_size * 0.8])

class Level:
    def __init__(self, layout):
        self.layout = layout
        self.tile_size = WIDTH / (len(layout))
        starting_point = [0, 0]
        self.starting_point = starting_point
        self.dimension = len(layout)
        self.played = False
        self.stars = 0
        self.max_stars = 0
        self.changed_tiles = []
        self.record = 599
        
    def set_record(self, newRec):
        self.record = min(newRec, self.record)

    def get_record(self):
        return self.record
        
    def get_dimension(self):
        return int(self.dimension)
    def reset_level(self):
        global movable_rock_list
        for element in self.changed_tiles:
            if type(element[0]) == list:
                self.layout[int(element[0][0])][int(element[0][1])] = element[1]
                movable_rock_list = []
                self.stars = 0
      

    def get_layout(self):
        return self.layout

    def get_start(self, number):
        for i in range(len(self.layout)):
            for j in range(len(self.layout[i])):
                if self.layout[i][j] == 2:
                    self.starting_point = [i, j]
    
        return self.starting_point

    def get_tile_size(self):
        return self.tile_size

    def change_tile(self, coordinate, new_tile):
        oldTile = self.layout[int(coordinate[0])][int(coordinate[1])]
        if oldTile == 9:
            self.changed_tiles.append([coordinate, 8])
        else:
            self.changed_tiles.append([coordinate, oldTile])

        self.layout[int(coordinate[0])][int(coordinate[1])] = new_tile

    def collect_star(self):
        global notice
        self.stars += 1
        notice = True
        timerA.start()

    def check_stars(self):
        if self.stars >= self.max_stars:
            self.max_stars = self.stars

    def play_level(self):
        self.played = True
        self.stars = 0
    def get_played(self):
        return self.played

    def get_stars(self, max = None):
        if max == True:
            return self.max_stars
        return self.stars
    #def reset_level(self):
        
class Field:
    def __init__(self, level_list, starting_level = 1):
        self.levels = level_list
        self.current_level = level_list[starting_level - 1]
        self.current_starting_point = [0,0]
        self.current_tile_size = self.current_level.get_tile_size()
        self.current_dimension = int(self.current_level.get_dimension())
        self.current_layout = self.current_level.get_layout()


    def get_level_list(self):
        return self.levels

    def get_current_level(self, extra_parameter = None, startTile = 2):
        if extra_parameter == "layout":
            return self.current_layout
        elif extra_parameter == "start":
            self.current_starting_point = self.current_level.get_start(startTile)
            return self.current_starting_point
        elif extra_parameter == "tile_size":
            return self.current_tile_size
        elif extra_parameter == "dimension":
            return self.current_dimension
        elif extra_parameter == "star":
            return self.current_level.get_stars()
        else:
            return self.current_level

    def teleport_current_character(self):
        return ""
    def select_level(self, level, statusx = None):
        global status
        lvl = self.levels[level - 1]
        if level == 1 or lvl.get_played() == True:

            self.current_level = lvl
            lvl.reset_level()
            if level <= 5:
                self.current_dimension = 8
                self.current_tile_size = 68.75
            else:
                self.current_dimension = 10
                self.current_tile_size = 55.0
            self.current_layout = lvl.get_layout()
            if statusx != None:
                status = statusx
            main_character[0].teleport()
            main_character[-1].teleport()


    def next_level(self, startTile):
        global Ttime
        lvl = self.current_level
        lvl.set_record(Ttime)
        self.current_level = self.levels[self.levels.index(lvl) + 1]
        self.current_starting_point = self.current_level.get_start(startTile)
        self.current_tile_size = self.current_level.get_tile_size()
        self.current_dimension = int(self.current_level.get_dimension())
        self.current_layout = self.current_level.get_layout()

    def no_of_lvls_played(self):
        count = 0
        for lvl in self.levels:
            if not lvl.get_played():
                count += 1
        return count

class World:
    def __init__(self, worldName):
        ice_level1 = Level([[0,0,0,0,1,3,1,4],
                            [5,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,5,0],
                            [0,0,0,0,0,0,0,0],
                            [4,1,0,0,1,0,0,0],
                            [0,0,0,0,0,0,0,1],
                            [0,5,0,0,0,0,0,0],
                            [0,0,4,1,2,1,0,0]])

        ice_level2 = Level([[6,1,6,0,4,1,6,1],
                            [1,6,1,0,0,6,6,6],
                            [6,1,6,1,0,1,6,1],
                            [0,4,0,0,0,0,1,0],
                            [0,1,0,5,5,5,4,0],
                            [1,6,1,0,1,6,1,6],
                            [6,6,6,0,0,1,6,1],
                            [1,6,1,2,3,6,1,6]])


        ice_level3 = Level([[1,4,0,0,0,0,1,6],
                            [0,0,0,0,0,0,4,1],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,4],
                            [2,0,0,0,6,0,6,3],
                            [0,0,0,0,0,0,0,0],
                            [0,5,0,0,0,0,6,0],
                            [0,0,0,0,1,0,0,0]])

        ice_level4 = Level([[6,0,0,0,1,0,0,6],
                            [4,0,0,0,0,0,0,0],
                            [0,2,0,0,0,0,1,0],
                            [0,0,0,1,0,0,5,0],
                            [0,1,0,0,0,0,4,0],
                            [0,0,0,0,0,0,0,0],
                            [4,0,0,5,0,0,0,0],
                            [0,6,3,1,0,0,0,1]])





        ice_level5 = Level([[6,6,0,0,0,0,0,1],
                            [5,5,0,0,1,4,0,0],
                            [0,0,0,0,4,1,5,0],
                            [0,0,0,0,0,0,0,1],
                            [0,0,0,0,5,6,0,0],
                            [0,1,0,4,0,0,0,0],
                            [0,6,6,6,6,6,1,0],
                            [0,0,0,0,0,2,6,3]])



        ice_level10 = Level([[1,6,3,6,0,1,4,0,0,6],
                            [0,0,0,0,5,0,0,0,8,4],
                            [0,0,0,0,0,0,0,6,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,6,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,4],
                            [0,0,8,6,0,0,1,5,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [8,6,0,0,0,0,0,0,0,0],
                            [2,8,0,0,5,1,6,5,0,8]])

        ice_level8 = Level([[6,4,0,8,8,8,0,0,0,6],
                            [0,5,0,8,0,8,0,0,5,0],
                            [0,0,6,0,0,0,0,6,0,4],
                            [8,8,0,5,5,5,0,0,8,8],
                            [8,0,0,5,2,3,0,0,0,8],
                            [8,8,0,5,5,5,0,0,8,8],
                            [4,0,0,0,0,0,0,0,0,0],
                            [0,0,6,0,0,0,0,6,0,0],
                            [8,5,0,8,0,8,0,0,0,8],
                            [6,0,0,8,8,8,0,0,8,6]])

        ice_level9 = Level([[3, 0, 0, 0, 0, 0, 0, 0, 0, 6],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [8, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [6, 4, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [4, 0, 0, 0, 0, 2, 0, 0, 0, 0],
                            [8, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 6, 0, 0, 0, 8, 0, 0, 0, 0],
                            [0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
                            [0, 0, 0, 8, 6, 0, 0, 0, 0, 8]])

        ice_level7 = Level([[0, 4, 6, 1, 6, 6, 6, 6, 6, 6],
                            [0, 5, 0, 0, 8, 2, 0, 0, 0, 8],
                            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 5, 0, 0, 0, 0, 1, 0],
                            [0, 8, 0, 0, 8, 6, 1, 0, 0, 0],
                            [0, 6, 0, 1, 4, 6, 0, 0, 8, 6],
                            [0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
                            [0, 5, 0, 0, 5, 6, 0, 1, 0, 0],
                            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [6, 0, 1, 0, 0, 8, 1, 0, 0, 3]])

        ice_level6 = Level([[8, 6, 6, 6, 6, 2, 0, 0, 8, 5],
                            [0, 0, 5, 0, 0, 0, 0, 0, 6, 4],
                            [0, 0, 0, 0, 0, 5, 0, 8, 0, 0],
                            [8, 8, 0, 0, 6, 0, 0, 0, 1, 1],
                            [5, 0, 0, 8, 0, 0, 8, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 6, 6, 6, 6, 4],
                            [0, 0, 4, 0, 0, 0, 5, 0, 0, 1],
                            [1, 0, 1, 0, 0, 0, 0, 0, 0, 6],
                            [5, 6, 0, 0, 0, 0, 8, 0, 0, 3]])

        ice_levels = [ice_level1, ice_level2, ice_level3, ice_level4, ice_level5, ice_level6, ice_level7, ice_level8, ice_level9, ice_level10]
        
        water_level_1 = Water_Level([[[1], [0], [1], [1], [1], [2], [1], [2]],
                                    [[0], [0], [0], [0], [0], [1], [0], [2]],
                                    [[0], [2], [4], [1], [1], [2], [0], [2]],
                                    [[0], [2], [7], [3], [4], [2], [0], [2]],
                                    [[0], [0], [0], [0], [3], [2], [3], [2]],
                                    [[7], [2], [4], [0], [4], [2], [7], [2]],
                                    [[1], [5], [0], [0], [2], [2], [6], [2]],
                                    [[0], [3], [4], [3], [4], [4], [3], [4]]])

        water_level_2 = Water_Level([[[7], [0], [2], [0], [0], [2], [1], [2]],
                                    [[1], [3], [1], [3], [2], [4], [3], [2]],
                                    [[3], [8], [2], [4], [0], [0], [0], [2]],
                                    [[5], [0], [4], [3], [4], [1], [3], [6]],
                                    [[2], [3], [0], [4], [4], [7], [2], [0]],
                                    [[1], [0], [2], [1], [0], [3], [2], [0]],
                                    [[2], [0], [0], [0], [1], [2], [0], [3]],
                                    [[1], [1], [1], [1], [3], [7], [1], [0]]])

        water_level_4 = Water_Level([[[1], [1], [1], [1], [1], [1], [0], [2]],
                                    [[3], [8], [7], [1], [8], [8], [2], [8]],
                                    [[3], [1], [0], [2], [4], [4], [1], [3]],
                                    [[3], [3], [1], [2], [5], [3], [4], [3]],
                                    [[3], [3], [3], [2], [1], [3], [0], [7]],
                                    [[3], [7], [3], [0], [1], [1], [3], [8]],
                                    [[0], [3], [0], [2], [4], [4], [4], [4]],
                                    [[3], [4], [4], [0], [1], [1], [1], [6]]])

        water_level_5 = Water_Level([[[1], [1], [1], [0], [2], [0], [2], [2]],
                                    [[2], [0], [4], [1], [1], [3], [8], [7]],
                                    [[1], [2], [3], [7], [0], [0], [1], [0]],
                                    [[0], [1], [0], [4], [4], [3], [4], [2]],
                                    [[3], [4], [3], [0], [3], [4], [3], [7]],
                                    [[1], [0], [1], [3], [8], [3], [0], [2]],
                                    [[3], [3], [4], [0], [2], [3], [3], [2]],
                                    [[5], [1], [0], [3], [0], [0], [3], [6]]])

        water_level_3 = Water_Level([[[8], [1], [2], [1], [2], [1], [1], [2]],
                                    [[1], [3], [2], [3], [2], [2], [4], [2]],
                                    [[3], [2], [1], [3], [8], [0], [3], [2]],
                                    [[3], [1], [1], [2], [1], [1], [3], [2]],
                                    [[5], [2], [3], [7], [0], [2], [3], [2]],
                                    [[2], [8], [3], [4], [2], [4], [3], [7]],
                                    [[1], [2], [8], [3], [1], [2], [3], [0]],
                                    [[8], [1], [1], [3], [8], [1], [7], [6]]])

        water_level_6 = Water_Level([[[1], [2], [7], [8], [4], [1], [2], [1], [7], [2]],
                                    [[3], [0], [3], [1], [3], [3], [0], [0], [4], [4]],
                                    [[0], [1], [0], [1], [2], [3], [1], [1], [2], [0]],
                                    [[3, 2], [2], [0], [2], [1], [0], [1], [2], [1], [0]],
                                    [[5], [1, 4], [1, 4], [1, 4], [2, 4], [1, 4], [8], [8], [8], [3, 2]],
                                    [[2, 3], [8], [8], [8], [1, 4], [1, 3], [1, 4], [1, 4], [1, 4], [6]],
                                    [[0], [1], [2], [0], [3], [0], [3], [8], [3], [2, 3]],
                                    [[3], [7], [0], [3], [1], [1], [2], [1], [2], [0]],
                                    [[3], [3], [0], [1], [3], [3], [2], [2], [2], [2]],
                                    [[3], [8], [1], [0], [8], [4], [4], [8], [8], [8]]])

        water_level_7 = Water_Level([[[1], [2], [0], [2], [8], [4], [4], [4], [0], [2]],
                                    [[3], [0], [3], [2], [6], [4], [4], [1], [3], [8]],
                                    [[0], [2], [7], [4, 2], [2], [1], [3], [0], [4], [4]],
                                    [[3, 1], [8], [2], [4], [0], [2], [1], [1], [8, 0], [3]],
                                    [[5], [4], [0], [0], [3], [2], [3], [4], [0], [4]],
                                    [[1], [1], [2], [4, 3], [2], [4], [1], [1], [1, 3], [0]],
                                    [[8], [4], [4], [7], [2], [0], [2], [0], [4], [7]],
                                    [[1], [1], [0], [3], [0], [3], [2], [2], [0], [4]],
                                    [[0], [4], [2], [4], [4], [0], [4], [4], [0], [3]],
                                    [[3], [4], [0], [8], [8], [8, 0], [1], [1], [3], [8]]])

        water_level_8 = Water_Level([[[2], [2], [2], [1], [1], [2], [2], [0], [8], [4]],
                                    [[2], [7], [4, 2], [0], [4], [2, 4], [2], [3], [0], [3]],
                                    [[1], [2], [2], [3], [8], [8], [2], [2], [3, 4], [4]],
                                    [[6], [0, 8], [2], [1, 3], [3, 4], [4], [0], [1], [0], [2, 3]],
                                    [[0], [8], [4, 1], [0], [3], [2], [1], [1], [8], [4, 3]],
                                    [[3, 1], [1], [0], [1], [3], [0], [1], [0], [3], [3]],
                                    [[3], [2], [4], [4], [0], [3, 4], [4], [1], [1], [8, 0]],
                                    [[3], [1], [8, 0], [7], [2, 1], [8], [3], [2], [4, 1], [0]],
                                    [[3], [0], [3, 4], [4, 1], [0], [1, 3], [3, 4], [7], [3], [4]],
                                    [[8], [4], [3], [0], [4, 1], [3], [4], [4], [4], [5]]])

        water_level_9 = Water_Level([[[1], [2, 1], [1], [1], [1], [1], [0], [2], [2, 4], [4]],
                                    [[3], [2], [8, 0], [4], [4], [7], [2], [2], [7], [3]],
                                    [[0], [2], [3], [4], [3], [3], [2], [1], [1], [0]],
                                    [[3], [1], [1], [0], [3], [3], [4], [2], [4], [4]],
                                    [[3], [4], [4], [4], [3], [1], [8], [1], [2], [8]],
                                    [[5], [3], [2], [4], [0], [3], [2], [4], [0], [2, 3]],
                                    [[2, 1], [4, 3], [1], [0, 8], [4, 3], [4], [4], [1], [3], [2, 3]],
                                    [[6], [3], [4], [0], [1], [1], [1], [3], [8, 0], [2, 3]],
                                    [[3], [4], [4], [8, 0], [1, 2], [2, 3], [4], [0, 8], [0], [4, 3]],
                                    [[8], [8], [3, 4], [4], [3, 4], [7], [1], [3], [4], [8]]])

        water_level_10 = Water_Level([[[2, 1], [5], [4], [4], [4], [4], [4], [4], [4], [4]],
                                    [[2, 1], [2, 1], [3, 1], [0], [2, 1], [0], [2, 1], [4, 1], [0, 8], [0]],
                                    [[2, 1], [1], [2, 1], [3, 1], [1], [2, 1], [2, 1], [3, 1], [4, 1], [0]],
                                    [[8], [0], [4, 1], [3, 1], [0], [2, 1], [1], [0], [0, 8], [0]],
                                    [[3, 1], [2, 1], [1], [3, 1], [2, 1], [4, 1], [0], [3, 1], [4, 1], [0]],
                                    [[3, 1], [0], [3, 1], [7], [4, 1], [2, 1], [4, 1], [4, 1], [0, 8], [0]],
                                    [[3, 1], [1], [2, 1], [1], [8], [2, 1], [7], [2, 1], [4, 1], [0]],
                                    [[2, 1], [1], [8], [2, 1], [1], [2, 1], [3, 1], [4, 1], [0, 8], [0]],
                                    [[2, 1], [1], [7], [1], [3, 1], [0], [8], [3, 1], [4, 1], [0]],
                                    [[1], [3, 1], [4, 1], [4, 1], [4, 1], [4, 1], [4, 1], [4, 3], [0, 8], [6]]])

        water_levels = [water_level_1, water_level_2, water_level_3, water_level_4, water_level_5, water_level_6, water_level_7, water_level_8, water_level_9, water_level_10]
        
        lava_level1 = Level([[2, 0, 0, 0, 0, 0, 1, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, -2, -3, 0, 0],
                                  [0, 0, 0, 0, 0, 4, 0, 0],
                                  [-1, 0, -4, 0, 0, 1, 0, 5],
                                  [0, 0, 0, 0, 0, 0, 0, 1],
                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                  [4, 0, 0, 4, 1, -2, 0, 0]])

        lava_level2 = Level([[0, 0, 0, 1, 0, 0, 0, 4],
                                  [-3, 0, 0, 1, 0, -3, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0],
                                  [2, 0, 1, 0, 0, 0, 0, 0],
                                  [0, 0, 0, -2, 0, 1, -1, 1],
                                  [0, -3, 0, 1, 0, 0, 0, 4],
                                  [0, 0, 0, 4, 1, -4, 0, 0],
                                  [-4, 1, 0, 0, 0, 0, 1, 5]])

        lava_level3 = Level([[-1, 1, 0, 0, 0, 0, -5, 5],
                                   [1, -4, 0, 0, 1, 0, 0, 1],
                                   [4, 0, 0, 0, 0, 0, 0, 1],
                                   [0, 1, 0, 1, 0, -2, 0, 0],
                                   [2, 0, -5, 0, 0, 0, 1, 0],
                                   [0, 0, 0, 0, 4, 0, 0, 0],
                                   [0, 1, 0, 0, 1, 0, -3, 0],
                                   [0, -2, 4, 0, 0, 0, 0, 0]])

        lava_level4 = Level([[1, 0, 0, 1, -5, 0, 0, 4],
                                  [0, 0, 1, 0, 0, 0, -2, 0],
                                  [-4, 0, 0, 1, 0, 0, 1, 0],
                                  [0, 0, 0, 0, -3, 0, -4, 0],
                                  [0, 4, 1, 1, 0, 1, 0, 0],
                                  [1, 0, 0, 0, 0, 0, 0, 1],
                                  [-1, 0, 0, 1, 0, 0, 1, 5],
                                  [2, 0, 1, 0, -3, 0, 0, 4]])

        lava_level5 = Level([[-1, -1, -1, -1, -1, -1, -1, -1],
                                  [-1, 0, 0, 1, 1, 0, 1, -1],
                                  [1, 1, 0, 0, -2, 0, 4, 1],
                                  [0, 0, -3, 0, 0, 1, -4, 4],
                                  [0, 1, 0, 1, -2, 0, 0, 0],
                                  [0, 1, 4, 0, 0, 0, 0, 1],
                                  [0, 0, -5, 0, 1, 0, 0, 0],
                                  [2, 0, 1, 0, 0, 1, 0, 5]])

        lava_level6 = Level([[2, 0, 1, 0, 0, 1, 4, 0, 0, -4],
                                  [0, 0, 0, -1, 0, 0, 0, 0, -1, 0],
                                  [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                                  [0, 0, -2, 0, 0, 1, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 4],
                                  [0, 0, 0, -5, 0, 0, 0, 0, 0, 1],
                                  [0, 0, 1, 0, 0, -1, 0, 0, 1, 5],
                                  [1, -3, 0, 0, -4, 0, 0, 1, 1, -1],
                                  [0, 1, 0, 0, 0, 0, 0, 0,0, 0],
                                  [0, 0, 1, 4, 0, 0, 0, 0, 0, 0]])

        lava_level7 = Level([[4, 0, 0, 0, 0, 0, 0, 0, 1, 5],
                                 [-1, 0, 0, 0, 1, 0, 0, -5, 0, 0],
                                 [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
                                 [0, 0, 1, 0, -1, 0, 0, 0, 0, 4],
                                 [0, -4, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 0, 1, 0, 0, 1, 0, -2, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, -5, 0, 0, -2, 1, 0, 0],
                                 [2, -3, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 0, 0, 0, -2, 0, 1, 4, 0, 0]])

        lava_level8 = Level([[0, 0, 1, 4, 0, 0, 0, 1, 0, 1],
                                  [0, -3, 0, 0, 0, -3, 0, 1, 0, 0],
                                  [2, 0, 0, 0, 1, 0, 0, 0, -2, 0],
                                  [0, 0, 0, 6, 4, 0, 6, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, -1, 0, 0, 0, -1, 0],
                                  [0, -2, 0, 0, 6, 0, 0, 0, 0, 5],
                                  [1, 0, 0, 0, 1, 0, -5, 1, 0, 1],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [-5, 0, 4, 0, 1, 0, 0, 0, 0, 1]])

        lava_level9 = Level([[2, 0, 0, 0, 0, 0, 0, 0, 0, -3],
                                  [0, 0, -1, 1, 0, 0, 0, -2, 0, 0],
                                  [0, 0, 0, 0, 0, -1, 0, 4, 1, 0],
                                  [1, 0, 6, 0, 0, 0, 0, 1, 0, 0],
                                  [0, -3, 0, 4, 1, 0, 0, 0, 0, -2],
                                  [0, 0, 0, 0, 0, 0, -5, 0, 1, 0],
                                  [0, 1, 0, 0, -5, 0, 6, 0, 0, 0],
                                  [6, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                                  [0, 1, 0, 0, -4, 0, 0, 0, 0, 5],
                                  [-4, 0, 0, 0, 0, 0, 0, 1, 4, -2]])

        lava_level10 = Level([[2, 0, -2, 0, 0, 0, 1, 4, 1, 5],
                                   [6, 0, 0, 0, 0, 0, 0, 6, 4, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [-1, 0, 0, 0,1, -3, 0, 0, 0, 1],
                                   [0, 0, -2, 0, 0, 0, 0, -1, 0, -5],
                                   [0, 0, 1, 0, 6, 0, 1, 0, 0, 0],
                                   [1, 0, 0, 0, 0, -5, 0, 0, 6, 0],
                                   [4, 1, 0, -4, 0, 0, 6, 0, 0, 1],
                                   [0, -4, 0, 0, 0, -3, 1, 0, -1, 0],
                                   [0, 0, 0, 0, -2, 0, 0, 0, 0, -4]])

        lava_levels = [lava_level1, lava_level2, lava_level3, lava_level4, lava_level5, lava_level6, lava_level7, lava_level8, lava_level9, lava_level10]
        
        spaceship_level1 = Spaceship_Level([[2,0,0,0,1,0,0,0],
                                  [0,0,1,0,0,0,0,9],
                                  [1,0,0,0,5,0,0,1],
                                  [0,0,0,0,1,0,1,0],
                                  [8,0,1,0,0,0,0,0],
                                  [0,0,0,0,4,0,0,1],
                                  [1,1,0,0,0,0,0,0],
                                  [4,0,0,3,1,0,0,4]])


        spaceship_level2 = Spaceship_Level([[0,1,0,1,0,0,0,8],
                                  [3,0,5,1,0,0,0,1],
                                  [1,0,4,0,0,0,0,0],
                                  [0,1,0,5,5,4,1,0],
                                  [0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,1],
                                  [1,0,0,0,1,5,4,0],
                                  [2,0,0,0,1,0,1,9]])

        spaceship_level3 = Spaceship_Level([[0,0,0,1,8,0,0,0],
                                  [0,1,0,0,0,1,0,0],
                                  [2,4,0,0,0,0,1,0],
                                  [1,0,0,0,0,0,0,0],
                                  [0,0,0,1,3,0,0,5],
                                  [0,0,0,1,0,1,0,4],
                                  [1,0,0,0,0,0,1,9],
                                  [4,0,1,0,0,0,0,1]])

        spaceship_level4 = Spaceship_Level([[0,1,4,0,0,0,0,1],
                        [1,0,0,0,0,1,0,9],
                        [0,0,0,1,0,0,0,0],
                        [8,0,0,0,0,0,1,0],
                        [1,0,0,0,1,0,0,0],
                        [0,0,0,0,0,0,1,1],
                        [0,1,1,0,0,0,0,3],
                        [5,0,4,1,2,1,0,4]])

        spaceship_level5 = Spaceship_Level([[0,0,4,1,0,0,1,1],
                        [0,0,0,1,0,0,0,8],
                        [0,0,0,0,0,0,0,0],
                        [0,0,1,2,0,1,0,0],
                        [1,0,0,0,1,0,0,0],
                        [0,0,0,1,0,0,1,1],
                        [0,1,0,0,0,0,3,0],
                        [4,9,1,4,0,0,0,1]])

        spaceship_level6 = Spaceship_Level([[1,0,0,1,4,0,0,1,5,0],
                        [0,0,0,5,0,0,0,4,1,0],
                        [0,0,0,0,0,0,1,0,0,0],
                        [0,1,0,0,0,0,0,0,0,9],
                        [0,0,1,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,1,0,0],
                        [2,0,0,0,1,0,0,0,0,0],
                        [1,4,0,0,0,0,0,0,1,0],
                        [1,0,[1,1],[5,1],[5,1],[5,1],1,0,1,0],
                        [1,3,1,1,0,0,1,8,1,0]])


        spaceship_level7 = Spaceship_Level([[4,[6,1],0,0,0,1,0,0,0,0],
                        [1,[7,2,1],[5,2],[5,2],[5,2],[5,2],[5,2],[5,2],[5,2],[2,2]],
                        [2,[6,1],0,0,0,0,0,1,0,0],
                        [0,[6,1],1,0,0,0,0,0,5,0],
                        [0,[6,1],0,0,1,1,0,0,1,0],
                        [0,[6,1],0,0,5,0,1,0,0,0],
                        [0,[6,1],0,0,1,0,0,0,0,0],
                        [0,[6,1],0,0,0,0,3,1,0,0],
                        [0,[6,1],0,1,1,9,1,0,0,0],
                        [0,[4,1],0,0,4,1,4,8,0,1]])

        spaceship_level8 = Spaceship_Level([[4,0,0,0,0,0,5,1,2,0],
                        [1,[5,1],[5,1],[5,1],[5,1],[5,1],[5,1],[5,1],[5,1],[2,1]],
                        [0,0,0,0,0,0,0,0,0,0],
                        [8,0,1,[5,2],[5,2],[5,2],[5,2],[5,2],[5,2],[2,2]],
                        [0,0,0,5,0,0,1,0,0,4],
                        [0,0,0,0,1,[5,3],[5,3],[5,3],[5,3],[2,3]],
                        [0,0,0,0,0,1,[5,4],[5,4],[5,4],[2,4]],
                        [0,0,0,0,1,0,0,0,0,0],
                        [0,1,[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[5,5],[2,5]],
                        [9,4,0,0,0,0,0,0,1,3]])

        spaceship_level9 = Spaceship_Level([[1,[3,1],5,0,0,0,0,0,4,5],
                        [2,[6,1],0,0,0,0,0,0,1,0],
                        [0,[6,1],0,0,0,1,0,0,0,0],
                        [0,[6,1],0,0,1,0,1,0,0,0],
                        [0,[6,1],0,0,[6,2],0,0,0,0,3],
                        [0,[6,1],0,0,[6,2],0,0,0,0,0],
                        [0,1,4,0,[6,2],0,0,0,0,0],
                        [[5,3],[5,3],[5,3],[5,3],[7,3,2],[2,3],0,0,1,0],
                        [0,0,0,0,[4,2],0,0,1,0,0],
                        [0,0,1,0,0,8,9,4,0,1]])        



        spaceship_level10 = Spaceship_Level([[0,8,0,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,5,0,4,0,0,0],
                        [0,0,0,0,0,0,1,0,0,0],
                        [0,0,0,0,0,[1,1],[7,1,2],[5,1],[5,1],1],
                        [0,0,0,0,0,0,[6,2],0,0,0],
                        [0,0,4,1,9,0,[6,2],0,1,0],
                        [1,1,0,0,0,2,[6,2],[1,3],[7,3,4],[5,3]],
                        [0,0,0,0,0,0,[6,2],0,[4,4],3],
                        [[5,5],[5,5],[5,5],[2,5],0,1,[4,2],4,0,1]])

        spaceship_levels = [spaceship_level1, spaceship_level2, spaceship_level3, spaceship_level4, spaceship_level5, spaceship_level6, spaceship_level8, spaceship_level7 , spaceship_level9 , spaceship_level10]
        
        future_level1 = Level([[0, 0, 1, 1, [3], 4, [2], 3],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, [2], [3]],
                              [2, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, [1], 0, 0, 0, 0, 0],
                              [1, 0, 0, 0, 0, 4, 1, 1],
                              [1, 1, 0, 0, 0, 1 ,4, 0],
                              [1, 1, 0, 0, 0, 1, 0, [1]]])
                              


        future_level2 = Level([[1, 0, 0, 0, 0, 0, 0, 4],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, [3], 0, [3], [2], 3],
              [0, 0, 0, 4, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 2],
              [0, 0, 0, 0, 0, 0, 0, [1]],
              [1, 0, [1], 0, 0, 0, 0, 4],
              [0, 0, 0, 0, 0, 0, 1, [2]]])
              

        future_level5 = Level([[[1], 1, [2], 2, 1, 0, [2], 0],
                  [0, 1, 4, [1], 1, 0, 0, 0],
                  [0, 1, 1, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 4, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 4, 0, 0, 0, 0, 0, [3]],
                  [[3], 0, 0, 0, 1, 0, 0, 3]])

        future_level4 = Level([[0, 1, 4, 0, 0, 0, [1], 1],
                  [1, 0, 0, 0, 0, 1, 2, [1]],
                  [0, 0, 0, 0, 0, 0, 0, [3]],
                  [0, 0, 0, 0, [3], 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, [2]],
                  [0, 0, [2], 0, 0, 0, 0, 4],
                  [3, 0, 0, 0, 0, 0, [1], 1],
                  [1, 0, 0, 0, 0, 0, 0, 4]])
           
        future_level3 = Level([[0, 1, 4, 0, 0, 0, [1], 1],
                  [1, 0, 0, 0, 0, 0, 0, [1]],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [3, 0, 0, 0, 0, 0, 0, 0],
                  [4, 0, 0, 0, 0, 0, 1, 2],
                  [[3], 0, [2], 0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, [3], 0, 0, 4, [2], 1]])

        future_level6 = Level([[0, 0, 0, 0, 0, 0, [3], 0, 1, 6],
                   [0, 0, 0, 0, 0, 0, 6, 0, 1, 6],
                   [0, 0, 0, 0, 0, 0, [3], 0, 1, 6],
                   [0, 0, 0, 0, 0, 0, 4, 0, 1, 6],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 6],
                   [[2], 4, 0, 0, 0, 0, 0, 0, 1, 6],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, [2]],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 3],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 4],
                   [2, 0, 0, 0, 0, 0, [1], 0, 6, [1]]])
                   
              
        future_level7 = Level([[6, 6, 6, 6, 6, 6, 6, 6, 1, 3],
                   [6, 6, 6, 6, 6, 6, 6, 6, 1, [3]],
                   [2, 6, 6, 6, 6, 6, 6, 6, 1, 1],
                   [0, 6, 6, 6, 6, 6, 6, [3], 4, [2]],
                   [0, 6, 6, 6, 6, 6, 6, 6, 6, 6],
                   [0, 6, 6, 6, 6, 6, 1, 0, 0, 0],
                   [0, 6, 6, [2], 4, 0, 0, 1, 0, [1]],
                   [0, 6, 6, 6, 6, 6, 0, 0, 0, 0],
                   [0, 6, 6, 6, 6, 1, 0, 0, 0, 0],
                   [[1], 4, 0, 0, 0, 0, 0, 0, 1, 0]])
              
        future_level8 = Level([[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 1, 6, [2], [1]],
                   [3, 6, 4, 1, 0, 0, 0, 1, 0, [1]],
                   [[3], 1, 0, 0, 0, 1, 0, 0, 0, 0],
                   [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, [2], 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, [3], 0],
                   [1, 0, 0, 4, 0, 0, 0, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0, 4, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        future_level9 = Level([[0, 0, 0, 0, 0, 0, 1, 3, 1, 4],
                   [0, [3], 0, 0, 0, 0, 0, 0, 0, [1]],
                   [0, 0, 4, 0, 0, 0, 0, 0, 0, 6],
                   [6, 0, 0, 0, 0, 0, 0, 0, 0, 6],
                   [6, 0, 0, 0, 0, 0, 0, [1], 0, 6],
                   [6, 0, 0, 0, 0, 0, 0, 0, 0, 6],
                   [6, 0, 0, 0, 0, 0, 0, 0, [2], 6],
                   [6, 0, 0, 0, 0, 0, 0, 0, 0, 6],
                   [0, 0, [3], 0, 0, 0, 4, [2], 0, 6],
                   [2, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

        future_level10 = Level([[1, 6, 6, 6, 6, 3, 6, 6, 6, 1],
                   [6, [6], 0, 0, 0, 5, 0, 0, [2], 6],
                   [6, 0, [3], 0, 0, 0, 0, [4], 0, 6],
                   [6, 0, 0, [5], 4, 0, [6], 0, 0, 6],
                   [6, 0, 0, 0, 1, 1, 4, 0, 0, 6],
                   [6, 0, 0, 4, 1, 1, 0, 0, 0, 6],
                   [6, 0, 0, [1], 0, 0, [5], 0, 0, 6],
                   [6, 0, [2], 0, 0, 0, 0, [3], 0, 6],
                   [6, [4], 0, 0, 5, 0, 0, 0, [1], 6],
                   [1, 6, 6, 6, 2, 6, 6, 6, 6, 1]])

        future_levels = [future_level1, future_level2, future_level3, future_level4, future_level5, future_level6, future_level7, future_level8, future_level9, future_level10]

        self.ice_levels = ice_levels
        self.water_levels = water_levels
        self.lava_levels = lava_levels
        self.spaceship_levels = spaceship_levels
        self.future_levels = future_levels
        self.currentWorld = worldName
        self.finished = False
        self.ice_field = Ice_Field(ice_levels)
        self.water_field = Water_Field(water_levels)
        self.lava_field = Lava_Field(lava_levels)
        self.spaceship_field = Spaceship_Field(spaceship_levels)
        self.future_field = Future_Field(future_levels)
        starting_ice = self.ice_field.get_current_level("start",2)
        starting_water = self.water_field.get_current_level("start")
        starting_lava = self.lava_field.get_current_level("start",4)
        starting1_spaceship = self.spaceship_field.get_current_level("start1")
        starting2_spaceship = self.spaceship_field.get_current_level("start2")
        starting_future = [0,3]
        EXTRA_HEIGHT = WIDTH / self.ice_field.get_current_level("dimension")
        tile_size = WIDTH / self.ice_field.get_current_level("dimension")
        speed = [12,12]
        water_speed = [14, 14]
        self.ice_character = [Ice_Character([(tile_size * starting_ice[1]) + tile_size / 2, (tile_size * starting_ice[0]) + tile_size / 2 + (EXTRA_HEIGHT)], speed, main_character_front_image, main_character_front_info, main_character_back_image, main_character_back_info, main_character_left_image, main_character_left_info, main_character_right_image, main_character_right_info)]
        self.water_character = [Water_Character([(tile_size * starting_water[1]) + tile_size / 2, (tile_size * starting_water[0]) + tile_size / 2 + (EXTRA_HEIGHT)], water_speed, water_character_front_image, water_character_front_info, water_character_back_image, water_character_back_info, water_character_left_image, water_character_left_info, water_character_right_image, water_character_right_info)]
        self.lava_character = [Lava_Character([(tile_size * starting_lava[1]) + tile_size / 2, (tile_size * starting_lava[0]) + tile_size / 2 + (EXTRA_HEIGHT)], tile_size / 4, speed, lava_character_front_image, lava_character_front_info, lava_character_back_image, lava_character_back_info, lava_character_left_image, lava_character_left_info, lava_character_right_image, lava_character_right_info)]
        self.spaceship_character = [Spaceship_Normal_Character([(tile_size * starting1_spaceship[1]) + tile_size / 2, (tile_size * starting1_spaceship[0]) + tile_size / 2 + (EXTRA_HEIGHT)], speed, main_character_front_image, main_character_front_info, main_character_back_image, main_character_back_info, main_character_left_image, main_character_left_info, main_character_right_image, main_character_right_info), Spaceship_Alien_Character([(tile_size * starting2_spaceship[1]) + tile_size / 2, (tile_size * starting2_spaceship[0]) + tile_size / 2 + (EXTRA_HEIGHT)], speed, alien_character_front_image, alien_character_front_info, alien_character_back_image, alien_character_back_info, alien_character_left_image, alien_character_left_info, alien_character_right_image, alien_character_right_info)]
        self.future_character = [Future_Character([(tile_size * starting_future[1]) + tile_size / 2, (tile_size * starting_future[0]) + tile_size / 2 + (EXTRA_HEIGHT)], speed, main_character_front_image, main_character_front_info, main_character_back_image, main_character_back_info, main_character_left_image, main_character_left_info, main_character_right_image, main_character_right_info)]


    def get_field(self):
        if self.currentWorld == "ice":
            return self.ice_field
        elif self.currentWorld == "water":
            return self.water_field
        elif self.currentWorld == "lava":
            return self.lava_field
        elif self.currentWorld == "spaceship":
            return self.spaceship_field
        elif self.currentWorld == "future":
            return self.future_field
        else:
            print("world name wrong")
            return "error"
        
    def get_current_world(self):
        return self.currentWorld

    def get_character(self):
        if self.currentWorld == "ice":
            return self.ice_character
        elif self.currentWorld == "water":
            return self.water_character
        elif self.currentWorld == "lava":
            return self.lava_character
        elif self.currentWorld == "spaceship":
            return self.spaceship_character
        elif self.currentWorld == "future":
            return self.future_character
        else:
            print("world name wrong")
            return "error"

    def get_finished(self):
        return self.finished
    
    def finish_world(self):
        self.finished = True
    

class Ice_Character(Character):
    def check_tile(self, field):
        global tile_size, EXTRA_HEIGHT, message, status
        if len(field) == 8:
            tile_size = 68.75
        elif len(field) == 10:
            tile_size = 55.0
        i = ((self.pos[1] - EXTRA_HEIGHT) // tile_size)
        j = (self.pos[0] // tile_size)
        self.location = [i, j]

        currentTileLocation = [self.location[0], self.location[1]]
        currentTile = field[int(currentTileLocation[0])][int(currentTileLocation[1])]

        self.stop_if_last_tile(currentTile)
        self.check_if_won(currentTile, 3)

        if currentTile == 4:# star
            location = self.location
            game_field.get_current_level().change_tile(location,0)
            game_field.get_current_level().collect_star()


        if currentTile == 5 or currentTile == 2  or currentTile == 3: # stopper or start or end
            if self.direction == [1,0]:#right
                finalPosition = (self.location[1] )*tile_size + tile_size/2
                if self.pos[0] >= finalPosition:
                        self.stop_moving()

            elif self.direction == [-1,0]:#left
                finalPosition = (self.location[1]+ 1)*tile_size - tile_size/2
                if self.pos[0] <= finalPosition:
                        self.stop_moving()
            elif  self.direction == [0,-1]:#up
                finalPosition = (self.location[0] + 2)*tile_size - tile_size/2
                if self.pos[1] <= finalPosition:
                        self.stop_moving()

            elif  self.direction == [0,1]:#down
                finalPosition = (self.location[0] + 1)*tile_size + tile_size/2
                if self.pos[1] >= finalPosition:
                        self.stop_moving()



        if currentTile == 6:# water
            self.stop_moving()
            status = "too bad so sad"
            
    def findNextTile(self, field):
        dimension = game_field.get_current_level("dimension")
        dimension = dimension - 1

        if self.direction == [1,0]:#right
            finalPosition = (self.location[1] )*tile_size + tile_size*3/4
            finalPosition2 = (self.location[1] )*tile_size + tile_size/2


            nextTileLocation = [self.location[0], self.location[1] + 1]

            if self.location[1] == dimension:
                        nextTile = 0

            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]


            if nextTile == 1: #rock is next
                if self.pos[0] >= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2

            elif nextTile == 8 :# breakable rock
                 if self.pos[0] >= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
                    field[int(nextTileLocation[0])][int(nextTileLocation[1])] = 9




        elif self.direction == [-1,0]:#left
            finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[1]+ 1)*tile_size - tile_size/2

            nextTileLocation = [self.location[0], self.location[1] - 1]
            nextTile = 0

            if self.location[1] == 0:
                nextTile = 0

            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]

            if nextTile == 1: #rock is next
                if self.pos[0] <= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2

            elif nextTile == 8 :# breakable rock
                if self.pos[0] <= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
                    field[int(nextTileLocation[0])][int(nextTileLocation[1])] = 9




        elif self.direction == [0,-1]:#up

            finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[0] + 2)*tile_size - tile_size/2

            nextTile = 0
            nextTileLocation = [self.location[0] - 1, self.location[1] ]

            if self.location[0] == 0:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]


            if nextTile == 1: #rock is next
                if self.pos[1] <= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2

            elif nextTile == 8 :# breakable rock
                 if self.pos[1] <= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
                    field[int(nextTileLocation[0])][int(nextTileLocation[1])] = 9




        elif self.direction == [0,1]:#down
            finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4
            finalPosition2 = (self.location[0] + 1)*tile_size + tile_size/2

            nextTileLocation = [self.location[0] + 1, self.location[1] ]
            nextTile = 0

            if self.location[0] == dimension:
                nextTile = 0

            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]

            if nextTile == 1: #rock is next
                if self.pos[1] >= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2


            elif nextTile == 8 :# breakable rock
                if self.pos[1] >= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
                    field[int(nextTileLocation[0])][int(nextTileLocation[1])] = 9

    def death_animation(self, canvas):
        main_pos = [status, controller, player]
        new_map = map(str, main_pos)
        if new_map == [0, 0, 0, 1]:
            controller = "unavailable"
            time.sleep(2)
            create_new_character()
            eliminate_previous_character()
            new_angle = math.sin(pos)
        elif type(new_map) == math.radians(pos):
            controller = "nonexistant"
            new_angle = math.tan((4 *  pos[-1] ** 2)/math.cos(self.location**2))
            timer = simplegui.create_timer(3000, death_animation)
            player.new_movement = "beginning"
        
            
        
class Water_Character:
    def __init__(self, pos, vel, front_image, front_info, back_image, back_info, left_image, left_info, right_image, right_info):
        global EXTRA_HEIGHT
        self.pos = pos
        self.vel = vel
        self.front = [front_image, front_info]
        self.back = [back_image, back_info]
        self.left = [left_image, left_info]
        self.right = [right_image, right_info]
        self.moving = False
        self.current_image = front_image
        self.image_info = front_info
        self.direction = [0, 0]
        self.location = [((self.pos[1] - EXTRA_HEIGHT) // tile_size), (self.pos[0] // tile_size)]
        self.stoppedOnce = 0   
        self.pixels_moved = 0
        self.turn = 0
        self.previous_Tile = None
        self.whirlpool_angle = -4.0/30.0
        self.whirlpool_rotate_speed = 4.0/30.0       
        self.sizeratio = 0.5
    def get_moving(self):
        return self.moving        
    def move(self):
        if self.moving == True:
            self.pos[0] += (self.vel[0] * self.direction[0])
            self.pos[1] += (self.vel[1] * self.direction[1])   
            self.pixels_moved = (self.pixels_moved + self.vel[0])
            if (game_field.get_current_level().get_dimension() == 8):
                if self.pixels_moved >= 70.0:
                    self.stop_moving()
            else:
                if self.pixels_moved >= 56.0:
                    self.stop_moving()
    def start_moving(self, direction):
        if self.moving == False:
            self.direction = direction
            self.moving = True
            self.pixels_moved = 0
            self.previous_Tile = None
            if direction == [0, 1]:
                self.current_image = self.front[0]
                self.current_info = self.front[1]
            elif direction == [0, -1]:
                self.current_image = self.back[0]
                self.current_info = self.back[1]
            elif direction == [1, 0]:
                self.current_image = self.right[0]
                self.current_info = self.right[1]
            elif direction == [-1, 0]:
                self.current_image = self.left[0]
                self.current_info = self.left[1]    
                
    def get_pos(self):
        return self.pos
        
    def change_turn(self, new_turn):
        self.turn = new_turn
        
    def stop_moving(self):
        if self.moving == True:
            self.direction = [0, 0]
            self.moving = False
    
    def check_moving(self):
        return self.moving

    def findNextTile(self, field):
        dimension1= game_field.get_current_level("dimension") 
        dimension = dimension1 - 1
        if self.direction == [1,0]:#right
            if self.location[1] >= dimension:
                self.stop_moving()                          
                 
        elif self.direction == [-1,0]:#left
            if self.location[1]<= 0:
                self.stop_moving()
                        
        elif self.direction == [0,-1]:#up 
            if self.location[0] <= 0:
                self.stop_moving()
            
        elif self.direction == [0,1]:#down
            if self.location[0] >= dimension:
                self.stop_moving()
                       
    def get_turn(self):
        return self.turn
        
    def check_tile(self, field):
        global tile_size, EXTRA_HEIGHT, message, status, condition_right, condition_left, condition_up, condition_down
        if len(field) == 8:
            tile_size = 68.75
        elif len(field) == 10:
            tile_size = 55.0
        i = ((self.pos[1] - EXTRA_HEIGHT) // tile_size)
        j = (self.pos[0] // tile_size)
        self.location = [i, j]
        currentTileLocation = [self.location[0], self.location[1]] 
        currentTilex = field[int(currentTileLocation[0])][int(currentTileLocation[1])]
        
        if currentTilex[-1] != 8 and currentTilex[0] != 8 :
            if currentTilex[-(self.turn % 2)] == 0 or currentTilex[-(self.turn % 2)] == 5 or currentTilex[-(self.turn % 2)] == 6 or currentTilex[-(self.turn % 2)] == 8 or currentTilex[-(self.turn % 2)] == 7:
                if self.previous_Tile != currentTileLocation:
                    self.turn = self.turn + 1
        currentTile = currentTilex[-(self.turn % 2)]
        if currentTile == 7:# star
            location = self.location             
            game_field.get_current_level().change_tile(location,[0])
            game_field.get_current_level().collect_star()
        elif currentTile == 1:#right
            self.start_moving([1, 0])
        elif currentTile == 2:#down
            self.start_moving([0, 1])
        elif currentTile == 3:#up
            self.start_moving([0, -1])
        elif currentTile == 4:
            self.start_moving([-1, 0])
        elif currentTile == 6:
            lvl = game_field.get_current_level()
            if lvl.stars == 3:
                status = "LVL"
        elif currentTile == 8:
            status = "too bad so sad"
            
        elif currentTile == 9: 
            lvl = demo_game_field.get_current_level()
            if lvl.stars == 3: 
                self.stop_moving()
                message = "YOU WIN!!!!!!!!"
                timer2.start()
        
        self.previous_Tile = currentTileLocation

    def reset_size(self):
        self.sizeratio = 0.5
        
    def teleport(self):
        global tile_size, EXTRA_HEIGHT, Ttime
        starting = game_field.get_current_level("start")
        tile_size = game_field.get_current_level("tile_size")
        EXTRA_HEIGHT = WIDTH / game_field.get_current_level("dimension")
        self.pos = [(tile_size * starting[1]) + tile_size / 2, (tile_size * starting[0]) + tile_size / 2 + (EXTRA_HEIGHT)]		  
        self.turn = 0
        self.size_ratio = 0.5
        self.current_image = self.front[0]
        self.current_info = self.front[1]
        game_field.get_current_level().reset_level()
        Ttime = 0
        
    def draw(self, canvas):
        self.whirlpool_angle += self.whirlpool_rotate_speed
        if status == "too bad so sad" and self.sizeratio >= 0.2:
            canvas.draw_image(self.current_image, self.image_info.get_center(), self.image_info.get_size(), self.pos, [self.sizeratio * tile_size/ 0.6, self.sizeratio * tile_size / 0.6], self.whirlpool_angle)            
            self.sizeratio -= 0.015
        elif status != "too bad so sad":  
            self.sizeratio = 0.5
            canvas.draw_image(self.current_image, self.image_info.get_center(), self.image_info.get_size(), self.pos, [tile_size * 1, tile_size * 1])
        
        



class Lava_Character(Character):
    def __init__(self, pos, radius, vel, front_image, front_info, back_image, back_info, left_image, left_info, right_image, right_info):
        global EXTRA_HEIGHT
        self.pos = pos
        self.vel = vel
        self.front = [front_image, front_info]
        self.back = [back_image, back_info]
        self.left = [left_image, left_info]
        self.right = [right_image, right_info]
        self.moving = False
        self.current_image = front_image
        self.image_info = front_info
        self.direction = [0, 0]
        self.location = [((self.pos[1] - EXTRA_HEIGHT) // tile_size), (self.pos[0] // tile_size)]
        self.stoppedOnce = 0   
        self.radius = radius
        self.turn = 0
        self.pixels_moved = 0
        self.prevTile = 0
        self.condition = False
    def get_direction(self):
        return self.direction

    def get_radius(self):
        return self.radius

    def get_image_info(self):
        return self.image_info
    def get_turns(self):
        return self.turn

    def get_image(self):
        return self.current_image

    def check_tile(self, field):
        global tile_size, EXTRA_HEIGHT, message, status
        if len(field) == 8:
            tile_size = 68.75
        elif len(field) == 10:
            tile_size = 55.0
        i = ((self.pos[1] - EXTRA_HEIGHT) // tile_size)
        j = (self.pos[0] // tile_size)
        self.location = [i, j]

        currentTileLocation = [self.location[0], self.location[1]]
        currentTile =  field[int(currentTileLocation[0])][int(currentTileLocation[1])]
        self.location = currentTileLocation
        self.stop_if_last_tile(currentTile)
        self.check_if_won(currentTile, 5)
        #if self.condition == False:
        if self.prevTile != currentTileLocation and self.condition == False and currentTile >= 0:
            self.turn = (self.turn + 1) % 6
            self.condition = True
            
        if currentTile == 4:# star
            location = self.location
            game_field.get_current_level().change_tile(location,0)
            game_field.get_current_level().collect_star()

        elif currentTile < 0:
            explode = -(currentTile)
            if self.turn == explode:
                status = "too bad so sad"
                self.stop_moving()
        self.location = currentTileLocation

    def move(self):
        if self.moving == True:
            self.pos[0] += (self.vel[0] * self.direction[0])
            self.pos[1] += (self.vel[1] * self.direction[1])        
    def start_moving(self, direction):
        if self.moving == False:
            self.direction = direction
            self.moving = True
            self.pixels_moved = 0
            if direction == [0, 1]:
                self.current_image = self.front[0]
                self.current_info = self.front[1]
            elif direction == [0, -1]:
                self.current_image = self.back[0]
                self.current_info = self.back[1]
            elif direction == [1, 0]:
                self.current_image = self.right[0]
                self.current_info = self.right[1]
            elif direction == [-1, 0]:
                self.current_image = self.left[0]
                self.current_info = self.left[1]    
                
            
    def stop_moving(self):
        if self.moving == True:
            self.direction = [0, 0]
            self.moving = False
            self.condition = False
            self.prevTile = self.location
            
    def bounce(self):
        global bounce_condition
        self.pos[0] -= self.vel[0] * self.direction[0]
        self.pos[1] -= self.vel[1] * self.direction[1]  
        self.pixels_moved = self.pixels_moved + self.vel[0]
        if self.pixels_moved >= tile_size / 3:
            self.stop_moving()
            bounce_condition = False

    def findNextTile(self, field):

        dimension = (game_field.get_current_level("dimension"))- 1

        if self.direction == [1,0]:#right
            finalPosition = (self.location[1] )*tile_size + tile_size*3/4
            finalPosition2 = (self.location[1] )*tile_size + tile_size/2

            nextTileLocation = [self.location[0], self.location[1] + 1]

            if self.location[1] == dimension:
                        nextTile = 0

            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]


            if nextTile == 1: #rock is next
                if self.pos[0] >= finalPosition:

                    self.stop_moving()
                    self.pos[0] = finalPosition2
                    condition_right = True
                    condition_left = False
                    condition_up = False
                    condition_down = False


        elif self.direction == [-1,0]:#left
            finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[1]+ 1)*tile_size - tile_size/2

            nextTileLocation = [self.location[0], self.location[1] - 1]
            nextTile = 0

            if self.location[1]== 0:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]

            if nextTile == 1: #rock is next
                if self.pos[0] <= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2


        elif self.direction == [0,-1]:#up

            finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[0] + 2)*tile_size - tile_size/2
            nextTile = 0
            nextTileLocation = [self.location[0] - 1, self.location[1] ]

            if self.location[0] == 0:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]

            if nextTile == 1: #rock is next
                if self.pos[1] <= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2


        elif self.direction == [0,1]:#down
            finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4
            finalPosition2 = (self.location[0] + 1)*tile_size + tile_size/2

            nextTileLocation = [self.location[0] + 1, self.location[1] ]
            nextTile = 0

            if self.location[0] == dimension:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]

            if nextTile == 1: #rock is next
                if self.pos[1] >= finalPosition:

                    self.stop_moving()
                    self.pos[1] = finalPosition2

    def draw(self, canvas):
        canvas.draw_image(self.current_image, self.image_info.get_center(), self.image_info.get_size(), self.pos, [tile_size/ 2, tile_size / 2])

        
    

class Movable_Rock(Lava_Character):

    def move(self):
        if self.moving == True:
            self.pos[0] += self.vel[0] * self.direction[0]
            self.pos[1] += self.vel[1] * self.direction[1]  
            self.pixels_moved = self.pixels_moved + self.vel[0]
            if self.pixels_moved >= tile_size:
                self.stop_moving()

    def collide(self, other_object):
        global bounce_condition
        r1 = self.get_radius()
        r2 = other_object.get_radius()
        pos1 = self.pos
        pos2 = other_object.get_pos()
        if dist(pos1, pos2) < r1 + r2:
            self.start_moving(other_object.get_direction())
            direction = other_object.get_direction()
            bounce_condition = True
            other_object.start_moving([-(direction[0]), -(direction[1])])


    def check_tile(self, field):
        global tile_size, EXTRA_HEIGHT, message, status
        if len(field) == 8:
            tile_size = 68.75
        elif len(field) == 10:
            tile_size = 55.0
        i = ((self.pos[1] - EXTRA_HEIGHT) // tile_size)
        j = (self.pos[0] // tile_size)
        self.location = [i, j]

        currentTileLocation = [self.location[0], self.location[1]]
        currentTile =  field[int(currentTileLocation[0])][int(currentTileLocation[1])]

        self.stop_if_last_tile(currentTile)

        if currentTile == 5:
            if self.direction == [1,0]:#right
                finalPosition = (self.location[1] )*tile_size + tile_size*3/4
                if self.pos[0] >= finalPosition:
                    self.stop_moving()

            elif self.direction == [-1,0]:#left
                finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
                if self.pos[0] <= finalPosition:
                    self.stop_moving()
            elif  self.direction == [0,-1]:#up
                finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
                if self.pos[1] <= finalPosition:
                    self.stop_moving()

            elif  self.direction == [0,1]:#down
                finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4
                if self.pos[1] >= finalPosition:
                    self.stop_moving()


class Spaceship_Character:
    def __init__(self, pos, vel, front_image, front_info, back_image, back_info, left_image, left_info, right_image, right_info):
        global EXTRA_HEIGHT
        self.pos = pos
        self.vel = vel
        self.front = [front_image, front_info]
        self.back = [back_image, back_info]
        self.left = [left_image, left_info]
        self.right = [right_image, right_info]
        self.moving = False
        self.current_image = front_image
        self.image_info = front_info
        self.direction = [0, 0]
        self.location = [((self.pos[1] - EXTRA_HEIGHT) // tile_size), (self.pos[0] // tile_size)]
        self.stoppedOnce = 0   
  
    def get_location(self):
        return self.location
        
    def get_moving(self):
        return self.moving
    
    def move(self):
        if self.moving == True:
            self.pos[0] += (self.vel[0] * self.direction[0])
            self.pos[1] += (self.vel[1] * self.direction[1])        
    def start_moving(self, direction):
        if self.moving == False:
            self.direction = direction
            self.moving = True
            if direction == [0, 1]:
                self.current_image = self.front[0]
                self.current_info = self.front[1]
            elif direction == [0, -1]:
                self.current_image = self.back[0]
                self.current_info = self.back[1]
            elif direction == [1, 0]:
                self.current_image = self.right[0]
                self.current_info = self.right[1]
            elif direction == [-1, 0]:
                self.current_image = self.left[0]
                self.current_info = self.left[1]

                
                
    def stop_moving(self):
        if self.moving == True:
            self.direction = [0, 0]
            self.moving = False
    def check_moving(self):
        return self.moving
    def findNextTile(self, field, otherCharecterLocation):
        dimension1= game_field.get_current_level("dimension") 
        dimension = dimension1 - 1
        if self.direction == [1,0]:#right
            finalPosition = (self.location[1] )*tile_size + tile_size*3/4
            finalPosition2 = (self.location[1] )*tile_size + tile_size/2
            previousTileLocation = [self.location[0], self.location[1] - 1]
            nextTileLocation = [self.location[0], self.location[1] + 1]
            if self.location[1] == dimension:
                        nextTile = 0
            
                   
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
                        
            
            if nextTile == 1 or nextTileLocation == otherCharecterLocation: #rock is next or other charecter
                if self.pos[0] >= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
                   
        
        elif self.direction == [-1,0]:#left
            finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[1]+ 1)*tile_size - tile_size/2
            nextTileLocation = [self.location[0], self.location[1] - 1]
            nextTile = 0
            if self.location[1] == 0:
                nextTile = 0
                    
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
            if nextTile == 1 or nextTileLocation == otherCharecterLocation: #rock is next or other charecter

                if self.pos[0] <= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
                    
            
        elif self.direction == [0,-1]:#up 
            
            finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[0] + 2)*tile_size - tile_size/2
            nextTile = 0
            nextTileLocation = [self.location[0] - 1, self.location[1] ] 
            if self.location[0] == 0:
                nextTile = 0
            
           
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
                        
            if nextTile == 1 or nextTileLocation == otherCharecterLocation: #rock is next or other charecter

                if self.pos[1] <= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
                    
            
        elif self.direction == [0,1]:#down
            finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4
            finalPosition2 = (self.location[0] + 1)*tile_size + tile_size/2
            nextTileLocation = [self.location[0] + 1, self.location[1] ] 
            nextTile = 0
            if self.location[0] == dimension:
                nextTile = 0
            
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
            
            if nextTile == 1 or nextTileLocation == otherCharecterLocation: #rock is next or other charecter

                if self.pos[1] >= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
                    
                            
        
        elif self.direction == [-1,0]:#left
            finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
            nextTileLocation = [self.location[0], self.location[1] - 1]
            nextTile = 0
            if self.location[1]== 0:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
            if nextTile == 1: #rock is next
                if self.pos[0] <= finalPosition:
                    self.stop_moving()
                    
            
        elif self.direction == [0,-1]:#up 
            
            finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
            nextTile = 0
            nextTileLocation = [self.location[0] - 1, self.location[1] ] 
            if self.location[0] == 0:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
                        
            if nextTile == 1: #rock is next
                if self.pos[1] <= finalPosition:
                    
                    self.stop_moving()
                    
            
        elif self.direction == [0,1]:#down
            finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4
            nextTileLocation = [self.location[0] + 1, self.location[1] ] 
            nextTile = 0
            if self.pos[0] == dimension:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
            
            if nextTile == 1: #rock is next
                if self.pos[1] >= finalPosition:
                    self.stop_moving()
    
            
    def draw(self, canvas):
        canvas.draw_image(self.current_image, self.image_info.get_center(), self.image_info.get_size(), self.pos, [tile_size/ 2, tile_size / 2])

class Spaceship_Alien_Character(Spaceship_Character) :
        
    def check_tile(self, field):
        global tile_size, EXTRA_HEIGHT, message, status, condition_right, condition_left, condition_up, condition_down, character2_finish
        if len(field) == 8:
            tile_size = 68.75
            EXTRA_HEIGHT = 68.75
        elif len(field) == 10:
            tile_size = 55.0
            EXTRA_HEIGHT = 55.0
        i = ((self.pos[1] - EXTRA_HEIGHT) // tile_size)
        j = (self.pos[0] // tile_size)
        self.location = [i, j]
        character2_finish = False
        currentTileLocation = [self.location[0], self.location[1]] 
        currentTile =  field[int(currentTileLocation[0])][int(currentTileLocation[1])]
        if currentTile == 4:# star
            location = self.location
            game_field.get_current_level().change_tile(location,0)
            game_field.get_current_level().collect_star()
        
        dimension = game_field.get_current_level("dimension")
        if self.direction == [1,0]:#right  
            location = self.location[1] + 1 
            finalPosition = (self.location[1] )*tile_size + tile_size*3/4
            finalPosition2 = (self.location[1] )*tile_size + tile_size/2
            if location == dimension:
                 if self.pos[0] >= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
        
        elif self.direction == [-1,0]:#left
            finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[1]+ 1)*tile_size - tile_size/2
            if self.location[1] == 0:
                 if self.pos[0] <= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
        elif  self.direction == [0,-1]:#up
            finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[0] + 2)*tile_size - tile_size/2
            if self.location[0] == 0:
                if self.pos[1] <= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
                
        elif  self.direction == [0,1]:#down
            finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4 
            finalPosition2 = (self.location[0] + 1)*tile_size + tile_size/2 
            location = self.location[0] + 1 
            if location == dimension:
                if self.pos[1] >= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
            
        if currentTile == 5:
            if self.direction == [1,0]:#right  
                finalPosition = (self.location[1] )*tile_size + tile_size * 0.5
                if self.pos[0] >= finalPosition:
                        self.stop_moving()

            elif self.direction == [-1,0]:#left
                finalPosition = (self.location[1]+ 1)*tile_size - tile_size * 0.5
                if self.pos[0] <= finalPosition:
                        self.stop_moving()
            elif  self.direction == [0,-1]:#up
                finalPosition = (self.location[0] + 2)*tile_size - tile_size * 0.5
                if self.pos[1] <= finalPosition:
                        self.stop_moving()

            elif  self.direction == [0,1]:#down
                finalPosition = (self.location[0] + 1)*tile_size + tile_size * 0.5       
                if self.pos[1] >= finalPosition:
                        self.stop_moving()
        if currentTile == 9:
            character2_finish = True 
            lvl = game_field.get_current_level()
            if lvl.stars == 3 and character1_finish == True :
                status = "LVL"
        if type(currentTile)== list:
            

            if currentTile[0] == 1 or currentTile[0] == 2 or currentTile[0] == 3 or currentTile[0] == 4:
                for i in range(0, game_field.get_current_level("dimension")):
                    for j in range(0, game_field.get_current_level("dimension")):
                        tile = field[i][j]
                        if type(tile) == list:# laser related
                            if tile[1] == currentTile[1] and (tile[0] == 5 or tile[0] == 6) and len(tile) == 2 :
                                   game_field.get_current_level().change_tile([i,j], 0)
                            elif len(tile) == 3:# cross laser
                                    if tile[1] == currentTile[1]:
                                        laserNotRemovedCode = tile[2]
                                        newTile = [6 , laserNotRemovedCode]
                                        game_field.get_current_level().change_tile([i,j], newTile)


                                    elif tile[2] == currentTile[1]:
                                        laserNotRemovedCode = tile[1]
                                        newTile = [5 , laserNotRemovedCode]
                                        game_field.get_current_level().change_tile([i,j], newTile)
                location = self.location
                game_field.get_current_level().change_tile(location ,5)
            
            elif currentTile[0] == 5 or currentTile[0] == 6 or currentTile[0] == 7:
                lvl = game_field.get_current_level()
                self.stop_moving()
                starting = game_field.get_current_level("start1")
                EXTRA_HEIGHT = WIDTH / game_field.get_current_level("dimension")
                tile_size = WIDTH / game_field.get_current_level("dimension")
                self.pos = [(tile_size * starting[1]) + tile_size / 2, (tile_size * starting[0]) + tile_size / 2 + (EXTRA_HEIGHT)]	
                message = "Lasers will kill you!!!!"
                timer.start()



            

            

            
       
        
      
    def teleport(self):
        starting = game_field.get_current_level("start2")
        EXTRA_HEIGHT = WIDTH / game_field.get_current_level("dimension")
        tile_size = WIDTH / game_field.get_current_level("dimension")
        self.pos = [(tile_size * starting[1]) + tile_size / 2, (tile_size * starting[0]) + tile_size / 2 + (EXTRA_HEIGHT)]		  
class Spaceship_Normal_Character(Spaceship_Character):     
    def check_tile(self, field):
        global tile_size, character1_finished, EXTRA_HEIGHT, message, status, condition_right, condition_left, condition_up, condition_down
        character1_0finished = False
        if len(field) == 8:
            tile_size = 68.75
            EXTRA_HEIGHT = 68.75
        elif len(field) == 10:
            tile_size = 55.0
            EXTRA_HEIGHT = 55.0      
        i = ((self.pos[1] - EXTRA_HEIGHT) // tile_size)
        j = (self.pos[0] // tile_size)
        self.location = [i, j]
        currentTileLocation = [self.location[0], self.location[1]]
        currentTile =  field[int(currentTileLocation[0])][int(currentTileLocation[1])]
        location = self.location

        if currentTile == 4:# star
             
            game_field.get_current_level().change_tile(location,0)
            game_field.get_current_level().collect_star()
        
        dimension = game_field.get_current_level("dimension")
        if self.direction == [1,0]:#right  
            location = self.location[1] + 1 
            finalPosition = (self.location[1] )*tile_size + tile_size*3/4
            finalPosition2 = (self.location[1] )*tile_size + tile_size/2
            if location == dimension:
                 if self.pos[0] >= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
        
        elif self.direction == [-1,0]:#left
            finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[1]+ 1)*tile_size - tile_size/2
            if self.location[1] == 0:
                 if self.pos[0] <= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
        elif  self.direction == [0,-1]:#up
            finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[0] + 2)*tile_size - tile_size/2
            if self.location[0] == 0:
                if self.pos[1] <= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
                
        elif  self.direction == [0,1]:#down
            finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4 
            finalPosition2 = (self.location[0] + 1)*tile_size + tile_size/2 
            location = self.location[0] + 1 
            if location == dimension:
                if self.pos[1] >= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
            
        if currentTile == 5:
            if self.direction == [1,0]:#right  
                finalPosition = (self.location[1] )*tile_size + tile_size * 0.5
                if self.pos[0] >= finalPosition:
                        self.stop_moving()

            elif self.direction == [-1,0]:#left
                finalPosition = (self.location[1]+ 1)*tile_size - tile_size * 0.5
                if self.pos[0] <= finalPosition:
                        self.stop_moving()
            elif  self.direction == [0,-1]:#up
                finalPosition = (self.location[0] + 2)*tile_size - tile_size * 0.5
                if self.pos[1] <= finalPosition:
                        self.stop_moving()

            elif  self.direction == [0,1]:#down
                finalPosition = (self.location[0] + 1)*tile_size + tile_size * 0.5            
                if self.pos[1] >= finalPosition:
                        self.stop_moving()
        if currentTile == 3:
            character1_finish = True
            lvl = game_field.get_current_level()
            if lvl.stars == 3 and character2_finish == True :
                status = "LVL"
        
        if type(currentTile)== list:
            

            if currentTile[0] == 1 or currentTile[0] == 2 or currentTile[0] == 3 or currentTile[0] == 4:
                for i in range(0, game_field.get_current_level("dimension")):
                    for j in range(0, game_field.get_current_level("dimension")):
                        tile = field[i][j]
                        if type(tile) == list:# laser related
                            if tile[1] == currentTile[1] and (tile[0] == 5 or tile[0] == 6) and len(tile) == 2 :
                                   game_field.get_current_level().change_tile([i,j], 0)
                            elif len(tile) == 3:# cross laser
                                    if tile[1] == currentTile[1]:
                                        laserNotRemovedCode = tile[2]
                                        newTile = [6 , laserNotRemovedCode]
                                        game_field.get_current_level().change_tile([i,j], newTile)


                                    elif tile[2] == currentTile[1]:
                                        laserNotRemovedCode = tile[1]
                                        newTile = [5 , laserNotRemovedCode]
                                        game_field.get_current_level().change_tile([i,j], newTile)
                location = self.location
                game_field.get_current_level().change_tile(location ,5)
            
            elif currentTile[0] == 5 or currentTile[0] == 6 or currentTile[0] == 7:
                self.stop_moving()
                status = "too bad so sad"


                
                
        
    
    def teleport(self):
        starting = game_field.get_current_level("start1")
        EXTRA_HEIGHT = WIDTH / game_field.get_current_level("dimension")
        tile_size = WIDTH / game_field.get_current_level("dimension")
        self.pos = [(tile_size * starting[1]) + tile_size / 2, (tile_size * starting[0]) + tile_size / 2 + (EXTRA_HEIGHT)]		      



class Spaceship_Level:
    def __init__(self, layout):
        self.layout = layout
        self.tile_size = WIDTH / (len(layout))
        starting_point1 = [0, 0]
        starting_point2 = [0, 0]
        for i in range(len(layout)):
            for j in range(len(layout[i])):
                if layout[i][j] == 2:
                    starting_point1 = [i, j]
                if layout[i][j] == 8:
                    starting_point2 = [i, j]
        self.starting_point1 = starting_point1
        self.starting_point2 = starting_point2
        self.dimension = len(layout)
        self.played = False
        self.stars = 0
        self.max_stars = 0
        self.changed_tiles = []
        self.record = 599

    def set_record(self, newRec):
        self.record = min(newRec, self.record)

    def get_record(self):
        return self.record
    
    def get_dimension(self):
        return int(self.dimension)
    
    def reset_level(self):
        global movable_rock_list
        for element in self.changed_tiles:
            if type(element[0]) == list:
                self.layout[int(element[0][0])][int(element[0][1])] = element[1]
                movable_rock_list = []
                self.stars = 0
                
    def get_layout(self):
        return self.layout
    
    def get_start(self):
        startPoints = [self.starting_point1 , self.starting_point2]
        return startPoints
    
    def get_tile_size(self):
        return self.tile_size
       
    def change_tile(self, coordinate, new_tile):
        oldTile = self.layout[int(coordinate[0])][int(coordinate[1])]
        if oldTile == 9:
            self.changed_tiles.append([coordinate, 8])
        else:
            self.changed_tiles.append([coordinate, oldTile])

        self.layout[int(coordinate[0])][int(coordinate[1])] = new_tile
        
    def collect_star(self):
        global notice
        self.stars += 1
        notice = True
        timerA.start()
    
    def check_stars(self):
        if self.stars >= self.max_stars:
            self.max_stars = self.stars
    def get_played(self):
        return self.played

    
    def play_level(self):
        self.played = True
        self.stars = 0
        
    def get_stars(self, max = None):
        if max == True:
            return self.max_stars
        return self.stars
    
        


class Future_Character:
    def __init__(self, pos, vel, front_image, front_info, back_image, back_info, left_image, left_info, right_image, right_info):
        global EXTRA_HEIGHT
        self.pos = pos
        self.vel = vel
        self.front = [front_image, front_info]
        self.back = [back_image, back_info]
        self.left = [left_image, left_info]
        self.right = [right_image, right_info]
        self.moving = False
        self.current_image = front_image
        self.image_info = front_info
        self.direction = [0, 0]
        self.location = [((self.pos[1] - EXTRA_HEIGHT) // tile_size), (self.pos[0] // tile_size)]

        self.stoppedOnce = 0   
        self.on_teleporter = False
        self.prevTile = 0
        self.tele_coord = []
        self.sizeRatio = 1.0
        self.condition = False
        j = self.location[1]
        i = self.location[0]
        self.pos = [tile_size / 2 + tile_size * (i), tile_size / 2 + tile_size * (j + 1)]


    def countdown(self, final, initial, creator, player, time):
        pass

        
    def set_tele(self, boolean):
        self.on_teleporter = boolean
    def set_condition(self, boolean):
        self.condition = boolean
        
    
    def check_tile(self, field):
        global tile_size, EXTRA_HEIGHT, message, status, condition_right, condition_left, condition_up, condition_down
        if len(field) == 8:
            tile_size = 68.75
            EXTRA_HEIGHT = 68.75
        elif len(field) == 10:
            tile_size = 55.0
            EXTRA_HEIGHT = 55.0
        i = ((self.pos[1] - EXTRA_HEIGHT) // tile_size)
        j = (self.pos[0] // tile_size)
        self.location = [i, j]
        currentTileLocation = [self.location[0], self.location[1]]
        currentTile = field[int(currentTileLocation[0])][int(currentTileLocation[1])]
        if currentTile == 4:# star
            location = self.location
             
            game_field.get_current_level().change_tile(location,0)
            game_field.get_current_level().collect_star()
        
        dimension = game_field.get_current_level("dimension")
        if self.direction == [1,0]:#right  
            location = self.location[1] + 1 
            finalPosition = (self.location[1] )*tile_size + tile_size*3/4
            finalPosition2 = (self.location[1] )*tile_size + tile_size/2
            if location == dimension:
                 if self.pos[0] >= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
        
        elif self.direction == [-1,0]:#left
            finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[1]+ 1)*tile_size - tile_size/2
            if self.location[1] == 0:
                 if self.pos[0] <= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
        elif  self.direction == [0,-1]:#up
            finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[0] + 2)*tile_size - tile_size/2
            if self.location[0] == 0:
                if self.pos[1] <= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
                
        elif  self.direction == [0,1]:#down
            finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4 
            finalPosition2 = (self.location[0] + 1)*tile_size + tile_size/2 
            location = self.location[0] + 1 
            if location == dimension:
                if self.pos[1] >= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
            
        if currentTile == 5 or currentTile == 2 or currentTile == 3:
            if self.direction == [1,0]:#right  
                finalPosition = (self.location[1] )*tile_size + tile_size/2
                if self.pos[0] >= finalPosition:
                        self.stop_moving()

            elif self.direction == [-1,0]:#left
                finalPosition = (self.location[1]+ 1)*tile_size - tile_size/2
                if self.pos[0] <= finalPosition:
                        self.stop_moving()
            elif  self.direction == [0,-1]:#up
                finalPosition = (self.location[0] + 2)*tile_size - tile_size/2
                if self.pos[1] <= finalPosition:
                        self.stop_moving()

            elif  self.direction == [0,1]:#down
                finalPosition = (self.location[0] + 1)*tile_size + tile_size/2            
                if self.pos[1] >= finalPosition:
                        self.stop_moving()
        if currentTile == 3:
            lvl = game_field.get_current_level()
            if lvl.stars == 3:
                status = "LVL"
        
            else:
                if self.direction == [1,0]:#right  
                    finalPosition = (self.location[1] )*tile_size + tile_size*3/4
                    if self.pos[0] >= finalPosition:
                            self.stop_moving()

                elif self.direction == [-1,0]:#left
                    finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
                    if self.pos[0] <= finalPosition:
                            self.stop_moving()
                elif  self.direction == [0,-1]:#up
                    finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
                    if self.pos[1] <= finalPosition:
                            self.stop_moving()

                elif  self.direction == [0,1]:#down
                    finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4            
                    if self.pos[1] >= finalPosition:
                            self.stop_moving()


            
        if currentTile == 6:
            lvl = game_field.get_current_level()
            self.stop_moving()
            status = "too bad so sad"
            
        
        if currentTile == 7: 
            lvl = game_field.get_current_level()
            if lvl.stars == 3: 
                self.stop_moving()
                message = "YOU WIN!!!!!!!!"
                timer2.start()
        if type(currentTile) == list and self.on_teleporter == False and self.prevTile != currentTile:
            for i in range(0, int(game_field.get_current_level("dimension"))):
                for j in range(0, game_field.get_current_level("dimension")):
                    if [i, j] != currentTileLocation and field[i][j] == currentTile:
                        self.tele_coord = [j, i]
                        self.location = [j, i]
                        self.stop_moving()
                        self.pos = [tile_size / 2 + tile_size * (j), tile_size / 2 + tile_size * (i + 1)]
                                                
                        
        elif self.prevTile != currentTile:
            self.on_teleporter = False
        self.prevTile = currentTile
    def set_tele_coord(self, coord):
        self.tele_coord = coord
        
    def move(self):
        if self.moving == True:
            self.pos[0] += (self.vel[0] * self.direction[0])
            self.pos[1] += (self.vel[1] * self.direction[1])
        
    def start_moving(self, direction):
        if self.moving == False:
            self.direction = direction
            self.moving = True
            if direction == [0, 1]:
                self.current_image = self.front[0]
                self.current_info = self.front[1]
            elif direction == [0, -1]:
                self.current_image = self.back[0]
                self.current_info = self.back[1]
            elif direction == [1, 0]:
                self.current_image = self.right[0]
                self.current_info = self.right[1]
            elif direction == [-1, 0]:
                self.current_image = self.left[0]
                self.current_info = self.left[1]

    def stop_moving(self):
        if self.moving == True:
            self.direction = [0, 0]
            self.moving = False
        
    def get_moving(self):
        return self.moving
    def findNextTile(self, field):
        dimension1= game_field.get_current_level("dimension") 
        dimension = dimension1 - 1
        if self.direction == [1,0]:#right
            finalPosition = (self.location[1] )*tile_size + tile_size*3/4
            finalPosition2 = (self.location[1] )*tile_size + tile_size/2
            nextTileLocation = [self.location[0], self.location[1] + 1]
            if self.location[1] == dimension:
                        nextTile = 0
                           
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
                        
            
            if nextTile == 1: #rock is next
                if self.pos[0] >= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
                    condition_right = True
                    condition_left = False
                    condition_up = False
                    condition_down = False
        
        elif self.direction == [-1,0]:#left
            finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[1]+ 1)*tile_size - tile_size/2
            nextTileLocation = [self.location[0], self.location[1] - 1]
            nextTile = 0
            if self.location[1]== 0:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
            if nextTile == 1: #rock is next
                if self.pos[0] <= finalPosition:
                    self.stop_moving()
                    self.pos[0] = finalPosition2
                    condition_left = True
                    condition_right = False
                    condition_up = False
                    condition_down = False
            
        elif self.direction == [0,-1]:#up 
            
            finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
            finalPosition2 = (self.location[0] + 2)*tile_size - tile_size/2
            nextTile = 0
            nextTileLocation = [self.location[0] - 1, self.location[1] ] 
            if self.location[0] == 0:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
                        
            if nextTile == 1: #rock is next
                if self.pos[1] <= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
                    condition_up = True
                    condition_left = False
                    condition_right = False
                    condition_down = False
            
        elif self.direction == [0,1]:#down
            finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4
            finalPosition2 = (self.location[0] + 1)*tile_size + tile_size/2
            nextTileLocation = [self.location[0] + 1, self.location[1] ] 
            nextTile = 0
            if self.location[0] == dimension:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
            
            if nextTile == 1: #rock is next
                if self.pos[1] >= finalPosition:
                    self.stop_moving()
                    self.pos[1] = finalPosition2
                    condition_down = True
                    condition_left = False
                    condition_up = False
                    condition_right = False
                            
        
        elif self.direction == [-1,0]:#left
            finalPosition = (self.location[1]+ 1)*tile_size - tile_size*3/4
            nextTileLocation = [self.location[0], self.location[1] - 1]
            nextTile = 0
            if self.location[1]== 0:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
            if nextTile == 1: #rock is next
                if self.pos[0] <= finalPosition:
                    self.stop_moving()
                    
            
        elif self.direction == [0,-1]:#up 
            
            finalPosition = (self.location[0] + 2)*tile_size - tile_size*3/4
            nextTile = 0
            nextTileLocation = [self.location[0] - 1, self.location[1] ] 
            if self.location[0] == 0:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
                        
            if nextTile == 1: #rock is next
                if self.pos[1] <= finalPosition:
                    
                    self.stop_moving()
                    
            
        elif self.direction == [0,1]:#down
            finalPosition = (self.location[0] + 1)*tile_size + tile_size*3/4
            nextTileLocation = [self.location[0] + 1, self.location[1] ] 
            nextTile = 0
            if self.pos[0] == dimension:
                nextTile = 0
            else:
                nextTile = field[int(nextTileLocation[0])][int(nextTileLocation[1])]
            
            if nextTile == 1: #rock is next
                if self.pos[1] >= finalPosition:
                    self.stop_moving()
    def teleportation(self):
        location = self.tele_coord
        self.pos = [(tile_size * location[0]) + tile_size / 2, (tile_size * location[1]) + tile_size / 2 + (EXTRA_HEIGHT)]		  
        self.tele_coord = []
        
    def teleport(self):
        starting = game_field.get_current_level("start")
        i = starting[0]
        j = starting[1]
        self.location = [i, j]                 
        EXTRA_HEIGHT = WIDTH / game_field.get_current_level("dimension")
        tile_size = WIDTH / game_field.get_current_level("dimension")
        self.pos = [(tile_size * starting[1]) + tile_size / 2, (tile_size * starting[0]) + tile_size / 2 + (EXTRA_HEIGHT)]

    def draw(self, canvas):
        if self.tele_coord != [] and self.sizeRatio > 0.1 and self.condition == True:
            self.sizeRatio -= 0.05
        elif self.sizeRatio < 1.0 and self.tele_coord == []:
            self.sizeRatio += 0.05

        canvas.draw_image(self.current_image, self.image_info.get_center(), self.image_info.get_size(), self.pos, [tile_size/ 2 * self.sizeRatio, tile_size / 2 * self.sizeRatio])

class Ice_Field(Field):
    def draw(self, canvas):
        field = self.current_layout
        tile_size = self.current_tile_size
        for i in range(0, int(self.current_dimension)):
            canvas.draw_line([tile_size + (tile_size * i), EXTRA_HEIGHT], [tile_size + (tile_size * i), HEIGHT + EXTRA_HEIGHT],0.75, "White")
            #pygame.draw.line(canvas, white, [tile_size + (tile_size * i), EXTRA_HEIGHT], [tile_size + (tile_size * i), HEIGHT + EXTRA_HEIGHT], 1)
            for j in range(0, self.current_dimension):
                canvas.draw_line([0, tile_size + (tile_size * j)], [WIDTH, tile_size + (tile_size * j)],0.75, "White")
                #pygame.draw.line(canvas, white, [tile_size + (tile_size * i), EXTRA_HEIGHT], [tile_size + (tile_size * i), HEIGHT + EXTRA_HEIGHT], 1)
                if field[i][j] == 1:
                    #canvas.blit(ice_rock_image[0], [ice_rock_info.get_corner(), ice_rock_info.get_size()])
                    canvas.draw_image(ice_rock_image, ice_rock_info.get_center(), ice_rock_info.get_size(), [tile_size / 2 + (tile_size * j),tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                if field[i][j] == 2:
                    #canvas.blit(ice_snow_tile_image[0], [ice_snow_tile_info.get_corner(), ice_snow_tile_info.get_size()])
                    #text_draw = fontObj3.render("Start", True, draw_colour)
                    #canvas.blit(text_draw, (190, 220))
                    canvas.draw_image(ice_snow_tile_image, ice_snow_tile_info.get_center(), ice_snow_tile_info.get_size(), [tile_size / 2 + (tile_size * j),tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    canvas.draw_text("START", [tile_size / 2 + (tile_size * j) - tile_size / 2.5, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.0], tile_size / 4.9, "Blue")
                if field[i][j] == 3:
                    #canvas.blit(ice_snow_tile_image[0], [ice_snow_tile_info.get_corner(), ice_snow_tile_info.get_size()])
                    #text_draw = fontObj3.render("End", True, draw_colour)
                    #canvas.blit(text_draw, (190, 220))
                    canvas.draw_image(ice_snow_tile_image, ice_snow_tile_info.get_center(), ice_snow_tile_info.get_size(), [tile_size / 2 + (tile_size * j),tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    canvas.draw_text("END", [tile_size / 2 + (tile_size * j) - tile_size / 3.0, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.4], tile_size / 4.9, "Blue")
                if field[i][j] == 4:
                    #canvas.blit(star_image[0], [star_info.get_corner(), star_info.get_size()])
                    canvas.draw_image(star_image, star_info.get_center(), star_info.get_size(), [tile_size / 2 + (tile_size * j),tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                if field[i][j] == 5:
                    #canvas.blit(ice_snow_tile_image[0], [ice_snow_tile_info.get_corner(), ice_snow_tile_info.get_size()])
                    canvas.draw_image(ice_snow_tile_image, ice_snow_tile_info.get_center(), ice_snow_tile_info.get_size(), [tile_size / 2 + (tile_size * j),tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                if field[i][j] == 6:
                    canvas.draw_image(ice_water_image, ice_water_info.get_center(), ice_water_info.get_size(), [tile_size / 2 + (tile_size * j),tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])    
               
                    
                if field[i][j] == 8:
                    canvas.draw_image(breakable_rock, breakable_rock_info.get_center(), breakable_rock_info.get_size(), [tile_size / 2 + (tile_size * j),tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])   
                if field[i][j] == 9:
                    canvas.draw_image(broken_rock_image, broken_rock_info.get_center(), broken_rock_info.get_size(), [tile_size / 2 + (tile_size * j),tile_size + tile_size / 2 + (tile_size * i)], [tile_size * 2, tile_size * 2])   
                    timer5.start()
                if field[i][j] == 42:
                                    
                    canvas.draw_image(ice_snow_tile_image, ice_snow_tile_info.get_center(), ice_snow_tile_info.get_size(), [tile_size / 2 + (tile_size * j),tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    canvas.draw_text("END", [tile_size / 2 + (tile_size * j) - tile_size / 3.0, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.4], tile_size / 4.9, "Blue")
class Water_Level:
    def __init__(self, layout):
        self.layout = layout
        self.tile_size = WIDTH / (len(layout))
        starting_point = [0, 0]
        for i in range(len(layout)):
            for j in range(len(layout[i])):
                if layout[i][j] == [5]:
                    starting_point = [i, j]
        self.starting_point = starting_point
        self.dimension = len(layout)
        self.played = False
        self.stars = 0
        self.max_stars = 0
        self.changed_coordinates = []
        self.record = 599

    def set_record(self, newRec):
        self.record = min(newRec, self.record)

    def get_record(self):
        return self.record
        
    def get_dimension(self):
        return int(self.dimension)
    
    def reset_level(self):
        for i in self.changed_coordinates:
            self.layout[int(i[0])][int(i[1])] = [7]
        self.stars = 0
        self.turn = 0

    def get_layout(self):
        return self.layout
    
    def get_start(self):
        return self.starting_point
    
    def get_tile_size(self):
        return self.tile_size
       
    def change_tile(self, coordinate, new_tile):
        self.layout[int(coordinate[0])][int(coordinate[1])] = new_tile
        self.changed_coordinates.append(coordinate)      
        
    def collect_star(self):
        global notice
        self.stars += 1
        notice = True
        timerA.start()
    
    def check_stars(self):
        if self.stars >= self.max_stars:
            self.max_stars = self.stars
    
    def play_level(self):
        self.played = True
        self.stars = 0
    def get_played(self):
        return self.played
        
    def get_stars(self, max = None):
        if max == True:
            return self.max_stars
        return self.stars
                        
                                     
    
class Water_Field:
    def __init__(self, level_list, starting_level = 1):
        self.levels = level_list
        self.current_level = level_list[starting_level - 1]
        self.current_starting_point = [0,0]
        self.current_tile_size = self.current_level.get_tile_size()
        self.current_dimension = int(self.current_level.get_dimension())   
        self.current_layout = self.current_level.get_layout()
        self.condition = 0







        self.whirlpool_angle = -4.0/30.0
        self.whirlpool_rotate_speed = 4.0/30.0
        
    def get_level_list(self):
        return self.levels
    
    def get_current_level(self, extra_parameter = None):
        if extra_parameter == "layout":
            return self.current_layout
        elif extra_parameter == "start":
            return self.current_starting_point
        elif extra_parameter == "tile_size":
            return self.current_tile_size
        elif extra_parameter == "dimension":
            return self.current_dimension
        elif extra_parameter == "star":
            return self.current_level.get_stars()
        else:
            return self.current_level
    def select_level(self, level, statusx = None):
        global status
        lvl =self.levels[level - 1]
        if level == 1 or lvl.get_played() == True:
            self.current_level = self.levels[level - 1]
            self.current_starting_point = self.current_level.get_start()
            self.current_tile_size = self.current_level.get_tile_size()
            self.current_dimension = int(self.current_level.get_dimension())   
            self.current_layout = self.current_level.get_layout()
            if statusx != None:
                status = statusx
            main_character[0].teleport()
    
    def next_level(self, startTile):
        global Ttime
        lvl = self.current_level
        lvl.set_record(Ttime)
        self.current_level = self.levels[self.levels.index(lvl) + 1]
        self.current_starting_point = self.current_level.get_start()
        self.current_tile_size = self.current_level.get_tile_size()
        self.current_dimension = int(self.current_level.get_dimension())
        self.current_layout = self.current_level.get_layout()
        
    def no_of_lvls_played(self):
        count = 0
        for lvl in self.levels:
            if not lvl.get_played():
                count += 1
        return count

    def draw_water(self, canvas):
        field = self.current_layout
        tile_size = self.current_tile_size
        if (not ((status == "Paused" or status == "too bad so sad"))):
            if (self.condition % 3)== 0:  
                water_current_info.change_centre()
            if (self.condition % 2) == 0:
                self.whirlpool_angle = (self.whirlpool_angle + self.whirlpool_rotate_speed) % 360
            self.condition+=1
        for i in range(0, int(self.current_dimension)):            
            canvas.draw_line([tile_size + (tile_size * i), EXTRA_HEIGHT], [tile_size + (tile_size * i), HEIGHT + EXTRA_HEIGHT],\
                            0.25, "Black")
            for j in range(0, self.current_dimension):     
                canvas.draw_line([0, tile_size + (tile_size * j)], [WIDTH, tile_size + (tile_size * j)],\
                            0.25, "Black")
                tile = field[i][j][-(main_character[0].get_turn() % 2)]
                if tile == 1:
                    canvas.draw_image(water_current_image, water_current_info.get_center(), water_current_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                if tile == 2:
                    canvas.draw_image(water_current_image, water_current_info.get_center(), water_current_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size], math.radians(90))
                                      
                if tile == 3:
                    canvas.draw_image(water_current_image, water_current_info.get_center(), water_current_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size],  math.radians(270))
                if tile == 7:
                    canvas.draw_image(star_image, star_info.get_center(), star_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [tile_size / 2, tile_size / 2])
                if tile == 4:
                    canvas.draw_image(water_current_image, water_current_info.get_center(), water_current_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size],  math.radians(180))
               
                if tile == 5:
                    canvas.draw_text("START", [tile_size / 2 + (tile_size * j) - tile_size / 2.5, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.0], tile_size / 4.9, "White")
                if tile == 6:
                    canvas.draw_text("END", [tile_size / 2 + (tile_size * j) - tile_size / 3.0, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.4], tile_size / 4.9, "White")
                
                if tile == 8:
                    canvas.draw_image(whirlpool_image, whirlpool_info.get_center(), whirlpool_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size], self.whirlpool_angle)
                    #canvas.draw_image(whirlpool_image, whirlpool_info.get_center(), whirlpool_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size], -self.whirlpool_angle)
                    #canvas.draw_image(whirlpool_image, whirlpool_info.get_center(), whirlpool_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [4 * tile_size / 5, 4 * tile_size / 5], -self.whirlpool_angle)
                    #canvas.draw_image(whirlpool_image, whirlpool_info.get_center(), whirlpool_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [4 * tile_size / 5, 4 * tile_size / 5], self.whirlpool_angle)
                    #canvas.draw_image(whirlpool_image, whirlpool_info.get_center(), whirlpool_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [3 * tile_size / 5, 3 * tile_size / 5], self.whirlpool_angle)
                    canvas.draw_image(whirlpool_image, whirlpool_info.get_center(), whirlpool_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [1 * tile_size / 2, 1 * tile_size / 2], -self.whirlpool_angle)
                    #canvas.draw_image(whirlpool_image, whirlpool_info.get_center(), whirlpool_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [2 * tile_size / 5, 2 * tile_size / 5], -self.whirlpool_angle)
                    #canvas.draw_image(whirlpool_image, whirlpool_info.get_center(), whirlpool_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [2 * tile_size / 5, 2 * tile_size / 5], self.whirlpool_angle)
                    #canvas.draw_image(whirlpool_image, whirlpool_info.get_center(), whirlpool_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [tile_size / 3, tile_size / 3], self.whirlpool_angle)
                    #canvas.draw_image(whirlpool_image, whirlpool_info.get_center(), whirlpool_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [tile_size / 5, tile_size / 5], -self.whirlpool_angle)

                if tile == 42:
                    canvas.draw_text("END", [tile_size / 2 + (tile_size * j) - tile_size / 3.0, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.4], tile_size / 4.9, "White")

movable_rock_list = []

class Lava_Field(Field):
    def draw_lava(self, canvas):
        global movable_rock_list
        field = self.current_layout
        tile_size = self.current_tile_size
        for i in range(0, int(self.current_dimension)):
            canvas.draw_line([tile_size + (tile_size * i), EXTRA_HEIGHT], [tile_size + (tile_size * i), HEIGHT + EXTRA_HEIGHT],\
                            0.75, "White")
            for j in range(0, int(self.current_dimension)):
                canvas.draw_line([0, tile_size + (tile_size * j)], [WIDTH, tile_size + (tile_size * j)],\
                            0.75, "White")

                if field[i][j] == 1:
                    canvas.draw_image(lava_rock_tile_image, lava_rock_tile_info.get_center(), lava_rock_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size * 0.9, tile_size * 0.9])
                elif field[i][j] == 2:
                    canvas.draw_text("START", [tile_size / 2 + (tile_size * j) - tile_size / 2.5, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.0], tile_size / 4.9, "Black")
                elif field[i][j] == 5:
                    canvas.draw_text("END", [tile_size / 2 + (tile_size * j) - tile_size / 3.0, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.4], tile_size / 4.9, "Black")
                elif field[i][j] == 4:
                    canvas.draw_image(star_image, star_info.get_center(), star_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [tile_size / 2, tile_size  /2])
                elif field[i][j] == 6:
                    movable_rock = Movable_Rock([(tile_size * j) + tile_size / 2, (tile_size * i) + tile_size / 2 + (EXTRA_HEIGHT)], tile_size* 3 / 8,[5, 5], movable_rock_image, movable_rock_info, movable_rock_image, movable_rock_info, movable_rock_image, movable_rock_info, movable_rock_image, movable_rock_info)
                    movable_rock_list.append(movable_rock)
                    self.get_current_level().change_tile([i, j], 0)
                elif field[i][j] < 0:
                    turns = main_character[0].get_turns()
                    explode = -(field[i][j])
                    if explode == turns:
                        canvas.draw_image(volcano_with_fire_image, volcano_with_fire_info.get_center(), volcano_with_fire_info.get_size(), [tile_size / 2 + (tile_size * j) + 23, tile_size + tile_size / 2 + (tile_size * i) + 20], [tile_size * 1.7, tile_size   * 1.7])
                    else:
                        canvas.draw_image(volcano_no_fire_image, volcano_no_fire_info.get_center(), volcano_no_fire_info.get_size(), [tile_size / 2 + (tile_size * j) + 23, tile_size + tile_size / 2 + (tile_size * i) + 20], [tile_size * 1.7, tile_size   * 1.7])
        for rock in movable_rock_list:
            mrock_info = rock.get_image_info()
            mrock_image = rock.get_image()
            canvas.draw_image(mrock_image, mrock_info.get_center(), mrock_info.get_size(), rock.get_pos(), [tile_size, tile_size])
            
class Spaceship_Field:
    def __init__(self, level_list, starting_level = 1):
        self.levels = level_list
        self.current_level = level_list[starting_level - 1]
        self.current_starting_point = self.current_level.get_start()
        self.current_tile_size = self.current_level.get_tile_size()
        self.current_dimension = int(self.current_level.get_dimension())   
        self.current_layout = self.current_level.get_layout()
        

    def no_of_lvls_played(self):
        count = 0
        for lvl in self.levels:
            if not lvl.get_played():
                count += 1
        return count
    
    def select_level(self, level, statusx = None):
        global status
        lvl = self.levels[level - 1]
        if level == 1 or lvl.get_played() == True:
            self.current_level = self.levels[level - 1]
            lvl.reset_level()
            self.current_tile_size = self.current_level.get_tile_size()
            self.current_dimension = int(self.current_level.get_dimension())
            self.current_layout = self.current_level.get_layout()
            self.current_starting_point = self.current_level.get_start()
            if statusx != None:
                status = statusx
            main_character[0].teleport()
            main_character[-1].teleport()   
    def get_level_list(self):
        return self.levels
    
    def get_current_level(self, extra_parameter = None):
        if extra_parameter == "layout":
            return self.current_layout
        elif extra_parameter == "start1":
            return self.current_starting_point[0]
        elif extra_parameter == "start2":
            return self.current_starting_point[1]
        elif extra_parameter == "tile_size":
            return self.current_tile_size
        elif extra_parameter == "dimension":
            return self.current_dimension
        elif extra_parameter == "star":
            return self.current_level.get_stars()
        else:
            return self.current_level
    
    def next_level(self):
        global Ttime
        lvl = self.current_level
        lvl.set_record(Ttime)
        self.current_level = self.levels[self.levels.index(lvl) + 1]
        self.current_starting_point = self.current_level.get_start()
        self.current_tile_size = self.current_level.get_tile_size()
        self.current_dimension = int(self.current_level.get_dimension())   
        self.current_layout = self.current_level.get_layout()            
    def draw(self, canvas):
        field = self.current_layout
        tile_size = self.current_tile_size
        for i in range(0, int(self.current_dimension)):
            canvas.draw_line([tile_size + (tile_size * i), EXTRA_HEIGHT], [tile_size + (tile_size * i), HEIGHT + EXTRA_HEIGHT],\
                            0.75, "White")
            for j in range(0, self.current_dimension):
                canvas.draw_line([0, tile_size + (tile_size * j)], [WIDTH, tile_size + (tile_size * j)],\
                            0.75, "White")
                canvas.draw_image(metal_tile_image, metal_tile_info.get_center(), metal_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                if field[i][j] == 0:
                    canvas.draw_image(slime_tile_image, slime_tile_info.get_center(), slime_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                if field[i][j] == 1:
                    canvas.draw_image(alien_rock_image, alien_rock_info.get_center(), alien_rock_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                if field[i][j] == 2:
                    canvas.draw_image(slime_tile_image, slime_tile_info.get_center(), slime_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    canvas.draw_text("START1", [tile_size / 2 + (tile_size * j) - tile_size / 2.5, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.0], tile_size / 4.9, "Blue")
                if field[i][j] == 3:
                    canvas.draw_image(slime_tile_image, slime_tile_info.get_center(), slime_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    canvas.draw_text("END1", [tile_size / 2 + (tile_size * j) - tile_size / 3.0, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.4], tile_size / 4.9, "Blue")
                if field[i][j] == 4:
                    canvas.draw_image(slime_tile_image, slime_tile_info.get_center(), slime_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    canvas.draw_image(star_image, star_info.get_center(), star_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [tile_size / 2, tile_size / 2])

                if field[i][j] == 5:
                    canvas.draw_image(metal_tile_image, metal_tile_info.get_center(), metal_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    
               
                if field[i][j] == 8:	
                    canvas.draw_image(slime_tile_image, slime_tile_info.get_center(), slime_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    canvas.draw_text("START2", [tile_size / 2 + (tile_size * j) - tile_size / 2.5, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.0], tile_size / 4.9, "Blue")
                
                if field[i][j] == 9:
                    canvas.draw_image(slime_tile_image, slime_tile_info.get_center(), slime_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    canvas.draw_text("END2", [tile_size / 2 + (tile_size * j) - tile_size / 3.0, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.4], tile_size / 4.9, "Blue")

                if type(field[i][j]) == list :
                    
                    if field[i][j][0] == 1 :# right facing alien
                        canvas.draw_image(alien_right_image, alien_right_info.get_center(), alien_right_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    if field[i][j][0] == 2 :# left facing alien
                         canvas.draw_image(alien_left_image, alien_left_info.get_center(), alien_left_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    if field[i][j][0] == 3 :# down facing alien
                        canvas.draw_image(alien_front_image, alien_front_info.get_center(), alien_front_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    if field[i][j][0] == 4 :# up facing alien
                        canvas.draw_image(alien_back_image, alien_back_info.get_center(), alien_back_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    if field[i][j][0] == 5 :# horizontal lazer
                        canvas.draw_image(slime_tile_image, slime_tile_info.get_center(), slime_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])

                        canvas.draw_image(laser_horizontal_image, laser_horizontal_info.get_center(), laser_horizontal_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size * 1.5, tile_size * 1.5])
                    if field[i][j][0] == 6 :# vertical lazer
                        canvas.draw_image(slime_tile_image, slime_tile_info.get_center(), slime_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])

                        canvas.draw_image(laser_vertical_image, laser_vertical_info.get_center(), laser_vertical_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size * 1.5, tile_size * 1.5])
                    if field[i][j][0] == 7 :# cross lazer
                        canvas.draw_image(slime_tile_image, slime_tile_info.get_center(), slime_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])

                        canvas.draw_image(laser_vertical_image, laser_vertical_info.get_center(), laser_vertical_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size * 1.5, tile_size * 1.5])   
                        canvas.draw_image(laser_horizontal_image, laser_horizontal_info.get_center(), laser_horizontal_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size * 1.5, tile_size * 1.5])
class Future_Field(Field):
    def draw(self, canvas):
        field = self.current_layout
        temp = len(field)
        if temp == 8:
            tile_size = 68.75
        elif temp == 10:
            tile_size = 55.0
        else:
            tile_size = self.current_tile_size
        #print "observe :   " + str(tile_size)
        for i in range(0, temp):
            
            canvas.draw_line([tile_size + (tile_size * i), EXTRA_HEIGHT], [tile_size + (tile_size * i), HEIGHT + EXTRA_HEIGHT],0.75, "White")
           #pygame.draw.line(canvas, white, [tile_size + (tile_size * i), EXTRA_HEIGHT], [tile_size + (tile_size * i), HEIGHT + EXTRA_HEIGHT], 1)
            for j in range(0, temp):
                canvas.draw_line([0, tile_size + (tile_size * j)], [WIDTH, tile_size + (tile_size * j)],0.75, "White")
                #pygame.draw.line(canvas, white, [0, tile_size + (tile_size * j)], [WIDTH, tile_size + (tile_size * j)], 1)
                if field[i][j] == 1:
                    #canvas.blit(building, [building_info.get_center()[0] - building_info.get_size()[0] / 2, building_info.get_center()[1] - building_info.get_size()[1] / 2], [tile_size, tile_size])
                    canvas.draw_image(building_image, building_info.get_center(), building_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                if field[i][j] == 2:
                    canvas.draw_image(future_stopper_tile_image, future_stopper_tile_info.get_center(), future_stopper_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    canvas.draw_text("START", [tile_size / 2 + (tile_size * j) - tile_size / 2.5, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.0], tile_size / 4.9, "White")
                if field[i][j] == 3:
                    canvas.draw_image(future_stopper_tile_image, future_stopper_tile_info.get_center(), future_stopper_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    canvas.draw_text("END", [tile_size / 2 + (tile_size * j) - tile_size / 3.0, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.4], tile_size / 3.9, "White")
                if field[i][j] == 4:
                    canvas.draw_image(star_image, star_info.get_center(), star_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                if field[i][j] == 5:
                    canvas.draw_image(future_stopper_tile_image, future_stopper_tile_info.get_center(), future_stopper_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])        
                if field[i][j] == 6:
                    canvas.draw_image(poison_gas_image, poison_gas_info.get_center(), poison_gas_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])    
                if field[i][j] == 42:
                    canvas.draw_image(future_stopper_tile_image, future_stopper_tile_info.get_center(), future_stopper_tile_info.get_size(), [tile_size / 2 + (tile_size * j),\
                                                                                                 tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])
                    canvas.draw_text("END", [tile_size / 2 + (tile_size * j) - tile_size / 3.0, tile_size + tile_size / 2 + (tile_size * i) + tile_size / 7.4], tile_size / 4.9, "Blue")
                if type(field[i][j]) == list:
                    canvas.draw_image(teleporter_tile_image, teleporter_tile_info.get_center(), teleporter_tile_info.get_size(), [tile_size / 2 + (tile_size * j), tile_size + tile_size / 2 + (tile_size * i)], [tile_size, tile_size])        




ice_world = World("ice")
water_world = World("water")
lava_world = World("lava")
spaceship_world = World("spaceship")
future_world = World("future")
worlds = [ice_world,water_world,lava_world, spaceship_world, future_world]
current_world = worlds[worldCount]

ice_field = ice_world.get_field()
water_field = water_world.get_field()
lava_field = lava_world.get_field()
spaceship_field = spaceship_world.get_field()
future_field = future_world.get_field()
fields = [ice_field,water_field,lava_field, spaceship_field, future_field]
game_field = fields[worldCount]

File = open("C:\Python27\Lib\json\level-data.json", "r")
data = File.read()
FFFFile = open("C:/Python27/Lib/json/record-data.json", "r")
dddata = FFFFile.read()
for tempnum in range(0, 5):
    tempfield = fields[tempnum]
    lvl_played = int(data[tempnum])
    lvls = tempfield.get_level_list()
    for lvlno in range(1, lvl_played+1):
        lvls[lvlno].play_level()
    for lvlno in range(0, 10):
        lvls[lvlno].set_record(int(dddata[tempnum * 30 + lvlno * 3] + dddata[tempnum * 30 + lvlno * 3 + 1] + dddata[tempnum * 30 + lvlno * 3 + 2]))


tile_size = game_field.get_current_level("tile_size")
EXTRA_HEIGHT = WIDTH / game_field.get_current_level("dimension")

ice_character = ice_world.get_character()
water_character = water_world.get_character()
lava_character = lava_world.get_character()
spaceship_character = spaceship_world.get_character()
future_character = future_world.get_character()
characters = [ice_character,water_character,lava_character, spaceship_character, future_character]
main_character = characters[worldCount]


disabled = False

def keydown(key):
    
    global status, code

    if key == simplegui.KEY_MAP['q']:
            File = open("C:\Python27\Lib\json\level-data.json", "w+")
            data = ""
            for tempnum in range(0, 5):
                tempfield = fields[tempnum]
                data += str(10 - tempfield.no_of_lvls_played())
            File.write(data)
    
    if status == "inPlay" and disabled == False and main_character[0].get_moving() == False and main_character[-1].get_moving() == False:
        if key == simplegui.KEY_MAP['left'] :
            main_character[0].start_moving([-1, 0])
            main_character[-1].start_moving([-1, 0])
        elif key == simplegui.KEY_MAP['right']:
            main_character[0].start_moving([1, 0])
            main_character[-1].start_moving([1, 0])
        elif key == simplegui.KEY_MAP['up']:
            main_character[0].start_moving([0, -1])
            main_character[-1].start_moving([0, -1])
        elif key == simplegui.KEY_MAP['down'] :
            main_character[0].start_moving([0, 1])
            main_character[-1].start_moving([0, 1])
        elif key == simplegui.KEY_MAP['a']:
            main_character[0].start_moving([-1, 0])
            code += a
        elif key == simplegui.KEY_MAP['d']:
            main_character[0].start_moving([1, 0])
        elif key == simplegui.KEY_MAP['w']:
            main_character[0].start_moving([0, -1])
        elif key == simplegui.KEY_MAP['s']:
            main_character[0].start_moving([0, 1])
        elif key == simplegui.KEY_MAP['r']:
            code += "r"
        elif key == simplegui.KEY_MAP['c']:
            code = ""
        elif key == simplegui.KEY_MAP['m']:
            code += "m"
        elif key == simplegui.KEY_MAP['e']:
            code += "e"
        elif key == simplegui.KEY_MAP['h']:
            code += "h"
        elif key == simplegui.KEY_MAP['l']:
            code += "l"
        elif key == simplegui.KEY_MAP['o']:
            code += "o"
            
        if code == "re":
            lvl = game_field.get_current_level()
            lvl.reset_level()
            status = "inPlay"
            main_character[0].teleport()
            main_character[-1].teleport()
            code = ""
        if code == "meh":
            status = "LVL"
            code = ""
        if code == "chello":
            status = "LVL"
        if code == "ler":
            F1ile = open("C:/Python27/Lib/json/level-data.json", "w")
            F2ile = open("C:/Python27/Lib/json/temp-data.json", "w")
            F3ile = open("C:/Python27/Lib/json/record-data.json", "w")
            F4ile = open("C:/Python27/Lib/json/temp-record-data.json", "w")
            F1ile.write("00000")
            F2ile.write("00000")
            F3ile.write("599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599")
            F4ile.write("599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599599")
                        
# Handler to draw on canvas
def draw_ice(canvas):
    if status == "inPlay":
        canvas.draw_image(ice_tile_image, ice_tile_info.get_center(), ice_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw(canvas)
        draw_options(canvas)
        main_character[0].draw(canvas)
        main_character[0].findNextTile(game_field.get_current_level("layout"))
        main_character[0].move()
        main_character[0].check_tile(game_field.get_current_level("layout"))

    
    elif status == "too bad so sad":
        canvas.draw_image(ice_tile_image, ice_tile_info.get_center(), ice_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw(canvas)
        draw_options(canvas)
        canvas.draw_image(try_again_image, try_again_info.get_center(), try_again_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
        canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
        canvas.draw_text("RETRY", [270, 540], 22, "White")
        
    elif status == "HomeScreen":
        canvas.draw_image(ice_level_select_image, ice_level_select_info.get_center(), ice_level_select_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [140, 510], [140, 550], [40, 550]], 5, "Blue", "Blue") #copy to all classes
        canvas.draw_text("BACK", [50, 540], 22, "White")
        canvas.draw_polygon([[180, 510], [400, 510], [400, 550], [180, 550]], 5, "Blue", "Blue")
        canvas.draw_text("HOW TO PLAY", [190, 540], 22, "White")
        canvas.draw_polygon([[40, 260], [80, 260], [80, 300], [40, 300]], 5, "Blue", "Blue")
        canvas.draw_text("1", [50, 290], 22, "White")
        canvas.draw_polygon([[130, 260], [170, 260], [170, 300], [130, 300]], 5, "Blue", "Blue")
        canvas.draw_text("2", [140, 290], 22, "White")
        canvas.draw_polygon([[220, 260], [260, 260], [260, 300], [220, 300]], 5, "Blue", "Blue")
        canvas.draw_text("3", [230, 290], 22, "White")
        canvas.draw_polygon([[310, 260], [350, 260], [350, 300], [310, 300]], 5, "Blue", "Blue")
        canvas.draw_text("4", [320, 290], 22, "White")
        canvas.draw_polygon([[400, 260], [440, 260], [440, 300], [400, 300]], 5, "Blue", "Blue")
        canvas.draw_text("5", [410, 290], 22, "White")
        canvas.draw_polygon([[40, 330], [80, 330], [80, 370], [40, 370]], 5, "Blue", "Blue")
        canvas.draw_text("6", [50, 360], 22,"White")
        canvas.draw_polygon([[130, 330], [170, 330], [170, 370], [130, 370]], 5, "Blue", "Blue")
        canvas.draw_text("7", [140, 360], 22, "White")
        canvas.draw_polygon([[220, 330], [260, 330], [260, 370], [220, 370]], 5, "Blue", "Blue")
        canvas.draw_text("8", [230, 360], 22, "White")
        canvas.draw_polygon([[310, 330], [350, 330], [350, 370], [310, 370]], 5, "Blue", "Blue")
        canvas.draw_text("9", [320, 360], 22, "White")
        canvas.draw_polygon([[400, 330], [440, 330], [440, 370], [400, 370]], 5, "Blue", "Blue")
        canvas.draw_text("10", [410, 360], 22, "White")
        
        for num in range(0, game_field.no_of_lvls_played() - 1):
            if num < 5:                
                canvas.draw_polygon([[-50 + (5 - num) * 90, 330], [-10 + (5 - num) * 90, 330], [-10 + (5 - num) * 90, 370], [-50 + (5 - num) * 90, 370]], 5, "Silver", "Silver")                
            elif num < 9:    
                canvas.draw_polygon([[-50 + (10 - num) * 90, 260], [-10 + (10 - num) * 90, 260], [-10 + (10 - num) * 90, 300], [-50 + (10 - num) * 90, 300]], 5, "Silver", "Silver")
        
    elif status == "LVL":
        canvas.draw_image(ice_level_passed_image, ice_level_passed_info.get_center(), ice_level_passed_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
        if (game_field.get_current_level() != game_field.get_level_list()[-1]):
            canvas.draw_polygon([[260, 510], [455, 510], [455, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("NEXT LEVEL", [270, 540], 22, "White")
        
    elif status == "HowToPlay":
        canvas.draw_image(ice_instructions_image, ice_instructions_info.get_center(), ice_instructions_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[540, 590],  [540, 550], [350, 550],[350, 590]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [360, 580], 22, "White")
        
    elif status == "Paused":
        canvas.draw_image(ice_tile_image, ice_tile_info.get_center(), ice_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw(canvas)
        draw_options(canvas)
        main_character[0].draw(canvas)
        
        

def group_collide(group, other_object):
    for element in group:
        element.collide(other_object)

def draw_spaceship(canvas):
    if status == "inPlay":
        main_character1_location = main_character[0].get_location()
        main_character2_location = main_character[-1].get_location()
        main_character1 = main_character[0]
        main_character2 = main_character[-1]

        canvas.draw_image(metal_tile_image, metal_tile_info.get_center(), metal_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw(canvas)
        draw_options(canvas)
        main_character1.draw(canvas)
        main_character1.findNextTile(game_field.get_current_level("layout"),main_character2_location)
        main_character1.move()
        main_character1.check_tile(game_field.get_current_level("layout"))
        main_character2.draw(canvas)
        main_character2.findNextTile(game_field.get_current_level("layout"),main_character1_location)
        main_character2.move()
        main_character2.check_tile(game_field.get_current_level("layout"))



    elif status == "HomeScreen":
        canvas.draw_image(spaceship_level_select_image, spaceship_level_select_info.get_center(), spaceship_level_select_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [140, 510], [140, 550], [40, 550]], 5, "Blue", "Blue") #copy to all classes
        canvas.draw_text("BACK", [50, 540], 22, "White")
        canvas.draw_polygon([[180, 510], [400, 510], [400, 550], [180, 550]], 5, "Blue", "Blue")
        canvas.draw_text("HOW TO PLAY", [190, 540], 22, "White")
        canvas.draw_polygon([[40, 260], [80, 260], [80, 300], [40, 300]], 5, "Blue", "Blue")
        canvas.draw_text("1", [50, 290], 22, "White")
        canvas.draw_polygon([[130, 260], [170, 260], [170, 300], [130, 300]], 5, "Blue", "Blue")
        canvas.draw_text("2", [140, 290], 22, "White")
        canvas.draw_polygon([[220, 260], [260, 260], [260, 300], [220, 300]], 5, "Blue", "Blue")
        canvas.draw_text("3", [230, 290], 22,  "White")
        canvas.draw_polygon([[310, 260], [350, 260], [350, 300], [310, 300]], 5, "Blue", "Blue")
        canvas.draw_text("4", [320, 290], 22, "White")
        canvas.draw_polygon([[400, 260], [440, 260], [440, 300], [400, 300]], 5, "Blue", "Blue")
        canvas.draw_text("5", [410, 290], 22, "White")
        canvas.draw_polygon([[40, 330], [80, 330], [80, 370], [40, 370]], 5, "Blue", "Blue")
        canvas.draw_text("6", [50, 360], 22, "White")
        canvas.draw_polygon([[130, 330], [170, 330], [170, 370], [130, 370]], 5, "Blue", "Blue")
        canvas.draw_text("7", [140, 360], 22, "White")
        canvas.draw_polygon([[220, 330], [260, 330], [260, 370], [220, 370]], 5, "Blue", "Blue")
        canvas.draw_text("8", [230, 360], 22, "White")
        canvas.draw_polygon([[310, 330], [350, 330], [350, 370], [310, 370]], 5, "Blue", "Blue")
        canvas.draw_text("9", [320, 360], 22, "White")
        canvas.draw_polygon([[400, 330], [440, 330], [440, 370], [400, 370]], 5, "Blue", "Blue")
        canvas.draw_text("10", [410, 360], 22, "White")
        
        for num in range(0, game_field.no_of_lvls_played() - 1):
            if num < 5:                
                canvas.draw_polygon([[-50 + (5 - num) * 90, 330], [-10 + (5 - num) * 90, 330], [-10 + (5 - num) * 90, 370], [-50 + (5 - num) * 90, 370]], 5, "Silver", "Silver")                
            elif num < 9:    
                canvas.draw_polygon([[-50 + (10 - num) * 90, 260], [-10 + (10 - num) * 90, 260], [-10 + (10 - num) * 90, 300], [-50 + (10 - num) * 90, 300]], 5, "Silver", "Silver")
        

    elif status == "LVL":
        canvas.draw_image(spaceship_level_passed_image, spaceship_level_passed_info.get_center(), spaceship_level_passed_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
       
        if (game_field.get_current_level() != game_field.get_level_list()[-1]):
            canvas.draw_polygon([[260, 510], [455, 510], [455, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("NEXT LEVEL", [270, 540], 22, "White")
        
    elif status == "HowToPlay":
        canvas.draw_image(spaceship_instructions_image, spaceship_instructions_info.get_center(), spaceship_instructions_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[540, 590],  [540, 550], [350, 550],[350, 590]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [360, 580], 22, "White")
    elif status == "Paused":
        main_character1 = main_character[0]
        main_character2 = main_character[-1]
        canvas.draw_image(metal_tile_image, metal_tile_info.get_center(), metal_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw(canvas)
        draw_options(canvas)
        main_character1.draw(canvas)
        main_character2.draw(canvas)
        canvas.draw_image(pause_image_image, pause_image_info.get_center(), pause_image_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
        canvas.draw_image(play_button_image, play_button_info.get_center(), play_button_info.get_size(), [30, EXTRA_HEIGHT - tile_size / 2], [pause_sign_info.get_size()[0] / 25, pause_sign_info.get_size()[1] / 27])


    elif status == "too bad so sad":

        game_field.draw(canvas)
        draw_options(canvas)

        canvas.draw_image(try_again_image, try_again_info.get_center(), try_again_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
        canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
        canvas.draw_text("RETRY", [270, 540], 22, "White")            
    
        
def draw_future(canvas):
    if status == "inPlay":
        canvas.draw_image(technology_tile_image, technology_tile_info.get_center(), technology_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw(canvas)
        draw_options(canvas)
        main_character[0].draw(canvas)
        main_character[0].findNextTile(game_field.get_current_level("layout"))
        main_character[0].move()
        main_character[0].check_tile(game_field.get_current_level("layout"))

        if message!= "":
            canvas.draw_polygon([[0, ((HEIGHT + EXTRA_HEIGHT) / 2) - 20], [WIDTH, ((HEIGHT + EXTRA_HEIGHT) / 2) - 20], [WIDTH, (HEIGHT + EXTRA_HEIGHT) / 2 + 15], [0, (HEIGHT + EXTRA_HEIGHT) / 2 + 15]], 5, "Blue", "Blue")
            canvas.draw_text(message, [15, (HEIGHT + EXTRA_HEIGHT) / 2 + 5],22, "White")
    elif status == "HomeScreen":
        canvas.draw_image(future_level_select_image, future_level_select_info.get_center(), future_level_select_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [140, 510], [140, 550], [40, 550]], 5, "Blue", "Blue") #copy to all classes
        canvas.draw_text("BACK", [50, 540], 22, "White")
        canvas.draw_polygon([[180, 510], [400, 510], [400, 550], [180, 550]], 5, "Blue", "Blue")
        canvas.draw_text("HOW TO PLAY", [190, 540], 22, "White")
        canvas.draw_polygon([[40, 260], [80, 260], [80, 300], [40, 300]], 5, "Blue", "Blue")
        canvas.draw_text("1", [50, 290], 22, "White")
        canvas.draw_polygon([[130, 260], [170, 260], [170, 300], [130, 300]], 5, "Blue", "Blue")
        canvas.draw_text("2", [140, 290], 22, "White")
        canvas.draw_polygon([[220, 260], [260, 260], [260, 300], [220, 300]], 5, "Blue", "Blue")
        canvas.draw_text("3", [230, 290], 22, "White")
        canvas.draw_polygon([[310, 260], [350, 260], [350, 300], [310, 300]], 5, "Blue", "Blue")
        canvas.draw_text("4", [320, 290], 22, "White")
        canvas.draw_polygon([[400, 260], [440, 260], [440, 300], [400, 300]], 5, "Blue", "Blue")
        canvas.draw_text("5", [410, 290], 22, "White")
        canvas.draw_polygon([[40, 330], [80, 330], [80, 370], [40, 370]], 5, "Blue", "Blue")
        canvas.draw_text("6", [50, 360], 22, "White")
        canvas.draw_polygon([[130, 330], [170, 330], [170, 370], [130, 370]], 5, "Blue", "Blue")
        canvas.draw_text("7", [140, 360], 22, "White")
        canvas.draw_polygon([[220, 330], [260, 330], [260, 370], [220, 370]], 5, "Blue", "Blue")
        canvas.draw_text("8", [230, 360], 22, "White")
        canvas.draw_polygon([[310, 330], [350, 330], [350, 370], [310, 370]], 5, "Blue", "Blue")
        canvas.draw_text("9", [320, 360], 22, "White")
        canvas.draw_polygon([[400, 330], [440, 330], [440, 370], [400, 370]], 5, "Blue", "Blue")
        canvas.draw_text("10", [410, 360], 22, "White")
        
        for num in range(0, game_field.no_of_lvls_played() - 1):
            if num < 5:                
                canvas.draw_polygon([[-50 + (5 - num) * 90, 330], [-10 + (5 - num) * 90, 330], [-10 + (5 - num) * 90, 370], [-50 + (5 - num) * 90, 370]], 5, "Silver", "Silver")                
            elif num < 9:    
                canvas.draw_polygon([[-50 + (10 - num) * 90, 260], [-10 + (10 - num) * 90, 260], [-10 + (10 - num) * 90, 300], [-50 + (10 - num) * 90, 300]], 5, "Silver", "Silver")
        
    
        
    elif status == "LVL":
        canvas.draw_image(future_level_passed_image, future_level_passed_info.get_center(), future_level_passed_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
       
        if (game_field.get_current_level() != game_field.get_level_list()[-1]):
            canvas.draw_polygon([[260, 510], [455, 510], [455, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("NEXT LEVEL", [270, 540], 22, "White")
            
    elif status == "HowToPlay":
        canvas.draw_image(future_instructions_image, future_instructions_info.get_center(), future_instructions_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[540, 590],  [540, 550], [350, 550],[350, 590]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [360, 580], 22, "White")
        
    elif status == "Paused":
        canvas.draw_image(technology_tile_image, technology_tile_info.get_center(), technology_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw(canvas)
        draw_options(canvas)
        main_character[0].draw(canvas)
        canvas.draw_image(pause_image_image, pause_image_info.get_center(), pause_image_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
        canvas.draw_image(play_button_image, play_button_info.get_center(), play_button_info.get_size(), [30, EXTRA_HEIGHT - tile_size / 2], [pause_sign_info.get_size()[0] / 25, pause_sign_info.get_size()[1] / 27])
    elif status == "too bad so sad":
        canvas.draw_image(technology_tile_image, technology_tile_info.get_center(), technology_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw(canvas)
        draw_options(canvas)
        canvas.draw_image(try_again_image, try_again_info.get_center(), try_again_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
        canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
        canvas.draw_text("RETRY", [270, 540], 22, "White")               
      
def draw_lava(canvas):
    global movable_rock_list, bounce_condition
    if status == "inPlay":
        canvas.draw_image(lava_tile_image, lava_tile_info.get_center(), lava_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw_lava(canvas)
        draw_options(canvas)
        main_character[0].draw(canvas)
        main_character[0].findNextTile(game_field.get_current_level("layout"))
        main_character[0].check_tile(game_field.get_current_level("layout"))
        if bounce_condition == False:
            main_character[0].move()
        else:
            main_character[0].bounce()
        group_collide(movable_rock_list, main_character[0])
        for element in movable_rock_list:
            element.check_tile(game_field.get_current_level("layout"))
            element.findNextTile(game_field.get_current_level("layout"))
            element.move()
            
    elif status == "HomeScreen":
        canvas.draw_image(lava_title_screen_image, lava_title_screen_info.get_center(), lava_title_screen_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [140, 510], [140, 550], [40, 550]], 5, "Blue", "Blue") #copy to all classes
        canvas.draw_text("BACK", [50, 540], 22, "White")
        canvas.draw_polygon([[180, 510], [400, 510], [400, 550], [180, 550]], 5, "Blue", "Blue")
        canvas.draw_text("HOW TO PLAY", [190, 540], 22, "White")
        canvas.draw_polygon([[40, 260], [80, 260], [80, 300], [40, 300]], 5, "Blue", "Blue")
        canvas.draw_text("1", [50, 290], 22, "White")
        canvas.draw_polygon([[130, 260], [170, 260], [170, 300], [130, 300]], 5, "Blue", "Blue")
        canvas.draw_text("2", [140, 290], 22, "White")
        canvas.draw_polygon([[220, 260], [260, 260], [260, 300], [220, 300]], 5, "Blue", "Blue")
        canvas.draw_text("3", [230, 290], 22, "White")
        canvas.draw_polygon([[310, 260], [350, 260], [350, 300], [310, 300]], 5, "Blue", "Blue")
        canvas.draw_text("4", [320, 290], 22, "White")
        canvas.draw_polygon([[400, 260], [440, 260], [440, 300], [400, 300]], 5, "Blue", "Blue")
        canvas.draw_text("5", [410, 290], 22, "White")
        canvas.draw_polygon([[40, 330], [80, 330], [80, 370], [40, 370]], 5, "Blue", "Blue")
        canvas.draw_text("6", [50, 360], 22, "White")
        canvas.draw_polygon([[130, 330], [170, 330], [170, 370], [130, 370]], 5, "Blue", "Blue")
        canvas.draw_text("7", [140, 360], 22, "White")
        canvas.draw_polygon([[220, 330], [260, 330], [260, 370], [220, 370]], 5, "Blue", "Blue")
        canvas.draw_text("8", [230, 360], 22, "White")
        canvas.draw_polygon([[310, 330], [350, 330], [350, 370], [310, 370]], 5, "Blue", "Blue")
        canvas.draw_text("9", [320, 360], 22, "White")
        canvas.draw_polygon([[400, 330], [440, 330], [440, 370], [400, 370]], 5, "Blue", "Blue")
        canvas.draw_text("10", [410, 360], 22, "White")
        
        for num in range(0, game_field.no_of_lvls_played() - 1):
            if num < 5:                
                canvas.draw_polygon([[-50 + (5 - num) * 90, 330], [-10 + (5 - num) * 90, 330], [-10 + (5 - num) * 90, 370], [-50 + (5 - num) * 90, 370]], 5, "Silver", "Silver")                
            elif num < 9:    
                canvas.draw_polygon([[-50 + (10 - num) * 90, 260], [-10 + (10 - num) * 90, 260], [-10 + (10 - num) * 90, 300], [-50 + (10 - num) * 90, 300]], 5, "Silver", "Silver")
    
    elif status == "LVL":
        canvas.draw_image(lava_level_passed_image, lava_level_passed_info.get_center(), lava_level_passed_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
       
        if (game_field.get_current_level() != game_field.get_level_list()[-1]):
            canvas.draw_polygon([[260, 510], [455, 510], [455, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("NEXT LEVEL", [270, 540], 22, "White")
            
    elif status == "HowToPlay":
        canvas.draw_image(lava_instructions_image, lava_instructions_info.get_center(), lava_instructions_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[540, 590],  [540, 550], [350, 550],[350, 590]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [360, 580], 22, "White")
        
    elif status == "Paused":
        canvas.draw_image(lava_tile_image, lava_tile_info.get_center(), lava_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw_lava(canvas)
        draw_options(canvas)
        main_character[0].draw(canvas)
        canvas.draw_image(pause_image_image, pause_image_info.get_center(), pause_image_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
        canvas.draw_image(play_button_image, play_button_info.get_center(), play_button_info.get_size(), [30, EXTRA_HEIGHT - tile_size / 2], [pause_sign_info.get_size()[0] / 25, pause_sign_info.get_size()[1] / 27])
    elif status == "too bad so sad":
        canvas.draw_image(lava_tile_image, lava_tile_info.get_center(), lava_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw_lava(canvas)
        draw_options(canvas)
        canvas.draw_image(try_again_image, try_again_info.get_center(), try_again_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
        canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
        canvas.draw_text("RETRY", [270, 540], 22, "White")        
       
def draw_water(canvas):
    if status == "inPlay":
        canvas.draw_image(water_tile_image, water_tile_info.get_center(), water_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        #game_field.draw_ice(canvas)
        game_field.draw_water(canvas)
        draw_options(canvas)
        main_character[0].draw(canvas)
        main_character[0].findNextTile(game_field.get_current_level("layout"))
        main_character[0].move()
        if main_character[0].check_moving() == False:
            main_character[0].check_tile(game_field.get_current_level("layout"))

        if message!= "":
            canvas.draw_polygon([[0, ((HEIGHT + EXTRA_HEIGHT) / 2) - 20], [WIDTH, ((HEIGHT + EXTRA_HEIGHT) / 2) - 20], [WIDTH, (HEIGHT + EXTRA_HEIGHT) / 2 + 15], [0, (HEIGHT + EXTRA_HEIGHT) / 2 + 15]], 5, "Blue", "Blue")
            canvas.draw_text(message, [15, (HEIGHT + EXTRA_HEIGHT) / 2 + 5],22, "White")
    elif status == "HomeScreen":
        canvas.draw_image(water_level_select_image, water_level_select_info.get_center(), water_level_select_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [140, 510], [140, 550], [40, 550]], 5, "Blue", "Blue") #copy to all classes
        canvas.draw_text("BACK", [50, 540], 22, "White")
        canvas.draw_polygon([[180, 510], [400, 510], [400, 550], [180, 550]], 5, "Blue", "Blue")
        canvas.draw_text("HOW TO PLAY", [190, 540], 22, "White")
        canvas.draw_polygon([[40, 260], [80, 260], [80, 300], [40, 300]], 5, "Blue", "Blue")
        canvas.draw_text("1", [50, 290], 22, "White")
        canvas.draw_polygon([[130, 260], [170, 260], [170, 300], [130, 300]], 5, "Blue", "Blue")
        canvas.draw_text("2", [140, 290], 22, "White")
        canvas.draw_polygon([[220, 260], [260, 260], [260, 300], [220, 300]], 5, "Blue", "Blue")
        canvas.draw_text("3", [230, 290], 22, "White")
        canvas.draw_polygon([[310, 260], [350, 260], [350, 300], [310, 300]], 5, "Blue", "Blue")
        canvas.draw_text("4", [320, 290], 22, "White")
        canvas.draw_polygon([[400, 260], [440, 260], [440, 300], [400, 300]], 5, "Blue", "Blue")
        canvas.draw_text("5", [410, 290], 22, "White")
        canvas.draw_polygon([[40, 330], [80, 330], [80, 370], [40, 370]], 5, "Blue", "Blue")
        canvas.draw_text("6", [50, 360], 22,"White")
        canvas.draw_polygon([[130, 330], [170, 330], [170, 370], [130, 370]], 5, "Blue", "Blue")
        canvas.draw_text("7", [140, 360], 22, "White")
        canvas.draw_polygon([[220, 330], [260, 330], [260, 370], [220, 370]], 5, "Blue", "Blue")
        canvas.draw_text("8", [230, 360], 22, "White")
        canvas.draw_polygon([[310, 330], [350, 330], [350, 370], [310, 370]], 5, "Blue", "Blue")
        canvas.draw_text("9", [320, 360], 22, "White")
        canvas.draw_polygon([[400, 330], [440, 330], [440, 370], [400, 370]], 5, "Blue", "Blue")
        canvas.draw_text("10", [410, 360], 22, "White")
        for num in range(0, game_field.no_of_lvls_played() - 1):
            if num < 5:                
                canvas.draw_polygon([[-50 + (5 - num) * 90, 330], [-10 + (5 - num) * 90, 330], [-10 + (5 - num) * 90, 370], [-50 + (5 - num) * 90, 370]], 5, "Silver", "Silver")                
            elif num < 9:    
                canvas.draw_polygon([[-50 + (10 - num) * 90, 260], [-10 + (10 - num) * 90, 260], [-10 + (10 - num) * 90, 300], [-50 + (10 - num) * 90, 300]], 5, "Silver", "Silver")
    elif status == "LVL":
        canvas.draw_image(water_level_passed_image, water_level_passed_info.get_center(), water_level_passed_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
       
        if (game_field.get_current_level() != game_field.get_level_list()[-1]):
            canvas.draw_polygon([[260, 510], [455, 510], [455, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("NEXT LEVEL", [270, 540], 22, "White")
        
    elif status == "HowToPlay":
        canvas.draw_image(water_instructions_image, water_instructions_info.get_center(), water_instructions_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[540, 590],  [540, 550], [350, 550],[350, 590]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [360, 580], 22, "White")
        
    elif status == "Paused":
        canvas.draw_image(water_tile_image, water_tile_info.get_center(), water_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw_water(canvas)
        draw_options(canvas)
        main_character[0].draw(canvas)
        canvas.draw_image(pause_image_image, pause_image_info.get_center(), pause_image_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
        canvas.draw_image(play_button_image, play_button_info.get_center(), play_button_info.get_size(), [30, EXTRA_HEIGHT - tile_size / 2], [pause_sign_info.get_size()[0] / 25, pause_sign_info.get_size()[1] / 27])
        canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
        canvas.draw_text("RETRY", [270, 540], 22, "White")
    elif status == "too bad so sad":
        canvas.draw_image(water_tile_image, water_tile_info.get_center(), water_tile_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        game_field.draw_water(canvas)
        draw_options(canvas)
        main_character[0].draw(canvas)
        canvas.draw_image(try_again_image, try_again_info.get_center(), try_again_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
        canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
        canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
        canvas.draw_text("RETRY", [270, 540], 22, "White")        
        
        
def click(pos):
    global status, game_field, playedLevels, main_character, tile_size, EXTRA_HEIGHT, Ttime
    if status == "MainScreen":
        global worldCount, main_character, game_field, current_world
        worldCount = pos[0] // 110
        main_character = characters[worldCount]
        current_world = worlds[worldCount]
        game_field = fields[worldCount]
        status = "HomeScreen"
        return
    if status == "HomeScreen":
        center = [60, 280]
        size = [40, 40]
        inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
        if (pos[0] - 40) % 90 <= size[0] and (pos[0] - 40) % 90 > 0 and inheight:            
            game_field.select_level((pos[0] - 40) // 90 + 1, "inPlay")
            Ttime = 0
        else:
            center = [60, 350]
            inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
            if (pos[0] - 40) % 90 <= size[0] and (pos[0] - 40) % 90 > 0 and inheight:            
                game_field.select_level((pos[0] - 40) // 90 + 6, "inPlay")
                Ttime = 0
            else:
                center = [290, 530]
                size = [220, 40]
                inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
                inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
                if inheight == True and inwidth == True:
                    status = "HowToPlay"
                    return
                else:
                    center = [90, 530]
                    size = [100, 40]
                    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
                    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
                    if inheight == True and inwidth == True:
                        status = "MainScreen"
                        return
    elif status == "inPlay":
        center = [30, 20]
        size = [pause_image_info.get_size()[0] /  10, pause_image_info.get_size()[1] / 12]
        inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
        inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
        if inheight == True and inwidth == True:
            status = "Paused"
            return
    elif status == "Paused" or status == "too bad so sad":
        center = [135, 530]
        size = [190, 40]
        inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
        inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
        if inheight == True and inwidth == True:
            status = "HomeScreen"
            return
        else:
            center = [30, 20]
            size = [pause_sign_info.get_size()[0] /  10, pause_sign_info.get_size()[1] / 12]
            inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
            inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
            if inheight == True and inwidth == True and status != "too bad so sad":
                status = "inPlay"
                return
            else:
                center = [335, 530]
                size = [150, 40]
                inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
                inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
                if inheight == True and inwidth == True:
                    lvl = game_field.get_current_level()
                    lvl.reset_level()
                    status = "inPlay"
                    main_character[0].teleport()
                    main_character[-1].teleport()
                    return
    elif status == "LVL":
        center = [357, 530]
        size = [195, 40]
        inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
        inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
        if inheight == True and inwidth == True:
            if worldCount == 0:
                game_field.next_level(2)
            elif worldCount == 1:
                game_field.next_level([5])
            elif worldCount == 2:
                game_field.next_level(4)
            elif worldCount == 3:
                game_field.next_level()
            elif worldCount == 4:
                game_field.next_level(2)
            lvl = game_field.get_current_level()
            lvl.play_level()
            main_character[0].stop_moving()
            main_character[-1].stop_moving()
            if worldCount == 0:
                starting = game_field.get_current_level("start",2)
                        
            elif worldCount == 1:
                starting = game_field.get_current_level("start")
            elif worldCount == 2:
                starting = game_field.get_current_level("start",4)
            elif worldCount == 3:
                starting = game_field.get_current_level("start")
            elif worldCount == 4:
                starting = game_field.get_current_level("start",2)
            EXTRA_HEIGHT = WIDTH / game_field.get_current_level("dimension")
            tile_size = WIDTH / game_field.get_current_level("dimension")
            main_character[0].teleport()
            main_character[-1].teleport()
            status = "inPlay"
            Ttime = 0
            return
        else:
            center = [90, 530]
            size = [100, 40]
            inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
            inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
            if inheight == True and inwidth == True:
                status = "MainScreen"
                return
    elif status == "HowToPlay":
        center = [445, 580]
        size = [190, 40]
        inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
        inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
        if inheight == True and inwidth == True:
            status = "HomeScreen"
            return
            
def draw_options(canvas):
    recTime = game_field.get_current_level().get_record()
    canvas.draw_polygon([[2, 2], [2, EXTRA_HEIGHT], [WIDTH, EXTRA_HEIGHT], [WIDTH, 2]], 0.1, "White")
    canvas.draw_text("World " + str(worldCount + 1) + " Lvl:" + str(game_field.get_level_list().index(game_field.get_current_level()) + 1), [40, EXTRA_HEIGHT - tile_size / 10], 30, "#ededff", "century-gothic")
    canvas.draw_text("" + str(Ttime // 60) + ":" + str((Ttime % 60) // 10) + str((Ttime % 60) % 10) + " Record: " + "" + str(recTime // 60) + ":" + str((recTime % 60) // 10) + str((recTime % 60) % 10), [290, (EXTRA_HEIGHT - tile_size / 10) - 7], 24, "#ededff", "comic")
    if status != "Paused":
        canvas.draw_image(pause_sign_image, pause_sign_info.get_center(), pause_sign_info.get_size(), [50, EXTRA_HEIGHT - tile_size / 2], [pause_sign_info.get_size()[0] / 15, pause_sign_info.get_size()[1] / 17])

    '''if stars == 0:
        canvas.draw_image(zero_stars_collected_image, zero_stars_collected_info.get_center(), zero_stars_collected_info.get_size(), [450, EXTRA_HEIGHT / 2], [WIDTH / 4, EXTRA_HEIGHT])
    elif stars == 1:
        canvas.draw_image(one_stars_collected_image, one_stars_collected_info.get_center(), one_stars_collected_info.get_size(), [450, EXTRA_HEIGHT / 2], [WIDTH / 4, EXTRA_HEIGHT])
    elif stars == 2:
        canvas.draw_image(two_stars_collected_image, two_stars_collected_info.get_center(), two_stars_collected_info.get_size(), [450, EXTRA_HEIGHT / 2], [WIDTH / 4, EXTRA_HEIGHT])
    elif stars == 3:
        canvas.draw_image(three_stars_collected_image, three_stars_collected_info.get_center(), three_stars_collected_info.get_size(), [450, EXTRA_HEIGHT / 2], [WIDTH / 4, EXTRA_HEIGHT])
 '''
    
def draw(canvas):
            
    if worldCount == 0:
        draw_ice(canvas)
        if status == "too bad so sad":
            canvas.draw_image(try_again_image, try_again_info.get_center(), try_again_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
            canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
            canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
            canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("RETRY", [270, 540], 22, "White")
        elif status == "Paused":
            canvas.draw_image(pause_image_image, pause_image_info.get_center(), pause_image_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
            canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
            canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
            canvas.draw_image(play_button_image, play_button_info.get_center(), play_button_info.get_size(), [30, EXTRA_HEIGHT - tile_size / 2], [pause_sign_info.get_size()[0] / 25, pause_sign_info.get_size()[1] / 27])
            canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("RETRY", [270, 540], 22, "White")
        
    elif worldCount == 1:
        draw_water(canvas)
        if status == "too bad so sad":
            canvas.draw_image(try_again_image, try_again_info.get_center(), try_again_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
            canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
            canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
            canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("RETRY", [270, 540], 22, "White")
        elif status == "Paused":
            canvas.draw_image(pause_image_image, pause_image_info.get_center(), pause_image_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
            canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
            canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
            canvas.draw_image(play_button_image, play_button_info.get_center(), play_button_info.get_size(), [30, EXTRA_HEIGHT - tile_size / 2], [pause_sign_info.get_size()[0] / 25, pause_sign_info.get_size()[1] / 27])
            canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("RETRY", [270, 540], 22, "White")
    elif worldCount == 2:
        draw_lava(canvas)
        if status == "too bad so sad":
            canvas.draw_image(try_again_image, try_again_info.get_center(), try_again_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
            canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
            canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
            canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("RETRY", [270, 540], 22, "White")

        elif status == "Paused":
            canvas.draw_image(pause_image_image, pause_image_info.get_center(), pause_image_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
            canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
            canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
            canvas.draw_image(play_button_image, play_button_info.get_center(), play_button_info.get_size(), [30, EXTRA_HEIGHT - tile_size / 2], [pause_sign_info.get_size()[0] / 25, pause_sign_info.get_size()[1] / 27])
            canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("RETRY", [270, 540], 22, "White")
    elif worldCount == 3:
        draw_spaceship(canvas)
        if status == "too bad so sad":
            canvas.draw_image(try_again_image, try_again_info.get_center(), try_again_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
            canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
            canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
            canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("RETRY", [270, 540], 22, "White")
        elif status == "Paused":
            canvas.draw_image(pause_image_image, pause_image_info.get_center(), pause_image_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
            canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
            canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
            canvas.draw_image(play_button_image, play_button_info.get_center(), play_button_info.get_size(), [30, EXTRA_HEIGHT - tile_size / 2], [pause_sign_info.get_size()[0] / 25, pause_sign_info.get_size()[1] / 27])
            canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("RETRY", [270, 540], 22, "White")
    elif worldCount == 4:
        draw_future(canvas)
        if status == "too bad so sad":
            canvas.draw_image(try_again_image, try_again_info.get_center(), try_again_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
            canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
            canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
            canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("RETRY", [270, 540], 22, "White")
        elif status == "Paused":
            canvas.draw_image(pause_image_image, pause_image_info.get_center(), pause_image_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
            canvas.draw_polygon([[40, 510], [230, 510], [230, 550], [40, 550]], 5, "Blue", "Blue")
            canvas.draw_text("MAIN MENU", [50, 540], 22, "White")
            canvas.draw_image(play_button_image, play_button_info.get_center(), play_button_info.get_size(), [30, EXTRA_HEIGHT - tile_size / 2], [pause_sign_info.get_size()[0] / 25, pause_sign_info.get_size()[1] / 27])
            canvas.draw_polygon([[260, 510], [410, 510], [410, 550], [260, 550]], 5, "Blue", "Blue")
            canvas.draw_text("RETRY", [270, 540], 22, "White")
    if status == "inPlay":
        draw_options(canvas)
    if status == "MainScreen":
        canvas.draw_image(main_title_image, main_title_info.get_center(), main_title_info.get_size(), [WIDTH / 2, (HEIGHT + EXTRA_HEIGHT) / 2], [WIDTH, HEIGHT + EXTRA_HEIGHT])
        canvas.draw_text("Click on a world to play", [50, 530], 20, "White")
    if status == "inPlay" and notice:
        stars = game_field.get_current_level("star")
        if stars == 1:
            canvas.draw_image(one_stars_collected_image, one_stars_collected_info.get_center(), one_stars_collected_info.get_size(), [275, 300], [WIDTH, HEIGHT * 0.35])
        elif stars == 2:
            canvas.draw_image(two_stars_collected_image, two_stars_collected_info.get_center(), two_stars_collected_info.get_size(), [275, 300], [WIDTH, HEIGHT * 0.35])
        elif stars == 3:
            canvas.draw_image(three_stars_collected_image, three_stars_collected_info.get_center(), three_stars_collected_info.get_size(), [275, 300], [WIDTH, HEIGHT * 0.35])

        
def tick():
    global message
    main_character[0].teleport()
    main_character[-1].teleport()

    message = ""
    timer.stop()
  
def tock():
    global status, message
    message = ""
    status = "HomeScreen"
    
def ticktock():
    global sound
    sound.pause()
    sound.rewind()
    sound.play()

def ticktocktick():
    field = game_field.get_current_level("layout")
    for i in range(0, int(game_field.get_current_level("dimension"))):
        for j in range(0, game_field.get_current_level("dimension")):
            if field[i][j] == 9:
                lvl = game_field.get_current_level()
                lvl.change_tile([i, j], 0)
    timer5.stop()

def tocktick():
    global disabled
    disabled = False
    timerqwerty.stop()
    
def ticktockticktock():
    global message, disabled
    message = ""
    lvl = game_field.get_current_level()
    main_character[0].reset_size()
    main_character[0].stop_moving()
    starting = game_field.get_current_level("start")
    EXTRA_HEIGHT = WIDTH / game_field.get_current_level("dimension")
    tile_size = WIDTH / game_field.get_current_level("dimension")
    lvl.reset_level()
    main_character[0].teleport()
    main_character[0].change_turn(0)
    timer_water.stop()
    #disabled = True
    #timerqwerty.start()
    
def ticktockticktocktick():
    main_character[0].teleportation()
    main_character[0].set_tele(True)
    main_character[0].set_tele_coord([])  
    timer4.stop()
def ticktockticktockticktock():
    main_character[0].set_condition(True)
    timer6.stop()

def twick():
    FFile = open("C:/Python27/Lib/json/temp-data.json", "w+")
    data = ""
    for tempnum in range(0, 5):
        tempfield = fields[tempnum]
        data += str(10 - tempfield.no_of_lvls_played())
    FFile.write(data)
    FFFile = open("C:/Python27/Lib/json/temp-record-data.json", "w+")
    ddata = ""
    for tempnum in range(0, 5):
        for temptempnum in range(0, 10):
            lvl = fields[tempnum].get_level_list()[temptempnum]
            ddata += "" + str(lvl.get_record()//100) + str((lvl.get_record()%100)//10) + str(lvl.get_record() % 10)
    FFFile.write(ddata)

def twock():
    global Ttime
    if status == "inPlay":
        Ttime += 1

def twicktwock():
    global notice
    notice = False
    timerA.stop()
    
    
warnings.filterwarnings("ignore")

frame = simplegui.create_frame("Rainbow Raider", WIDTH, HEIGHT + EXTRA_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
timer = simplegui.create_timer(2000, tick)
timer_water = simplegui.create_timer(2000, ticktockticktock)
timer2 = simplegui.create_timer(2000, tock)
timer3 = simplegui.create_timer(200000, ticktock)
timer5 = simplegui.create_timer(500, ticktocktick)
timer4 = simplegui.create_timer(1000, ticktockticktocktick)
timer6 = simplegui.create_timer(1501, ticktockticktockticktock)
timerQ = simplegui.create_timer(10000, twick)
timerCounter = simplegui.create_timer(1000, twock)
timerA = simplegui.create_timer(5000, twicktwock)

timerQ.start()
timerCounter.start()

timerqwerty = simplegui.create_timer(20, tocktick)
# Start the frame animation
frame.start()
timer3.start()


frame.start()




