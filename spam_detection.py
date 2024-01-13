# spam_detection.py

def is_spam(feedback_responses, response_time):
    # Check if 90% of feedback answers are the same
    unique_responses = set(feedback_responses)
    if len(unique_responses) == 1 and len(feedback_responses) > 1:
        return True

    # Check if response time is less than a second
    if response_time < 1.0:
        return True

    return False

# Example usage:
if __name__ == "__main__":
    feedback_responses = ["Excellent", "Excellent", "Excellent", "Good", "Excellent"]
    response_time = 0.8

    if is_spam(feedback_responses, response_time):
        print("This feedback is marked as spam.")
    else:
        print("This feedback is not spam.")
