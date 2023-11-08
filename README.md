# -illuminarean

## Test Automation Engineer (QA) 사전 과제
---
#### ＜수행과제＞
다음 조건을 만족시키는 자동화 코드를 작성해주세요.
- 이동경로 : 일루미나리안 사이트 ＞ [Work] ＞ [GOODVIBE WORKS 바로가기] ＞ [무료체험신청] ＞ 내용 입력 ＞ 신청 취소
- 담당 업무 리스트에서 클릭으로 1개, 검색으로 1개 선택해주세요.
- 그 외 내용은 자유롭게 채워 넣어주세요.
- 무료 이용 신청 버튼은 클릭하지 않으셔도 됩니다.
---
#### 실행 환경
1. Python 3.12 설치
2. Python 실행 환경을 virtualenv로 격리
3. Selenium 4.15.2 설치
4. main.py 실행
---
#### 테스트 실행 방법에 대한 설명
```
$ python -m pip install --user -U virtualenv
$ python -m virtualenv venv
$ python -m pip install --upgrade pip
$ python -m pip install --use-deprecated=legacy-resolver -r requirements.txt
```
---
#### 추후 개선/해결해야 하는 부분들에 대한 설명
1. data driven test를 수행해야 할 경우 인수들을 yaml 파일로 정리하고 호출할 수 있도록 개선
2. [무료체험신청] 부분이 중복 테스트라면 진입정도만 확인하고 상세 내용은 한번만 확인하는 것으로 개선
3. playwright와 같은 cross-browsing framework로 테스트 전환
