# 반응형 포트폴리오 웹사이트 구현 & 반응형 웹 페이지 구현

## 학습한 내용
- HTML, CSS, Bootstrap 사용 반복 숙달

## 어려웠던 부분
- 영화 사진을 삽입할 때 반복문을 사용하여 넣을 수 없었다
- 사진 위에 글자를 넣을 때 화면 크기를 변경하면 글씨가 마음대로 움직인다

## 해결 과정
- 반복문 없이 코드 반복으로 삽입
- 글자 크기를 %로 변경했더니 상위 콘텐츠에 귀속되어 그림속에 잘 유지되었다

## 기억하면 좋을 것들
- `row-cols-` : 한 줄에 보여질 컨텐츠

- Grid system breakpoints
  - xs (< 576px)
  - sm (≥ 576px)
  - md (≥ 768px)
  - lg (≥ 992px)
  - xl (≥ 1200px)
  - xxl (≥ 1400px)

- media query
  ```
  $media (min-width: 1200px) {
    div {
      width: 992px
    }
  }
  ```

- gutter : `g-4`