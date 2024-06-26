---
title: 'SG: Skip-Gram'
date: 2023-03-31T06:05:00+09:00
categories: [AI, Algorithm & Concept]
tags: [Natural Language Processing, Word2Vec, Skip-Gram, Multi Classification]
type: post
---
- Word2Vec을 학습하는 방법 중 하나.
- **CBOW가 뒤집어진 모델**

    CBOW와 입력층과 출력층이 반대로 구성되어 있다.
    
    ![SG](/imgs/SG-2.png)
    

- 벡터의 평균을 구하는 과정이 없다.

- CBOW보다 성능이 좋다고 알려져있다.

    참고로 이 때의 성능은 학습 과정의 Loss가 아니라 임베딩 벡터의 표현력을 의미한다.

- CBOW와 마찬가지로 Multi-Classification Model에 해당한다.  
    
    ![SG](/imgs/SG-1.png)