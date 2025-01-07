

# Django Blog API

This project is a simple Django-based blog API that allows users to perform CRUD operations on blog posts and manage user-specific posts.

## Features

- **Homepage View**: Renders the homepage of the blog.
- **List and Create Posts**: View all posts or create a new one.
- **Retrieve, Update, Delete Posts**: Perform operations on individual posts using their unique IDs.
- **User-Specific Posts**: Retrieve posts for the current authenticated user.
- **Author-Specific Posts**: Fetch posts created by a specific author.

## API Endpoints

### General Endpoints

1. **Homepage**
   - **URL**: `/homepage/`
   - **View**: `views.homepage`
   - **Description**: Displays the homepage of the blog.

2. **List and Create Posts**
   - **URL**: `/`
   - **View**: `views.PostListCreateView`
   - **Description**: 
     - `GET`: List all posts.
     - `POST`: Create a new blog post.

3. **Post Details (Retrieve, Update, Delete)**
   - **URL**: `/<int:pk>/`
   - **View**: `views.PostRetrieveUpdateDeleteView`
   - **Description**:
     - `GET`: Retrieve details of a post by its ID.
     - `PUT`: Update a post by its ID.
     - `DELETE`: Delete a post by its ID.

### User-Specific Endpoints

4. **Posts for Current User**
   - **URL**: `/current_user/`
   - **View**: `views.get_posts_for_current_user`
   - **Description**: Fetch all posts for the currently authenticated user.

5. **Author-Specific Posts**
   - **URL**: `/posts_for/`
   - **View**: `views.ListPostsForAuthor`
   - **Description**: Retrieve all posts created by a specific author.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install Dependencies**:
   Make sure you have Python and pip installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the API**:
   Open your browser or API client (like Postman) and navigate to:
   - `http://127.0.0.1:8000/homepage/` for the homepage.
   - `http://127.0.0.1:8000/` for listing or creating posts.
   - Other routes as described in the API endpoints.

## File Structure

- **`views.py`**: Contains the logic for handling API requests.
- **`urls.py`**: Defines the routing for API endpoints.
- **`models.py`**: (if applicable) Contains the database schema for posts and users.
- **`serializers.py`**: (if applicable) Serializes the data for API communication.

## Future Improvements

- Add authentication and permissions for enhanced security.
- Implement pagination for the list views.
- Include comprehensive tests for all views and endpoints.

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

