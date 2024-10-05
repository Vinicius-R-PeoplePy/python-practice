document.addEventListener('DOMContentLoaded', function() {
    const currentQuestionIndexInput = document.getElementById('current-question-index');
    let currentQuestionIndex = parseInt(currentQuestionIndexInput.value, 10) || 0;
    let questions = [];
    let correctAnswers = 0;
    let incorrectAnswers = 0;

    async function loadQuestion(questionIndex) {
        try {
            const response = await fetch(`/api/intermediary/questions/${questionIndex + 1}`);
            if (!response.ok) throw new Error('Question not found');
            const question = await response.json();
            questions = [question];
            clearHighlighting();
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
            answerSelect.style.backgroundColor = 'lightgreen';
            correctAnswers++;
        } else {
            alert("Error, wrong answer!");
            answerSelect.style.backgroundColor = 'red';
            incorrectAnswers++;
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
        answerSelect.style.backgroundColor = '';
    }

    document.getElementById("next-button").addEventListener("click", function() {
        if (this.classList.contains("disabled")) {
            alert("You can't advance! Please, give an aswer!");
        } else {
            currentQuestionIndex++;
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

    loadQuestion(currentQuestionIndex);
});

document.addEventListener('DOMContentLoaded', function() {
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

/* 
const background = document.querySelector('.background');
for (let i = 0; i < 10; i++) { // Create 10 question marks
    const questionMark = document.createElement('div');
    questionMark.className = 'question-mark';
    questionMark.textContent = '?';
    questionMark.style.top = `${Math.random() * 100}%`;
    questionMark.style.left = `${Math.random() * 100}%`;
    background.appendChild(questionMark);
}


*/