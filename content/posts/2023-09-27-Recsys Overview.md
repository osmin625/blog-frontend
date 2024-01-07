---
title: 추천 시스템 개요
date: 2023-09-27-13:53:00 +0900
categories: [DL Algorithm, Recommendation System]
tags: [Recsys, Overview]
math: true
img_path: /assets/post_imgs/
pin: true
---
> Naver BoostCamp AI Tech에서 학습한 내용을 재구성했습니다.  
> 해당 게시글은 지속적으로 업데이트할 예정입니다.  
> 노션에 정리했던 내용을 복습하며 블로그에 조금씩 업로드하고 있습니다.  
{: .prompt-info }

### [추천 시스템](https://osmin625.github.io/posts/%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C/)

### [추천 시스템 평가 패러다임](https://osmin625.github.io/posts/%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C-%ED%8F%89%EA%B0%80-%EC%A7%80%ED%91%9C/)

![recsys](ro.png)
# Rule Base

[인기도 기반 추천](https://osmin625.github.io/posts/%EC%9D%B8%EA%B8%B0%EB%8F%84-%EA%B8%B0%EB%B0%98-%EC%B6%94%EC%B2%9C/)

[연관 분석(Association Analysis)](https://www.notion.so/Association-Analysis-6ca43cfdd8da4ad89cdefa807331c4ff?pvs=21)

# [CBF: Content Based Filtering](https://www.notion.so/CBF-Content-Based-Filtering-ee188eb44e6a4fd38992c8182405128c?pvs=21)

#### 1. Vectorizer — **아이템 특성을 벡터 형태로 어떻게 표현하는가**

- [TF-IDF](https://www.notion.so/TF-IDF-9478a90aa99e44c1820b26b296535223?pvs=21)
    
    [TF-IDF 기반 추천](https://www.notion.so/TF-IDF-0465ef82197b423e92cbd7516e964d7b?pvs=21)
    
- [BM25](https://www.notion.so/BM25-857f76f951ef44e6a8ffa08c022dbbcb?pvs=21)
- [Word2Vec](https://www.notion.so/Word2Vec-c21d23fa76c8478f921fdc392f599f95?pvs=21)

#### 2. Similarity — **특성화된 아이템이 서로 얼마나 비슷한가**

- [Similarity](https://www.notion.so/Similarity-e210820646c04d248e6ca2b5f2db7bae?pvs=21)

- [Distance](https://www.notion.so/Distance-dcb9f23eabba4d25829a6a26a33c892e?pvs=21)

# [CF: Collaborative Filtering(협업 필터링)](https://www.notion.so/CF-Collaborative-Filtering-fd1b3079e33d4bf28c3d6e11a833842e?pvs=21)

- ## [NBCF: Neighborhood-based CF(이웃 기반 협업 필터링)](https://www.notion.so/NBCF-Neighborhood-based-CF-4d0471ef262d4a7da8175e095c9f72a2?pvs=21)
- ## [MBCF: Model based Collaborative Filtering(모델 기반 협업 필터링)](https://www.notion.so/MBCF-Model-based-Collaborative-Filtering-75c21283fe794ad48670abf344ae04b1?pvs=21)
    
    <details markdown="1">
    <summary>Supervised Learning Model</summary>

    **ML based CF**

    - [Naive Bayes Classification](https://www.notion.so/Naive-Bayes-Classification-33b7db10c9314bcf8c7dda33785846e9?pvs=21)
    - [GBM: Gradient Boosting Machine](https://www.notion.so/GBM-Gradient-Boosting-Machine-ad2a50e8de754365ae06f0ac90adcaa1?pvs=21)
    [GBDT: Gradient Boosting Decision Trees](https://www.notion.so/GBDT-Gradient-Boosting-Decision-Trees-082ff2ad256a436f9ce28f7b2181d5ca?pvs=21)
        - [XGBoost: Extreme gradient boosting](https://www.notion.so/XGBoost-Extreme-gradient-boosting-3f2f693c177e430d983f678e2d1e1c74?pvs=21)
        - [LGBM: LightGBM](https://www.notion.so/LGBM-LightGBM-26aed012b6a5416aac0b4650b0155e5e?pvs=21)
        - [CatBoost](https://www.notion.so/CatBoost-474c3b0d5e124ae19aff470924694636?pvs=21)

    **DL based CF**

    <details markdown="1">
    <summary>Background</summary>
    <br>
    
    **DL based CF의 장점**

    1. **Nonlinear Transformation**
        - data의 non-linearity를 효과적으로 나타낼 수 있다.
        - 복잡한 user-item interaction pattern을 효과적으로 모델링
            
            user의 선호도 예측 용이
            
    2. **Representation Learning**
        - 사람이 직접 feature design하지 않아도 된다.
        - 텍스트, 이미지, 오디오 등 다양한 종류의 정보를 추천 시스템에 활용할 수 있다.
            - 과거 아이템의 이미지를 활용하여 새로운 아이템에 대한 특징 추출 가능
            - 사용자가 남긴 텍스트를 활용하여 취향에 대한 특징 추출 가능
            - 새로운 아이템이나 인기 없는 아이템도 추천이 가능
            - 사용자에게 아이템을 왜 추천하는 이유에 대한 설명력이 증가
            - 다양한 맥락 정보를 함께 활용하기 때문에 보다 정교한 추천이 가능
    3. **Sequence Modeling**
        - DNN은 자연어처리, 음성 신호 처리 등 sequential modeling task에서 성공적으로 적용된다.
        - 추천 시스템에서 next-item prediction, session-based recommendation등에 사용된다.
    4. **Various Architectures**
        - CNN, RNN 등 비정형 데이터 특징 추출에 특화된 구조 활용이 가능하다.
    5. **Flexibility**
        - Tensorflow, PyTorch 등 다양한 DL 프레임워크 오픈
        - 추천시스템 모델링 flexibility가 높으며 더 효율적으로 서빙할 수 있다.
        - end-to-end 구조로써 Domain adaptation,Generative modeling등의 응용 모델 활용이 가능하다.

    **단점**

    1. **Interpretability** → Black Box
    2. **Data Requirement** → 많은 양의 데이터 필요
    3. **Extensive Hyperparameter Tuning** → 많은 시간 소요

    추천에서는 DL이 ML을 압도하지는 않는다. 

    추천을 수행할 때 Latency가 중요하기 때문에, 너무 복잡한 모델은 사용하지 못한다.
    </details>    

    [MLP: Multilayer Perceptron(다층 퍼셉트론)](https://www.notion.so/MLP-Multilayer-Perceptron-e33b62a970784be2bcd83dab0b55e220?pvs=21) 계열 모델

    - [NCF: Neural Collaborative Filtering](https://www.notion.so/NCF-Neural-Collaborative-Filtering-7ea11a83950c466a91a46ed5d7b7bab3?pvs=21)
    - [YouTube Recommendation](https://www.notion.so/YouTube-Recommendation-29e3b9ef81784ed6b8b3c29b2b5c7aaa?pvs=21)

    [AE: Autoencoder(**오토인코더)**](https://www.notion.so/AE-Autoencoder-994ae0144c034d249cf5da6e7f618c1a?pvs=21) 계열 모델

    입력값 (rating)을 reconstruction (decoding) 할 수 있게끔 학습함으로써 rating이 가지고 있는 잠재적인 패턴이 latent factor(information bottleneck)에 암호화 (encoding)된다.

    ![recsys](ro1.png)

    [DAE: Denoising Autoencoder](https://www.notion.so/DAE-Denoising-Autoencoder-d6800d81dced436b8b00911996978dd2?pvs=21)

    - [U/I-RBM](https://www.notion.so/U-I-RBM-1d121b28c9f74d0a90046b3188b17044?pvs=21)
    - [AutoRec](https://www.notion.so/AutoRec-dd00ba485fd244b783ced96109ae916f?pvs=21)
    - [NeuMF: Neural MF](https://www.notion.so/NeuMF-Neural-MF-4a9f4d36220b49f0afea9f298a4a3807?pvs=21)
    - [CDAE: Collaborative Denoising Auto-Encoder](https://www.notion.so/CDAE-Collaborative-Denoising-Auto-Encoder-ba86511b225748d1ae1ed298d828266c?pvs=21)

    [GNN: Graph Neural Network](https://www.notion.so/GNN-Graph-Neural-Network-3187fc20130b45f189ec91ee55e85480?pvs=21) 계열 모델

    [GCN: Graph Convolution Network](https://www.notion.so/GCN-Graph-Convolution-Network-e9a3a153c8f747d89b6f7cda4f39311c?pvs=21)

    - [NGCF: Neural Graph Collaborative Filtering](https://www.notion.so/NGCF-Neural-Graph-Collaborative-Filtering-c7298066e8b3423f8fb430305cdb2696?pvs=21)
    - [LightGCN](https://www.notion.so/LightGCN-96a9cf2cf19c452586b432fb01e1563e?pvs=21)

    [CNN: Convolutional Neural Network(컨볼루션 신경망)](https://www.notion.so/CNN-Convolutional-Neural-Network-5fe961c5ba07444688035a28c4925a4b?pvs=21) 계열 모델

    - [Image-Based Recommendations](https://www.notion.so/Image-Based-Recommendations-7ab89ac403d54c738d9be9afab18dbce?pvs=21)
    - [VBPR: Visual BPR](https://www.notion.so/VBPR-Visual-BPR-7142388f354b44b6978c6916f1f94946?pvs=21)
    - [DeepCoNN(심층 협력 신경망)](https://www.notion.so/DeepCoNN-c627c7b226814600b73b211d8a5f5829?pvs=21)

    [RNN:Recurrent Neural Network(순환신경망)](https://www.notion.so/RNN-Recurrent-Neural-Network-a3cbd14760f6406b9d926e1062365982?pvs=21) 계열 모델

    [LSTM(Long Short Term Memory)](https://www.notion.so/LSTM-Long-Short-Term-Memory-ce7b82de1e554356875ddda3aa02dc91?pvs=21), [GRU(Gated Recurrent Unit)](https://www.notion.so/GRU-Gated-Recurrent-Unit-e9fb943fdd2b48b5a99047b7bc3084da?pvs=21)

    - [GRU4Rec](https://www.notion.so/GRU4Rec-7e0959bd25ae4fc79b148bb86544bf00?pvs=21)
    - [RRN: Recurrent Recommender Network](https://www.notion.so/RRN-Recurrent-Recommender-Network-af2ab646a37f4f9580e783231ad33f75?pvs=21)
    - [WDN: Wide & Deep Network](https://www.notion.so/WDN-Wide-Deep-Network-7e6a7cd23fd444f5a4bc3db8fbdf9b96?pvs=21)
    - [DeepFM](https://www.notion.so/DeepFM-964f67dd360b4c1f88c4a0bd0698f0e5?pvs=21)
    - [DIN: Deep Interest Network](https://www.notion.so/DIN-Deep-Interest-Network-7f7dab7f46074f5481e9cabc4f04eca7?pvs=21)
    - DCN: Deep & Cross Network
    - [BST: Behavior Sequence Transformer](https://www.notion.so/BST-Behavior-Sequence-Transformer-9b06a51043dd4d15bc565b8ef52eb7a2?pvs=21)
    - [TabNet](https://www.notion.so/TabNet-1e5c27561c974f6e80af1989a106cfde?pvs=21)
    </details>

    <details markdown='1'>
    <summary>Unsupervised Learning Model</summary>
    <br>
    <details markdown="1">
    <summary>Background : User-free Model</summary>

    <br>
    비지도학습 모델들 중, User-free 모델로 활용되는 경우가 많다.

    **User-free 모델의 장점 ($=\gamma_u$를 사용하지 않을 때의 장점)**

    1. **새로운 사용자에 대해 inference가 가능하다.**
        
        $\gamma_u$는 새로운 사용자가 발생할 때마다 재학습을 필요로 한다.
        
    2. **이력이 거의 없는 사용자에 대한 대응이 가능하다.**
        
        MF 계열의 모델은 이런 상황에서 $\gamma_u$가 제대로 학습되지 않으므로 성능이 좋지 않다.
        
    3. **CF 모델에서 종종 무시되곤 하는 sequential 시나리오에 대해 대응이 가능하다.**
        
        MF의 $\gamma_u$는 sequence를 고려하지 않는다.
        
    - 실제 추천 시스템의 deployment를 고려하면, 새로운 사용자가 발생할 때마다 재학습이 필요한 점은 큰 단점이다.
    - 따라서, user-free 모델은 전통적인 MF 계열의 모델보다 실용적이라고 볼 수 있다.
    </details>

    [**Latent Factor Model(Embedding)**](https://www.notion.so/Latent-Factor-Model-Embedding-7e8eb7413b9e45ceb5ed2a16151c12c0?pvs=21)

    - [SVD: Singular Value Decomposition(특이값 분해)](https://www.notion.so/SVD-Singular-Value-Decomposition-2bc5621a4b8b423587cce5c72387332a?pvs=21)
    - [MF: Matrix Factorization](https://www.notion.so/MF-Matrix-Factorization-e4a47b3afa0c4159ab9ad24920f2f6a5?pvs=21)
        - [WRMF: Weighted Regularized MF (MF for Implicit Feedback)](https://www.notion.so/WRMF-Weighted-Regularized-MF-MF-for-Implicit-Feedback-0fedc650822c476da6d348dbc97a47a7?pvs=21)
        - [ALS: Alternating Least Square](https://www.notion.so/ALS-Alternating-Least-Square-f7558a78197f4f1c8657aeaf6e5a29fd?pvs=21)
        - [BPR: Bayesian Personalized Ranking](https://www.notion.so/BPR-Bayesian-Personalized-Ranking-19396cb2510e4bdb935c62fb7e29d87e?pvs=21)

        [Feedback](https://www.notion.so/Feedback-bc67a3ec8d14494f84ff96524491fbee?pvs=21)

        - [Word2Vec](https://www.notion.so/Word2Vec-c21d23fa76c8478f921fdc392f599f95?pvs=21)
            - [**CBOW: Continous Bag of Word**](https://www.notion.so/CBOW-Continous-Bag-of-Word-d8b1a8e79e294cdb91f0edd1dccb9ac4?pvs=21)
            - [**SG: Skip-Gram**](https://www.notion.so/SG-Skip-Gram-0efdda659ed345f299b0ee4b0ded2c26?pvs=21)
            - [**SGNS: Skip-Gram with Negative Sampling**](https://www.notion.so/SGNS-Skip-Gram-with-Negative-Sampling-e3a03df0c93d493a8a266043d4ac3b76?pvs=21)
        - [Item2Vec](https://www.notion.so/Item2Vec-9ce90b51bfce4be49bf049f7a4c1e962?pvs=21)

    [Clustering(군집화)](https://www.notion.so/Clustering-18087dfdaaec466086fcff5a1808aa86?pvs=21)

    - [KNN: K-Nearest Neighbor(K-최근접 이웃)](https://www.notion.so/KNN-K-Nearest-Neighbor-K-e3a1dcf5f76c4c33b8f12432a11c466d?pvs=21)
    - [ANN: Approximate Nearest Neighbor](https://www.notion.so/ANN-Approximate-Nearest-Neighbor-9a41dc0e2de54f7ab83ee8f990f5c086?pvs=21)
        - [ANNOY: Approximate Nearest Neighbor Oh Yeah](https://www.notion.so/ANNOY-Approximate-Nearest-Neighbor-Oh-Yeah-f6e0897863d048ecb2db4843bb337755?pvs=21)
        - [**HNSW: Hierarchical Navigable Small World Graphs**](https://www.notion.so/HNSW-Hierarchical-Navigable-Small-World-Graphs-c52ea0f832e84eae9392120f7a05ae99?pvs=21)
        - [IVF: Inverted File Index](https://www.notion.so/IVF-Inverted-File-Index-c382c3cb19634e7cb7e2af6d445cf686?pvs=21)
        - [PQ: Product Quantization — Compression](https://www.notion.so/PQ-Product-Quantization-Compression-cea6b89b3ff14201bbaa75536a6840b3?pvs=21)

        **Clustering의 경우 다른 추천 방법론과 함께 사용하여 효과적인 추천 수행이 가능하다.**

        - 군집내의 다른 사용자가 선호하는 아이템 추천
        - 군집화 이후 협력 필터링(Collaborative Filtering) 사용을 통해 예측 정확도 향상
        - 비슷한 사용자 군집의 데이터를 추출하여 아이템 선호도를 계산하고, 이를 사전 확률(prior probability)로 활용하여 베이지안 방법론 적용
    </details>

## RL(강화 학습)

### [MAB: Multi-Armed Bandit](https://www.notion.so/MAB-Multi-Armed-Bandit-b00d09a3729c4f64a8c360f2c922f7a7?pvs=21)

# [**Hybrid CF**](https://www.notion.so/Hybrid-CF-103266a4a91643e58bf6f565b7b627ca?pvs=21)

## [**CARS: Context-aware Recommender System(맥락 기반 추천 시스템)**](https://www.notion.so/CARS-Context-aware-Recommender-System-28277faab5fc4fbf843f2e5108981179?pvs=21)

- [FM: Factorization Machine](https://www.notion.so/FM-Factorization-Machine-3b520957d16d4f5caa4a8dd648043692?pvs=21)
- [FFM: Field-aware Factorization Machine](https://www.notion.so/FFM-Field-aware-Factorization-Machine-c6a926483b534648b9f699b0749e575b?pvs=21)

# 추천 라이브러리

- **Surprise**
- **Implicit**
- **Lightfm**
- **MSrecommenders**
- Spotlight
- Buffalo
- Torchrec
- TFrecommenders