---
title: Autoregression
date: 2023-06-28-16:10:00 +0900
categories: [AI Math, Statistics]
tags: [Autoregression,Autoregressive Model]
math: true
---
회귀 분석의 관점에서 과거의 데이터를 보고 현재 또는 미래의 결과를 예측하는 것

즉, Regression을 자기 자신에게 적용하는 것

$$
y_1, \ldots, y_n \rightarrow y_{n+1}
$$

$$
\mathrm{MSE}=\frac{1}{n} \sum_{i=1}^n\left(f\left(y_1, \ldots y_i\right)-y_{i+1}\right)^2
$$

## 종류

### Moving Average(이동평균)

가장 간단한 방법

- 최신 트렌드를 반영하기 위해 최근 K개의 평균을 향후 예측에 활용한다.
- K의 값에 따라 경향성을 다르게 모델링할 수 있다.
- K가 커질수록 최신 트렌드의 반영 정도가 줄어든다.

평균 뿐만 아니라 다양한 형태로 Moving Average의 모델링이 가능하다.

$$
f\left(y_1, \ldots, y_n\right)=\frac{1}{K} \sum_{k=0}^{K-1} y_{n-k}
$$

$$
f\left(y_1, \ldots, y_{n+1}\right)=\frac{1}{K}\left(K \cdot f\left(y_1, \ldots, y_n\right){-y_{n-K+1}}{+y_{n+1}}\right)
$$

- ${-y_{n-K+1}}$: 가장 오래된 값 삭제
- ${+y_{n+1}}$ : 최근 값 추가

### Weighted Moving Average

**단순히 평균이 아니라 최근 값에 대한 가중치를 더 크게 주는 방법**

- 선형적으로 비중을 조절하는 것 뿐만 아니라 지수, 로그 등을 활용하여 다양한 방법으로 모델링이 가능하다.
    
    지수 함수를 활용하여 최근 값의 비중을 기하급수적으로 증가시켰다.
    
    $$
    \begin{gathered}f\left(y_1\right)=y_1 \\f\left(y_1, \ldots, y_{n+1}\right)=\alpha f\left(y_1, \ldots, y_n\right)+(1-\alpha) \cdot y_{n+1}\end{gathered}
    $$
    

### Learning-based Moving Average

**Weighted moving average에서의 가중치를 학습하는 방법**

$$
f\left(y_1, \ldots, y_n\right)=\sum_{k=0}^{K-1} \theta_k \cdot y_{n-k}
$$

주기적인 변화가 있는 교통량 예측, 시즌 별 상품 소비 예측 등에 사용된다.

주 단위, 월 단위 등의 주기성을 모델링하는 데 보다 적합하다.