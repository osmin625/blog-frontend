---
title: '1 x 1 Convolution'
categories: ['DL Algorithm','Computer Vision']
date: 2023-01-13 15:39:00 +0900
tags: ['Convolution Neural Network', 'Bottle-neck']
---

차원 축소를 위해 활용한다.

이미지에서 단 하나의 픽셀만 보기 때문에, 이미지에서 영역을 살펴보는 의미는 없다.

**다만, 1 * 1 Convolution을 이용하여 기존 Spatial Dimension을 그대로 유지한 채, 채널의 개수를 128개에서 32개로 줄인다.** 

![1x1 Conv_1](/assets/post_imgs/1x1 Conv_1.png)

이를 통해 NN의 층을 더 깊게 쌓으면서도, 채널의 수를 줄여서 파라미터의 수를 줄일 수 있다.

- 1 * 1 Convolution을 사용하지 않는 경우
    
    ![1x1 Conv_2](/assets/post_imgs/1x1 Conv_2.png)
    
- 1 * 1 Convolution을 사용한 경우
    
    ![1x1 Conv_3](/assets/post_imgs/1x1 Conv_3.png)
    

파라미터 수를 147,456개에서 40,960개로 효과적으로 줄일 수 있다.

대표적인 예로 **Bottleneck architecture 구조**가 1 * 1 Convolution을 이용한다.

[1x1 convolution의 의미 = 차원 축소, 그리고 bottleneck (컨볼루션과 보틀넥)](https://lv99.tistory.com/21)