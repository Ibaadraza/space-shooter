def on_a_pressed():
    global Blast
    Blast = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 4 e a . . . . . . . . . 
                    . . . . 5 . a a a . . . . . . . 
                    . . . . 4 e a a a a a a a . . . 
                    . . . . 5 . b 4 b b 4 b a a . . 
                    . . . . 4 e 4 5 4 4 5 4 a 2 a e 
                    . . . . 5 . b 4 b b 4 b a a . . 
                    . . . . 4 e a a a a a a a . . . 
                    . . . . 5 . a a a . . . . . . . 
                    . . . . 4 e a . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Shooter,
        100,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_score():
    game.game_over(True)
info.on_score(10000, on_on_score)

def on_life_zero():
    game.game_over(False)
info.on_life_zero(on_life_zero)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite)
    sprites.destroy(otherSprite)
    info.change_score_by(100)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    sprites.destroy(otherSprite2, effects.fire, 500)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

Bad_Dude: Sprite = None
Blast: Sprite = None
Shooter: Sprite = None
effects.star_field.start_screen_effect()
Shooter = sprites.create(img("""
        . . . . . . . . . 7 9 7 . . . . 
            . . . . . . . . 9 9 9 . . . . . 
            . . . . 9 9 9 9 9 9 . . . . . . 
            . . . 9 9 9 9 9 9 . . . . . . . 
            . . 9 9 . . . . . . . . . . . . 
            . 9 9 . . . . . 8 8 . . . . . . 
            9 8 8 8 8 8 8 8 8 8 6 . . . . . 
            9 7 7 7 7 7 7 7 7 7 6 . . . . . 
            . 9 9 . . . . . 7 7 . . . . . . 
            . . 9 9 . . . . . . . . . . . . 
            . . . 9 9 9 9 9 9 . . . . . . . 
            . . . . 9 9 9 9 9 9 . . . . . . 
            . . . . . . . . 9 9 9 . . . . . 
            . . . . . . . . . 7 9 7 . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(Shooter, 100, 100)
Shooter.set_stay_in_screen(True)
info.set_life(3)

def on_update_interval():
    global Bad_Dude
    Bad_Dude = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . a a a a a a a a a a . . . 
                    . . a a 3 3 3 3 3 3 3 3 a a . . 
                    . . a 3 3 3 3 3 3 3 3 3 3 a . . 
                    . . a a c c c c c c c c a a . . 
                    . . . a c c 1 c c 1 c c a . . . 
                    . . . . a d d d d d d a . . . . 
                    . . . a a b b d d b b a a . . . 
                    . . a a b b c 5 5 c b b a a . . 
                    . a a b b c c 5 5 c c b b a a . 
                    . a b b c c 5 5 5 5 c c b b a . 
                    a b d c c 5 5 c c 5 5 c c d b a 
                    a b c c 5 5 3 3 3 3 5 5 c c b a 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    Bad_Dude.x = scene.screen_width()
    Bad_Dude.vx = -20
    Bad_Dude.y = randint(10, scene.screen_height() - 10)
game.on_update_interval(2000, on_update_interval)
