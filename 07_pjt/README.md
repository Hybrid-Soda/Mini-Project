# Finance & Movie

### 학습한 내용
- serializer 사용: DepositProducts와 DepositOptions 모델을 이용하여 데이터베이스와 상호 작용하고, 이 데이터를 JSON 형식으로 직렬화하여 API 응답으로 전송
- 외부 API 통신: Python의 requests 라이브러리를 사용하여 외부 금융 API에서 데이터를 가져오고, 이를 저장하는 로직을 구현
- RESTful API 메소드 구현: GET과 POST 메소드를 이용해 데이터를 조회하거나 저장하는 엔드포인트를 구현

### 어려웠던 부분
- 에러 핸들링 누락: 외부 API 호출 시, 응답이 성공적이지 않을 경우를 대비한 예외 처리
이로 인해 API 키가 유효하지 않거나 네트워크 문제 등이 발생할 경우, 에러를 적절히 처리하지 못할 수 있다.
- DepositOptions - DepositProducts 외래 키 연결: 올바른 데이터 매핑을 보장하는 로직을 설계하고 구현하는 과정

### 해결 과정
- API 요청 최적화: 외부 API로부터 데이터를 요청하는 부분에서 중복 요청을 제거하고, 필요한 데이터만 요청하도록 수정
- 예외 처리 추가: requests 호출에 대한 예외 처리를 추가하여, API 호출 과정에서 발생할 수 있는 문제를 핸들링
- 데이터 무결성 보장: get_object_or_404 함수를 사용하여 DepositProducts 테이블에서 해당 상품 코드를 가진 객체를 찾고, 이 객체를 DepositOptions의 외래 키로 설정

### 기억하면 좋을 것들
- REST API 설계 원칙: API를 설계할 때는 REST 원칙을 따르는 것이 중요하며, 이를 통해 유지보수가 쉽고 확장 가능한 애플리케이션을 구축할 수 있다.
- 예외 처리의 중요성: 외부 API를 사용할 때는 항상 예외 처리를 적극적으로 구현해야 하며, 이는 시스템의 안정성 보장
- 코드의 재사용과 최적화: 코드를 작성할 때는 중복을 최소화, 가능한 한 효율적으로 작성하는 것이 중요하다.
이를 통해 코드의 가독성과 성능을 동시에 개선할 수 있다.