Feature: User-api
  As a user,
  I want to register this app
  With My Information

  Scenario: Normal Register
    Given A normal user
    When user add id and password
    Then user enter key to send

  Scenario: Empty shaker
    Given A Salt Shaker with 0 doses
    When I shake the shaker 1 times
    Then 0 salt doses falls on my plate
    And The shaker contains 0 doses

  Scenario: Custom Shaker
    Given A Salt Shaker with 100 doses
    When I shake the shaker 99 times
    Then 99 salt doses falls on my plate
    And The shaker contains 1 doses


  Scenario: Serve multiple times
    Given A Salt Shaker with <doses> doses
    When I shake the shaker <shakes> times
    Then <expected_served> salt doses fall on my plate
    And The shaker contains <expected_remaining> doses



    Examples:
      | doses | shakes | expected_remaining | expected_served |
      | 20    | 10     | 10                 | 10              |
      | 50    | 10     | 40                 | 10              |
      | 20    | 20     | 0                  | 20              |
      | 3     | 2      | 1                  | 2               |
      | 3     | 5      | 0                  | 3               |