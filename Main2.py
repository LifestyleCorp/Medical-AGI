import pygame
import random
import math

# Initialize pygame
pygame.init()

# Hospital Constants
DOCTOR_SPEED = 2
NURSE_SPEED = 3
PATIENT_SPEED = 1
HELP_REQUEST_CHANCE = 0.01  # Chance per frame that a patient requests help

# Constants
WINDOW_WIDTH = 810
WINDOW_HEIGHT = 800
SPEED = 3
DETECTION_RADIUS = 100
CONVERSION_RADIUS = 20
EDGE_AVOID_RADIUS = 50
REPULSION_RADIUS = 20
ICON_WIDTH = 30
ICON_HEIGHT = 30



# Load and scale hospital related icons
doctor_icon = pygame.image.load('doc1.png')
doctor_icon = pygame.transform.scale(doctor_icon, (ICON_WIDTH, ICON_HEIGHT))

# Load and scale nurse icon
nurse_icon = pygame.image.load('doc1.png')
nurse_icon = pygame.transform.scale(nurse_icon, (ICON_WIDTH, ICON_HEIGHT))

# Load and scale patient icon
patient_icon = pygame.image.load('doc1.png')
patient_icon = pygame.transform.scale(patient_icon, (ICON_WIDTH, ICON_HEIGHT))

# Load and scale hospital floor plan
background_image = pygame.image.load('hospitallayout1i.png')
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

class Entity:
    def __init__(self, x, y, role):
        self.x = x
        self.y = y
        self.role = role       

    # Modify draw method to reflect hospital roles instead of tribes
    def draw(self):
        if self.role == 'doctor':
            screen.blit(doctor_icon, (self.x - ICON_WIDTH//2, self.y - ICON_HEIGHT//2))
        elif self.role == 'nurse':
            screen.blit(nurse_icon, (self.x - ICON_WIDTH//2, self.y - ICON_HEIGHT//2))
        else:  # 'patient'
            screen.blit(patient_icon, (self.x - ICON_WIDTH//2, self.y - ICON_HEIGHT//2))
        
    # New movement methods reflecting different roles and their movement patterns
    def move(self):
        if self.role == 'doctor':
            # Doctors move at their own pace, visiting patients
            self.patrol()
        elif self.role == 'nurse':
            # Nurses might need to respond to patient needs quickly
            self.respond_to_needs()
        elif self.role == 'patient':
            # Patients generally stay put or move slowly
            self.wander()

    # Example methods for different character behaviors
    def patrol(self):
        # A simple patrol pattern for doctors, could be improved with actual pathfinding logic
        move_x = random.randint(-1, 1) * DOCTOR_SPEED
        move_y = random.randint(-1, 1) * DOCTOR_SPEED
        self.x += move_x
        self.y += move_y
        self.avoid_edges()

    def respond_to_needs(self):
        # Nurses might need to move to a patient's location quickly 
        # Further implementation would be based on patients' requests for help
        move_x = random.randint(-1, 1) * NURSE_SPEED
        move_y = random.randint(-1, 1) * NURSE_SPEED
        self.x += move_x
        self.y += move_y
        self.avoid_edges()

    def wander(self):
        # Patients simply wander around their room or in the ward
        move_x = random.randint(-1, 1) * PATIENT_SPEED
        move_y = random.randint(-1, 1) * PATIENT_SPEED
        self.x += move_x
        self.y += move_y
        self.avoid_edges()

    def move_towards(self, target_x, target_y):
        angle = math.atan2(target_y - self.y, target_x - self.x)
        self.x += (SPEED + random.uniform(-0.3, 0.3)) * math.cos(angle)
        self.y += (SPEED + random.uniform(-0.3, 0.3)) * math.sin(angle)
        self.avoid_edges()

    def move_away_from(self, target_x, target_y):
        angle = math.atan2(target_y - self.y, target_x - self.x)
        self.x -= (SPEED + random.uniform(-0.3, 0.3)) * math.cos(angle)
        self.y -= (SPEED + random.uniform(-0.3, 0.3)) * math.sin(angle)
        self.avoid_edges()


    def avoid_edges(self):
        if self.x < EDGE_AVOID_RADIUS:
            self.move_towards(self.x + EDGE_AVOID_RADIUS, self.y)
        elif self.x > WINDOW_WIDTH - EDGE_AVOID_RADIUS:
            self.move_towards(self.x - EDGE_AVOID_RADIUS, self.y)
        if self.y < EDGE_AVOID_RADIUS:
            self.move_towards(self.x, self.y + EDGE_AVOID_RADIUS)
        elif self.y > WINDOW_HEIGHT - EDGE_AVOID_RADIUS:
            self.move_towards(self.x, self.y - EDGE_AVOID_RADIUS)        

    # Avoid edges logic can be kept as it was before as a simple edge avoidance
    # ...

entities = []


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Medical Agi")
clock = pygame.time.Clock()
running = True


# Example to create patients, doctors, and nurses
for _ in range(10):
    entities.append(Entity(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), 'patient'))
for _ in range(5):
    entities.append(Entity(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), 'doctor'))
for _ in range(10):
    entities.append(Entity(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), 'nurse'))

def adjust_movement(entities):
    for entity in entities:
        entity.move()

# ...

# Now in the game loop, we replace the old logic with the following:

while running:
    screen.blit(background_image, (0, 0))

    adjust_movement(entities)

    for event in pygame.event.get():
        # If the user wants to close the game
        if event.type == pygame.QUIT:
            running = False

    # Let's simulate a patient occasionally needing help
    for entity in entities:
        if entity.role == 'patient' and random.random() < HELP_REQUEST_CHANCE:            
            # Here you would implement logic to alert nearby nurses or set a help needed flag for the patient
            pass

    # Now draw the entities
    for entity in entities:
        entity.draw()


    
    # Update the full display Surface to the screen
    pygame.display.flip()

    # Ensure program maintains a rate of 60 frames per second
    clock.tick(60)

# If the loop ends, quit pygame
