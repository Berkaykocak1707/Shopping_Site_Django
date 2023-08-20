## ShoppingSite (Django)

### Overview

ShoppingSite is a Django-based e-commerce platform that offers users the ability to browse products, view product details, and manage their shopping carts. The platform provides an intuitive user interface, allowing for efficient navigation and a seamless shopping experience.

### Key Features

1. **Product Browsing**: 
    - View all available products, with priority given to products currently on sale.
    - Products are categorized, facilitating easier navigation and discovery.

2. **Product Details**:
    - Access detailed information about a specific product.
    - View related products based on product categorization.

3. **Shopping Cart Management**:
    - Add products to the shopping cart.
    - Update product quantities within the cart.
    - Remove products from the cart.
    - Ensure inactive products are flagged and prevented from being added to the cart.

### Installation

1. Clone this repo to your local machine.
2. Create and activate a virtual environment in the directory where the project is located.
3. Run the command `pip install -r requirements.txt` to install the dependencies listed in the `requirements.txt` file.
4. Adjust your email settings in the `settings.py` file.
5. Adjust the email sending functions in the `views.py` file.
6. Run the command `python manage.py migrate` to create the database.
7. Start the server with the command `python manage.py runserver`.

### Contribution

If you wish to contribute to the development of ShoppingSite, please submit a pull request or open an issue for discussion.
