document.getElementById('searchForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = document.getElementById('query').value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
        const results = await response.json();
        console.log(results);
    } catch (error) {
        console.error("error:", error);
    }
});