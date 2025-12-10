## Follows & Feed

### Follow / Unfollow
- POST /api/accounts/follow/<user_id>/ — follow the user with id `<user_id>`
- POST /api/accounts/unfollow/<user_id>/ — unfollow the user with id `<user_id>`
- GET /api/accounts/following/ — list users you follow
- GET /api/accounts/followers/ — list users following you

Permissions: authenticated users only.

### Feed
- GET /api/feed/ — returns posts made by users you follow (most recent first)
- Supports filtering/search via `?search=...` and ordering `?ordering=-created_at`.
- Uses pagination if enabled in settings.
