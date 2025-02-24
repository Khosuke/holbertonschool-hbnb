
# High-level Package diagram:

This is the high-level package diagram that illustrates the three-layer architecture of the application and the communication between these layers via the facade pattern.

![Package Diagram (1)](High-Level_Package_Diagram.png)

## Architecture Layers

### 1. Presentation Layer
**Purpose**: Handles user interface and user interaction components.

**Components**:
- User_Management: Handles user registration, authentication, and profile management interfaces.
- Place_Management: Manages property listing, editing, and search interfaces.
- Review_Management: Provides interfaces for creating and viewing property reviews.
- Amenity_Management: Manages property amenity selection and configuration interfaces.

### 2. Business Logic Layer
**Purpose**: Implements core business rules, data processing, and application logic.

**Components**:
- User_Model: Implements user-related business rules and operations.
- Place_Model: Handles property-related logic and validations.
- Review_Model: Manages review creation and rating calculations.
- Amenity_Model: Processes amenity-related business rules.

### 3. Persistence Layer
**Purpose**: Manages data storage and retrieval operations.

**Component**:
- Database: Handles all data persistence operations.

# Class Diagram:

This is the class diagram for the Business Logic layer, focusing on the User, Place, Review, and Amenity entities, including their attributes, methods, and relationships. And which also includes the relationships between Places and Amenities.

![Class Diagram (1)](Class_Diagram.png)

## The Differents Classes:

### User Class
The User class serves as the central entity representing platform users (both renters and property owners).

**Key Features:**
- Comprehensive user profile management with secure handling of sensitive data (private email and password).
- Role-based access control through the Admin boolean.
- Encapsulated sensitive data with private getters/setters.

### Place Class
Represents rental properties available on the platform.

**Key Features:**
- Geographic location tracking (Longitude, Latitude).
- Property categorization (TypeOfPlace).
- Price management.
- Full CRUD operations for property management.

### Review Class
Handles user feedback and ratings for properties.

**Key Features:**
- Numerical rating system (float Rating).
- Text-based feedback (Comment).
- Maintains relationships with both User and Place through IDs.
- Audit trail with creation and update timestamps.

### Amenities Class
Manages available features and facilities for properties.

**Key Features:**
- Timestamp tracking for amenity creation and updates.
- Extensible design for adding new amenity types.

### Amenity_Place Class
Junction table implementing many-to-many relationship between Places and Amenities.

### 1. Relationship Choices
- **User-Place**: Composition indicating strong ownership.
  - Rationale: Places cannot exist without a creating user.
  - Implementation: Cascade deletion when user is removed.

- **User-Review**: Association relationship.
   - Rationale: Users and Reviews can exist independently.
   - Implementation: Reviews are not deleted if the User who submited it is deleted.

- **Place-Review**: Composition relationship.
  - Rationale: Reviews are dependent on the existence of places.
  - Implementation: Reviews are deleted if the associated place is removed.

- **Place-Amenities**: Aggregation relationship.
  - Rationale: Amenities can exist independently of places.
  - Implementation: Allows amenities to be reused across multiple properties.

# Sequence Diagram: User create an account

This sequence diagram illustrates the user registration process in the HBnB platform. The diagram shows the complete flow from initial user data submission through validation, email verification, password security, and account creation, including error handling for existing email addresses.

![Sequence Create Account Diagram (1)](Sequence-User_Create_Account.png)

### Main Success Scenario
1. User submits registration data via POST request
2. API forwards data for validation
3. Business logic validates requirements
4. Database confirms email availability
5. Password is securely hashed
6. User account is created
7. UserID is returned to client

### Alternative Flow
1. **Email Already Exists**
   - Database finds existing email
   - Returns conflict error
   - User receives 409 status code
   - Registration is prevented

2. **Database Error**
   - System cannot access place data
   - Returns 500 status with error information
   - Ensures proper error handling for system failures


# Sequence Diagram : User Create a new Place listing

Users can create places on the HBnB platform.
This sequence diagram illustrates the process to create a place by the user. The diagram shows the complete flow from the initial user data submission through validation and final creation of the place, highlighting the importance of error handling for a reliable user experience.

![Sequence Create New Place (1)](Sequence-User_Create_Place.png)

### Main Success Scenario
1. User submits Places Data via POST request
2. API forwards data for validation.
3. Business logic verifies requirements.
4. Database stores the new place.
5. A New Place is created.
6. API returns 201 Created with Place ID.

### Alternative Flow
1. **Invalide Data**:
   - Place data requirements are invalid.
   - Return Bad Request Error.
   - User receive 400 status code.
   - Place creation is prevented.

This approach ensures efficient and structured place creation with proper error handling.

2. **Database insertion fails**
   - API returns a 500 Internal Server Error.
   - Ensures proper error handling for system failures


# Sequence Diagram: User Review submission

Users can leave reviews for places they have visited, including a rating and a comment.
This sequence diagram illustrates the process to submit a review for a place by the user in the HBnB platform. The diagram shows the complete flow from initial user data submission through validation, including error handling.

![Sequence Review Submission (1)](Sequence-User_Post_Review.png)

### Main Success Scenario
1. User sends a POST request to the API to submit a comment.
2. The API checks if the user is authenticated.
3. The API forwards the request to the BusinessLogic for validation and processing of the review.
4. The BusinessLogic validates the content of the review.
5. The BusinessLogic inserts the review into the database.
6. The database returns a success response (with the review ID) to the BusinessLogic.
7. The BusinessLogic forwards the review ID to the API.
8. The API returns a 201 Created response to the user with the review ID.

### Alternative Flow
1. **User not logged in**
   - the API stops the process and returns a 401 Unauthorized response directly to the user.

2. **Review validation fails**
   - The BusinessLogic returns a 400 Bad Request response to the API because the review validation fails.
   - The API returns a 400 Bad Request response to the user.

3. **Database insertion fails**
   - API returns a 500 Internal Server Error.
   - Ensures proper error handling for system failures

# Sequence Diagram : User Fetching Places

This sequence diagram illustrates the process of fetching a list of places in the HBnB booking system. The diagram demonstrates the interaction flow between the user interface, API layer, business logic, and database when retrieving place listings based on search criteria.

![Sequence User Fetch Places Diagram (1)](Sequence-User_Fetching_Places.png)

### Main Success Scenario
1. User sends GET request with search criteria
2. API forwards request to business logic
3. Business logic validates criteria
4. Database query executes with valid criteria
5. Results are formatted and returned to user

### Alternative Flows
1. **Empty Results**
   - Valid search with no matching places
   - Returns 200 status with empty list
   - Allows client to handle zero-result cases gracefully

2. **Invalid Criteria**
   - Search parameters fail validation
   - Returns 400 status with error details
   - Prevents unnecessary database queries

3. **Database Error**
   - System cannot access place data
   - Returns 500 status with error information
   - Ensures proper error handling for system failures
