# shop_api_django

[JPA 활용편](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8-JPA-%ED%99%9C%EC%9A%A9-1#)을 공부하였다.
[앞선 프로젝트](https://github.com/Joje1283/jpashop/pulls?q=is%3Apr+is%3Aclosed)처럼 장고에서도 개발을 진행해본다.

# 계획
일반적으로 웹 앱 개발 과정은 다음과 같다.
1. 요구사항 분석
2. 도메인과 테이블 설계
3. 아키텍처 구성
4. 핵심 비즈니스 로직 개발
5. 웹 계층 개발

[여러가지 이유](https://tech.junhabaek.net/django%EC%99%80-ddd%EB%8A%94-%ED%95%A8%EA%BB%98%ED%95%A0-%EC%88%98-%EC%97%86%EB%8A%94-%EC%A1%B4%EC%9E%AC%EC%9D%BC%EA%B9%8C-6602cf392c09)로 장고에서는 DDD 적용이 어렵다고 하지만 
도메인 분석 -> 엔티티(모델) 구현 -> 도메인 개발(서비스)을 통해 먼저 백엔드를 탄탄히 하고 이후 웹 계층을 개발하는 순서의 맥락은 가능할 것 같다.

Spring Boot, FastAPI를 공부하며 장고에서도 DDD를 할수 있지 않을까? 비즈니스로직 관리는? 등등 여러 고민을 했다. 
하지만 여러 아티클이나 토론을 볼수록 장고에서는 장고다운 패턴이 성능과 관리 측면에서 가장 안정적일것 같다는 생각이 든다.
특히나 Service.py나 Repository.py를 따로 작성할까도 생각해보았지만 관두기로 했다.
결국은 누구나 다 아는대로 비즈니스 로직은 Model에, Model 리팩토링은 Manager에 하면 될 것 같다.

## 리포지토리 계층은?
아래는 Repository+ORM vs ORM이라는 주제의 레딧의 토론을 보고 정리한 내용이다. ( [참고](https://www.reddit.com/r/django/comments/d0596f/comment/ez8tf4e/?utm_source=share&utm_medium=web2x&context=3)  )
### 정리
- ORM은 Active Recore ORM과 Data Mapper ORM으로 나뉜다.
- 일반적으로 JPA, SQLAlchemy같은 Data Mapper ORM은 Repository계층과 함께 사용되는 경우가 많다.
- Django ORM과 같은 Active Record ORM은 Domain과 Database 스키마간의 긴밀한 결합을 가정하고 설계되었다.
  - 데이터베이스의 세부사항을 도메인에 포함하고 있어서 많은 마법이 일어나고 있다. (이시점에서 모델을 단순한 객체로 보기에는 무리가 있다)
  - 모델 필드가 dirty하면 누군가 필드 값을 변경할 때마다 데이터베이스에 적용되었는지 여부를 알기 힘들다.
  - ORM의 특성에 대해 부단히 연구해야 하지만 빠른 개발을 하는데 유리하다.
- SQLAlchemy와 같은 Data Mapper ORM은 도메인 모델에서 데이터 엑세스 로직을 분리한다.
  - 이 때는 도메인 객체를 단순히 파이썬 객체로 취급할 수 있게 된다.
  - 테스트 작성이 용이하나, 작성해야 하는 코드량이 많다.
### 결론
- Django ORM은 근본적으로 데이터베이스 엑세스 로직이 합쳐져 있다. 
- 리포지토리를 나누었을 때 추상 계층을 통해 얻는 코드 안정성보다, 모델이 지원해주는 다양한 기능으로 인한 통제되지 않는 버그가 많을 수 있다.
- 따라서 repository는 구현하지 않는다. 대신 이후에 FastAPI + SQLAlchemy를 실습할 때 적용해 보려 한다.
PS. 비즈니스로직은 장고에서 추천하는대로 Fat Model 패턴으로 구현한다. (모델 리팩토링하기는 다음 [링크](https://www.softkraft.co/django-best-practises/) 을 참고)
