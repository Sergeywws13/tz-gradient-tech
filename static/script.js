document.addEventListener('DOMContentLoaded', function() {
    const shortenForm = document.getElementById('shorten-form');
    const longUrlInput = document.getElementById('long-url');
    const resultDiv = document.getElementById('result');
    const shortLink = document.getElementById('short-link');

    const statsForm = document.getElementById('stats-form');
    const statsShortId = document.getElementById('stats-short-id');
    const statsResult = document.getElementById('stats-result');
    const statsShortSpan = document.getElementById('stats-short');
    const statsVisitsSpan = document.getElementById('stats-visits');

    shortenForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const longUrl = longUrlInput.value.trim();
        if (!longUrl) return;

        try {
            const response = await fetch('/shorten', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ long_url: longUrl })
            });
            const data = await response.json();
            if (response.ok) {
                const shortId = data.data;
                const shortUrl = `${window.location.origin}/${shortId}`;
                shortLink.href = shortUrl;
                shortLink.textContent = shortUrl;
                resultDiv.style.display = 'block';
                resultDiv.classList.remove('error');
            } else {
                showError(resultDiv, data.detail || 'Ошибка при создании ссылки');
            }
        } catch (error) {
            showError(resultDiv, 'Ошибка сети');
        }
    });

    statsForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const shortId = statsShortId.value.trim();
        if (!shortId) return;

        try {
            const response = await fetch(`/stats/${shortId}`);
            const data = await response.json();
            if (response.ok) {
                statsShortSpan.textContent = shortId;
                statsVisitsSpan.textContent = data.visits;
                statsResult.style.display = 'block';
                statsResult.classList.remove('error');
            } else {
                showError(statsResult, data.detail || 'Ссылка не найдена');
            }
        } catch (error) {
            showError(statsResult, 'Ошибка сети');
        }
    });

    function showError(element, message) {
        element.textContent = message;
        element.style.display = 'block';
        element.classList.add('error');
    }
});