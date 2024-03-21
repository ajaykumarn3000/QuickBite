# User Authentication API

## User Registration [/user/auth/register]

### Register a New User [POST]

Registers a new user and initiates the OTP verification process.

+ Request (application/json)

    + Body

            {
                "username": "string",
                "passcode": "string",
                "user_type": "string"
            }

+ Response 200 (application/json)

    + Body

            {
                "message": "OTP Successfully Sent"
            }

+ Response 404 (application/json)

    + Body

            {
                "detail": "Email not found Database"
            }

+ Response 406 (application/json)

    + Body

            {
                "detail": "User has already registered"
            }

### Verify Email [POST]

Verifies a user's email using the provided OTP.

+ Request (application/json)

    + Body

            {
                "otp": "string",
                "email": "string"
            }

+ Response 200 (application/json)

    + Body

            {
                "Message": "User successfully verified",
                "token": "string"
            }

+ Response 400 (application/json)

    + Body

            {
                "detail": "Incorrect or expired OTP"
            }

+ Response 500 (application/json)

    + Body

            {
                "detail": "Internal Server Error"
            }

## User Login [/user/auth/login]

### Authenticate User [POST]

Authenticates a user based on their UID and passcode.

+ Request (application/json)

    + Body

            {
                "uid": "string",
                "passcode": "string"
            }

+ Response 200 (application/json)

    + Body

            {
                "message": "User has now logged in",
                "token": "string"
            }

+ Response 404 (application/json)

    + Body

            {
                "detail": "User not registered"
            }

+ Response 406 (application/json)

    + Body

            {
                "detail": "Incorrect Password"
            }


# Staff Authentication API

## Staff Registration [/staff/auth/register]

### Register a New Staff [POST]

Registers a new staff member and initiates the OTP verification process.

+ Request (application/json)

    + Body

            {
                "email": "string",
                "passcode": "string"
            }

+ Response 200 (application/json)

    + Body

            {
                "message": "OTP Successfully Sent"
            }

+ Response 406 (application/json)

    + Body

            {
                "detail": "Staff already registered"
            }

## Staff Login [/staff/auth/login]

### Authenticate Staff [POST]

Authenticates a staff member based on their email and passcode.

+ Request (application/json)

    + Body

            {
                "email": "string",
                "passcode": "string"
            }

+ Response 200 (application/json)

    + Body

            {
                "message": "Login Successful"
            }

+ Response 404 (application/json)

    + Body

            {
                "detail": "Email not registered"
            }

+ Response 406 (application/json)

    + Body

            {
                "detail": "Incorrect password"
            }


# Kitchen Menu API

## Menu [/kitchen/menu]

### Retrieve Menu [GET]

Retrieves the menu items.

+ Request Header

    + Headers

            Authorization: Bearer <token>

+ Response 200 (application/json)

    + Body

            {
                "item1": { ... },
                "item2": { ... },
                ...
            }

## Add Item [/kitchen/menu/add]

### Add Item to Menu [POST]

Adds a new item to the menu.

+ Request (application/json)

    + Body

            {
                "name": "string",
                "quantity": 0,
                "price": 0,
                "type": "string"
            }

+ Response 201 (application/json)

    + Body

            {
                "message": "Item added to the menu",
                "item": "string"
            }

+ Response 409 (application/json)

    + Body

            {
                "detail": "Item already exists"
            }

## Edit Item [/kitchen/menu/edit/{item_id}]

### Edit Menu Item [POST]

Modifies the price and/or quantity of an existing menu item.

+ Parameters

    + item_id (int)

+ Request (application/json)

    + Body

            {
                "item_price": 0,
                "item_quantity": 0
            }
