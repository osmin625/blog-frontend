---
title: 손실 함수(Loss Function)에 대해 알아보자.
date: 2022-11-19-00:04:00 +0900
categories: ['AI Knowledge', 'Loss Function' ]
tags: ['Loss Function', 'MAE', 'MSE', 'RMSE', 'Cross-Entropy', 'Regression','Classification']
math: true
img_path: /assets/post_imgs/
---
> ✔️ 간단 요약  
> 신경망의 학습 중 받는 벌점의 기준  
> 회귀와 분류 문제에서 다른 loss function을 사용한다.  
{: .prompt-info }
> Gradient, MAE, MSE, RMSE

**Loss : 예측 값과 실제 값의 차이**

신경망의 학습 중 오답에 대해 받는 벌점

두 값의 차이는 단순히 뺄셈의 절댓값을 의미하는 것은 아니며, 상황에 따라 다양하게 나타난다.

ex) 정답과 완전히 동떨어진 대답을 하면 더 많은 벌점을 받는다.

### **Loss Function**

신경망이 벌점을 받는 기준

신경망의 학습 과정에서 가중치 $\mathbf w$를 평가하는 **함수**.

나는 손실 함수가 함수라는 것을 제대로 인지하지 못했을 때 모델 평가 Metric과 헷갈렸기 때문에, 손실 **함수**라는 것을 다시 한번 인지하고 지나가자.

2차원 그래프로 비유했을 때, 가중치 $\mathbf w$는 x좌표에 해당하고 손실 함수의 값은 y좌표에 해당한다.

손실 함수의 최솟값이 되는 지점에 $\mathbf w$를 위치시키는 것이 신경망의 목표이다.

고등 수학을 빌려 설명하자면, 단순히 미분값이 0이 되는 지점을 파악하여 손실 함수의 최솟값을 구하면 된다.

하지만 고차원에서의 손실 함수 미분은 쉽지 않을 뿐더러, 함수 전체에서 미분값이 0이 되는 지점을 바로 찾아내는 것은 현실적으로 불가능하다.

따라서, 신경망은 $\mathbf w$에서 손실 함수의 기울기를 측정하여 loss가 낮아지는 방향으로 가중치를 조금씩 이동하는 전략을 사용한다.

이 때의 조금을 결정하는 것이 Optimizer이다.

해결하고자 하는 문제에 맞게 loss function을 설정해 사용해주면 된다.

![Loss](loss_function.png)

신경망 학습을 통해 손실 함수 $J$의 최저점을 찾아야 한다.

## **신경망의 학습 알고리즘**

1. 훈련 데이터 입력
2. 매개변수 $\mathbf w$를 난수로 초기화
3. while (true):
    1. 손실 함수$J(\mathbf w)$ 계산(loss 계산)
    2. loss를 낮추는 방향 $\Delta \mathbf w$ 계산
    3. $\mathbf w = \mathbf w + \Delta \mathbf w$
4. return 가중치(매개변수)

## **손실 함수 J(w)의 조건**

- w가 훈련 집합에 있는 샘플을 모두 맞히면, $J(w) = 0$이다.
- w가 틀리는 샘플이 많을수록 $J(w)$의 값이 크다.

위의 조건을 만족하는 수식은 아주 다양하기 때문에, 적절한 손실 함수를 선택해야 한다.

## 손실 함수의 종류

### 회귀(Regression)

- **MAE(Mean Absolute Error)** — $\left|정답 - 예측값\right|$의 평균
    
    > **간단 요약**
    > 
    > 
    > 틀린 만큼 벌점을 얻는다.
    > 
    > 모든 지점에서 그래디언트는 동일하다.
    > 
    
    가장 간단한 손실 함수.
    
    제곱을 취하지 않기 때문에, 모든 오차는 그대로 반영된다.
    
    직관적으로 말하자면, 오차만큼 벌점이 쌓인다.
    
    기울기 관점으로, 모든 가중치에서 그래디언트의 크기가 동일하다.
    
    따라서 MSE나 RMSE에 비해 상대적으로 이상치에 대해 Robust하다.
    
    (이상치도 오차만큼만 벌점이 쌓이기 때문)
    
    $$
    \frac{1}{n} \sum_{i=1}^n\left|{y_i}-\hat y_i\right|
    $$
    
    
    ![Loss_function](loss_function1.png)
