Feature: API - Post
  #API testing for posts


  @api @automated
  Scenario: Creating a post successfully
    Given I start session
    When I create a new post
    Then I confirm post created

  @api @automated
  Scenario: Listing a post
    Given I start session
    When I get details for post '5'
    Then I confirm OK response
    Then I confirm post '5' listed

  @api @automated
  Scenario: Updating a post successfully
    Given I start session
    When I update post '5'
    Then I confirm OK response
    Then I confirm post '5' updated

  @api @automated
  Scenario: Deleting post successfully
    Given I start session
    When I delete post '5'
    Then I confirm OK response




