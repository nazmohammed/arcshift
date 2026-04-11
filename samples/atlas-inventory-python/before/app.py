"""
Legacy Flask application for Atlas Inventory.
Demonstrates: synchronous routes, manual JSON, no type hints, basic auth.
"""
from flask import Flask, request, jsonify
from models import db, Product, InventoryTransaction

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:pass@localhost/atlas"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

API_KEY = "hardcoded-api-key-123"  # Legacy: hardcoded secret


def require_api_key(f):
    """Legacy decorator for API key authentication."""
    from functools import wraps

    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get("X-API-Key")
        if key != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)

    return decorated


@app.route("/api/products", methods=["GET"])
@require_api_key
def get_products():
    products = Product.query.all()
    return jsonify(
        [
            {
                "id": p.id,
                "name": p.name,
                "sku": p.sku,
                "stock_quantity": p.stock_quantity,
                "category": p.category,
            }
            for p in products
        ]
    )


@app.route("/api/products/<int:product_id>", methods=["GET"])
@require_api_key
def get_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(
        {
            "id": product.id,
            "name": product.name,
            "sku": product.sku,
            "stock_quantity": product.stock_quantity,
            "category": product.category,
        }
    )


@app.route("/api/inventory/adjust", methods=["POST"])
@require_api_key
def adjust_inventory():
    data = request.get_json()
    if not data or "product_id" not in data or "quantity_change" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    product = Product.query.get(data["product_id"])
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    product.stock_quantity += data["quantity_change"]

    transaction = InventoryTransaction(
        product_id=product.id,
        quantity_change=data["quantity_change"],
        reason=data.get("reason", "Manual adjustment"),
    )
    db.session.add(transaction)
    db.session.commit()

    return jsonify({"product_id": product.id, "new_stock": product.stock_quantity})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
