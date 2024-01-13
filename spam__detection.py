const survey = new Survey.Model(json);

survey.onComplete.add((sender, options) => {
    const feedbackResponses = [];

    // Extract feedback responses from the survey data
    survey.pages.forEach(page => {
        page.questions.forEach(question => {
            feedbackResponses.push(question.value);
        });
    });

    const responseTime = (options.endTime - options.startTime) / 1000; // Convert to seconds

    // Spam detection logic
    if (isSpam(feedbackResponses, responseTime)) {
        console.log("This feedback is marked as spam.");
    } else {
        console.log("This feedback is not spam.");
    }
});

$("#surveyElement").Survey({ model: survey });

// Spam detection function
function isSpam(feedbackResponses, responseTime) {
    // Check if 90% of feedback answers are the same
    const uniqueResponses = new Set(feedbackResponses);
    if (uniqueResponses.size === 1 && feedbackResponses.length > 1) {
        return true;
    }

    // Check if response time is less than a second
    if (responseTime < 1.0) {
        return true;
    }

    return false;
}
