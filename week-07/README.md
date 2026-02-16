# Hurdles Loop Challenge 🏁

## 📌 Project Description
This project was completed using Reeborg's World.
The goal was to make the robot jump over multiple hurdles and reach the flag.

##  What I Learned
- How to use functions
- How to create custom functions (turn_right, jump)
- How to use while loops
- How to use if/else conditions
- How to check front_is_clear()
- How to think logically about movement and obstacles

##  My Solution Code

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
📷 Screenshots

(Add screenshots of your robot jumping and the green success message here)

🎯 Final Result

The robot successfully jumps all hurdles and reaches the goal.