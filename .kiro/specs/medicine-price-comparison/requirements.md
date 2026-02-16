# Requirements Document

## Introduction

This document specifies the requirements for a Medicine Price Comparison & Alternative Suggestion System - a Django-based web application that enables users to search for medicines, compare prices across pharmacies, discover cheaper alternatives with identical compositions, and calculate potential savings.

## Glossary

- **System**: The Medicine Price Comparison & Alternative Suggestion System web application
- **User**: Any person accessing the web application to search for medicine information
- **Medicine**: A pharmaceutical product with a brand name, composition, strength, and manufacturer
- **Pharmacy**: A retail establishment that sells medicines
- **Price_Record**: A specific price for a medicine at a particular pharmacy with a timestamp
- **Alternative**: A medicine with the same composition as the searched medicine but potentially different brand name
- **Composition**: The active pharmaceutical ingredients in a medicine
- **Savings_Percentage**: The percentage difference between the highest and lowest prices for a medicine
- **Search_Query**: User input text for finding medicines
- **Price_Comparison_Table**: A sorted display of all pharmacies selling a medicine with their prices
- **Alternative_List**: A ranked list of medicines with the same composition as the searched medicine

## Requirements

### Requirement 1: Medicine Search

**User Story:** As a user, I want to search for medicines by brand name, so that I can find price information for the medicine I need.

#### Acceptance Criteria

1. WHEN a user enters a search query, THE System SHALL perform case-insensitive matching against medicine brand names
2. WHEN a user enters a partial brand name, THE System SHALL return all medicines whose brand names contain the search query as a substring
3. WHEN a search query matches multiple medicines, THE System SHALL display all matching results
4. WHEN a search query matches no medicines, THE System SHALL display a message indicating no results were found
5. THE System SHALL process search queries without requiring exact spelling or capitalization

### Requirement 2: Price Comparison Display

**User Story:** As a user, I want to see all pharmacies selling a selected medicine with their prices, so that I can identify the cheapest option.

#### Acceptance Criteria

1. WHEN a user selects a medicine from search results, THE System SHALL retrieve all Price_Records for that medicine
2. WHEN displaying Price_Records, THE System SHALL sort them by price in ascending order
3. WHEN displaying the Price_Comparison_Table, THE System SHALL highlight the pharmacy with the lowest price
4. THE System SHALL display pharmacy name, price, and last updated timestamp for each Price_Record
5. WHEN multiple Price_Records exist, THE System SHALL calculate and display the Savings_Percentage between the highest and lowest prices

### Requirement 3: Savings Calculation

**User Story:** As a user, I want to see how much money I can save by choosing the cheapest pharmacy, so that I can make informed purchasing decisions.

#### Acceptance Criteria

1. WHEN displaying Price_Records for a medicine, THE System SHALL calculate the lowest price from all Price_Records
2. WHEN displaying Price_Records for a medicine, THE System SHALL calculate the highest price from all Price_Records
3. THE System SHALL calculate Savings_Percentage as ((highest_price - lowest_price) / highest_price) * 100
4. THE System SHALL display the Savings_Percentage prominently on the results page
5. WHEN only one Price_Record exists, THE System SHALL display zero savings or indicate no comparison available

### Requirement 4: Alternative Medicine Suggestion

**User Story:** As a user, I want to see cheaper alternatives with the same composition, so that I can find more affordable options with equivalent therapeutic effects.

#### Acceptance Criteria

1. WHEN displaying results for a medicine, THE System SHALL identify all medicines with matching composition
2. WHEN identifying alternatives, THE System SHALL exclude the originally searched medicine from the Alternative_List
3. FOR each alternative medicine, THE System SHALL retrieve the lowest price from all available Price_Records
4. THE System SHALL sort the Alternative_List by lowest price in ascending order
5. THE System SHALL display brand name, composition, manufacturer, and lowest price for each alternative

### Requirement 5: Data Persistence

**User Story:** As a system administrator, I want medicine and price data stored in a database, so that the system can provide consistent and queryable information.

#### Acceptance Criteria

1. THE System SHALL store Medicine records with brand_name, composition, strength, and manufacturer fields
2. THE System SHALL store Pharmacy records with name and website_url fields
3. THE System SHALL store Price_Record entries with foreign keys to Medicine and Pharmacy, plus price and last_updated fields
4. THE System SHALL use Django ORM for all database operations
5. THE System SHALL use SQLite as the database engine

### Requirement 6: User Interface

**User Story:** As a user, I want a clean and responsive interface, so that I can easily search for medicines and view results on any device.

#### Acceptance Criteria

1. THE System SHALL provide a homepage with a prominent search bar
2. THE System SHALL use Bootstrap 5 for responsive layout that adapts to mobile, tablet, and desktop screens
3. WHEN displaying results, THE System SHALL show the Price_Comparison_Table and Alternative_List on a single results page
4. THE System SHALL use visual indicators (badges, colors, or icons) to highlight the cheapest pharmacy option
5. THE System SHALL display a healthcare disclaimer on the results page stating that users should consult healthcare professionals

### Requirement 7: Application Architecture

**User Story:** As a developer, I want a clean 3-tier architecture, so that the application is maintainable and follows best practices.

#### Acceptance Criteria

1. THE System SHALL implement a Presentation layer handling all HTML templates and user interface rendering
2. THE System SHALL implement an Application layer containing business logic for price comparison and alternative identification
3. THE System SHALL implement a Data layer using Django models and ORM for database access
4. THE System SHALL organize code into a Django project structure with separate apps for core functionality
5. THE System SHALL separate static files (CSS, JavaScript) from templates and application code

### Requirement 8: Sample Data

**User Story:** As a developer or tester, I want sample seed data, so that I can test the application without manually entering data.

#### Acceptance Criteria

1. THE System SHALL provide a data seeding mechanism using Django management commands or fixtures
2. THE System SHALL include sample Medicine records covering multiple compositions and brands
3. THE System SHALL include sample Pharmacy records with realistic names
4. THE System SHALL include sample Price_Records demonstrating price variations across pharmacies
5. THE System SHALL ensure seed data demonstrates the alternative suggestion feature with medicines sharing compositions

### Requirement 9: Search Performance

**User Story:** As a user, I want search results to appear quickly, so that I can efficiently find medicine information.

#### Acceptance Criteria

1. WHEN a user submits a search query, THE System SHALL return results within 2 seconds for databases with up to 10,000 medicine records
2. THE System SHALL use database indexing on frequently queried fields (brand_name, composition)
3. THE System SHALL limit search results to a reasonable number (e.g., top 50 matches) to maintain performance
4. WHEN performing price comparisons, THE System SHALL use optimized queries to minimize database round trips
5. WHEN identifying alternatives, THE System SHALL use efficient filtering and aggregation queries

### Requirement 10: Data Validation

**User Story:** As a system administrator, I want data validation on all inputs, so that the database maintains data integrity.

#### Acceptance Criteria

1. WHEN creating or updating Medicine records, THE System SHALL validate that brand_name is not empty
2. WHEN creating or updating Medicine records, THE System SHALL validate that composition is not empty
3. WHEN creating or updating Price_Records, THE System SHALL validate that price is a positive decimal number
4. WHEN creating or updating Pharmacy records, THE System SHALL validate that name is not empty
5. THE System SHALL use Django model validation and form validation to enforce these constraints
