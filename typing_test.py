import time
import random

# Sentences to type
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a versatile and powerful programming language.",
    "Typing speed depends on accuracy and practice.",
    "Automation saves time and increases productivity.",
    "Practice makes perfect in coding and typing."
]

print("💻 Typing Speed Test")
print("----------------------")
input("⏳ Press Enter when you're ready to start...")

# Choose a random sentence
sentence = random.choice(sentences)
print("\n📝 Type this:\n")
print(sentence)
print("\n⏱️ Timer starts when you begin typing...")

# Start timing
start_time = time.time()
typed_input = input("\n🔡 Your input: ")
end_time = time.time()

# Calculate results
time_taken = round(end_time - start_time, 2)
word_count = len(sentence.split())
accuracy = sum(1 for a, b in zip(typed_input, sentence) if a == b) / len(sentence) * 100
wpm = round((len(typed_input.split()) / time_taken) * 60, 2)

# Show results
print("\n✅ Results:")
print(f"Time Taken: {time_taken} seconds")
print(f"Words Per Minute (WPM): {wpm}")
print(f"Accuracy: {accuracy:.2f}%")
