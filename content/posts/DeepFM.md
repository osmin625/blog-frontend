---
title: DeepFM
date: 2023-04-04T17:38:00+09:00
tags: [Deep Model, Factorization Machine, Neural Network, CTR Prediction]
categories: [DL Algorithm, Recommendation System]
type: post
---
DeepFM: A Factorization-Machine based Neural Network for CTR Prediction

Wide & Deep 모델과 달리 두 요소(wide, deep)가 입력값을 공유하도록 한 end-to-end 방식의 논문

### **Background**

추천 시스템에서는 implicit feature interaction을 학습하는 것이 중요하다.

예시) 식사 시간에 배달앱 다운로드 수 증가 (order-2 interaction)

10대 남성은 슈팅/RPG게임을 선호 (order-3 interaction)

기존 모델들은 low-나 high-order interaction 중 어느 한 쪽에만 강하다.

Wide & Deep 모델은 이 둘을 통합하여 문제 해결

하지만 wide component에 feature engineering(=Cross-Product Transformation)이 필요하다.

이러한 문제를 해결하고자 DeepFM에서는 FM을 wide component로 사용하여 **입력값을 공유한다.**

**DeepFM = Factorization Machine + Deep Neural Network**

## 모델 구조

### **FM for low-order feature interaction**

기존의 FM모델과 완전히 동일한 구조

수식이 동일하다.

FM 구조

$$
\hat{y}(\mathrm{x})=w_0+\sum_{i=1}^n w_i x_i{+\sum_{i=1}^n \sum_{j=i+1}^n\left\langle\mathrm{v}_i, \mathrm{v}_j\right\rangle x_i x_j} \\

w_0 \in \mathbb{R}, \quad w_i \in \mathbb{R}, \quad \mathrm{v}_i \in \mathbb{R}^k
$$

order-2 feature interaction을 효과적으로 잡는다.

![DeepFM](/imgs/DeepFM-1.png)

각 field가 하나의 feature를 의미한다.

모두 Sparse한 feature로 구성한다.

- Addition으로 연결된 선
    
    1차 Term을 의미
    
- 각각의 Feature은 동일한 차원으로 임베딩된 후, 내적을 통해 feature간 interaction을 학습한다.

![DeepFM](/imgs/DeepFM-2.png)

### **DNN for high-order feature interaction**

모든 feature들은 동일한 차원(k)의 임베딩으로 치환된다.

이 때, 임베딩에 사용되는 가중치는 FM Component의 가중치($v_{ij}$)와 동일하다.

![DeepFM](/imgs/DeepFM-3.png)

$$
\begin{aligned}& a^0=\left[e_1, e_2, \ldots, e_m\right] \\& a^{(l+1)}=\sigma\left(W^l a^l+b^l\right) \\& y_{D N N}=W^{|H|+1} a^{|H|}+b^{|H|+1}\end{aligned}
$$

각 Embedding은 모두 연결되어 가로로 붙게 된다.

이렇게 탄생한 임베딩 벡터가 MLP Layer의 Input Layer가 된다.

이후, L개의 Feed-Forward Network를 지나며 마지막에 클릭 여부를 Output으로 제출한다.

### 전체 구조

$$
\tt \hat y = sigmoid(y_{FM} + y_{DNN})
$$

![DeepFM](/imgs/DeepFM-4.png)
FM과 Deep의 장점을 모두 가진다.

## 타 모델과의 비교

![DeepFM](/imgs/DeepFM-5.png)
### FNN
    
FM 모델을 사용하지만, End-to-End 학습이 아니다.

FM모델을 활용한 이후, 그 임베딩을 다시 가지고 와서 활용한다.

즉, Pre-training이 필요하다.
    
### PNN
    
DeepFM과 흡사하지만, Low-order Interaction(Memorization부분)이 빠져있다.
    

![DeepFM](/imgs/DeepFM-6.png)
### 성능

![DeepFM](/imgs/DeepFM-7.png)