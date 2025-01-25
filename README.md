Here is the entire test data compiled into one markdown file that you can copy and paste:

```markdown
# Test Data for Testing URLs in Django Application

## 1. User Registration
**URL:** `POST /register/`  
**Payload:**
```json
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "Password123!",
    "role": "member",
    "phone": "1234567890"
}
```
**Expected Response:**
```json
{
    "message": "User registered successfully!"
}
```

## 2. Memberships
### 2.1 Create a Membership
**URL:** `POST /memberships/`  
**Payload:**
```json
{
    "user": 1,  // Replace with the user ID from the database
    "status": "active"
}
```
**Expected Response:**
```json
{
    "id": 1,
    "user": 1,
    "status": "active",
    "start_date": "2025-01-24",
    "renewal_date": null
}
```

### 2.2 List Memberships
**URL:** `GET /memberships/`  
**Expected Response:**
```json
[
    {
        "id": 1,
        "user": 1,
        "status": "active",
        "start_date": "2025-01-24",
        "renewal_date": null
    }
]
```

### 2.3 Retrieve a Membership
**URL:** `GET /memberships/<id>/`  
**Expected Response:**
```json
{
    "id": 1,
    "user": 1,
    "status": "active",
    "start_date": "2025-01-24",
    "renewal_date": null
}
```

### 2.4 Update a Membership
**URL:** `PUT /memberships/<id>/`  
**Payload:**
```json
{
    "status": "inactive"
}
```
**Expected Response:**
```json
{
    "id": 1,
    "user": 1,
    "status": "inactive",
    "start_date": "2025-01-24",
    "renewal_date": null
}
```

### 2.5 Delete a Membership
**URL:** `DELETE /memberships/<id>/`  
**Expected Response:**
```json
{
    "message": "Membership deleted successfully."
}
```

## 3. Documents
### 3.1 Upload a Document
**URL:** `POST /documents/`  
**Headers:**
- `Content-Type: multipart/form-data`

**Payload (multipart form):**
```bash
curl -X POST http://127.0.0.1:8000/documents/ \
-F "user=1" \
-F "file=@path_to_file.pdf"
```

### 3.2 List Documents
**URL:** `GET /documents/`

### 3.3 Retrieve a Document
**URL:** `GET /documents/<id>/`

### 3.4 Update a Document
**URL:** `PUT /documents/<id>/`  
**Payload:**
```json
{
    "verified": true
}
```

### 3.5 Delete a Document
**URL:** `DELETE /documents/<id>/`

## 4. Savings Plans
### 4.1 Create a Savings Plan
**URL:** `POST /savings-plans/`  
**Payload:**
```json
{
    "user": 1,
    "plan_name": "Retirement Plan",
    "interest_rate": 5.5
}
```

### 4.2 List Savings Plans
**URL:** `GET /savings-plans/`

### 4.3 Retrieve a Savings Plan
**URL:** `GET /savings-plans/<id>/`

### 4.4 Update a Savings Plan
**URL:** `PUT /savings-plans/<id>/`  
**Payload:**
```json
{
    "plan_name": "Updated Plan Name",
    "interest_rate": 6.0
}
```

## 5. Contributions
### 5.1 Create a Contribution
**URL:** `POST /contributions/`  
**Payload:**
```json
{
    "savings_plan": 1,
    "amount": 1000.00
}
```

### 5.2 Update a Contribution
**URL:** `PUT /contributions/<id>/`  
**Payload:**
```json
{
    "amount": 1500.00
}


