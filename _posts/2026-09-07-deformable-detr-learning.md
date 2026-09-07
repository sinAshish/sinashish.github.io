---
layout: post
title: Visualizing Deformable DETR Attention
date: 2026-09-07 16:30:00-0400
description: Visualizations of multi-scale deformable attention mechanism in DETR.
tags: computer-vision deep-learning transformers
categories: research
toc:
  sidebar: left
giscus_comments: false
related_posts: false
---

> **WIP. Made these while learning about DETR at Amii.**

Deformable DETR (DEtection TRansformer) is an incredible advancement in object detection. By utilizing **deformable attention**, it overcomes the slow convergence and multi-scale resolution challenges of the original DETR model. 

Instead of attending to all spatial locations across the image (which is computationally expensive, especially at higher resolutions), Deformable DETR only attends to a small set of key sampling points around a reference point.

Below are some custom Manim visualizations I made to understand this mechanism better.

---

### Deformable Attention Overview

This animation shows the core mechanism where key sampling points are dynamically selected around reference points across different scales of the feature maps, and attention is computed over them.

{% include video.liquid path="assets/img/blogs/DeformableAttentionScene.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}

---

### Detailed Deformable Attention Weights

In this detailed visualization, we look closer at how the sampling offsets and attention weights are dynamically predicted from the query feature, showing exactly how the model decides where and what to focus on.

{% include video.liquid path="assets/img/blogs/DeformableAttentionDetailed.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}

---

*These visualizations are a work-in-progress. More updates on the implementation and mathematical formulation to come!*
