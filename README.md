# CO Love House 프로젝트♡
#### ■ 팀명 : 속세를 떠나고 싶다
#### ■ 프로젝트 기간
 - 1차 : 2023.01.08 - 2024.01.17
### 구성원
---
|이름|역할|
|--|--|
|장영지|PM, 프론트엔드, 백엔드|
|김유진|웹 스크래핑|
|공명윤|프론트엔드, 백엔드|
#### ■ 사이트 : [CO Love House](http://192.168.10.245:8000/)
#### ■ 프로젝트 소개
   1. 1~2인 가구를 위한 주거 공간을 빠르게 검색하기 위한 코리빙하우스 플랫폼
   2. 투어하기 예약 및 이용자들의 후기 확인
   3. 커뮤니티에서 글쓰기, 검색, 삭제 기능
   4. 관리자 - 회원관리, 매물관리


### 웹 스크래핑 대상
---
- [디어스 판교](https://dears.kr/ko)
- [디어스 명동](https://www.dearsmd.com/)
- [맹그로브](https://mangrove.city/)
- [하품](https://www.hapoom.co/)
- [커먼시티](https://www.commontown.co/ko)
- [에피소드](https://www.epsd.co.kr/ep369/)


### 사용 collection
---
|컬렉션|각 key값|
|--|--|
|ROOM_DATA|room_brand, room_local, room_image, room_image_two, room_title, room_type, room_any, room_size, room_layout, room_option, room_default_option, room_note|
|ENTER_ROOM_DATA|address, dong_address, ho_adress, price|
|USER_DATA|name, email, password, phonenumber|
|ENTER_USER_DATA|name, email, password, phonenumber, enter_number|
|NOTICE_DATA|notice_title, notice_text|
|REVIEW_DATA|review_title, review_content, review_image|


## 프로젝트 진행
---
- [Naming Rule](https://docs.google.com/spreadsheets/d/1pgseXMtVbRS0Qu6j2i6_T3EC-cICqrJl/edit#gid=1553145129) [image](images/naming_rules.png)
- [Program List](https://docs.google.com/spreadsheets/d/177dosTpc5QXqKI9N2E94pvYRHJ3T5lHF/edit#gid=389956398)
- [Screen Definition](https://app.diagrams.net/#G13JhyVSufPlX4SV4WNJss9p5QtiRxywyE)
- [의뢰서](https://docs.google.com/presentation/d/1jXnKIb6BObgcawwsQxdnuJaKzaEq_aynAtOu1oHNn7U/edit#slide=id.p1)
- [DB구성](images/main.png) ![ERD](https://github.com/btg1631/project_coliving/blob/main/images/main.png)
- [요구사항 정의서](https://docs.google.com/spreadsheets/d/1PaTjeLzbWQcow_RhyxXIo4exBDXDtT7A/edit#gid=1623924950)
![image](https://github.com/btg1631/project_coliving/blob/main/images/%ED%99%94%EB%A9%B4%EC%A0%95%EC%9D%98%EC%84%9C.png)
#### ■ 팀원별 구현 기능
![image](https://github.com/btg1631/project_coliving/blob/main/images/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%EB%A6%AC%EC%8A%A4%ED%8A%B8(%EC%97%85%EB%AC%B4%EB%82%B4%EC%97%AD).png)
### 🎥 [구현 영상](https://www.youtube.com/watch?v=DL7DeUd5Dhg)
![구현영상 첫화면](https://github.com/btg1631/project_coliving/blob/main/images/%EA%B5%AC%ED%98%84%EC%98%81%EC%83%81.png)
#### ■ 주요 기능
**<사용자>**
- 회원가입 → 로그인 → 방 검색 → 투어하기 또는 예약 → 마이페이지 → 예약 조회 및 수정, 삭제
- 마이페이지(회원 기본정보 확인 및 수정)
- 커뮤니티 글 쓰기, 삭제

**<기업회원>**
- 마이페이지, 매물등록 및 관리

```

```