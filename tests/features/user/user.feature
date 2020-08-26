Feature: 유저와 관련된 모든 Feature
    유저와 관련된 모든 Feature를 작성

    Scenario Outline: 유저가 회원가입을 하려고 한다
        Given 유저는 <email>, <password>, <nickname>, <age>, <hobby> 를 입력한다
        When 유저가 위 정보 중 몇가지 정보를 빼고 보낸다.
        Then 서버는 400 과 빠진 <property> 를 포함하는 메세지로 응답한다.
