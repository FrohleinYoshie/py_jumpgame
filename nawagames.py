import pygame
import sys
import random

# 初期化
pygame.init()

# 画面サイズ
screen_width = 400
screen_height = 400

# 色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 縄の設定
rope_speed = 2
rope_width = 10
rope_length = 10  # 新しい縄の長さ
rope_color = black

# プレイヤーの設定
player_width = 20
player_height = 40
player_color = red
player_jump = -10
player_gravity = 0.5  # 重力

# 初期位置
player_x = screen_width // 4
player_y = screen_height - player_height

# ゲームスピード
game_speed = 60  # ゲームスピードを調整

# 画面作成
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jump the Rope")

# フォント
font = pygame.font.Font(None, 36)

# ジャンプ状態
is_jumping = False

# ジャンプ高さ
jump_height = 0
jump_speed = 10  # ジャンプ速度

# 縄の位置
rope_x = screen_width - rope_width
# 祐逸の追加: ランダムな高さの縄
rope_height = random.randint(10, 90)

# ジャンプ関数
def jump():
    global is_jumping, jump_height
    if not is_jumping:
        is_jumping = True
        jump_height = player_jump

# ゲームオーバー画面
def game_over(score):
    screen.fill(white)
    text = font.render(f"Game Over - Score: {score}", True, black)  # 祐逸の追加: スコア表示
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# 祐逸の追加: スコア変数
score = 0

# メインループ
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

    # ジャンプ処理
    if is_jumping:
        player_y += jump_height
        jump_height += player_gravity  # 重力を適用
        if player_y >= screen_height - player_height:
            player_y = screen_height - player_height
            is_jumping = False
            jump_height = 0  # 地面に着地したらジャンプ高さをリセット

    # 縄の移動
    rope_x -= rope_speed

    # 縄が画面外に出たら新しい縄を設定
    if rope_x < 0:
        rope_x = screen_width
        rope_speed += 0.2  # 縄の速度を少しずつ増加
        # 祐逸の追加: ランダムな高さの縄
        rope_height = random.randint(10, 90)

        # 祐逸の追加: スコア増加
        score += 1

    # 衝突判定
    if player_x + player_width > rope_x and player_x < rope_x + rope_width:
        if player_y + player_height > screen_height - rope_height:  # 祐逸の変更: ランダムな高さを考慮
            game_over(score)  # 祐逸の変更: ゲームオーバー時にスコア表示

    # 画面描画
    screen.fill(white)
    pygame.draw.rect(screen, rope_color, (rope_x, screen_height - rope_height, rope_width, rope_height))  # 祐逸の変更: ランダムな高さを考慮
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    
    # 祐逸の追加: スコア表示
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

    clock.tick(game_speed)