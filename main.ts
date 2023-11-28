controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    Blast = sprites.createProjectileFromSprite(img`
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
        `, Shooter, 100, 0)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    info.changeLifeBy(-1)
    sprites.destroy(otherSprite2, effects.fire, 500)
    scene.cameraShake(4, 500)
})
info.onScore(10000, function () {
    game.gameOver(true)
})
info.onLifeZero(function () {
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(sprite)
    sprites.destroy(otherSprite)
    info.changeScoreBy(100)
})
let Bad_Dude: Sprite = null
let Blast: Sprite = null
let Shooter: Sprite = null
effects.starField.startScreenEffect()
Shooter = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(Shooter, 100, 100)
Shooter.setStayInScreen(false)
info.setLife(3)
game.onUpdateInterval(2000, function () {
    Bad_Dude = sprites.create(img`
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
        `, SpriteKind.Enemy)
    Bad_Dude.x = scene.screenWidth()
    Bad_Dude.vx = -20
    Bad_Dude.y = randint(10, scene.screenHeight() - 10)
})
