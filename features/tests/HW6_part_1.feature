# Created by Roman at 10/31/2020
Feature: HW_6

  Scenario: User can open and close Amazon Applications
 Given Open Amazon T&C page
 When Store original windows
 And Click on Amazon applications link
 And Switch to the newly opened window
 Then Amazon app page is opened
 And User can close new window and switch back to original