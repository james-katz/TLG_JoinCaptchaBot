# -*- coding: utf-8 -*-

'''
Script:
    pilutils.py
Description:
    Functions to generate images.
Author:
    James Katz
Creation date:
    01/17/2024
Last modified date:
    01/17/2024
Version:
    1.0
'''

import math
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap

from constants import CONST

def pil_gen_image_from_text(text, image_width=512, random_font_size=False, random_lines=False, output_path=CONST["POLLS_DIR"]):
    '''Generate an image from a text string.'''
    # Create a blank image with a white background        
    image = Image.new('RGB', (image_width, 1), color='white')
    draw = ImageDraw.Draw(image)

    # Set the font and size (using the default system font)
    font_size = 24
    if random_font_size:
        font_size = random.randint(24, 32)
    font = ImageFont.truetype(f'{CONST["FONTS_DIR"]}/{CONST["DEFAULT_FONT"]}', font_size)

    # Wrap the text based on the specified width
    wrapped_text = textwrap.fill(text, width=int(image_width / font_size * 2))

    # Calculate the total height required for the wrapped text
    text_height = draw.multiline_textsize(wrapped_text, font=font)[1]

    # Create a new image with the calculated height
    image = Image.new('RGB', (image_width, text_height + 8), color='white')
    draw = ImageDraw.Draw(image)

    # Draw the wrapped text on the image
    draw.multiline_text((0, 0), wrapped_text, font=font, fill='black')

    if random_lines:
        # Draw random lines on top of the image
        for _ in range(30):
            line_thickness = random.randint(1, 3)
            line_length = random.randint(10, min(image_width, text_height) // 2)
            line_angle = random.uniform(0, 2 * math.pi)
            line_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            # Calculate line endpoints
            x1 = random.randint(0, image_width)
            y1 = random.randint(0, text_height)
            x2 = x1 + int(line_length * math.cos(line_angle))
            y2 = y1 + int(line_length * math.sin(line_angle))

            # Draw the line on the image
            draw.line([(x1, y1), (x2, y2)], fill=line_color, width=line_thickness)

    # Save the image to the specified output path
    file_path = f"{output_path}/poll_question.png" 
    image.save(file_path)

    return file_path