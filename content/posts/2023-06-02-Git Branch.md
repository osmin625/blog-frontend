---
title: Git Branch는 무엇이고, 무엇을 위해 사용하는가?
date: 2022-10-09-07:49:00 +0900
categories: [Project Management,Git]
tags: [Git, Branch, Merge]
---

**독립적으로 특정 작업을 진행할 때 사용**한다.

팀으로 여러작업을 동시에 작업할 수 있다.

여러 Branch를 합치는 방법 — Merge

## merge
**branch의 모든 기록 보존, merge에 대한 기록 추가.**  

- 이 방법을 사용하면 merge에 대한 commit이 하나 생성되고 어느 시점에 merge를 진행했는지 쉽게 알 수 있다.
- branch가 늘어나고 여러 번의 merge가 생기게 되면, 그래프가 복잡해져 **커밋 히스토리(Commit History)**를 파악하기 더욱 어려워질 수 있다.

## squash and merge

 **여러 commit 기록 하나로 합치기, merge기록 남기지 않기.**  

 지저분한 커밋 이력들을 삭제하면서 master branch로 합칠 때 사용한다.

- merge할 때 여러 commit들을 하나로 합친다.    
    Squash를 하게 되면 모든 커밋 이력이 하나의 커밋으로 합쳐지며 **사라진다.**        
- merge에 대한 이력은 남기지 않는다.

## rebase and merge

**여러 commit 기록 남기기, merge 기록 남기지 않기.**  

기존의 커밋 이력을 유지하면서도, 깔끔하게 하나의 흐름으로 관리하고자 할 때 사용한다.

- **일반적으로 가장 많이 사용된다.**
- merge에 대한 이력이 남지 않는다.
    
    즉, 언제 merge가 됐는지 알 수 없다.
    
    만약 merge 시점에 대한 기록이 필요하다면 커밋으로 직접 명시해주면 된다.
    
- 모든 커밋이력들이 rebase 되어서 추가된다. 즉, fast-forward 된다.
    
    Rebase를 하면 커밋들의 Base가 변경되므로 Commit Hash 또한 변경 될 수 있다. 
    
    이로 인해 Force Push가 필요한 경우가 발생한다.
 
---
<details>
<summary>
내가 branch를 분기한 이후, 기존의 branch가 수정된 경우
</summary>

1. 내 branch에 기존 branch를 pull해서 conflict 해결하기.<br>

- 내가 작성한 커밋을 절대 변경하고 싶지 않은 경우<br>
- 내가 작성한 커밋 기록은 유지한채, Merge라는 기능을 통해 합쳐졌다라는 기록을 같이 남기게 된다.  <br>

2. merge할 때 rebase and merge하기. ← 더 나은 방법.

</details>

### Conflict가 발생한다면?

마지막으로 push 하는 사람이 해결해야 한다.

1. 마지막에 push하는 사람은 conflict 에러가 발생한다.
2. git status로 충돌 위치 확인하기
3. A와 B가 협의 후 수정하기

    CVN의 해결방법과 유사하다.
    

## 원격 브랜치 가져오기

- **`git remote update` 원격 저장소 갱신**
    
    가끔 갱신을 하지 않으면 push하고자 하는 원격 branch를 찾을 수 없다는 오류를 보게된다.
    
    해당 오류를 처음 만나면 *분명 branch있는데 왜 없어!* 하게 된다.
    
- **`git branch -r` 원격 저장소 branch 리스트 확인**
- **`git branch -d dev` 로컬 저장소 branch 제거하기**
- **`git checkout -t origin/dev` 원격 저장소 branch 가져오기**
    
    `-t`: 원격 저장소의 branch 이름과 동일한 로컬 branch를 생성
    
    `-f`: 문제가 발생하더라도 강제로 진행한다.
    

## branch 합치기, 병합하기

1. **`git checkout -b issue1` branch 생성하고 변경하기**
    - 위 명령어는 아래의 두 가지 명령어를 한 번에 수행한 것이다.
        1. `git branch issue1 main` main branch로부터 issue1 branch 생성하기
        2. `git checkout issue1` main branch에서 issue1 branch로 변경하기
    
    **— 코드 추가 작업 수행 —**
    
2. **`git checkout master` (작업이 완료되고 난 후) `master` 브랜치로 이동하기**
3. **`git merge issue1` issue1을 master에 merge (병합)하기**

## Branch 전략 — Flows

가장 최신 커밋이 어디에 존재하느냐에 따라 두 가지 방법으로 나뉜다.

- **Local 중심 — Git Flow**
- **Remote 중심 — Github Flow**