- **MSE(Mean Squared Error)** — $(정답 - 예측값)^2$의 평균
    
    > **간단 요약**
    > 
    > 
    > 정답과의 거리가 멀수록 더 많은 벌점을 부여하자!
    > 
    > 오차를 제곱 하면 되겠네?
    > 
    > 정답에서 멀어질수록 그래디언트의 크기가 증가한다.
    > 
    
    $$
    M S E=\frac{1}{n} \sum_{i=1}^n\left({y_i}-\hat y_i\right)^2
    $$
    
    ![Loss_function](loss_function2.png)
    
    미니 배치 단위로 처리(샘플의 오차를 평균 낸다.)
    
    $$
    \begin{aligned}J\left(\mathbf{U}^1, \mathbf{U}^2\right) & =\frac{1}{|M|} \sum_{\mathbf{x} \in M}\|\mathbf{y}-\mathbf{0}\|^2 \\& =\frac{1}{|M|} \sum_{\mathbf{x} \in M}\left\|\mathbf{y}-\tau_2\left(\mathbf{U}^2 \tau_1\left(\mathbf{U}^1 \mathbf{x}^{\mathrm{T}}\right)\right)\right\|^2\end{aligned}
    $$
    
    - 오차값에 제곱을 취하기 때문에 0~1 사이의 값은 상대적으로 작게 반영되고, 1보다 큰 값은 상대적으로 더 크게 반영된다.
    - 학습이 느려지거나 학습이 안되는 상황을 초래할 가능성이 있다.
    - 정답과 예측값의 차이가 클수록 더 크게 반영되기 때문에, 이상치에 매우 민감하다.
- **RMSE(Root MSE)** — $\sqrt{(정답 - 예측값)^2\text {의 평}균}$
    
    > **간단 요약**
    > 
    > 
    > MSE에 루트 씌운 값.
    > 
    > 얼핏 MAE와 동일한 것 아니야? 생각할 수 있지만, 계산 순서에서 차이가 발생하고, $1\over n$이 아니라 $1\over \sqrt n$을 했다는 점이 MAE와 다르다.
    > 
    
    $$
    R M S E=\sqrt{\frac{1}{n} \sum_{i=1}^n\left(\hat{y_i}-y_i\right)^2}
    $$
    
    ![Loss_function](loss_function3.png)
    
    MSE와 마찬가지로 각 오차값의 크기에 따라 다른 그래디언트를 가지게 된다.
    

![Loss_function](loss_function4.png)

### 분류(Classification)

**Entropy**

확률 분포의 무작위성(불확실성)을 측정하는 함수

$$
H(x)=-\sum_{i=1, k} P\left(e_i\right) \log P\left(e_i\right)
$$

- **Cross-Entropy**
    
    **정보량을 상징한다. → 불공정성 문제 해결**
    
    두 확률 분포 P와 Q가 다른 정도를 측정하는 함수
    
    $$
    H(P, Q)=-\sum_{i=1, k} P\left(e_i\right) \log Q\left(e_i\right)
    $$
    
    - 공정한 주사위에는 특별한 정보가 존재하지 않는다.
        
        $$
        -\left(\frac{1}{6} \log \frac{1}{6}+\ldots+\frac{1}{6} \log \frac{1}{6}\right)=1.7918
        $$
        
    - 찌그러진 주사위에서는 특정 값이 더 잘나온다는 정보가 추가된다.
        
        공정한 주사위와 찌그러진 주사위의 교차 엔트로피
        
        $$
        -\left(\frac{1}{6} \log \frac{1}{2}+\frac{1}{6} \log \frac{1}{10}+\cdots+\frac{1}{6} \log \frac{1}{10}\right)=2.0343
        $$
        
- **Binary Cross-Entropy**
    
    `tf.nn.sigmoid_cross_entropy_with_logits( )`
    
    $$
    B C E=-\frac{1}{N} \sum_{i=0}^N y_i \cdot \log \left(\hat{y_i}\right)+\left(1-y_i\right) \cdot \log \left(1-\hat{y_i}\right)
    $$
    
- **Categorical Cross-Entropy**
    
    `tf.nn.softmax_cross_entropy_with_logits_v2( )`
    
    $$
    C C E=-\frac{1}{N} \sum_{i=0}^N \sum_{j=0}^J y_j \cdot \log \left(\hat{y_j}\right)+\left(1-y_j\right) \cdot \log \left(1-\hat{y_j}\right)
    $$
