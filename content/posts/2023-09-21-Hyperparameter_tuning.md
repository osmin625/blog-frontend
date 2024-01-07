---
title: 모델의 성능이 더이상 오르지 않을 때 (Hyper-Parameter Tuning)
date: 2023-03-13-09:58:00 +0900
categories: [AI Knowledge, Hyperparameter]
tags: [Hyperparameter Tuning]
math: true
img_path: /assets/post_imgs/
---

**하이퍼 파라미터**

모델 스스로 학습하지 않는 값.

사람이 직접 지정해주어야 한다.

### 결과를 개선하고 싶을 때

1. 모델을 바꾸기
    
    중요하지만, 이미 높은 성능의 모델이 공개되어있기 때문에 상대적으로 덜 중요.
    
2. **데이터를 바꾸기 →** 성능 개선을 위해 가장 중요하다.
3. 하이퍼 파라미터 Tuning
    
    약간의 성능 개선이 간절한 경우 수행한다.
    
    마지막 0.01의 성능 개선이라도 필요한 경우 사용한다.
    
4. generalization 등 적용

### Hyperparameter Tuning

가장 기본적인 방법 - grid vs random

- grid
    
    적절한 하이퍼파라미터를 찾을 때, 값들을 일정한 범위를 정해 선택하는 것.
    
- random
    
    값을 랜덤하게 찾아서 가장 성능이 잘나오는 것을 선택한다.
    
![hyperparameter](hyperparameter_tuning.png)

요즘에는 잘 쓰이지 않고, 베이지안 기반 기법이 많이 쓰인다.

### Ray

multi-node multi processing 지원 모듈

ML/DL의 병렬 처리를 위해 개발된 모듈

기본적으로 현재의 분산병렬 ML/DL 모듈의 표준

Hyperparameter Search를 위한 다양한 모듈 제공

![hyperparameter](hyperparameter_tuning1.png)

```python
data_dir = os.path.abspath("./data")
load_data(data_dir)
# search space 지정
config = {
		"l1": tune.sample_from(lambda _: 2 ** np.random.randint(2, 9)),
		"l2": tune.sample_from(lambda _: 2 ** np.random.randint(2, 9)),
		"lr": tune.loguniform(1e-4, 1e-1),
		"batch_size": tune.choice([2, 4, 8, 16])
}

# 학습 스케줄링 알고리즘 지정
scheduler = ASHAScheduler(
		# ASHAS : 실행 도중 낮은 loss를 가지는 metric들을 버리는 알고리즘
		metric="loss", mode="min", max_t=max_num_epochs, grace_period=1, reduction_factor=2)

# 결과 출력 양식 지정
reporter = CLIReporter(
		metric_columns=["loss", "accuracy", "training_iteration"])

# 병렬 처리 양식으로 학습 시행
result = tune.run(
		partial(train_cifar, data_dir=data_dir),
		resources_per_trial={"cpu": 2, "gpu": gpus_per_trial},
		config=config, num_samples=num_samples,
		scheduler=scheduler,
		progress_reporter=reporter)
```

```python
data_dir = os.path.abspath("./data")
    load_data(data_dir)
    config = {
        "l1": tune.sample_from(lambda _: 2 ** np.random.randint(2, 9)),
        "l2": tune.sample_from(lambda _: 2 ** np.random.randint(2, 9)),
        "lr": tune.loguniform(1e-4, 1e-1),
        "batch_size": tune.choice([2, 4, 8, 16])
    }

    scheduler = ASHAScheduler(
        metric="loss",
        mode="min",
        max_t=max_num_epochs,
        grace_period=1,
        reduction_factor=2)
    

    reporter = CLIReporter(
        # parameter_columns=["l1", "l2", "lr", "batch_size"],
        metric_columns=["loss", "accuracy", "training_iteration"])
    

    result = tune.run(
        partial(train_cifar, data_dir=data_dir),
        resources_per_trial={"cpu": 2, "gpu": gpus_per_trial},
        config=config,
        num_samples=num_samples,
        scheduler=scheduler,
        progress_reporter=reporter)
```

---

1. 모델의 모든 layer에서 learning rate가 항상 같아야 할까?
2. 하이퍼 파라미터 탐색의 우선순위 어떻게 될까?
- [Pytorch와 Ray 같이 사용하기](https://pytorch.org/tutorials/beginner/hyperparameter_tuning_tutorial.html)