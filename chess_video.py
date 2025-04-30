import pygame
import random
import chess
import imageio
import os
from chess_ai import ChessAI

# Constants for board dimensions
WIDTH, HEIGHT = 480, 480
SQUARE_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARK = (100, 100, 100)

# Load piece images
PIECE_IMAGES = {}

def load_piece_images():
    pieces = ['r', 'n', 'b', 'q', 'k', 'p']
    colors = ['w', 'b']
    for color in colors:
        for piece in pieces:
            name = color + piece
            image = pygame.image.load(f"assets/{name}.png")  # Load images from assets folder
            PIECE_IMAGES[name] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))

def draw_board(screen, board):
    colors = [WHITE, GRAY]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            row = 7 - chess.square_rank(square)
            col = chess.square_file(square)
            color = 'w' if piece.color == chess.WHITE else 'b'
            name = color + piece.symbol().lower()
            screen.blit(PIECE_IMAGES[name], (col*SQUARE_SIZE, row*SQUARE_SIZE))

def record_frame(screen, frames):
    image_data = pygame.surfarray.array3d(screen)
    image_data = image_data.swapaxes(0, 1)  # Convert to (height, width, 3)
    frames.append(image_data)

def main(use_alpha_beta=True, output_filename="chess_game.mp4"):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess AI")
    load_piece_images()

    board = chess.Board()
    ai = ChessAI(depth=2)
    frames = []
    clock = pygame.time.Clock()

    draw_board(screen, board)
    pygame.display.flip()
    record_frame(screen, frames)
    running = True
    move_count = 0

    while running and not board.is_game_over() and move_count < 60:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.time.wait(10)

        if board.turn == chess.WHITE:
            move = ai.find_best_move(board, use_alpha_beta=use_alpha_beta)
        else:
            move = random.choice(list(board.legal_moves))

        board.push(move)
        move_count += 1

        draw_board(screen, board)
        pygame.display.flip()
        record_frame(screen, frames)
        clock.tick(30)

    pygame.quit()

    # Save video
    imageio.mimsave(output_filename, frames, fps=1)
    print(f"\nVideo saved as: {output_filename}")
    print(f" Game Over. Result: {board.result()}")

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    print("you need to have chess piece images in the 'assets/' folder.")
    print("started running the game...")
    main(use_alpha_beta=True, output_filename="alphabeta.gif")
    main(use_alpha_beta=False, output_filename="minimax.gif")

