
# Authentication and Accessing Restricted Resources

This documentation provides instructions on obtaining access tokens and accessing restricted resources for your application.

## Obtaining Access Tokens

To obtain access tokens for authentication, perform the following steps:

### Step 1: Login

Make a POST request to the login endpoint:

```http
POST http://127.0.0.1:9000/api/login
```

Include the following parameters in the request body:

- `username`: Your username
- `password`: Your password

Upon successful login, you will receive access tokens.

## Accessing Restricted Resources

Once you have obtained the access token, you can use it to access restricted resources.

### Step 2: Access Restricted Resources

Make a GET request to the restricted resource endpoint:

```http
GET http://127.0.0.1:9000/api/restricted
```

Include the obtained access token in the request headers:

```http
Authorization: Bearer [YOUR_ACCESS_TOKEN]
```

Replace `[YOUR_ACCESS_TOKEN]` with the actual access token obtained during the login process.

**Note:** Ensure that you have proper authentication before attempting to access restricted resources.

---
