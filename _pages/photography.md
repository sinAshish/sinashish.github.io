---
layout: page
title: photography
permalink: /photography/
description: A collection of moments captured from various places I've visited.
nav: false
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
                {% assign tags = "mountains, beaches, sports, random" | split: ", " %}
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
    <!-- grid-sizer for masonry to calculate column width accurately -->
    <div class="col-12 col-sm-6 col-md-3 col-lg-3 grid-sizer" style="height: 0; padding: 0; margin: 0; visibility: hidden;"></div>
    {% for photo in site.data.photography %}
    <div class="col-12 col-sm-6 col-md-3 col-lg-3 mb-4 grid-item {{ photo.tags | join: ' ' }}">
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
  
  if (typeof $ !== 'undefined' && $('.grid').length) {
    $('.grid').masonry('layout');
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
// Parse hash on load
document.addEventListener("DOMContentLoaded", function() {
    var hash = window.location.hash.substring(1);
    if (hash) {
        filterSelection(hash);
    } else {
        filterSelection("all");
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