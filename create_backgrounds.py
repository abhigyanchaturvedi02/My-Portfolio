import os
import random
import math

# Create photos directory if it doesn't exist
photos_dir = os.path.join(os.getcwd(), "photos")
if not os.path.exists(photos_dir):
    os.makedirs(photos_dir)
    print(f"Created directory: {photos_dir}")

# Function to create a minimalist HTML background
def create_html_background(filename, bg_color, pattern_type, pattern_color):
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Background - {pattern_type}</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: {bg_color};
            width: 100vw;
            height: 100vh;
            overflow: hidden;
        }}
        
        .container {{
            width: 100%;
            height: 100%;
            position: relative;
"""

    # Add specific CSS based on pattern type
    if pattern_type == "grid":
        html_content += f"""
            background-image: 
                linear-gradient({pattern_color} 1px, transparent 1px),
                linear-gradient(90deg, {pattern_color} 1px, transparent 1px);
            background-size: 40px 40px;
"""
    elif pattern_type == "dots":
        html_content += f"""
            background-image: radial-gradient({pattern_color} 1px, transparent 1px);
            background-size: 40px 40px;
"""
    elif pattern_type == "gradient":
        darker_color = darken_color(bg_color, 10)
        html_content += f"""
            background: linear-gradient(to bottom, {bg_color}, {darker_color});
"""
    elif pattern_type == "diagonal":
        html_content += f"""
            background-image: 
                linear-gradient(45deg, {pattern_color} 25%, transparent 25%),
                linear-gradient(-45deg, {pattern_color} 25%, transparent 25%);
            background-size: 60px 60px;
            background-position: 0 0, 30px 30px;
            opacity: 0.1;
"""
    elif pattern_type == "minimal":
        html_content += f"""
            background: {bg_color};
"""
        # Add a few random minimal shapes
        for i in range(5):
            size = random.randint(100, 300)
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            opacity = random.uniform(0.03, 0.08)
            shape = "square" if random.random() > 0.5 else "circle"
            
            html_content += f"""
            .shape-{i} {{
                position: absolute;
                width: {size}px;
                height: {size}px;
                {"border-radius: 50%;" if shape == "circle" else ""}
                background-color: {pattern_color};
                opacity: {opacity};
                top: {y}%;
                left: {x}%;
            }}
"""

    # Close style and add HTML if needed
    html_content += f"""
        }}
    </style>
</head>
<body>
    <div class="container">
"""

    # Add shape divs for minimal pattern
    if pattern_type == "minimal":
        for i in range(5):
            html_content += f'        <div class="shape-{i}"></div>\n'

    html_content += """
    </div>
</body>
</html>
"""

    # Save the HTML file
    file_path = os.path.join(photos_dir, filename)
    with open(file_path, "w") as f:
        f.write(html_content)
    
    print(f"Created {filename}")

# Helper function to darken a color
def darken_color(hex_color, percent):
    # Remove # if present
    hex_color = hex_color.lstrip('#')
    
    # Convert to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    # Darken
    factor = 1 - percent/100
    r = max(0, int(r * factor))
    g = max(0, int(g * factor))
    b = max(0, int(b * factor))
    
    # Convert back to hex
    return f"#{r:02x}{g:02x}{b:02x}"

# Create backgrounds
print("Generating minimalist background HTML files...")

# Light theme backgrounds
create_html_background("grid-light.html", "#fcfcfc", "grid", "#f0f0f0")
create_html_background("dots-light.html", "#fcfcfc", "dots", "#f0f0f0")
create_html_background("gradient-light.html", "#fcfcfc", "gradient", "#f0f0f0")
create_html_background("diagonal-light.html", "#fcfcfc", "diagonal", "#f0f0f0")
create_html_background("minimal-light.html", "#fcfcfc", "minimal", "#f0f0f0")

# Dark theme backgrounds
create_html_background("grid-dark.html", "#191919", "grid", "#252525")
create_html_background("dots-dark.html", "#191919", "dots", "#252525")
create_html_background("gradient-dark.html", "#191919", "gradient", "#252525")
create_html_background("diagonal-dark.html", "#191919", "diagonal", "#252525")
create_html_background("minimal-dark.html", "#191919", "minimal", "#252525")

# Create a simple instructions file
instructions = """
# Minimalist Portfolio Background Templates

This folder contains HTML background templates you can use for your minimalist portfolio website.

## How to use:
1. Open any HTML file in your browser to preview the background
2. Take a screenshot of your favorite background
3. Save the screenshot as an image file (jpg or png)
4. Use the image as a background in your portfolio's CSS

## Available Backgrounds:
- grid-light.html & grid-dark.html: Subtle grid pattern backgrounds
- dots-light.html & dots-dark.html: Dotted pattern backgrounds
- gradient-light.html & gradient-dark.html: Subtle gradient backgrounds
- diagonal-light.html & diagonal-dark.html: Diagonal pattern backgrounds
- minimal-light.html & minimal-dark.html: Minimalist backgrounds with subtle shapes

These backgrounds are inspired by minimalist design principles, focusing on clean aesthetics
with subtle visual elements.
"""

with open(os.path.join(photos_dir, "README.md"), "w") as f:
    f.write(instructions)

print("All background templates have been generated in the 'photos' directory.")
print("Open any .html file in your browser to preview, then take a screenshot to use as background.") 