# Created by skliarovrn at 7/9/22
Feature: Test for MAC top filter

  Scenario: Verify that user can see all items under MAC
    Given Open GetTop
    When Hover over MAC
    Then Verify all 4 items under MAC


  Scenario: Verify that MacBook Pro 13-inch link opens correct page
    Given Open GetTop
    When Hover over MAC
    And Click on MacBook Pro 13-inch
    Then Verify MacBook Pro 13-inch page is opened


  Scenario: Verify that MacBook Pro 16-inch link opens correct page
    Given Open GetTop
    When Hover over MAC
    And Click on MacBook Pro 16-inch
    Then Verify MacBook Pro 16-inch page is opened


  Scenario: Verify that MacBook Air link opens correct page
    Given Open GetTop
    When Hover over MAC
    And Click on MacBook Air
    Then Verify MacBook Air page is opened