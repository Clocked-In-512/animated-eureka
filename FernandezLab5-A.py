
##Robert Fernandez
##Complete
##This program will calculate the average score to determine the star rating for each Restuarant.

def determine_stars(avg_score):
    """Calculate the star rating based on the average score."""
    if avg_score > 9:
        return '*****'
    elif avg_score >= 8.0:
        return '****'
    elif avg_score >= 7.0:
        return '***'
    elif avg_score >= 6.0:
        return '**'
    elif avg_score >= 5.0:
        return '*'
    else:
        return 'No stars'

def main():
    "Collects ratings from the user and calculates the average score. Displays the average score and the star rating."
    scores = []
    for _ in range(5):
        while True:
            try:
                score = float(input("Enter critic's score between 0 and 10: "))
                if 0 <= score <= 10:
                    scores.append(score)
                    break
                else:
                    print("Error: Please enter a number between 0 and 10.")
            except ValueError:
                print("Error: Please enter a valid number.")
    avg_score = sum(scores) / len(scores)
    avg_score_rounded = round(avg_score, 2)
    stars = determine_stars(avg_score_rounded)
    print(f"Your score of {avg_score_rounded} gives you {stars}")

if __name__ == "__main__":
    main()
