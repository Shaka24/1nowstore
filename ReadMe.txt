Register a new user: Make a POST request to /api/register/ to create a new user.
Obtain a token: Make a POST request to /api/token/ with the user's credentials (username and password) to obtain a JWT token.
Access protected resources: Use the obtained JWT token in the Authorization header for subsequent requests to endpoints like /api/products/ or /api/orders/
