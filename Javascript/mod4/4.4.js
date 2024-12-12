document.getElementById('searchForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = document.getElementById('query').value;
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
        const results = await response.json();
        results.forEach(tvShow => {
            const { show } = tvShow;
            const article = document.createElement('article');
            article.innerHTML = `
                <h2>${show.name}</h2>
                <a href="${show.url}" target="_blank">${show.url}</a>
                <img src="${show.image?.medium || 'https://via.placeholder.com/210x295?text=Not%20Found'}" alt="${show.name}">
                <div>${show.summary}</div>
            `;
            resultsDiv.appendChild(article);
        });
    } catch (error) {
        console.error("Äe toimi", error);
    }
});
