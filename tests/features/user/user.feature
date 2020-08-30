Feature: 유저와 관련된 모든 Feature
    유저와 관련된 모든 Feature를 작성

    Scenario Outline: 유저가 회원가입을 하려고 하는데 정보가 몇가지가 없다.
        Given 유저는 <email>, <password>, <nickname>, <age>, <language> 를 입력한다
        When 유저가 위 정보 중 <info> 를 빼고 보낸다.
        Then 서버는 <code> 과 빠진 <message> 를 포함하는 메세지로 응답한다

        Examples:
            | email          | password | nickname | age | language | info  | message  | code |
            | test@gmail.com | 123456   | test_man | 20  | python   | email | no email | 400  |
