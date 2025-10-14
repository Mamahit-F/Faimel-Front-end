import turtle
import time

# Setup window
window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor("light pink")
window.title("Surat Cinta untuk Pacar")

# Set turtle
pen = turtle.Turtle()
pen.speed(3)
pen.width(3)

# Function to draw a heart
def draw_heart():
    pen.color("red")
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Function to draw a flower
def draw_flower():
    pen.color("purple")
    pen.begin_fill()
    for _ in range(36):
        pen.forward(100)
        pen.left(170)
    pen.end_fill()

# Function to display love message
def love_message():
    pen.penup()
    pen.goto(-200, 200)
    pen.color("black")
    pen.write("Hai Cintaku!", font=("Arial", 24, "bold"))
    
    pen.goto(-300, 150)
    pen.write("Aku cuma mau bilang kalau kamu adalah orang yang\npaling berharga dalam hidupku.", font=("Arial", 16, "normal"))
    
    pen.goto(-250, 100)
    pen.write("Setiap saat bersamamu begitu indah dan menyenangkan.", font=("Arial", 16, "normal"))
    
    pen.goto(-300, 50)
    pen.write("Terima kasih sudah ada di sampingku. Aku sayang kamu!", font=("Arial", 16, "normal"))
    
    pen.goto(-100, -200)
    pen.color("red")
    pen.write("❤️ Selamanya ❤️", font=("Arial", 20, "bold"))

# Draw the animated elements
def main():
    # Draw heart
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    draw_heart()
    
    # Pause for effect
    time.sleep(1)
    pen.clear()
    
    # Draw flower
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    draw_flower()
    
    # Pause for effect
    time.sleep(1)
    pen.clear()
    
    # Display the love message
    love_message()

# Run the main function
main()

# Hide pen and close window on click
pen.hideturtle()
window.exitonclick()
