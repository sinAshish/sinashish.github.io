---
layout: about
title: about
permalink: /
# subtitle: <a href='https://dev3.noahlab.com.hk'>Huawei’s Noah’s Ark Lab</a> CV/ML Researcher

profile:
  align: right
  images: 
    - profile_pics/cvpr-headshot.webp
    - profile_pics/ashish-iitr-main.webp
    - profile_pics/ashish-iitr-candle.webp
    - profile_pics/ashish-iitr-stairs.webp
    - profile_pics/chatgpt-dating.webp
    - profile_pics/chatgpt-sfu-degree.webp
    - profile_pics/sf-headshot.webp
  image_circular: true # crops the image to make it circular
  more_info: >
    <div style="text-align: center;">
      <p style="display: block;">CV/ML Researcher</p>
      <p style="display: block;">Berkeley/SF</p>
      <p style="display: block; font-size: 0.85rem; margin-top: 5px;"><i>Refresh to render Ashish in new scenes</i></p>
    </div>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 10 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

<p style="min-height: 1.5rem; margin-bottom: 1rem;"><span id="typewriter"></span><span class="cursor" style="display: inline-block; margin-left: 2px; animation: blink 1s step-end infinite;">|</span></p>

<style>
@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}
</style>
<script>
document.addEventListener("DOMContentLoaded", function() {
  const words = ["Hi", "नमस्ते", "こんにちは"];
  let i = 0;
  const speed = 100; // typing speed
  const deleteSpeed = 50; // deleting speed
  const wait = 2000; // time to wait at the end of a word
  
  function typeWriter() {
    let word = words[i];
    let el = document.getElementById("typewriter");
    if (!el) return;
    let txt = el.innerHTML;
    
    // Typing forward
    if (txt.length < word.length && !el.classList.contains('deleting')) {
      el.innerHTML = word.substring(0, txt.length + 1);
      setTimeout(typeWriter, speed);
    } 
    // Wait at the end of word
    else if (txt.length === word.length && !el.classList.contains('deleting')) {
      el.classList.add('deleting');
      setTimeout(typeWriter, wait);
    } 
    // Deleting backward
    else if (txt.length > 0 && el.classList.contains('deleting')) {
      el.innerHTML = word.substring(0, txt.length - 1);
      setTimeout(typeWriter, deleteSpeed);
    } 
    // Move to next word
    else if (txt.length === 0 && el.classList.contains('deleting')) {
      el.classList.remove('deleting');
      i = (i + 1) % words.length;
      setTimeout(typeWriter, speed);
    }
  }
  
  // Start the effect
  setTimeout(typeWriter, 500);
});
</script>

I am currently a PhD student in the Computational Precision Health (CPH) program at UC Berkeley and UCSF.

My research interests lie at the intersection of computer vision and machine learning, with applications in healthcare and scientific discovery. I am particularly interested in developing novel algorithms and leveraging recent advances in representation learning, generative modeling, and geometric deep learning to develop robust and interpretable AI systems dedicated to transforming healthcare, particularly in precision medicine and drug discovery.

I hold an MSc ([thesis](https://summit.sfu.ca/item/38512)) in Computer Science from [Simon Fraser University](https://sfu.ca), where I worked with [Prof. Ghassan Hamarneh](https://www.medicalimageanalysis.com/about/ghassans-bio), and a Bachelor’s in Materials Science from [IIT Roorkee](https://www.iitr.ac.in/). 

Previously, I was an ML Resident at [AMII](https://www.amii.ca), an ML Researcher at [Huawei’s Noah’s Ark Lab](https://dev3.noahlab.com.hk), a Risk Analyst at [Wells Fargo](https://wellsfargo.com/), a Research Engineer at [Preferred Networks](https://preferred.jp/en/), and an intern with [Prof. Jonghyun Choi](https://ppolon.github.io) and [Prof. Jose Dolz](https://josedolz.github.io).

If you are interested in my work, have opportunities, or would like to collaborate, please feel free to [reach out](mailto:ashishsinha108@gmail.com).

**Offline:** 📚 [Reading](https://goodreads.com/sinashish) · 🎬 [Movies](https://letterboxd.com/sinashish/) · 🏃 [Running](https://www.strava.com/athletes/98067428) · 📷 [Photography](https://instagram.com/_a.sinha_) · 🥏 [Ultimate](/photography/#ultimate)
