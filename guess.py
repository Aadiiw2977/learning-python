secret = 7

print("🎮 Guess The Number Game")
guess = int(input("Enter a number (1-10): "))

if guess == secret:
    print("🎉 Correct! You Win!")
else:
    print("❌ Wrong! The correct number was", secret)
