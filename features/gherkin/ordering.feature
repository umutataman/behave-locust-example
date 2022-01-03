Feature: Ordering
  #Ordering scenarios


  @automated
  Scenario: Cannot order from different city
    Given I open page of city 'breezanddijk' and postcode '8766'
    When I search and find restaurant 'BRT Cypress Test Restaurant'
    And I add couple of burgers to basket and checkout
    And I enter address details for city 'Enschede'
    And I select payment method 'Cash'
    And I place the order
    Then I should see error message that cannot order from different city
    When I visit restaurants that delivery my city
    Then I should see 'BRT Cypress Test Restaurant'
    And I should see 'Enschede' address in location


