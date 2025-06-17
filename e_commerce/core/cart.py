class Cart:
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get('cart', {})
        if not cart:
            cart=self.session["cart"]={}
        self.cart=cart

    def add(self, product, quantity=1):
        product_id=str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["quantity"]+=quantity
        else:
            self.cart[product_id]={
                "title":product.title,
                "price":product.price,
                "quantity":quantity,
                "image": product.get_first_image(),
            }
        self.save()

    def save(self):
        self.session.modified=True


    def get_cart(self):
        return self.cart
    
    def remove(self, product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session["cart"]
        del self.cart
        self.save()
        