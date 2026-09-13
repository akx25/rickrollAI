from PIL import Image
import os
import time

gif = Image.open("gif.gif")

text = "NEVER GONNA GIVE YOU UP "
chars = text.replace(" ", "")

while True:
    try:
        for frame in range(gif.n_frames):
            gif.seek(frame)

            img = gif.convert("RGB")

            width = 70
            height = int(img.height / img.width * width * 0.5)
            img = img.resize((width, height))

            os.system("cls" if os.name == "nt" else "clear")

            char_index = 0

            for y in range(img.height):
                line = ""

                for x in range(img.width):
                    r, g, b = img.getpixel((x, y))

                    brightness = (r + g + b) // 3
                    
                    if brightness < 80:
                        char = " "
                    else:
                        char = chars[char_index % len(chars)]
                        char_index += 1

                    line += f"\033[38;2;{r};{g};{b}m{char}"

                print(line + "\033[0m")

            time.sleep(0.04)

    except KeyboardInterrupt:
        print("\nQuit.")
        break
