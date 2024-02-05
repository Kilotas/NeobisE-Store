
The API will be accessible at http://127.0.0.1:8000/api/.

## API Endpoints

- **Schema and Documentation:** [API Docs](http://127.0.0.1:8000/api/docs/)

### Orders

- **Create Order:** [Order Creation](http://127.0.0.1:8000/api/orders/create/)
- **User Orders:** [User Orders](http://127.0.0.1:8000/api/orders/user/) (Authenticated)
- **Admin Orders:** [Admin Orders](http://127.0.0.1:8000/api/orders/admin/) (Admin)

### Products

- **Product List:** [Products](http://127.0.0.1:8000/api/products/)
- **Product Detail:** [Product Details](http://127.0.0.1:8000/api/products/int:pk)
- **Product Ratings:** [Product Ratings](http://127.0.0.1:8000/api/products/int:product_id/ratings/)

### Comments and Reviews

- **Comment List:** [Comments](http://127.0.0.1:8000/api/comments/)
- **Review List:** [Reviews](http://127.0.0.1:8000/api/reviews/)

### User Operations

- **User Registration:** [Register](http://127.0.0.1:8000/api/v1/register/)
- **DRF Authentication:** [Authentication](http://127.0.0.1:8000/api/v1/drf-auth/)

## API Documentation

The API documentation, including the OpenAPI schema, is available at [API Docs](http://127.0.0.1:8000/api/docs/). Utilize this documentation to explore and understand the available endpoints, request methods, and data formats.

## Additional Information

- **Django Admin Panel:** Access the Django admin panel at [Admin Panel](http://127.0.0.1:8000/admin/) to manage database
