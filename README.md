# API Routes

## Transaction
- **GET** - `/api/transaction/:transactionId` - Retrieve a transaction by ID
- **POST** - `/api/transaction/` - Create a new transaction
- **PUT** - `/api/transaction/:transactionId` - Update an existing transaction
- **DELETE** - `/api/transaction/:transactionId` - Delete a transaction

## Category
- **GET** - `/api/category/:categoryId` - Retrieve a category by ID
- **POST** - `/api/category/` - Create a new category
- **PUT** - `/api/category/:categoryId` - Update an existing category
- **DELETE** - `/api/category/:categoryId` - Delete a category

## Account
- **GET** - `/api/account/:accountId` - Retrieve an account by ID
- **POST** - `/api/account/` - Create a new account
- **PUT** - `/api/account/:accountId` - Update an existing account
- **DELETE** - `/api/account/:accountId` - Delete an account

## User
- **GET** - `/api/user/:userId` - Retrieve a user by ID
- **POST** - `/api/user/` - Create a new user
- **PUT** - `/api/user/:userId` - Update an existing user

## Auth
- **POST** - `/api/auth/login/` - Authenticate user (login)
- **POST** - `/api/auth/logout/` - End user session (logout)
- **GET**  - `/api/auth/csrf_token/` - Retrieve a CSRF token