import pygame as pg

class World():
    def __init__(self, data, map_image):
        self.tile_map = []
        self.waypoints = []
        self.level_data = data
        self.image = map_image

    def process_data(self):
        # Look through data to extract relevent information
        
        for layer in self.level_data['layers']:
            print(layer['name'])
            if layer['name'] == 'tilemap':
                self.tile_map = layer['data']
                print(self.tile_map)
            elif layer['name'] == 'waypoints':
                for object in layer['objects']:
                    waypoint_data = object['polyline']
                    self.process_waypoints(waypoint_data)
                    

    def process_waypoints(self, data):
        # Iterate through waypoints to extract individual x and y coordinates
        for point in data:
            temp_x = point.get('x')
            temp_y = point.get('y')
            self.waypoints.append((temp_x, temp_y))


    def draw(self, surface):
        # Blit makes a copy of the image and draws it on the screen
        surface.blit(self.image, (0, 0))