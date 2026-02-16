# Implementation Plan: Medicine Price Comparison & Alternative Suggestion System

## Overview

This implementation plan breaks down the Medicine Price Comparison system into discrete coding tasks. Each task builds incrementally on previous work, starting with project setup, then data models, business logic, views, templates, and finally testing. The plan follows Django best practices and the 3-tier architecture specified in the design.

## Tasks

- [-] 1. Set up Django project structure and configuration
  - Create Django project `medcompare` with `core` app
  - Configure settings.py for SQLite database, static files, and templates
  - Set up URL routing in project and app level
  - Create directory structure for templates and static files
  - Install required dependencies (Django, hypothesis for property testing)
  - _Requirements: 7.4, 7.5_

- [ ] 2. Implement data models with validation
  - [~] 2.1 Create Medicine model with fields and validation
    - Implement Medicine model with brand_name, composition, strength, manufacturer
    - Add database indexes on brand_name and composition
    - Add validation for non-empty brand_name and composition
    - _Requirements: 5.1, 10.1, 10.2_
  
  - [~] 2.2 Create Pharmacy model with fields and validation
    - Implement Pharmacy model with name and website_url
    - Add unique constraint on name field
    - Add validation for non-empty name
    - _Requirements: 5.2, 10.4_
  
  - [~] 2.3 Create Price model with relationships and validation
    - Implement Price model with ForeignKeys to Medicine and Pharmacy
    - Add price field with validation for positive values
    - Add last_updated timestamp field
    - Add unique_together constraint on (medicine, pharmacy)
    - Add composite index on (medicine, price)
    - _Requirements: 5.3, 10.3_
  
  - [ ]* 2.4 Write property test for model persistence
    - **Property 8: Model persistence round-trip**
    - **Validates: Requirements 5.1, 5.2, 5.3**
  
  - [ ]* 2.5 Write property tests for validation rules
    - **Property 10: Medicine validation rejects empty brand names**
    - **Property 11: Medicine validation rejects empty compositions**
    - **Property 12: Price validation rejects non-positive values**
    - **Property 13: Pharmacy validation rejects empty names**
    - **Validates: Requirements 10.1, 10.2, 10.3, 10.4**

- [~] 3. Create and run database migrations
  - Generate initial migrations for all models
  - Apply migrations to create database schema
  - Verify database tables and indexes are created correctly
  - _Requirements: 5.1, 5.2, 5.3_

- [ ] 4. Implement business logic services
  - [~] 4.1 Create MedicineSearchService
    - Implement search_medicines method with case-insensitive partial matching
    - Use Django ORM filter with icontains lookup
    - Order results by brand_name
    - Add result limit (50 medicines maximum)
    - _Requirements: 1.1, 1.2, 1.3, 1.5, 9.3_
  
  - [ ]* 4.2 Write property tests for search service
    - **Property 1: Case-insensitive partial search completeness**
    - **Property 9: Search result limit enforcement**
    - **Validates: Requirements 1.1, 1.2, 1.3, 1.5, 9.3**
  
  - [~] 4.3 Create PriceComparisonService
    - Implement get_price_comparison method
    - Retrieve all prices for a medicine with select_related for pharmacy
    - Sort prices in ascending order
    - Calculate lowest_price, highest_price, and savings_percentage
    - Handle edge case of no prices or single price
    - _Requirements: 2.1, 2.2, 2.5, 3.1, 3.2, 3.3_
  
  - [ ]* 4.4 Write property tests for price comparison service
    - **Property 2: Price records completeness and ordering**
    - **Property 3: Lowest price identification**
    - **Property 4: Savings calculation correctness**
    - **Validates: Requirements 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.3**
  
  - [~] 4.5 Create AlternativeFinderService
    - Implement find_alternatives method
    - Filter medicines by matching composition, excluding original medicine
    - For each alternative, get lowest price using order_by and first()
    - Sort alternatives by lowest_price in ascending order
    - _Requirements: 4.1, 4.2, 4.3, 4.4_
  
  - [ ]* 4.6 Write property tests for alternative finder service
    - **Property 5: Alternative identification correctness**
    - **Property 6: Alternative lowest price accuracy**
    - **Property 7: Alternative sorting correctness**
    - **Validates: Requirements 4.1, 4.2, 4.3, 4.4**

- [~] 5. Checkpoint - Ensure all tests pass
  - Run all property tests and unit tests
  - Verify business logic services work correctly
  - Ask the user if questions arise

