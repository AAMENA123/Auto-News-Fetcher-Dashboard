
document.addEventListener('DOMContentLoaded', function() {
    const fetchNewsBtn = document.getElementById('fetchNewsBtn');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const newsContainer = document.getElementById('newsContainer');

    fetchNewsBtn.addEventListener('click', function() {
        loadingIndicator.style.display = 'block';

        fetch("/fetch-news/", {
            method: "POST"
        })
        .then(response => response.json())
        .then(data => {
            loadingIndicator.style.display = 'none';

            if (data.status === "success") {
                data.articles.forEach(article => {
                    const card = `
                        <div class="col-lg-4 col-md-6">
                            <div class="card news-card">
                                ${article.url_to_image ? `<img src="${article.url_to_image}" class="card-img-top article-img" alt="News Image">` : ""}
                                <div class="card-body">
                                    <h5 class="card-title">${article.title}</h5>
                                    <p class="card-text">${article.summary || ""}</p>
                                    <div class="d-flex justify-content-between align-items-center">
                                        <small class="text-muted">${article.source} - ${article.published_at}</small>
                                        ${article.url ? `<a href="${article.url}" target="_blank" class="btn btn-sm btn-outline-primary">Read more</a>` : ""}
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                    newsContainer.innerHTML = card + newsContainer.innerHTML;
                });
            } else {
                alert("Error fetching news: " + data.message);
            }
        })
        .catch(err => {
            loadingIndicator.style.display = 'none';
            alert("Something went wrong: " + err);
        });
    });
});

