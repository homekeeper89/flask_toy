Feature: Service with User
    유저와 관련된 모든 Feature

    Scenario Outline: Check user registred
        Given user has type and <unique_key> and <pwd>
        When user want to register
        Then server send to <code> and <flag>

        Examples: User Info
            | unique_key | pwd           | code | flag |
            | some_id    | some_password | 200  | true |