---
layout: post
title: Visualizing Deformable DETR Attention
date: 2025-09-20 16:30:00-0400
description: Visualizations of multi-scale deformable attention mechanism in DETR.
tags: computer-vision deep-learning transformers
categories: research
toc:
  sidebar: left
giscus_comments: false
related_posts: false
---

> **WIP. Made these while learning about DETR at Amii.**

Standard self-attention in transformers suffers from quadratic computational complexity $O(H^2W^2)$ relative to the spatial resolution of the feature map. In object detection architectures like DETR [1], this makes high-resolution or multi-scale feature maps prohibitively expensive to compute. 

**Deformable DETR** [2] resolves this bottleneck using **deformable attention**, which scales linearly with image size by restricting attention computations to a small, learned set of key sampling points around a reference point.

Below are some custom Manim visualizations I made to understand this mechanism better.

---

### 1. Deformable Attention Overview

This animation illustrates how standard global self-attention (connecting every pixel to every other pixel) is replaced by sparse, localized attention. The model dynamically predicts a coordinate reference point $p_q$ and a sparse set of $K$ sampling locations across different feature scales:

{% include video.liquid path="assets/img/blogs/DeformableAttentionScene.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}

---

### 2. Multi-Scale Deformable Attention ($MSDeformAttn$)

Mathematically, given input feature maps $\{x^l\}_{l=1}^L$, let $q$ be a query element with feature $z_q$ and reference point $p_q$. The multi-scale deformable attention is formulated as:

$$\text{MSDeformAttn}(z_q, p_q, \{x^l\}_{l=1}^L) = \sum_{m=1}^M W_m \left[ \sum_{l=1}^L \sum_{k=1}^K A_{mlqk} \cdot W'_m x^l(p_q + \Delta p_{mlqk}) \right]$$

Where:
*   $M$ represents the number of attention heads.
*   $L$ is the number of feature map scales.
*   $K$ is the number of sampled keys per scale (typically small, e.g., $K=4$).
*   $\Delta p_{mlqk}$ represents the predicted **sampling offset**, shown in the animation below as the yellow arrows shifting from the uniform reference points.
*   $A_{mlqk}$ is the **attention weight**, visualized below by the changing sizes of the red sampling dots.

{% include video.liquid path="assets/img/blogs/DeformableAttentionDetailed.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true muted=true %}

Since the predicted offset $p_q + \Delta p_{mlqk}$ is continuous, sub-pixel feature representations are sampled using **bilinear interpolation** $x^l(\cdot)$ over the nearest grid coordinates, ensuring the entire operation remains fully differentiable.

---

### References

1. Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, and Sergey Zagoruyko. **"End-to-End Object Detection with Transformers."** *European Conference on Computer Vision (ECCV)*, 2020. [arXiv:2005.12872](https://arxiv.org/abs/2005.12872).
2. Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang Chao, and Jifeng Dai. **"Deformable DETR: Simple and Efficient End-to-End Object Detection."** *International Conference on Learning Representations (ICLR)*, 2021. [arXiv:2010.04159](https://arxiv.org/abs/2010.04159).

---

*These visualizations are a work-in-progress. More updates on implementation to come!*
