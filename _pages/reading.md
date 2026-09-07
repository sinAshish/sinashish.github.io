---
layout: page
title: reading list
permalink: /reading/
description: ""
nav: true
nav_order: 1
---

<div class="row align-items-center mb-4">
  <div class="col">
    <p class="mb-0" style="font-size: 1.1rem; line-height: 1.5;">
      Apart from research, I enjoy reading books and manga. I alternate between reading fiction and non-fiction books. Some of the books that I've read over the years are listed below. You can also see them on my <a href="https://goodreads.com/sinashish" target="_blank" rel="noopener noreferrer">Goodreads</a>. The books I especially liked are rated 4 or above.<br><span class="text-muted" style="font-size: 0.95rem;">Inspired by <a href="https://irenechen.net/reading-list/" target="_blank" rel="noopener noreferrer">Irene Chen's</a> page.</span>
    </p>
  </div>
  <div class="col-auto">
    <button class="btn btn-sm btn-outline-primary" id="toggle-view-btn" onclick="toggleView()" style="border-radius: 4px; font-weight: 500;">
      <i class="fa-solid fa-list mr-1"></i> List View
    </button>
  </div>
</div>

<div class="reading-list">
  {% assign years = "" | split: "" %}
  {% for book in site.data.reading %}
    {% unless years contains book.year %}
      {% assign years = years | push: book.year %}
    {% endunless %}
  {% endfor %}
  {% assign sorted_years = years | sort | reverse %}

  {% for target_year in sorted_years %}
    <!-- {{ target_year }} Section -->
    <div class="year-section mb-5">
      <h3 class="border-bottom pb-2 mb-4">{{ target_year }}</h3>
      
      <!-- Grid View -->
      <div class="row row-cols-1 row-cols-md-2 row-cols-lg-6 g-4 grid-view-container">
        {% for book in site.data.reading %}
          {% if book.year == target_year %}
            <div class="col mb-4">
              <div class="card h-100 hoverable">
                <a href="https://www.goodreads.com/book/show/{{ book.book_id }}" target="_blank" rel="noopener noreferrer" class="text-reset d-block text-decoration-none h-100">
                  {% if book.has_cover %}
                    <img src="/assets/img/reading/{{ book.book_id }}.webp" class="card-img-top p-2" alt="{{ book.title }}" style="object-fit: cover; height: 180px;">
                  {% else %}
                    <div class="card-img-top p-2 d-flex align-items-center justify-content-center bg-light text-center" style="height: 180px;">
                      <span style="font-size: 3rem; filter: grayscale(20%);">📖</span>
                    </div>
                  {% endif %}
                  <div class="card-body p-2 d-flex flex-column" style="height: calc(100% - 180px);">
                    <h5 class="card-title text-reset text-decoration-none" style="font-size: 0.9rem; margin-bottom: 0.25rem;">
                      {{ book.title }}
                    </h5>
                    <div class="d-flex justify-content-between align-items-end mt-auto">
                      <p class="card-text text-muted small mb-0">{{ book.author }}</p>
                      <div class="text-muted small" style="font-size: 0.8rem;">
                        {% if book.rating > 0 %}
                          {{ book.rating }} ★
                        {% endif %}
                      </div>
                    </div>
                  </div>
                </a>
              </div>
            </div>
          {% endif %}
        {% endfor %}
      </div>

      <!-- List View -->
      <div class="list-view-container d-none">
        <ul class="list-group" style="background: transparent;">
          {% assign idx = 0 %}
          {% for book in site.data.reading %}
            {% if book.year == target_year %}
              {% assign idx = idx | plus: 1 %}
              <li class="list-group-item d-flex justify-content-between align-items-center border-0 p-1 bg-transparent" style="font-size: 0.95rem;">
                <div class="ms-2 me-auto">
                  <span class="text-muted mr-2 font-weight-bold" style="min-width: 25px; display: inline-block;">{{ idx }}.</span>
                  <a href="https://www.goodreads.com/book/show/{{ book.book_id }}" target="_blank" rel="noopener noreferrer" class="text-reset font-weight-normal text-decoration-none">{{ book.title }}</a>
                  <span class="text-muted small ml-1">by {{ book.author }}</span>
                  {% if book.rating > 0 %}
                    <span class="text-muted small ml-2" style="font-size: 0.8rem;">{{ book.rating }} ★</span>
                  {% endif %}
                </div>
              </li>
            {% endif %}
          {% endfor %}
        </ul>
      </div>

    </div>
  {% endfor %}
</div>

<script>
function toggleView() {
  const btn = document.getElementById('toggle-view-btn');
  const grids = document.querySelectorAll('.grid-view-container');
  const lists = document.querySelectorAll('.list-view-container');
  
  if (btn.innerHTML.includes('List View')) {
    btn.innerHTML = '<i class="fa-solid fa-grip mr-1"></i> Grid View';
    grids.forEach(el => el.classList.add('d-none'));
    lists.forEach(el => el.classList.remove('d-none'));
  } else {
    btn.innerHTML = '<i class="fa-solid fa-list mr-1"></i> List View';
    grids.forEach(el => el.classList.remove('d-none'));
    lists.forEach(el => el.classList.add('d-none'));
  }
}
</script>
