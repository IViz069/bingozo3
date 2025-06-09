from __future__ import annotations
import os
import random
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "arial_black.ttf"
FONT_SIZE = 100
TEMPLATE_PATH = "img/carta.png"

START_X = 250
START_Y = 650
CELL_WIDTH = 255
CELL_HEIGHT = 260
FIRST_COLUMN_OFFSET = 30


def create_output_directory() -> Path:
    """Create a timestamped directory to store the generated bingo cards."""
    timestamp = datetime.now().strftime("%d-%b-%Y-%H-%M-%S")
    path = Path(timestamp)
    path.mkdir(exist_ok=True)
    return path


def generate_columns() -> list[list[int]]:
    """Return a list of five columns with random bingo numbers."""
    return [
        random.sample(range(1, 16), 5),
        random.sample(range(16, 31), 5),
        random.sample(range(31, 46), 5),
        random.sample(range(46, 61), 5),
        random.sample(range(61, 76), 5),
    ]


def draw_card(columns: list[list[int]], font: ImageFont.FreeTypeFont) -> Image.Image:
    """Draw the bingo numbers on the template image."""
    image = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(image)

    for col_idx, column in enumerate(columns):
        for row_idx, number in enumerate(column):
            # Skip the center square (free space)
            if col_idx == 2 and row_idx == 2:
                continue

            x = START_X + col_idx * CELL_WIDTH
            y = START_Y + row_idx * CELL_HEIGHT

            # Adjust alignment for single digit numbers in the first column
            if col_idx == 0 and number < 10:
                x += FIRST_COLUMN_OFFSET

            draw.text((x, y), str(number), font=font, fill=(255, 255, 255))

    return image


def log_card(file_handle, index: int, columns: list[list[int]]):
    """Write the bingo numbers of a card to the log file."""
    file_handle.write(f"bingo{index:03}\n")
    file_handle.write("B   I   N   G   O\n")

    for row_idx in range(5):
        row_values = []
        for col_idx, column in enumerate(columns):
            if col_idx == 2 and row_idx == 2:
                row_values.append("  ")
            else:
                row_values.append(f"{column[row_idx]:>2}")
        file_handle.write("  ".join(row_values) + "\n")

    file_handle.write("--------------------------------\n")


def main():
    num_cards = int(input("Ingrese la cantidad de bingos a generar: "))
    output_dir = create_output_directory()
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    log_path = output_dir / f"bingos{output_dir.name}.txt"

    with open(log_path, "w") as log_file:
        for index in range(num_cards):
            columns = generate_columns()
            card_image = draw_card(columns, font)
            card_image.save(output_dir / f"bingo{index:03}.png")
            log_card(log_file, index, columns)
            print(f"Bingo {index:03} generado")


if __name__ == "__main__":
    main()
