import pygame as pg
import sys

#Sound Effect by <a href="https://pixabay.com/users/soundreality-31074404/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=233951">Jurij</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=233951">Pixabay</a>
pg.init()
pg.font.init()
pg.mixer.init()
WIDTH, HEIGHT = (1000, 600)
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption("Classrooms through the ages | C_MENU")
c = 0 #menu
roboto = pg.font.SysFont('Roboto', 32)
center = (WIDTH / 2, HEIGHT / 2)
def renderonscr(screen: pg.Surface, content: str, pos: tuple = (0, 0), size: int = 32, font: str = 'Roboto', color = 'white', outline_color = '', outline_thickness: int = 3) -> None:
    __font = pg.font.SysFont(font, size)
    lines = content.split("\n")

    offsets = [(dx, dy) for dx in range(-outline_thickness, outline_thickness + 1) 
                      for dy in range(-outline_thickness, outline_thickness + 1) 
                      if dx != 0 or dy != 0]

    if outline_color != '':
        outline_surface = __font.render(content, True, outline_color)
        for dx, dy in offsets:
            screen.blit(outline_surface, outline_surface.get_rect(center=(pos[0] + dx, pos[1] + dy)))
    
    y_offset = 0
    for line in lines:
        text_surface = __font.render(line, True, color)
        screen.blit(text_surface, text_surface.get_rect(center=(pos[0], pos[1] + y_offset)))
        y_offset += size


