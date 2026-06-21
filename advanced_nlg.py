
import random

# Templates for different categories
templates = {
    "weather": [
        "Today the weather is {condition} with a temperature of {temp}°C.",
        "The forecast predicts {condition} skies and {temp}°C temperature.",
        "Current weather conditions are {condition} with {temp}°C."
    ],

    "sports": [
        "{team} won the match by {score} runs.",
        "An exciting game ended with {team} scoring {score}.",
        "{team} delivered a great performance with a score of {score}."
    ],

    "news": [
        "Breaking News: {event} has attracted attention across the country.",
        "Latest Update: {event} is trending today.",
        "Top Story: {event} has become a major topic of discussion."
    ]
}


def generate_text(category):
    if category == "weather":
        data = {
            "condition": random.choice(["sunny", "cloudy", "rainy", "stormy"]),
            "temp": random.randint(20, 40)
        }

    elif category == "sports":
        data = {
            "team": random.choice(["India", "Australia", "England", "South Africa"]),
            "score": random.randint(100, 350)
        }

    elif category == "news":
        data = {
            "event": random.choice([
                "a new technology launch",
                "an international summit",
                "a scientific discovery",
                "a major sports event"
            ])
        }

    else:
        return "Invalid category selected."

    template = random.choice(templates[category])
    return template.format(**data)


def save_output(text):
    with open("generated_text.txt", "a") as file:
        file.write(text + "\n")


print("===== Natural Language Generator =====")
print("Available Categories:")
print("1. weather")
print("2. sports")
print("3. news")

category = input("\nEnter category: ").lower()

result = generate_text(category)

print("\nGenerated Text:")
print(result)

save_choice = input("\nDo you want to save the output? (yes/no): ").lower()

if save_choice == "yes":
    save_output(result)
    print("Output saved successfully in generated_text.txt")

print("\nThank you for using the Natural Language Generator!")