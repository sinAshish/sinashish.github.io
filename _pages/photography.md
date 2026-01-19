---
layout: page
title: photography
permalink: /photography/
description: A collection of moments captured from various places I've visited.
nav: true
nav_order: 3
images:
  lightbox2: true
---

<div class="row mb-4">
    <div class="col-12 text-center">
        <div class="tag-category-list">
            <ul class="p-0 m-0" id="filter-buttons">
                <li>
                    <i class="fa-solid fa-hashtag fa-sm"></i> <span onclick="filterSelection('all')" style="cursor: pointer; border-bottom: 1px solid transparent;">All</span>
                </li>
                <p>&bull;</p>
                {% assign tags = "" | split: "," %}
                {% for photo in site.data.photography %}
                    {% for tag in photo.tags %}
                        {% unless tags contains tag %}
                            {% assign tags = tags | push: tag %}
                        {% endunless %}
                    {% endfor %}
                {% endfor %}
                {% for tag in tags %}
                    <li>
                        <i class="fa-solid fa-hashtag fa-sm"></i> <span onclick="filterSelection('{{ tag }}')" style="cursor: pointer; border-bottom: 1px solid transparent;">{{ tag }}</span>
                    </li>
                    {% unless forloop.last %}
                        <p>&bull;</p>
                    {% endunless %}
                {% endfor %}
            </ul>
        </div>
    </div>
</div>

<div class="row grid">
    {% for photo in site.data.photography %}
    <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4 grid-item {{ photo.tags | join: ' ' }}">
        <a href="{{ '/assets/img/photography/' | append: photo.filename | relative_url }}"
           data-lightbox="photography"
           data-title="
             <strong>{{ photo.title }}</strong><br>
             <i class='fa-solid fa-location-dot'></i> {{ photo.location }} &nbsp; &middot; &nbsp; <i class='fa-solid fa-calendar'></i> {{ photo.date | date: '%B %d, %Y' }}<br>
             {% for tag in photo.tags %}<i class='fa-solid fa-hashtag fa-sm'></i> {{ tag }} {% unless forloop.last %} &nbsp; {% endunless %}{% endfor %}<br>
             {{ photo.caption }}
           ">
            <img src="{{ '/assets/img/photography/' | append: photo.filename | relative_url }}" 
                 class="img-fluid z-depth-1 rounded" 
                 alt="{{ photo.title }}"
                 style="width: 100%; height: 250px; object-fit: cover;"
                 onerror="this.onerror=null; this.src='https://via.placeholder.com/600x400?text={{ photo.title | url_encode }}';">
        </a>
    </div>
    {% endfor %}
</div>

<style>
    #filter-buttons span {
        transition: all 0.2s ease-in-out;
    }
    #filter-buttons span.active {
        border-bottom: 1px solid var(--global-text-color) !important;
        font-weight: bold;
    }
</style>

<script>
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("grid-item");
  if (c == "all") c = "";
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "d-none");
    if (x[i].className.indexOf(c) == -1) w3AddClass(x[i], "d-none");
  }
  
  var btnContainer = document.getElementById("filter-buttons");
  // Select all spans that are direct children of li
  var spans = btnContainer.querySelectorAll("li span");
  for (var i = 0; i < spans.length; i++) {
    spans[i].classList.remove("active");
    // Check if text matches. Handle "All" specifically.
    var text = spans[i].textContent.trim();
    if (c === "" && text === "All") {
        spans[i].classList.add("active");
    } else if (text === c) {
        spans[i].classList.add("active");
    }
  }
}
// Set 'All' as active initially
document.addEventListener("DOMContentLoaded", function() {
    var allSpan = document.querySelector("#filter-buttons li span");
    if(allSpan && allSpan.textContent.trim() === "All") {
        allSpan.classList.add("active");
    }
});

function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
  }
}

function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);     
    }
  }
  element.className = arr1.join(" ");
}
</script>