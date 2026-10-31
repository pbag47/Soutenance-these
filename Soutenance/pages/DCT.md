---
title: -- DCTLMS-I
level: 1
---

# Transformée en Cosinus Discrète de type 1

$$
\mathbf{P} = \begin{pmatrix}
    1 & 2 & 2 & \cdots & 2 & 1 \\
    1 & 2 \cos{\frac{\pi}{L-1}} & 2 \cos{\frac{2 \pi}{L-1}} & \cdots & 2 \cos{\frac{(L-2)\pi}{L-1}} & -1 \\
    1 & 2 \cos{\frac{2 \pi}{L-1}} & 2 \cos{\frac{4 \pi}{L-1}} & \cdots & 2 \cos{\frac{2(L-2)\pi}{L-1}} & 1 \\
    \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
    1 & 2 \cos{\frac{(L-2) \pi}{L-1}} & 2 \cos{\frac{2(L-2) \pi}{L-1}} & \cdots & 2 \cos{\frac{(L-2)^2\pi}{L-1}} & \cos{((L-2)\pi)} \\
    1 & -2 & 2 & \cdots & 2 \cos{((L-2)\pi)} &  \cos{((L-1)\pi)}
\end{pmatrix}
$$

$\hat{\mathbf{R}}_n$ : matrice de Toeplitz symétrique, rapprochement avec les matrices circulaires et les propriétés de la Transformée de Fourier

<img
    src="/images/R_plus_sym_tp.png"
    class="object-contain h-150pt"
/>


<!-- mat(
      1, 2, dots.c, 1 ;
      1, 2 cos(pi / var.nb(L-1)), dots.c, -1 ;
      dots.v, dots.v, dots.down, dots.v ;
      1, -2, dots.c, (-1)^(var.nb(L-1))
    ), -->


<!-- 
$$
\begin{align}
    \nonumber \hat{\mathbf{R}}_n^+ &= \begin{bmatrix}
    \mathbb{E}\{ x_n' x_n' \} & \mathbb{E}\{ x_n' x_{n-1}'\} & \cdots & \mathbb{E}\{ x_n' x_{n-L+1}' \} \\
    \mathbb{E}\{ x_n' x_{n-1}' \} & \mathbb{E}\{ x_{n-1}' x_{n-1}'\} & \cdots & \mathbb{E}\{ x_{n-1}' x_{n-L+1}' \} \\
    \vdots & \vdots & \ddots & \vdots \\
    \mathbb{E}\{ x_{n}' x_{n-L+1}' \} & \mathbb{E}\{ x_{n-1}' x_{n-L+1}'\} & \cdots & \mathbb{E}\{ x_{n-L+1}' x_{n-L+1}' \}
    \end{bmatrix}
\end{align}
$$

$$
% \begin{array}{cc|c|cc}
%   \cdot & \cdot & \cdot & 0 & 0 \\
%   \cdot & \cdot & \cdot & 0 & 0 \\
%   \hline
%   \cdot & \cdot & \mathbf{X} & \cdot & \cdot \\
%   \hline
%   0 & 0 & \cdot & \cdot & \cdot \\
%   0 & 0 & \cdot & \cdot & \cdot 
% \end{array}

\begin{bmatrix}%{cc:c:cc}
  \colorbox{#1e3a8a}{$\cdot$} & \colorbox{#1e3a8a}{$\cdot$} & \colorbox{#1e3a8a}{$\cdot$} & 0 & 0 \\
  \colorbox{#1e3a8a}{$\cdot$} & \colorbox{#1e3a8a}{$\hat{\mathbf{R}}_n$} & \colorbox{#1e3a8a}{$\cdot$} & 0 & 0 \\
  \colorbox{#1e3a8a}{$\cdot$} & \colorbox{#1e3a8a}{$\cdot$} & \colorbox{#581c87}{$\cdot$} & \colorbox{#7f1d1d}{$\cdot$} & \colorbox{#7f1d1d}{$\cdot$} \\
  0 & 0 & \colorbox{#7f1d1d}{$\cdot$} & \colorbox{#7f1d1d}{$\hat{\mathbf{R}}_n$} & \colorbox{#7f1d1d}{$\cdot$} \\
  0 & 0 & \colorbox{#7f1d1d}{$\cdot$} & \colorbox{#7f1d1d}{$\cdot$} & \colorbox{#7f1d1d}{$\cdot$} 
\end{bmatrix}
$$

$$
\begin{bmatrix}
  \colorbox{#1e3a8a}{$\begin{matrix} \cdot & \cdot \\ \cdot & \cdot \end{matrix}$} & \begin{matrix} 0 & 0 \\ 0 & 0 \end{matrix} \\
  \begin{matrix} 0 & 0 \\ 0 & 0 \end{matrix} & \colorbox{#7f1d1d}{$\begin{matrix} \cdot & \cdot \\ \cdot & \cdot \end{matrix}$}
\end{bmatrix}
$$
 -->
