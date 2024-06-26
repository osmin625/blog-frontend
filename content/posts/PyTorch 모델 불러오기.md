---
title: PyTorch 모델 저장하고 불러오기
date: 2023-03-13T9:58:00+09:00
categories: [Framework & Library, PyTorch]
tags: [PyTorch, save]
# math: true
# img_path: /imgs/
# image:lqip: image_filename
type: post
---

### model.save()

학습의 결과를 저장하기 위한 함수

모델 형태(architecture)와 파라미터를 저장

모델 학습 중간 과정의 저장을 통해 최선의 결과 모델을 선택

만들어진 모델을 외부 연구자와 공유하여 학습 재연성 향상

```python
# Print model's state_dict
print("Model's state_dict:") # state dict: 모델의 파라미터를 표시
for param_tensor in model.state_dict():
		print(param_tensor, "\t", model.state_dict()[param_tensor].size())

## 방법 1.
# 모델의 파라미터만 저장하기
**torch.save**(model.**state_dict()**, os.path.join(MODEL_PATH, "model.pt")) 
# 모델은.pt 파일로 저장한다.
# dict type으로 저장된다.

new_model = TheModelClass()
# 모델의 Architecture가 동일한 경우 파라미터만 저장하고 불러온다.
new_model.**load_state_dict**(torch.load(os.path.join(MODEL_PATH, "model.pt")))

## 방법 2.
# 모델의 architecture와 함께 저장한다.
torch.**save**(model, os.path.join(MODEL_PATH, "model.pt"))
model = torch.**load**(os.path.join(MODEL_PATH, "model.pt"))
# 모델의 architecture와 함께 load한다.
# 사실 모델 자체를 공유하는 경우 코드로 공유하는 방법이 있기 때문에,
# 일반적으로 위의 방식이 더 많이 쓰인다.
```

### checkpoints

학습의 중간 결과를 저장하여 최선의 결과를 선택

earlystopping 기법 사용시 이전 학습의 결과물을 저장한다.

loss와 metric 값을 지속적으로 확인 저장

일반적으로, epoch, loss, metric을 함께 저장하여 확인한다.

colab에서 지속적인 학습을 위해서는 반드시 필요하다.

```python
torch.save({ # 모델의 정보는 epoch와 함께 저장
				'epoch': e,
				'model_state_dict': model.state_dict(),
				'optimizer_state_dict': optimizer.state_dict(),
				'loss': epoch_loss,
				},
f"saved/checkpoint_model_{e}*{epoch_loss/len(dataloader)}*{epoch_acc/len(dataloader)}.pt")

checkpoint = torch.load(PATH)
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
loss = checkpoint['loss']
```

### Pretrained Learning

[Transfer Learning](https://www.notion.so/Transfer-Learning-3424e634f0c34d46bd0b17378f7251b9?pvs=21) 

- [Computer Vision 모델 레포지토리](https://github.com/rwightman/pytorch-image-models)
- [Segmentation 모델 레포지토리](https://github.com/qubvel/segmentation_models.pytorch)
- [Transfer Learning vs Fine-tuning 관련 내용](https://heeya-stupidbutstudying.tistory.com/entry/DL-Transfer-Learning-vs-Fine-tuning-%EA%B7%B8%EB%A6%AC%EA%B3%A0-Pre-training)
- [Andrew Ng 교수님의 Transfer Learning 영문강의 (YouTube)](https://www.youtube.com/watch?v=yofjFQddwHE)
