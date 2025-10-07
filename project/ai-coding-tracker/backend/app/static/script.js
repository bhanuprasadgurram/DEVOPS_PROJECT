let currentChallenge = null;
let currentSubmissionId = null;

const API_BASE = window.location.origin;

async function loadChallenges() {
    try {
        const response = await fetch(`${API_BASE}/api/problems`);
        const challenges = await response.json();
        displayChallenges(challenges);
    } catch (error) {
        console.error('Error loading challenges:', error);
        document.getElementById('challengesList').innerHTML =
            '<p class="error">Failed to load challenges. Please try again.</p>';
    }
}

function displayChallenges(challenges) {
    const container = document.getElementById('challengesList');
    container.innerHTML = '';

    challenges.forEach(challenge => {
        const card = document.createElement('div');
        card.className = 'challenge-card';
        card.onclick = () => selectChallenge(challenge);

        card.innerHTML = `
            <div class="difficulty-badge ${challenge.difficulty}">${challenge.difficulty}</div>
            <h3>${challenge.title}</h3>
            <p>${challenge.description.substring(0, 120)}...</p>
        `;

        container.appendChild(card);
    });
}

function selectChallenge(challenge) {
    currentChallenge = challenge;

    document.querySelector('.challenges-section').style.display = 'none';
    document.getElementById('codeSection').style.display = 'block';
    document.getElementById('feedbackSection').style.display = 'none';

    document.getElementById('challengeTitle').textContent = challenge.title;
    document.getElementById('challengeDescription').textContent = challenge.description;

    const difficultyBadge = document.getElementById('difficultyBadge');
    difficultyBadge.textContent = challenge.difficulty;
    difficultyBadge.className = `difficulty-badge ${challenge.difficulty}`;

    const testCasesContainer = document.getElementById('testCases');
    if (challenge.test_cases && challenge.test_cases.length > 0) {
        testCasesContainer.innerHTML = '<h4>Test Cases:</h4>';
        challenge.test_cases.forEach((testCase, index) => {
            const testCaseDiv = document.createElement('div');
            testCaseDiv.className = 'test-case';
            testCaseDiv.innerHTML = `
                <strong>Test ${index + 1}:</strong><br>
                Input: ${testCase.input}<br>
                Expected Output: ${testCase.output}
            `;
            testCasesContainer.appendChild(testCaseDiv);
        });
    } else {
        testCasesContainer.innerHTML = '';
    }

    document.getElementById('codeEditor').value = '';
}

async function submitCode() {
    const code = document.getElementById('codeEditor').value.trim();
    const language = document.getElementById('languageSelect').value;

    if (!code) {
        alert('Please write some code before submitting!');
        return;
    }

    if (!currentChallenge) {
        alert('Please select a challenge first!');
        return;
    }

    try {
        const submitResponse = await fetch(`${API_BASE}/api/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                challenge_id: currentChallenge.id,
                code: code,
                language: language
            })
        });

        const submitResult = await submitResponse.json();
        currentSubmissionId = submitResult.submission_id;

        document.getElementById('codeSection').style.display = 'none';
        document.getElementById('feedbackSection').style.display = 'block';
        document.getElementById('feedbackContent').innerHTML =
            '<div class="loading">Analyzing your code...</div>';

        await getFeedback();

    } catch (error) {
        console.error('Error submitting code:', error);
        alert('Failed to submit code. Please try again.');
    }
}

async function getFeedback() {
    if (!currentSubmissionId) {
        alert('No submission found!');
        return;
    }

    try {
        const feedbackResponse = await fetch(`${API_BASE}/api/feedback`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                submission_id: currentSubmissionId
            })
        });

        const feedbackResult = await feedbackResponse.json();
        displayFeedback(feedbackResult.feedback);

    } catch (error) {
        console.error('Error getting feedback:', error);
        document.getElementById('feedbackContent').innerHTML =
            '<p class="error">Failed to get feedback. Please try again.</p>';
    }
}

function displayFeedback(feedback) {
    const container = document.getElementById('feedbackContent');

    const scoreHtml = `
        <div class="score-display">
            <h3>${feedback.quality_score}/100</h3>
            <p>Code Quality Score</p>
        </div>
    `;

    const complexityHtml = `
        <div class="feedback-section-item">
            <h4>Code Metrics</h4>
            <ul>
                <li>Complexity: <strong>${feedback.complexity}</strong></li>
                <li>Readability: <strong>${feedback.readability}</strong></li>
            </ul>
        </div>
    `;

    const strengthsHtml = feedback.strengths && feedback.strengths.length > 0 ? `
        <div class="feedback-section-item">
            <h4>Strengths</h4>
            <ul>
                ${feedback.strengths.map(s => `<li>${s}</li>`).join('')}
            </ul>
        </div>
    ` : '';

    const suggestionsHtml = feedback.suggestions && feedback.suggestions.length > 0 ? `
        <div class="feedback-section-item">
            <h4>Suggestions for Improvement</h4>
            <ul>
                ${feedback.suggestions.map(s => `<li>${s}</li>`).join('')}
            </ul>
        </div>
    ` : '';

    const bestPracticesHtml = feedback.best_practices && feedback.best_practices.length > 0 ? `
        <div class="feedback-section-item">
            <h4>Best Practices Applied</h4>
            <ul>
                ${feedback.best_practices.map(bp => `<li>${bp}</li>`).join('')}
            </ul>
        </div>
    ` : '';

    container.innerHTML = scoreHtml + complexityHtml + strengthsHtml + suggestionsHtml + bestPracticesHtml;
}

function tryAgain() {
    document.getElementById('feedbackSection').style.display = 'none';
    document.getElementById('codeSection').style.display = 'block';
}

function backToChallenges() {
    document.getElementById('codeSection').style.display = 'none';
    document.getElementById('feedbackSection').style.display = 'none';
    document.querySelector('.challenges-section').style.display = 'block';
    currentChallenge = null;
    currentSubmissionId = null;
}

document.addEventListener('DOMContentLoaded', () => {
    loadChallenges();
});
