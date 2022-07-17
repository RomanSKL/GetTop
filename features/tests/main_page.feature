# Created by skliarovrn at 7/15/22
Feature: Tests on a main page

  Scenario: Top Banner arrows
    Given Open GetTop
    When Hover over Banner 1
    When Click right arrow
    And Verify Banner 2
    When Click left arrow
    Then Verify Banner 1

  Scenario: Top Banner dots
    Given Open GetTop
    When Click right dott
    And Verify Banner 2
    When Click left dott
    Then Verify Banner 1

  Scenario: Verify that clicking on banner1 iPad Pro opens correct category page
    Given Open GetTop
    When Click on Banner 1
    Then Verify correct category page is open for Banner 1

    Scenario: Verify that clicking on banner2 MacBook Pro opens correct category page
      Given Open GetTop
      When Click right dott
      When Click on Banner 2
      Then Verify correct category page is open for Banner 2