- [ ] 6. Implement views and URL routing
  - [~] 6.1 Create home view
    - Implement home view function to render search page
    - Create URL pattern for homepage (root path)
    - _Requirements: 6.1_
  
  - [~] 6.2 Create search view
    - Implement search view to handle search queries
    - Extract query parameter from GET request
    - Call MedicineSearchService to get results
    - Render search results template with context
    - Handle empty query by redirecting to home
    - _Requirements: 1.1, 1.2, 1.3, 1.4_
  
  - [~] 6.3 Create results view
    - Implement results view to display price comparison and alternatives
    - Call PriceComparisonService to get price data
    - Call AlternativeFinderService to get alternatives
    - Handle Medicine.DoesNotExist exception
    - Render results template with full context
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 4.1, 4.2, 4.3, 4.4, 4.5_
  
  - [ ]* 6.4 Write unit tests for views
    - Test home view renders correctly
    - Test search view with valid and empty queries
    - Test results view with valid and invalid medicine IDs
    - Test edge cases (no prices, no alternatives)
    - _Requirements: 1.4, 6.1, 6.3_

- [~] 7. Create Django forms
  - Create MedicineSearchForm with query field
  - Add Bootstrap CSS classes to form widgets
  - Add placeholder text and autocomplete attributes
  - _Requirements: 1.1, 6.1_

- [ ] 8. Implement templates with Bootstrap 5
  - [~] 8.1 Create base template
    - Create base.html with Bootstrap 5 CDN links
    - Add navigation structure
    - Define content blocks for child templates
    - Add custom CSS link
    - _Requirements: 6.2_
  
  - [~] 8.2 Create home template
    - Create home.html extending base template
    - Add prominent search bar using MedicineSearchForm
    - Add hero section with application description
    - Style with Bootstrap components
    - _Requirements: 6.1_
  
  - [~] 8.3 Create search results template
    - Create search_results.html for displaying medicine list
    - Display search query and result count
    - Show clickable medicine cards linking to results page
    - Handle empty results case
    - _Requirements: 1.3, 1.4_
  
  - [~] 8.4 Create results template
    - Create results.html for price comparison and alternatives
    - Display medicine details at top
    - Create price comparison table with pharmacy, price, last_updated columns
    - Highlight lowest price row with Bootstrap badge or color
    - Display savings percentage prominently
    - Create alternatives section with cards or table
    - Add healthcare disclaimer at bottom
    - Handle edge cases (no prices, no alternatives, single price)
    - _Requirements: 2.3, 2.4, 2.5, 3.4, 4.5, 6.3, 6.5_

- [~] 9. Add custom styling and JavaScript
  - Create custom.css for additional styling beyond Bootstrap
  - Add hover effects for medicine cards
  - Style savings badge prominently
  - Create main.js for any client-side interactivity (optional)
  - Ensure responsive design works on mobile, tablet, desktop
  - _Requirements: 6.2_

- [~] 10. Configure Django admin interface
  - Register Medicine, Pharmacy, and Price models with admin
  - Customize admin list displays with relevant fields
  - Add search and filter capabilities in admin
  - Configure admin to show validation errors
  - _Requirements: 5.1, 5.2, 5.3_

- [ ] 11. Create seed data management command
  - [~] 11.1 Implement seed_data management command
    - Create management/commands/seed_data.py
    - Create 20+ medicine records covering 5-6 compositions
    - Create 5-7 pharmacy records with realistic names
    - Create 60+ price records with 10-40% price variations
    - Ensure multiple medicines share compositions for alternatives
    - Include medicines for common drugs (Paracetamol, Ibuprofen, etc.)
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_
  
  - [ ]* 11.2 Write unit tests for seed data command
    - Test that running seed command creates expected number of records
    - Test that medicines with shared compositions exist
    - Test that price variations exist across pharmacies
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_

- [~] 12. Checkpoint - Integration testing
  - Run seed_data command to populate database
  - Test complete user workflow: search → select → view results
  - Verify price comparison displays correctly
  - Verify alternatives display correctly
  - Verify savings calculations are accurate
  - Test edge cases with seed data
  - Ask the user if questions arise

- [~] 13. Create project documentation
  - Create README.md with project overview
  - Document installation steps (pip install requirements)
  - Document database setup (migrations)
  - Document how to run seed data command
  - Document how to run development server
  - Document how to run tests
  - Add screenshots or usage examples
  - _Requirements: All_

- [ ]* 14. Write integration tests
  - Test complete search-to-results workflow
  - Test with realistic data volumes
  - Test all edge cases end-to-end
  - _Requirements: All_

- [~] 15. Final checkpoint - Complete system verification
  - Run all tests (unit, property, integration)
  - Verify all requirements are met
  - Test responsive design manually
  - Verify healthcare disclaimer is visible
  - Ensure all validation rules work
  - Ask the user if questions arise

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Property tests validate universal correctness properties with 100+ iterations
- Unit tests validate specific examples and edge cases
- Hypothesis library will be used for property-based testing in Python
- Bootstrap 5 will be loaded via CDN for simplicity
- SQLite requires no additional configuration in Django
