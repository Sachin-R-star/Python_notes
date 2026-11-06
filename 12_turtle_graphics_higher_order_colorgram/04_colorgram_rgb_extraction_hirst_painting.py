"""
================================================================================
LECTURE 126: Extracting RGB Values from Images using Colorgram (#lec117)
Project Application: Damien Hirst Spot Painting
================================================================================

BRIEF HINGLISH EXPLANATION:
---------------------------
1. Colorgram Package kya hai?
   - Ek Python package jo images ko analyze karke usme se dominant RGB colors extract karta hai.
   - Installation: `pip install colorgram.py`
   - Extraction syntax: `colors = colorgram.extract("image.jpg", num_colors)`

2. Processing Colorgram Objects:
   - `colors` ek list of color objects return karta hai.
   - Har object ke paas `rgb` property hoti hai: `c.rgb.r`, `c.rgb.g`, `c.rgb.b`.
   - Python tuple format me convert karte hain: `(r, g, b)`.

3. Filtering Background Colors:
   - Aksar images ka background white ya off-white hota hai (`r > 240, g > 240, b > 240`).
   - Spot painting ke liye hum near-white colors ko filter-out (remove) kar dete hain taaki canvas par white dots invisible na hon.

4. Hirst Painting Algorithm:
   - 10 x 10 grid of dots (Total 100 dots).
   - Har dot ka size: 20 pixels radius.
   - Har dot ke beech ka distance: 50 pixels spacing.
   - Har dot par randomly extracted color choose kiya jata hai.
"""

import random

# Extracted color palette from Hirst Painting image (Standard RGB sample list)
SAMPLE_HIRST_RGB_COLORS = [
    (198, 12, 32),
    (248, 236, 25),
    (40, 76, 143),
    (238, 224, 5),
    (225, 121, 175),
    (223, 160, 4),
    (132, 24, 7),
    (17, 184, 197),
    (134, 178, 214),
    (206, 68, 128),
    (138, 214, 182),
    (235, 165, 149),
    (38, 153, 72)
]

def extract_colors_from_image(image_path, num_colors=20):
    """
    Extracts RGB tuples from image using colorgram.py package.
    Gracefully handles environment if colorgram is not installed.
    """
    try:
        import colorgram
        print(f"Extracting {num_colors} colors from '{image_path}' using colorgram.py...")
        extracted_colors = colorgram.extract(image_path, num_colors)
        rgb_colors = []

        for color in extracted_colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b

            # Filter out near-white background colors
            if r > 240 and g > 240 and b > 240:
                continue
            rgb_colors.append((r, g, b))

        print(f"Extracted {len(rgb_colors)} valid foreground colors successfully!")
        return rgb_colors
    except ImportError:
        print("(colorgram.py not installed. Run 'pip install colorgram.py' to extract from real files)")
        print("Using curated RGB palette extracted from Hirst Painting artwork.")
        return SAMPLE_HIRST_RGB_COLORS


def simulate_hirst_spot_painting(grid_size=10, dot_radius=20, spacing=50):
    """
    Simulates the 10x10 spot painting grid coordinates and color assignments.
    """
    print("\n--- Simulating 10x10 Hirst Spot Painting ---")
    palette = SAMPLE_HIRST_RGB_COLORS

    grid_dots = []
    for row in range(grid_size):
        for col in range(grid_size):
            x = col * spacing
            y = row * spacing
            chosen_color = random.choice(palette)
            grid_dots.append({"row": row, "col": col, "x": x, "y": y, "color_rgb": chosen_color})

    print(f"Total dots planned: {len(grid_dots)}")
    print("Sample Dot 1:", grid_dots[0])
    print("Sample Dot 50:", grid_dots[49])
    print("Sample Dot 100:", grid_dots[99])
    print("Hirst painting grid calculation completed successfully! 🎨")
    return grid_dots


if __name__ == "__main__":
    print("==========================================")
    print("     COLORGRAM RGB EXTRACTION & HIRST     ")
    print("==========================================")
    colors = extract_colors_from_image("hirst_image.jpg", num_colors=15)
    print(f"\nColor Palette Sample ({len(colors)} colors):")
    for idx, c in enumerate(colors[:5]):
        print(f"  Color #{idx + 1}: RGB{c}")

    simulate_hirst_spot_painting(grid_size=10)
