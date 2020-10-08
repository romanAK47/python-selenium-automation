# Created by Roman at 10/8/2020
Feature: Cancelling Order

  # User can search for Cancelling an order on Amazon and verify page has "Cancel Order" somewhere on it

  Scenario: Amazon Search for Cancelling an Order
    Given Open Amazon Customer Help Page
    When Input "Cancel Order" and click Search
    Then Verify that page contains "Cancel Order"