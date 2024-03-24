---
title: Cross-Entropy(=Log loss, 교차 엔트로피)
date: 2023-09-22T06:54:00+09:00
categories: [AI Math, Statistics]
tags: [Cross Entropy, Entropy]
type: post
---
**두 확률 분포 P와 Q가 다른 정도를 측정하는 함수**

`$$
H(P, Q)=-\sum_{i=1, k} P\left(e_i\right) \log Q\left(e_i\right)
$$`

**최선의 전략이 아닐 때의 질문 개수의 기댓값**

엔트로피를 최적화된 전략 하에서 질문 개수에 대한 기댓값이라고 설명했다.

하지만 현실 문제의 대부분의 경우 최선의 전략을 찾기 어렵다.

스무 고개에서 최적의 전략이 각 사건의 확률에 의해 결정되듯이, 전략은 곧 확률 분포라고 이해할 수 있다.

결국 엔트로피는 전략`$(\log P_i)$`과 사건`$(P_i)$`의 분포가 동일한 상태를 의미하고,

교차 엔트로피는 전략`$(\log Q_i)$`과 사건`$(P_i)$`의 분포가 다른 상태를 의미한다.

**전략과 사건의 분포의 차이는 곧 사건의 분포가 가지는 정보량을 상징한다.**

MSE의 불공정성 문제 해결

- 공정한 주사위에는 특별한 정보가 존재하지 않는다.
    
    `$$
    -\left(\frac{1}{6} \log \frac{1}{6}+\ldots+\frac{1}{6} \log \frac{1}{6}\right)=1.7918
    $$`
    
- 찌그러진 주사위에서는 특정 값이 더 잘나온다는 정보가 추가된다.
    
    공정한 주사위와 찌그러진 주사위의 교차 엔트로피
    
    `$$
    -\left(\frac{1}{6} \log \frac{1}{2}+\frac{1}{6} \log \frac{1}{10}+\cdots+\frac{1}{6} \log \frac{1}{10}\right)=2.0343
    $$`
    

[https://hyunw.kim/blog/2017/10/26/Cross_Entropy.html](https://hyunw.kim/blog/2017/10/26/Cross_Entropy.html)

### **Binary Cross-Entropy**

`tf.nn.sigmoid_cross_entropy_with_logits( )`

`$$
B C E=-\frac{1}{N} \sum_{i=0}^N y_i \cdot \log \left(\hat{y_i}\right)+\left(1-y_i\right) \cdot \log \left(1-\hat{y_i}\right)
$$`

### **Categorical Cross-Entropy**

`tf.nn.softmax_cross_entropy_with_logits_v2( )`

`$$
C C E=-\frac{1}{N} \sum_{i=0}^N \sum_{j=0}^J y_j \cdot \log \left(\hat{y_j}\right)+\left(1-y_j\right) \cdot \log \left(1-\hat{y_j}\right)
$$`
