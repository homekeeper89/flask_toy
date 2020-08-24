Feature: 유저 로그인 테스트

    Scenario: 정상 가입 후 로그인 케이스
        Given 한 User가 있다.
        When 해당 User가 올바른 정보로 가입한다.
        Then 정상적으로 로그인이 성공해야 한다.