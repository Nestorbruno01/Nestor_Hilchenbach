stars = ['*', '.', '+', '✦', '✧', '☆', '★', ' ']
message = input("What inspirational message should appear the sky? (3–30 characters): ")
while not (3 <= len(message) <= 30):
    message = input("Please enter a message between 3 and 30 characters: ")
sky_width = int(input("How wide do you want the sky to be? (min.20)"))
while sky_width < 20:
    sky_width = int(input("Please enter a number of atleast 20"))
sky_height = int(input("How high do you want the sky to be? (min. 5"))
while sky_height < 5:
    sky_height = int(input("Please enter a number of atleast 5"))

import random
for row in range(sky_height):
    if row == sky_height // 2:
        message_space = (sky_width - len(message)) // 2
        left = ''.join(random.choice(stars) for _ in range(message_space))
        right = ''.join(random.choice(stars) for _ in range(sky_width - message_space - len(message)))
        print(left + message.upper() + right)
    else:
        print(''.join(random.choice(stars) for _ in range(sky_width)))