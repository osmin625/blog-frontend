---
title: Alexnet 모델의 파라미터 수 계산
categories: [AI, Model]
date: 2023-01-13T15:15:00+09:00
tags: ['CV', 'Convolution Neural Network', 'Alex-Net']
type: post
---
![Alex-net](/imgs/Alex_struc.png)

### **Conv Layer**

**Layer 1 파라미터 수 = 11 * 11 * 3 * 48 * 2 ⇒ 35k**

- 입력 : 224 * 224 * 3
- filter : 11 * 11 * (3)
    
    3은 생략되어 있지만, 입력 크기와 동일한 채널을 가질 것이기 때문에 3으로 유추할 수 있다.
    
- 모델 이미지상 커널이 위 아래로 두 개이기 때문에 * 2를 했다.
    
    gpu 메모리 용량 등의 이유로 이처럼 구성하는 경우가 많다.
    

 **Layer 2 파라미터 수 = 5 * 5 * 48 * 128 * 2 ⇒ 307k**

 **Layer 3 파라미터 수 = 3 * 3 * 128 * 2 * 192 * 2 ⇒ 663k**

 **Layer 4 파라미터 수 = 3 * 3 * 192 * 128 * 2 ⇒ 884k**

**Layer 5 파라미터 수 = 3 * 3 * 192 * 128 * 2 ⇒ 442k**

### **Dense Layer**

**Layer 6 파라미터 수 = 13 * 13 * 128 * 2 * 2048 * 2 ⇒ 117M**

**Layer 7 파라미터 수 = 2048 * 2 * 2048 * 2 ⇒ 16M**

**Layer 8 파라미터 수 = 2048 * 2 * 1000 ⇒ 4M**

Dense Layer의 파라미터가 Conv Layer의 파라미터 수에 비해 월등히 많은 것을 볼 수 있다.

성능을 올리기 위해선 파라미터를 줄여야 한다.

따라서, 네트워크가 발전됨에 따라 뒷부분의 Fully Connected Layer을 최대한 줄이고, 앞의 Conv Layer을 깊게 쌓게 된다.