if __name__ == "__main__":
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        match c:
            case 0:
                pg.display.set_caption("Classrooms through the ages | C_0_MENU")
                screen.blit(pg.image.load("images\\mainbg.jpg"), (0,-200))
                renderonscr(screen, "CLASSROOMS", pos=(center[0], center[1] - 250), size=100, outline_color='black')
                renderonscr(screen, "THROUGH THE AGES",pos=(center[0], center[1] - 150), size=90, outline_color='black', color='lightgray')
                pg.draw.aaline(screen, 'black', (0, HEIGHT /2 - 120), (WIDTH, HEIGHT / 2 - 120))
                tmp = pg.Rect(0,0, 210, 110)
                tmp.center = (WIDTH / 6, HEIGHT / 1.5)
                pg.draw.rect(screen, 'black', tmp)
                tmp.center = (WIDTH / 6 * 3, HEIGHT / 1.5)
                pg.draw.rect(screen, 'black', tmp)
                tmp.center = (WIDTH / 6 * 5, HEIGHT / 1.5)
                pg.draw.rect(screen, 'black', tmp)
                b1954 = pg.Rect(0,0, 200, 100)
                b1954.center = tmp.center = (WIDTH / 6, HEIGHT / 1.5)
                pg.draw.rect(screen, 'gray', b1954)
                renderonscr(screen, "1994", b1954.center, color='black')
                b2024 = pg.Rect(0,0, 200, 100)
                b2024.center = tmp.center = (WIDTH / 6 * 3, HEIGHT / 1.5)
                pg.draw.rect(screen, 'blue', b2024)
                renderonscr(screen, '2024', b2024.center, color='white')
                b2054 = pg.Rect(0,0, 200, 100)
                b2054.center = tmp.center = (WIDTH / 6 * 5, HEIGHT / 1.5)
                pg.draw.rect(screen, 'lightblue', b2054)
                renderonscr(screen, "2054", b2054.center, color="darkblue")
                tmp = pg.Rect(0,0,130, 90)
                tmp.center = (WIDTH / 6 * 2, HEIGHT - 60)
                pg.draw.rect(screen, 'black', tmp)
                bsg = pg.Rect(0,0,120,80)
                bsg.center = (WIDTH / 6 * 2, HEIGHT - 60)
                pg.draw.rect(screen, 'turquoise', bsg)
                renderonscr(screen, 'STUDY\nGUIDE', (bsg.center[0], bsg.center[1] - 20))
                tmp.center = (WIDTH / 6 * 4, HEIGHT - 60)
                pg.draw.rect(screen, 'black', tmp)
                bhelp = pg.Rect(0,0,120,80)
                bhelp.center = tmp.center
                pg.draw.rect(screen, 'green', bhelp)
                renderonscr(screen, 'HELP', bhelp.center)
                if event.type == pg.MOUSEBUTTONDOWN:
                    if b1954.collidepoint(event.pos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c  = 1
                    if b2024.collidepoint(event.pos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 2
                    if b2054.collidepoint(event.pos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 3
                    if bsg.collidepoint(event.pos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 4
                    if bhelp.collidepoint(event.pos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 6
            case 1:
                pg.display.set_caption("Classrooms through the ages | C_1_1994")
                back = pg.Rect(0,0, 70, 70)
                back.topleft = (0,0)
                bg = pg.image.load("images\\1994class.png")
                screen.blit(bg, (0,0))
                img_scale = 4
                calc = pg.transform.scale(pg.image.load("images\\i_ti82.png"), (35.8 * img_scale, 56.9 * img_scale))
                screen.blit(calc, (WIDTH/6 - 50, HEIGHT / 2))
                tbk = pg.transform.scale(pg.image.load("images\\i_tbk.png"), (39.8 * img_scale, 39.8 * img_scale))
                screen.blit(tbk, (WIDTH / 6 * 2.5 - 50 , HEIGHT / 2 - 130))
                chkbrd = pg.transform.scale(pg.image.load("images\\i_chkbrd.png"), (66.2 * img_scale, 37.7 * img_scale))
                screen.blit(chkbrd, (WIDTH / 6 * 4 - 50, HEIGHT / 2 - 150))
                mousePos = pg.mouse.get_pos()
                if calc.get_rect(topleft= (WIDTH/6 - 50, HEIGHT / 2)).collidepoint(mousePos):
                    inf = pg.Surface((350,200), pg.SRCALPHA)
                    inf.fill('black')
                    inf.set_alpha(200)
                    screen.blit(inf, mousePos)
                    renderonscr(screen, "Calculator", (mousePos[0] + 75, mousePos[1] + 30))
                    pg.draw.aaline(screen, 'white', (mousePos[0] + 5, mousePos[1] + 45), (mousePos[0] + 295, mousePos[1] + 45))
                    renderonscr(screen, "The TI-82 was a calculator\nused in classrooms in 1994. It\ncould show graphs, help with\nmath problems, and do simple\ncalculations. Unlike today’s\ncalculators, it had a black-and-\nwhite screen.",  (mousePos[0] + 179, mousePos[1] + 60), size = 20)
                if tbk.get_rect(topleft= (WIDTH/6 * 2.5 - 50, HEIGHT / 2 - 130)).collidepoint(mousePos):
                    inf = pg.Surface((350,200), pg.SRCALPHA)
                    inf.fill('black')
                    inf.set_alpha(200)
                    screen.blit(inf, mousePos)
                    renderonscr(screen, "Textbook", (mousePos[0] + 75, mousePos[1] + 30))
                    pg.draw.aaline(screen, 'white', (mousePos[0] + 5, mousePos[1] + 45), (mousePos[0] + 295, mousePos[1] + 45))
                    renderonscr(screen, "Textbooks were paper books\nused for learning in school. They\nwere filled with lots of words,\npictures, and exercises. Students relied \ncompletely on these without any computers.",  (mousePos[0] + 179, mousePos[1] + 60), size = 20)
                if chkbrd.get_rect(topleft= (WIDTH/6 * 4 - 50, HEIGHT / 2 - 150)).collidepoint(mousePos):
                    inf = pg.Surface((350,200), pg.SRCALPHA)
                    inf.fill('black')
                    inf.set_alpha(200)
                    screen.blit(inf, mousePos)
                    renderonscr(screen, "Chalkboard", (mousePos[0] + 75, mousePos[1] + 30))
                    pg.draw.aaline(screen, 'white', (mousePos[0] + 5, mousePos[1] + 45), (mousePos[0] + 295, mousePos[1] + 45))
                    renderonscr(screen, "In 1994, classrooms used chalkboards\nto write lessons for students.\nTeachers would use chalk to\nwrite on the board, and it would\nleave dust behind, which students would\n have to clean up.",  (mousePos[0] + 179, mousePos[1] + 60), size = 20)
                pg.draw.rect(screen, 'red', back)
                renderonscr(screen, "BACK", back.center, outline_color='black')
                renderonscr(screen, "1994", outline_color="black", pos=(WIDTH - 90, 30))
                if event.type == pg.MOUSEBUTTONDOWN:
                    if back.collidepoint(event.pos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 0
            case 2:
                pg.display.set_caption("Classrooms through the ages | C_2_2024")
                back = pg.Rect(0,0, 70, 70)
                back.topleft = (0,0)
                bg = pg.image.load("images\\2024class.jpg")
                screen.blit(bg, (0,0))
                img_scale = 4
                pCalc = pg.transform.scale(pg.image.load("images\\i_phonecalc.png"), (32.4 * img_scale, 52.2 * img_scale))
                screen.blit(pCalc, (WIDTH/6 - 50, HEIGHT / 2))
                smrtbrd = pg.transform.scale(pg.image.load("images\\i_smrtbrd.png"), (62.2 * img_scale, 37.7 * img_scale))
                screen.blit(smrtbrd, (WIDTH / 6 * 2.5 - 70 , HEIGHT / 2 - 130))
                proj =  pg.transform.scale(pg.image.load("images\\i_proj.png"), (67.9 * img_scale, 36.7 * img_scale))
                screen.blit(proj, (WIDTH / 6 * 4 - 50, HEIGHT / 2 - 150))
                mousePos = pg.mouse.get_pos()
                if pCalc.get_rect(topleft= (WIDTH/6 - 50, HEIGHT / 2)).collidepoint(mousePos):
                    inf = pg.Surface((350,200), pg.SRCALPHA)
                    inf.fill('black')
                    inf.set_alpha(200)
                    screen.blit(inf, mousePos)
                    renderonscr(screen, "Phone", (mousePos[0] + 75, mousePos[1] + 30))
                    pg.draw.aaline(screen, 'white', (mousePos[0] + 5, mousePos[1] + 45), (mousePos[0] + 295, mousePos[1] + 45))
                    renderonscr(screen, "Phones allow students to research topics,\ncalculate equations, and more.\nThey also help with finishing homework",  (mousePos[0] + 179, mousePos[1] + 60), size = 20)
                if smrtbrd.get_rect(topleft= (WIDTH/6 * 2.5 - 70, HEIGHT / 2 - 130)).collidepoint(mousePos):
                    inf = pg.Surface((350,300), pg.SRCALPHA)
                    inf.fill('black')
                    inf.set_alpha(200)
                    screen.blit(inf, mousePos)
                    renderonscr(screen, "SmartBoard", (mousePos[0] + 75, mousePos[1] + 30))
                    pg.draw.aaline(screen, 'white', (mousePos[0] + 5, mousePos[1] + 45), (mousePos[0] + 295, mousePos[1] + 45))
                    renderonscr(screen, "In 2024, many classrooms use smart\nboards instead of chalkboards.\nSmart boards are like giant touch\nscreens. Teachers can write on\nthem using special pens or their\nhands. They can also show videos,\npictures, and even connect to\nthe internet.\nStudents can interact with\nthe board too, making learning\nmore fun and engaging.",  (mousePos[0] + 179, mousePos[1] + 60), size = 20)
                if proj.get_rect(topleft= (WIDTH/6 * 4 - 50, HEIGHT / 2 - 150)).collidepoint(mousePos):
                    inf = pg.Surface((350,200), pg.SRCALPHA)
                    inf.fill('black')
                    inf.set_alpha(200)
                    screen.blit(inf, mousePos)
                    renderonscr(screen, "Projector", (mousePos[0] + 75, mousePos[1] + 30))
                    pg.draw.aaline(screen, 'white', (mousePos[0] + 5, mousePos[1] + 45), (mousePos[0] + 295, mousePos[1] + 45))
                    renderonscr(screen, "Modern projectors can\n display clear, bright images\n and videos, often in high\n definition.",  (mousePos[0] + 179, mousePos[1] + 60), size = 20)
                pg.draw.rect(screen, 'red', back)
                renderonscr(screen, "BACK", back.center, outline_color='black')
                renderonscr(screen, "2024", outline_color="black", pos=(WIDTH - 90, 30))
                if event.type == pg.MOUSEBUTTONDOWN:
                    if back.collidepoint(event.pos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 0 
            case 3:
                pg.display.set_caption("Classrooms through the ages | C_3_2054")
                back = pg.Rect(0,0, 70, 70)
                back.topleft = (0,0)
                bg = pg.image.load("images\\2054class.jpg")
                screen.blit(bg, (0,0))
                img_scale = 4
                vr = pg.transform.scale(pg.image.load("images\\i_bquest.png"), (84.6 * img_scale, 29.5 * img_scale))
                screen.blit(vr, (WIDTH/6 - 110, HEIGHT / 2))
                ai = pg.transform.scale(pg.image.load("images\\i_ai.png"), (52.4 * img_scale, 43.2 * img_scale))
                screen.blit(ai, (WIDTH / 6 * 2.5 - 70 , HEIGHT / 2 - 130))
                bot =  pg.transform.scale(pg.image.load("images\\i_bot.png"), (54.6 * img_scale, 45.7 * img_scale))
                screen.blit(bot, (WIDTH / 6 * 4 - 50, HEIGHT / 2 - 150))
                mousePos = pg.mouse.get_pos()
                if vr.get_rect(topleft= (WIDTH/6 - 110, HEIGHT / 2)).collidepoint(mousePos):
                    inf = pg.Surface((350,150),pg.SRCALPHA)
                    inf.fill('black')
                    inf.set_alpha(200)
                    screen.blit(inf, mousePos)
                    renderonscr(screen, "VR headset", (mousePos[0] + 75, mousePos[1] + 30))
                    pg.draw.aaline(screen, 'white', (mousePos[0] + 5, mousePos[1] + 45), (mousePos[0] + 295, mousePos[1] + 45))
                    renderonscr(screen, "In the future, VR headsets\nwill enable students and teachers alike\nto interact and learn like never before!",  (mousePos[0] + 179, mousePos[1] + 60), size = 20)
                if ai.get_rect(topleft= (WIDTH/6 * 2.5 - 70, HEIGHT / 2 - 130)).collidepoint(mousePos):
                    inf = pg.Surface((350,200), pg.SRCALPHA)
                    inf.fill('black')
                    inf.set_alpha(200)
                    screen.blit(inf, mousePos)
                    renderonscr(screen, "AI", (mousePos[0] + 75, mousePos[1] + 30))
                    pg.draw.aaline(screen, 'white', (mousePos[0] + 5, mousePos[1] + 45), (mousePos[0] + 295, mousePos[1] + 45))
                    renderonscr(screen, "Artificial intelligence will become\n even more intelligent and widely\nused in schools. On top of\nhelping with homework, AI will \neven be able to tutor!",  (mousePos[0] + 179, mousePos[1] + 60), size = 20)
                if bot.get_rect(topleft= (WIDTH/6 * 4 - 50, HEIGHT / 2 - 150)).collidepoint(mousePos):
                    inf = pg.Surface((350,140), pg.SRCALPHA)
                    inf.fill('black')
                    inf.set_alpha(200)
                    screen.blit(inf, mousePos)
                    renderonscr(screen, "Robot", (mousePos[0] + 75, mousePos[1] + 30))
                    pg.draw.aaline(screen, 'white', (mousePos[0] + 5, mousePos[1] + 45), (mousePos[0] + 295, mousePos[1] + 45))
                    renderonscr(screen, "Robots will be prominentely\nused in schools. They can\nperform actions, like handing out\ntest papers, or even act as substitute teachers!",  (mousePos[0] + 179, mousePos[1] + 60), size = 20)
                pg.draw.rect(screen, 'red', back)
                renderonscr(screen, "BACK", back.center, outline_color='black')
                renderonscr(screen, "2054", outline_color="black", pos=(WIDTH - 90, 30))
                if event.type == pg.MOUSEBUTTONDOWN:
                    if back.collidepoint(event.pos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 0 
            case 4:
                pg.display.set_caption("Classrooms through the ages | C_4_SG")
                back = pg.Rect(0,0, 70, 70)
                back.topleft = (0,0)
                screen.fill('lightcyan')
                next = pg.Rect(0,0,70,70)
                next.bottomright = (WIDTH, HEIGHT)
                for y in  range(50, 700, 50):
                    match y:
                        case 50:
                            renderonscr(screen, 'MATH AND GEOMETRY FORMULAS', (center[0],y), 60, outline_color='black', color='lightgray')
                        case 100:
                            renderonscr(screen, 'Area of circle: A=πr^2', (center[0], y), color='black')
                        case 150:
                            renderonscr(screen, 'Area of triangle: A=(B x H) / 2', (center[0], y), color='black')
                        case 200:
                            renderonscr(screen, 'Volume of sphere: A=4πr^2', (center[0], y), color='black')
                        case 250:
                            renderonscr(screen, 'Pythagorean theorem: a^2 = b^2 + c^2', (center[0], y), color='black')
                            pg.draw.aaline(screen, 'black', (0, y +  25), (WIDTH, y + 25))
                        case 300:
                            renderonscr(screen, 'HISTORY FACTS', (center[0],y), 60, outline_color='black', color='lightgray')
                        case 350:
                            renderonscr(screen, 'Great Pyramid of Giza: Built 4,500 years ago in Egypt',(center[0], y), color='black' )
                        case 400:
                            renderonscr(screen, 'First Airplane: Wright brothers flew first plane in 1903.',(center[0], y), color='black' )
                        case 450:
                             renderonscr(screen, 'American Revolution: Colonies fought for independence in 1775.',(center[0], y), color='black' )
                pg.draw.rect(screen, 'red', back)
                renderonscr(screen, "BACK", back.center, outline_color='black')
                pg.draw.rect(screen, 'darkblue', next)
                renderonscr(screen, 'NEXT', next.center, outline_color='black')
                mousePos = pg.mouse.get_pos()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if back.collidepoint(mousePos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 0
                    if next.collidepoint(mousePos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 5
            case 5:
                pg.display.set_caption("Classrooms through the ages | C_5_SG")
                back = pg.Rect(0,0, 70, 70)
                back.topleft = (0,0)
                screen.fill('lightcyan')
                next = pg.Rect(0,0,70,70)
                next.bottomleft = (0, HEIGHT)
                for y in  range(50, 700, 50):
                    match y:
                        case 50:
                            renderonscr(screen, 'GEOGRAPHY FACTS', (center[0],y), 60, outline_color='black', color='lightgray')
                        case 100:
                            renderonscr(screen, 'Amazon Rainforest: Largest rainforest, home to diverse species.', (center[0], y), color='black')
                        case 150:
                            renderonscr(screen, "Great Barrier Reef: World's largest coral reef system.", (center[0], y), color='black')
                        case 200:
                            renderonscr(screen, 'Mount Everest: Tallest mountain, 29,032 feet high.', (center[0], y), color='black')
                        case 250:
                            renderonscr(screen, "Sahara Desert: World's largest hot desert, in Africa.", (center[0], y), color='black')
                            pg.draw.aaline(screen, 'black', (0, y +  25), (WIDTH, y + 25))
                        case 300:
                            renderonscr(screen, 'SCIENCE INFO', (center[0],y), 60, outline_color='black', color='lightgray')
                        case 350:
                            renderonscr(screen, 'Water Boils: 212°F (100°C) at sea level.',(center[0], y), color='black' )
                        case 400:
                            renderonscr(screen, 'DNA: Blueprint of life, carries genetic information.',(center[0], y), color='black' )
                        case 450:
                             renderonscr(screen, "Gravity: Force pulling objects toward Earth's center.",(center[0], y), color='black' )
                pg.draw.rect(screen, 'red', back)
                renderonscr(screen, "BACK", back.center, outline_color='black')
                pg.draw.rect(screen, 'darkblue', next)
                renderonscr(screen, 'LAST', next.center, outline_color='black')
                mousePos = pg.mouse.get_pos()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if back.collidepoint(mousePos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 0
                    if next.collidepoint(mousePos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 4
            case 6:
                pg.display.set_caption("Classrooms through the ages | C_6_HELP")
                back = pg.Rect(0,0, 70, 70)
                back.topleft = (0,0)
                screen.fill('turquoise')
                pg.draw.rect(screen, 'red', back)
                renderonscr(screen, "1. Select year for the classroom you'd like to see\n2. Click the button in the main menu for that year\n3. Hover over the objects in classroom to read about them", center, 50, color='black')
                renderonscr(screen, "BACK", back.center, outline_color='black')
                renderonscr(screen, 'HELP', (center[0],50), 60, outline_color='black', color='lightgray')
                pg.draw.aaline(screen, 'black', (0, 75), (WIDTH, 75))
                mousePos = pg.mouse.get_pos()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if back.collidepoint(mousePos):
                        pg.mixer_music.load("click.mp3")
                        pg.mixer_music.play()
                        c = 0
            case _:
                screen.fill('black')   
        renderonscr(screen, "Ver. 2.0", (70, HEIGHT - 20), 25, color='darkgray')
        pg.display.flip()
        clock.tick(60)