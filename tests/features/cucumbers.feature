Feature: Cucumber Baskter
    As a gardener,
    I want to carry cucumber in a basket,
    So that i don't drop them all.

    Scenario: Add cucumbers to a basket
        Given the basket has 2 cucumbers
        When 4 cucumbers are added to the basket
        Then the basket contains 6 cucumbers

    Scenario: Remove cucumbers from a basket
        Given the basket has 8 cucumbers
        When 3 cucumbers are removed from the basket
        Then the basket contains 5 cucumbers