# Created by Roman at 10/8/2020
Feature: Amazon Shopping Cart

  # User opens Amazon and verifies Shopping Cart is Empty

  Scenario: Amazon Shopping Cart is Empty
    Given Open Amazon Home Page
    When Click on Shopping Cart
    Then Verify Shopping Cart is Empty