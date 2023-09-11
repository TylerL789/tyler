scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleBlueCrystal, function (sprite2, location2) {
    info.changeScoreBy(1)
    tiles.setTileAt(location2, sprites.dungeon.collectibleBlueCrystal)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleRedCrystal, function (sprite4, location4) {
    info.changeScoreBy(1)
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.field0, function (sprite, location) {
    info.changeScoreBy(1)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.buttonTeal, function (sprite7, location7) {
    info.changeScoreBy(1)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestOpen, function (sprite5, location5) {
    game.over(true)
})
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.field1, function (sprite3, location3) {
    info.changeScoreBy(1)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleInsignia, function (sprite6, location6) {
    info.changeScoreBy(1)
})
tiles.setTilemap(tilemap`level1`)
let mySprite = sprites.create(img`
    b b b b . . . . . . . . b b b b 
    c 9 9 b b . . . . . . b b 9 9 b 
    c 9 9 9 b b . . . . b b 9 9 9 c 
    c 9 b 9 9 b c c c c b 9 9 b 9 c 
    c 9 b b 9 9 b c c b 9 9 b b 9 c 
    c 9 3 b 9 9 9 9 9 9 9 9 b 3 9 c 
    c 9 3 3 9 9 9 9 9 9 9 9 3 3 9 c 
    c 9 9 3 9 9 9 9 9 9 9 9 3 9 9 c 
    c 9 9 9 9 9 9 9 1 1 9 9 9 9 9 c 
    c 9 9 9 f f 9 1 1 1 9 f f 9 9 c 
    c 9 9 9 f f 9 1 1 1 1 f f 9 9 c 
    c 9 9 9 9 1 1 1 1 1 1 1 9 9 9 c 
    c 9 9 9 1 1 1 1 f f f 1 1 9 9 c 
    c 9 9 9 c 1 1 f f f 1 1 9 9 b c 
    c 9 9 9 c c 1 1 1 1 1 1 c 9 b c 
    c 9 9 9 9 9 b b 3 3 c c 9 9 b c 
    `, SpriteKind.Player)
tiles.placeOnRandomTile(mySprite, sprites.dungeon.chestClosed)
scene.cameraFollowSprite(mySprite)
controller.moveSprite(mySprite)
info.startCountdown(50)
