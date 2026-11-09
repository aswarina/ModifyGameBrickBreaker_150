import tkinter as tk
import random

class Ball:
    def __init__(self, canvas, paddle, bricks, color):
        self.canvas = canvas
        self.paddle = paddle
        self.bricks = bricks
        self.color = color
        self.radius = 10
        self.speed_x = 3
        self.speed_y = -3
        self.hit_bottom = False
        
        # Bola putih bersih dengan outline pink soft
        self.id = canvas.create_oval(10, 10, 10 + self.radius * 2, 10 + self.radius * 2, fill=self.color, outline="#FFB6C1", width=2, tags='ball')
        self.canvas.move(self.id, 230, 300)

    def draw(self):
        self.canvas.move(self.id, self.speed_x, self.speed_y)
        pos = self.canvas.coords(self.id)
        
        if pos[0] <= 0 or pos[2] >= 500:
            self.speed_x = -self.speed_x
        if pos[1] <= 0:
            self.speed_y = -self.speed_y
        if pos[3] >= 400:
            self.hit_bottom = True

        # Pantulan dengan Paddle
        paddle_pos = self.canvas.coords(self.paddle.id)
        if len(paddle_pos) > 0:
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                    overlap = pos[3] - paddle_pos[1]
                    self.canvas.move(self.id, 0, -overlap - 2)
                    
                    center_paddle = (paddle_pos[0] + paddle_pos[2]) / 2
                    center_ball = (pos[0] + pos[2]) / 2
                    offset = (center_ball - center_paddle) / (self.paddle.width / 2)
                    self.speed_x = offset * 5
                    self.speed_y = -abs(self.speed_y)

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.width = 90
        self.height = 12
        self.id = canvas.create_rectangle(0, 0, self.width, self.height, fill=color, outline="#FFFFFF", width=2)
        self.canvas.move(self.id, 205, 340)
        self.direction = 0
        
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress-Left>", self.turn_left)
        self.canvas.bind("<KeyPress-Right>", self.turn_right)
        self.canvas.bind("<KeyRelease-Left>", self.stop)
        self.canvas.bind("<KeyRelease-Right>", self.stop)

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[0] + self.direction >= 0 and pos[2] + self.direction <= 500:
            self.canvas.move(self.id, self.direction, 0)

    def turn_left(self, event):
        self.direction = -7

    def turn_right(self, event):
        self.direction = 7

    def stop(self, event):
        self.direction = 0

class Brick:
    def __init__(self, canvas, x, y, color, points, emoji):
        self.canvas = canvas.canvas if hasattr(canvas, 'canvas') else canvas
        self.points = points
        
        cx = x + 32.5
        cy = y + 15
        
        # Titik koordinat kurva polygon bentuk love
        points_coord = [
            cx, cy + 12,                  # Ujung bawah love
            cx - 30, cy - 5,              # Sisi kiri bawah
            cx - 32, cy - 15,             # Lingkaran kiri atas
            cx - 18, cy - 20,
            cx, cy - 8,                   # Lekukan tengah atas
            cx + 18, cy - 20,
            cx + 32, cy - 15,             # Lingkaran kanan atas
            cx + 30, cy - 5               # Sisi kanan bawah
        ]
        
        self.id = self.canvas.create_polygon(points_coord, fill=color, outline="#FFFFFF", width=1.5, smooth=True)
        self.emoji_id = self.canvas.create_text(cx, cy - 3, text=emoji, font=("Arial", 8))

class BrickBreakerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("💖✨ Love Aesthetic Brick Breaker 0150 ✨💖") 
        self.root.configure(bg="#FFF5F7")
        self.root.resizable(False, False)
        
        self.canvas = tk.Canvas(root, width=500, height=400, bg="#FFFCFB", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.root.update()
        
        self.score = 0
        self.lives = 3
        self.running = False
        
        self.score_text = self.canvas.create_text(60, 25, text=f"🍓 Score: {self.score}", fill="#DB7093", font=("Arial", 11, "bold"))
        self.lives_text = self.canvas.create_text(440, 25, text=f"🧸 Lives: {self.lives}", fill="#DB7093", font=("Arial", 11, "bold"))
        
        self.btn_start = tk.Button(root, text="🌷 ✨ START GAME YUK ✨ 🌷", font=("Arial", 11, "bold", "italic"), bg="#FFC0CB", fg="#6D5B71", activebackground="#FFB6C1", relief="raised", bd=3, command=self.start_game)
        self.btn_start.pack(pady=10)

    def setup_level(self):
        self.paddle = Paddle(self.canvas, "#FFC0CB")
        self.bricks = []
        
        colors = ["#FFC0CB", "#FFFACD", "#E6E6FA", "#E0FFFF"] 
        
        row_emojis = [
            ["🍓", "🎀", "🍓", "🎀", "🍓", "🎀"],
            ["🥞", "🍯", "🥞", "🍯", "🥞", "🍯"],
            ["☁️", "💜", "☁️", "💜", "☁️", "💜"],
            ["💧", "🦋", "💧", "🦋", "💧", "🦋"]
        ]
        
        points_map = [40, 30, 20, 10]
        
        for row in range(4):
            for col in range(6):
                x = 25 + col * 75
                y = 60 + row * 30
                brick = Brick(self.canvas, x, y, colors[row], points_map[row], row_emojis[row][col])
                self.bricks.append(brick)
                
        self.ball = Ball(self.canvas, self.paddle, self.bricks, "#FFFFFF")

    def start_game(self):
        if not self.running:
            self.btn_start.pack_forget()
            self.canvas.delete("game_message")
            self.score = 0
            self.lives = 3
            self.canvas.itemconfig(self.score_text, text=f"🍓 Score: {self.score}")
            self.canvas.itemconfig(self.lives_text, text=f"🧸 Lives: {self.lives}")
            
            self.setup_level()
            self.running = True
            self.game_loop()

    def game_loop(self):
        if self.running:
            self.paddle.draw()
            self.ball.draw()
            
            ball_pos = self.canvas.coords(self.ball.id)
            for brick in self.bricks[:]:
                # Menggunakan bbox() agar deteksi sentuhan bola akurat dengan bentuk love
                brick_pos = self.canvas.bbox(brick.id)
                if brick_pos:
                    if ball_pos[2] >= brick_pos[0] and ball_pos[0] <= brick_pos[2]:
                        if ball_pos[3] >= brick_pos[1] and ball_pos[1] <= brick_pos[3]:
                            self.canvas.delete(brick.id)
                            self.canvas.delete(brick.emoji_id)
                            self.bricks.remove(brick)
                            self.score += brick.points
                            self.canvas.itemconfig(self.score_text, text=f"🍓 Score: {self.score}")
                            self.ball.speed_y = -self.ball.speed_y
                            
                            if self.score % 50 == 0:
                                self.ball.speed_x *= 1.1
                                self.ball.speed_y *= 1.1
                            
            if len(self.bricks) == 0:
                self.running = False
                self.canvas.create_text(250, 200, text="🎉✨ YAY! YOU WIN! ✨🎉", fill="#C71585", font=("Arial", 20, "bold"), tags="game_message")
                self.btn_start.config(text="🔄 Main Lagi Yuk 🔄")
                self.btn_start.pack(pady=10)
                return

            if self.ball.hit_bottom:
                self.lives -= 1
                self.canvas.itemconfig(self.lives_text, text=f"🧸 Lives: {self.lives}")
                self.canvas.delete(self.ball.id)
                self.canvas.delete(self.paddle.id)
                
                if self.lives > 0:
                    self.paddle = Paddle(self.canvas, "#FFC0CB")
                    self.ball = Ball(self.canvas, self.paddle, self.bricks, "#FFFFFF")
                else:
                    self.running = False
                    self.canvas.create_text(250, 200, text="🥺 OOPS! GAME OVER 🥺", fill="#C71585", font=("Arial", 20, "bold"), tags="game_message")
                    self.btn_start.config(text="🔄 Coba Lagi Ya 🔄")
                    self.btn_start.pack(pady=10)
                    return

            self.root.after(10, self.game_loop)

if __name__ == "__main__":
    root = tk.Tk()
    game = BrickBreakerGame(root)
    root.mainloop()