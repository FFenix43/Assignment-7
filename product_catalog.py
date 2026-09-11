from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []
response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    product_tags = set(product['tags'])
    converted_products.append((product, product_tags))



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    matching_tags = len(product_tags.intersection(customer_tags))
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return matching_tags



# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    for products, product_tags in converted_products:
        matches = count_matches(product_tags, customer_tags)

        if matches > 0:
            recommendations.append((matches, products['name']))

    # sort recommendations by highest match
    recommendations.sort(reverse=True, key=lambda x: x[0])

    #format output one per line 
    output = [f"{name}  {matches} matching tags" for matches, name in recommendations]
    return "\n".join(output)
    

# TODO: Step 7 - Call your function and print the results
results = recommend_products(converted_products, customer_tags)
print("Recommended products based on your preferences:")
print(results if results else "No matching products found.")

# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?

#1. I used the set & intersection to find matching tags between the customer preferences
# and remove the duplicates. I also used loops like "for" or "while" to iterate through sets
#and collect variables from the user. And finally I used sorting & List to order from relevant
# to least relevant.


# 2. This code is going to change with a bigger dataset like 1000+ products because
#is going to need some SQL queries for a more efficient way to handle the data.