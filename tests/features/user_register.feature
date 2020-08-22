Feature: User Register Service
    User Register Service Step

    Scenario Outline: Normal User Register
        Given user give us <user_id>
        When the user_id is same to <limit_word>
        Then i should return <message> and <code>

        Examples:
            | user_id | limit_word | message             | code |
            | ssibal  | ssibal     | can't use that word | 400  |
            | hello   | ssibal     | can use that word   | 200  |