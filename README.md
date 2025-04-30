This project implements a chess game using AI-based game-playing algorithms. The game allows two players (AI vs AI  to play chess with evaluation functions and a minimax algorithm to decide moves. The game uses the popular Python library pygame for rendering the board and handling the user interface, and implements basic AI using a search tree to evaluate the best possible moves.

Performance Optimization and Evaluation Considerations
To optimize the performance and ensure smooth gameplay, several settings have been tweaked for balancing between speed and depth of AI evaluation.

1. Reduced Frame Delay (pygame.time.wait(10))
In order to avoid overwhelming the system with excessive processing and to allow for smoother gameplay, the time delay between frames during AI evaluation has been reduced. Specifically, the pygame.time.wait(10) function has been used to insert a 10-millisecond delay after each frame. This ensures that:

Smooth rendering: The game doesn't render frames too quickly, giving the player or the viewer a smooth visual experience.

Performance balance: The system is not overloaded by rapid rendering, especially during AI decision-making, which can require multiple evaluations.

While this delay is set to 10 milliseconds in the current setup, it can be adjusted depending on the system's performance capabilities. A lower value can make the game more responsive, while a higher value might be used to reduce the CPU load.


# pygame.time.wait(10)

2. AI Search Depth (depth = 2)
To control the strength and speed of the AI, the depth of the search tree used in the Minimax algorithm has been limited to depth 2. The search depth defines how many moves ahead the AI will consider when evaluating the best move. Here’s the trade-off:

Smaller depth (e.g., 2): The AI will calculate fewer possible moves, leading to faster decision-making but less strategic gameplay. This setting is useful for faster AI responses and for games where responsiveness is prioritized over deep strategic play.

Larger depth (e.g., 4 or 5): The AI will look ahead more moves and make more strategic decisions, but it will take longer to decide its next move. This would make the game feel more challenging but could slow down the gameplay.

In this implementation, a depth of 2 is used for the following reasons:

Efficiency: It provides a balance between AI decision-making time and gameplay speed.

Playability: This depth level allows for a more engaging experience without overwhelming the player with long wait times.

To modify the depth of AI's decision-making, the depth variable can be adjusted in the code:

# ChessAI(depth=2)

3. Customizing Performance
Both the frame delay (pygame.time.wait()) and AI depth (depth) can be customized based on your preference or system performance. Here’s how you can modify them:

To make the game faster, reduce the delay time or increase the depth.

To make the AI stronger and more strategic, increase the search depth.

However, keep in mind that increasing the depth might lead to slower AI decisions, especially as the AI evaluates more complex board positions.

 