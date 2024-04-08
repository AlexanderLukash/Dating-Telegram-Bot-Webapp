from backend.api.likes import router as router_likes
from backend.api.users import router as router_users

all_routers = [
    router_users,  # Add the router for users to the list of all routers
    router_likes  # Add the router for likes to the list of all routers
]

# This list contains all routers used in the FastAPI application.
# By including these routers in `all_routers`, you ensure that all API routes
# defined in the `router_users` and `router_likes` are included in the FastAPI application.
