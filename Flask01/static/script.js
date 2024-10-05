document.addEventListener('DOMContentLoaded', function() {
    const currentQuestionIndexInput = document.getElementById('current-question-index');
    let currentQuestionIndex = parseInt(currentQuestionIndexInput.value, 10);
    let questions = [];
    let correctAnswers = 0;
    let incorrectAnswers = 0;
    const totalQuestions = 31;

    async function loadQuestion(questionIndex) {
        if (questionIndex >= totalQuestions) {
            // quiz ended, hide question and show message
            document.getElementById("question-container").style.display = 'none';
            document.getElementById("quiz-ended").style.display = 'block';
            document.getElementById("prev-button").classList.add("disabled");
            return;
        }
        try {
            const response = await fetch(`/api/questions/${questionIndex + 1}`);
            if (!response.ok) throw new Error('Question not found');
            const question = await response.json();
            questions = [question];
            clearHighlighting();  // Clear highlighting before loading a new question
            displayQuestion();
        } catch (error) {
            console.error('Error fetching question:', error);
        }
    }

    function displayQuestion() {
        if (questions.length === 0) return;

        const currentQuestion = questions[0];
        document.getElementById("question-text").textContent = currentQuestion.question;
        const answerSelect = document.getElementById("answer-select");
        answerSelect.innerHTML = '<option value="">Select your answer</option>';
        currentQuestion.choices.forEach(choice => {
            const option = document.createElement("option");
            option.value = choice;
            option.textContent = choice;
            answerSelect.appendChild(option);
        });

        updateTrackingInfo();

        // Disable Next button initially
        document.getElementById("next-button").classList.add("disabled");
    }

    function checkAnswer() {
        const answerSelect = document.getElementById("answer-select");
        const selectedAnswer = answerSelect.value;

        if (selectedAnswer === "") {
            alert("You can't advance! Please, give an answer!");
            return;
        }

        const correctAnswer = questions[0].correct;
        if (selectedAnswer === correctAnswer) {
            alert("Good job, you can continue!");
            document.getElementById("next-button").classList.remove("disabled");
            answerSelect.style.backgroundColor = 'lightgreen';  // Highlight correct answer
            correctAnswers++;
            console.log("correct answers:", correctAnswers)
        } else {
            alert("Error, wrong answer!");
            answerSelect.style.backgroundColor = 'red';  // Highlight incorrect answer
            incorrectAnswers++;
            console.log("correct answers:", incorrectAnswers)
        }

        updateTrackingInfo();
    }

    function updateTrackingInfo() {
        document.getElementById('current-question-number').textContent = currentQuestionIndex + 1;
        document.getElementById('correct-answers').textContent = correctAnswers;
        document.getElementById('incorrect-answers').textContent = incorrectAnswers;
    }

    function clearHighlighting() {
        const answerSelect = document.getElementById("answer-select");
        answerSelect.style.backgroundColor = '';  // Reset the background color
    }

    document.getElementById("next-button").addEventListener("click", function() {
        if (this.classList.contains("disabled")) {
            alert("You can't advance! Please, give an answer!");
        } else {
            currentQuestionIndex++;
            if (currentQuestionIndex >= totalQuestions) {
                alert("You have finished the quiz!");
                submitScore(correctAnswers, incorrectAnswers);
                return;
            }
            loadQuestion(currentQuestionIndex);
            currentQuestionIndexInput.value = currentQuestionIndex;
        }
    });

    document.getElementById("prev-button").addEventListener("click", function() {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            loadQuestion(currentQuestionIndex);
            currentQuestionIndexInput.value = currentQuestionIndex;
        }
    });

    document.getElementById("answer-select").addEventListener("change", function() {
        checkAnswer();
    });

    // Load the initial question when the page loads
    loadQuestion(currentQuestionIndex);

    const toggleButton = document.getElementById('toggle-effect');
    const questionMarks = document.querySelectorAll('.question-mark');

    let effectActive = true;

    toggleButton.addEventListener('click', function() {
        effectActive = !effectActive; 
        questionMarks.forEach(mark => {
            mark.style.display = effectActive ? 'block' : 'none';
        });
    });
});

document.getElementById("next-button").addEventListener("click", function() {
    if (this.classList.contains("disabled")) {
        alert("You can't advance! Please, give an answer!");
    } else {
        currentQuestionIndex++;
        if (currentQuestionIndex >= totalQuestions) {
            // This is where you finish the quiz and submit the score
            alert("You have finished the quiz!");
            document.getElementById("submit-button").disabled = false; 
            alert("You have finished the quiz!");
            submitScore(correctAnswers, incorrectAnswers); // Pass the correct counts
            return;
        }
        loadQuestion(currentQuestionIndex);
        currentQuestionIndexInput.value = currentQuestionIndex;
    }
});

function submitScore(correctAnswers, incorrectAnswers) {
    const data = {
        correct_answers: correctAnswers || 0, // Ensure there's a value
        incorrect_answers: incorrectAnswers || 0,
    };
    
    console.log("Submitting score:", data); // Log before fetching

    fetch('/submit_score', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        } else if (!response.ok) {
            throw new Error('Error submitting score');
        }
        return response.json();
    })
    .then(data => {
        alert(data.message);
        window.location.href = "/user_score";
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to submit score. Please try again.');
    });
}




// Make sure to add this event listener for the submit button
document.getElementById("submit-score").addEventListener("click", function() {
    submitScore(correctAnswers, incorrectAnswers);
});