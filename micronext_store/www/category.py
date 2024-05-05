
import frappe
from frappe import _

def get_context(context):
    # Querying upcoming products (assuming you have a field named 'release_date' in your Item doctype)
    shoe_brands = frappe.db.sql("""
        SELECT name, image ,description
        FROM `tabBrand` 
        WHERE creation > CURDATE() 
        ORDER BY creation ASC 
    """, as_dict=True)
    context.shoe_brands = shoe_brands


# Define the server-side endpoint to handle the AJAX request for filtered products
@frappe.whitelist(allow_guest=True)
def get_filtered_products(brand=None):
    # Define your filter logic here based on the selected brand and other filters
    # For example, you can query the products from the database based on the selected brand

    # Sample query to fetch products based on the selected brand
    products = frappe.get_all("Item", filters={"brand": brand}, fields=["name", "item_name", "image", "price"])

    # Generate HTML content for each filtered product
    product_html = ""
    for product in products:
        product_html += """
        <div class="col-lg-4 col-md-6">
            <div class="single-product">
                <img class="img-fluid" src="{image}" alt="">
                <div class="product-details">
                    <h6>{item_name}</h6>
                    <div class="price">
                        <h6>{price}</h6>
                    </div>
                    <div class="prd-bottom">
                        <a href="#" class="social-info">
                            <span class="ti-bag"></span>
                            <p class="hover-text">add to bag</p>
                        </a>
                        <a href="#" class="social-info">
                            <span class="lnr lnr-heart"></span>
                            <p class="hover-text">Wishlist</p>
                        </a>
                        <a href="#" class="social-info">
                            <span class="lnr lnr-sync"></span>
                            <p class="hover-text">compare</p>
                        </a>
                        <a href="#" class="social-info">
                            <span class="lnr lnr-move"></span>
                            <p class="hover-text">view more</p>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        """.format(
            image=product.get("image", ""),
            item_name=product.get("item_name", ""),
            price=product.get("price", "")
        )

    return product_html