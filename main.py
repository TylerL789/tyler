def on_overlap_tile(sprite, location):
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player, sprites.builtin.field0, on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    info.change_score_by(1)
    tiles.set_tile_at(location2, sprites.dungeon.collectible_blue_crystal)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_blue_crystal,
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player, sprites.builtin.field1, on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_red_crystal,
    on_overlap_tile4)

def on_overlap_tile5(sprite5, location5):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_open,
    on_overlap_tile5)

def on_overlap_tile6(sprite6, location6):
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile6)

def on_overlap_tile7(sprite7, location7):
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.button_teal,
    on_overlap_tile7)

tiles.set_tilemap(tilemap("""
    level1
"""))
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
tiles.place_on_random_tile(mySprite, sprites.dungeon.chest_closed)
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite)
info.start_countdown(50)