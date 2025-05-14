

## 🔐 Machine-to-Machine Authentication (Client Credentials Flow)

This section explains how to authenticate using the **OAuth2 Client Credentials** flow and how to access protected endpoints using the issued token.

---

### 📌 Step 1: Obtain Access Token (Client Credentials Grant)

Make a `POST` request to the `/o/token/` endpoint with your client credentials and the required scope (`write` in this example):

#### ✅ Example Request

```bash
curl -X POST http://localhost:8000/o/token/ \
  -d "grant_type=client_credentials" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET"
```

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "write"
}
```

---

### 📌 Step 2: Use the Access Token

Once you receive the access token, include it in the `Authorization` header as a **Bearer token** when calling protected endpoints.

#### ✅ Example Request to Protected View

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     http://localhost:8000/protected/
```

---
