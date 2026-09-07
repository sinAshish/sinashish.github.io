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

Deformable DETR [2] is an incredible advancement in end-to-end object detection. By utilizing **deformable attention**, it overcomes the slow convergence and multi-scale resolution challenges of the original DETR [1] model.

Instead of attending to all spatial locations across the image (which is computationally expensive, especially at higher resolutions), Deformable DETR only attends to a small set of key sampling points around a reference point.

Below are some custom Manim visualizations I made to understand this mechanism better.

---

### Deformable Attention Overview

This animation shows the core mechanism where key sampling points are dynamically selected around reference points across different scales of the feature maps, and attention is computed over them.

{% include video.liquid path="assets/img/blogs/DeformableAttentionScene.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}

---

### Detailed Deformable Attention Weights

In this detailed visualization, we look closer at how the sampling offsets and attention weights are dynamically predicted from the query feature, showing exactly how the model decides where and what to focus on.

{% include video.liquid path="assets/img/blogs/DeformableAttentionDetailed.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}

---

### References

1. Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, and Sergey Zagoruyko. **"End-to-End Object Detection with Transformers."** *European Conference on Computer Vision (ECCV)*, 2020. [arXiv:2005.12872](https://arxiv.org/abs/2005.12872).
2. Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang Chao, and Jifeng Dai. **"Deformable DETR: Simple and Efficient End-to-End Object Detection."** *International Conference on Learning Representations (ICLR)*, 2021. [arXiv:2010.04159](https://arxiv.org/abs/2010.04159).

---

*These visualizations are a work-in-progress. More updates on the implementation and mathematical formulation to come!*
