---
title: 나를 위한 Git Flow 총정리
date: 2022-09-28T11:41:00+09:00
categories: [Tools, Project Management]
tags: [Git, Git Branch, Git Flow, Github]
type: post
---
**Local Repository 중심 Branch 관리 방법론**

기능이나 프로그램이 아닌, 개발자간의 약속

물론 이를 지원하는 모듈이 존재한다.

```bash
$ apt-get install git-flow
```

**장점**

- 신중하다.

**단점**

- 복잡하다.
- 배포할 때 거쳐야 할 단계가 많다.
    - 단계별로 관리하는 사람이 다른 경우, 특정 지점에서 병목이 발생할 수 있다.

총 5가지의 branch를 사용해서 개발이 진행된다.

1. **master**
    
    배포의 기준이 되는 branch.
    
    Release Tag를 기록하는 branch.
    
    제품을 배포하는 용도.
    
    배포용 브랜치이므로 개발자가 해당 브랜치에 직접 커밋하거나, Release 이외의 branch에서 직접 Merge할 일이 없다.
    
    - 예외적으로 hotfix 브랜치의 경우 main 브랜치에 직접 merge할 수 있다.
2. **hotfix**
    
    master 브랜치로 배포를 했는데 버그가 생겼을 때 main branch를 긴급 수정하는 branch.
    
3. **release**
    
    배포를 위해 master 브랜치로 보내기 전에 먼저 QA(품질검사)를 하기위한 branch
    
4. **develop**
    
    주로 개발이 이루어지는 브랜치
    
    develop branch를 기준으로 여러 개발자들이 각자 작업한 기능들 merge 수행
    
    하지만 많은 개발자가 동시에 develop 브랜치에서 작업을 한다면 자주 conflict가 발생할 수 있기 때문에, 실제로는 develop branch에도 직접 commit하는 일은 드물다.
    
5. **feature**
    
    단위 기능을 개발하는 branch.
    
    - Issue에 등록된 기능을 구현, Bugfix, Refactoring 등을 develop 브랜치로부터 각각 feature 브랜치를 만들어 작업을 수행
    
     기능 개발이 완료되면 develop 브랜치로 병합한다.
    
    `git flow feature start opencv`
    
    `feature/opencv` branch를 생성하는 것과 동일하다.
    
    - prefix
        - feat
        - refactor
        - fix
        - docs
        
        등을 붙인다.
        
        update readme 등의 커밋 기록을 10줄씩 남기지 말자!
        
    
    issue 하나가 feature branch 하나를 담당하는 것이 편하다.
    

## process

1. 동일한 브랜치인 master, develop 생성
    
    `git flow start`
    
    개발자들은 develop에서 개발을 진행(보통은 feature에서 개발을 진행)
    
    개발을 진행하다가 회원가입, 장바구니 등의 기능 구현이 필요할 경우 A개발자는 develop 브랜치에서 feature 브랜치를 하나 생성해서 회원가입 기능을 구현하고 B개발자도 develop 브랜치에서 feature 브랜치를 하나 생성해서 장바구니 기능을 구현
    
    완료된 feature 브랜치는 검토를 거쳐 다시 develop 브랜치에 합친다.(Merge)
    
2. 모든 기능이 완료되면 develop 브랜치를 release 브랜치로 만든다.
    
    그리고 QA(품질검사)를 하면서 보완점을 보완하고 버그를 픽스한다.
    
3. 모든 과정이 완료되면 이제 release 브랜치를 master 브랜치와 develop 브랜치로 보낸다.
4. master 브랜치에서 버전추가를 위해 태그를 하나 생성하고 배포한다.
5. 배포를 했는데 미처 발견하지 못한 버그가 있을 경우 hot fix 브랜치를 만들어 긴급 수정 후 태그를 생성하고 바로 수정 배포한다.

Git-flow 진행

react나 bootstrap같이 규모가 있는 개발을 할 경우 브랜치보다는 Fork와 Pull requests를 활용하여 구현한다.

flow Fork는 브랜치와 비슷하지만 프로젝트를 통째로 외부로 복제해서 개발을 하는 방식.

branch처럼 merge를 바로 하는 것이 아니라 PR을 보내면 원 프로젝트 관리자가 검토 후 해당  기능을 추가하는 방식으로 개발이 진행된다.

[Vincent Driessen(git flow 최초 제안자)의 블로그 참조. 보통 Git-flow를 설명할 때 가장 많이 사용되는 설명 이미지](https://t1.daumcdn.net/cfile/tistory/99CD994C5E69CCF223)


---

### Feature Branch 만들기

1. `git branch` 현재 나의 브랜치가 어디에 있는지 확인
2. `git checkout develop` develop 브랜치로 이동
3. `git pull origin develop` 코드를 작성하기전에 수정된 사항을 업데이트
4. `git branch feat/[기능명] develop` develop 브랜치로부터 feature 브랜치 생성
5. 코드 수정

### Feature Branch Commit & Pull Request 수행하기

1. commit 양식에 맞도록 메시지를 작성하기.
    
    커밋 메시지에 #23과 같이 issue 번호를 달게되면 해당 issue에 자동으로 매핑된다.
    
2. `git push origin [feature branch 이름]` 현재 나의 feature branch를 github에 push
3. github 홈페이지에서 pull request 요청
    
    ![https://user-images.githubusercontent.com/75417296/231333244-947fb4b5-cb0c-4afa-974b-40240c600e31.png](https://user-images.githubusercontent.com/75417296/231333244-947fb4b5-cb0c-4afa-974b-40240c600e31.png)
    
    - pull request 작성
        - 제목은 commit 메시지와 동일하게
        - base를 develop branch로 설정
        - 양식에 맞게 내용 작성
        - reviewer 등 설정가능
    - review 작성
    - merge
- merge 후 feature branch 제거merge한 후 하단에 branch 제거 버튼 클릭