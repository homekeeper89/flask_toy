Feature: User Instant Answer API
    As an application developer,
    I want to get instant answers for search terms via a REST API,
    So that my app can get answer anywhere.

    Scenario Outline: Basic App Api query
        Given the app api is quried with "<phrase>"
        Then the response status code is "200"
        And the response contains results for "<phrase>"

        Examples: Animalis
            | pharase  |
            | panda    |
            | python   |
            | platypus |
        Examples: Fruits
            | phrase    |
            | peach     |
            | pineapple |
            | papaya    |