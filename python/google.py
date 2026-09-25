

# Create canvas
W, H = 900, 900
BG = "#F7F7F7"
img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

cx, cy = W // 2, H // 2
radius = 270
ring_width = 70

# Google-like colors
segments = [
    ("#4285F4", 20, 150),   # Blue
    ("#EA4335", 150, 250),  # Red
    ("#FBBC05", 250, 330),  # Yellow
    ("#34A853", 330, 420),  # Green
]

# Draw the colorful ring segments
for color, start, end in segments:
    draw.arc(
        (cx - radius, cy - radius, cx + radius, cy + radius),
        start=start,
        end=end,
        fill=color,
        width=ring_width,
    )

# Remove the center to create the "G" shape
# Big white cut-out to carve the inner area
inner = (cx - 170, cy - 170, cx + 170, cy + 170)
draw.ellipse(inner, fill=BG, outline=BG)

# Add internal white bars to make the logo more like a Google G
# Top-left/upper horizontal cut
bar1 = (cx - 110, cy - 20, cx + 150, cy + 45)
draw.rectangle(bar1, fill=BG)

# Lower part of the G, to create the opening
bar2 = (cx - 30, cy + 70, cx + 140, cy + 135)
draw.rectangle(bar2, fill=BG)

# Optional subtle contour for a polished look
outline = (cx - radius, cy - radius, cx + radius, cy + radius)
draw.arc(outline, start=0, end=360, outline="#E2E2E2", width=2)

# Add a tiny shadow/glow effect
img = img.filter(ImageFilter.GaussianBlur(radius=0.4))

# Save the final logo
img.save("google_logo.png")
img.show()
print("Saved google_logo.png")
