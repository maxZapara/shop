const cartBtn=document.querySelector('.cart-btn');
const cart=document.querySelector('.cart');
const cartItemsBlock = document.querySelector('.cart-items');
const totalprice=document.querySelector('.total-price');

// document.addEventListener('DOMContentLoaded', () => {
//     const cartItems=JSON.parse(sessionStorage.getItem('cart'));
//     cartBtn.innerText=`${Object.keys(cartItems).length}`;
// });

window.addEventListener('pageshow', () => {
    console.log('Pageshow');
    if (!sessionStorage.getItem("already_loaded")) {
        const response=fetchCartItems();
        response
            .then(res => res.json())
            .then(data => {
                const cart_info = data.cart;
                sessionStorage.setItem('cart', JSON.stringify(cart_info));
                showCartItems(cart_info, cartItemsBlock, totalprice);

            })
            .catch(err => {
                console.log("Error get cart item:", err)
            })
        
        sessionStorage.setItem("already_loaded", true);
    } else {
        const cartItems = JSON.parse(sessionStorage.getItem('cart'));
        cartBtn.innerText = `${Object.keys(cartItems).length}`;
    }
})

cartBtn.addEventListener('click', showCart)

function showCart() {
    // cart.classList.toggle('active');
    if (cart.classList.contains('active')) {
        cart.classList.remove('active');
    } else {
        cartItems=JSON.parse(sessionStorage.getItem('cart'));
        showCartItems(cartItems, cartItemsBlock, totalprice);
        cart.classList.add('active');
    }
}

function showCartItems(cartItems, blockToShow, priceToShow) {
    cartBtn.innerText=`${Object.keys(cartItems).length}`
    blockToShow.innerHTML='';
    let price=0;

    for (const [key, value] of Object.entries(cartItems)) {
        const html = `
            <div class="cart-item">
                <img src="${value.image}" alt>
                <div class="cart-item-details">
                    <h3>${value.title}</h3>
                    <div class="cart-item-details-quantity">
                        <p>Price: ${value.price} $</p>
                        <div>
                            <input class="quantity-input" type="number" min="1" value="${value.quantity}" onchange='changeProductQuantity(${key}, this.value)'>
                            <button onclick="removeCartItem(${key})" class="remove-cart" style="background:red; font-size:16px; padding:8px">Remove</button>
                        </div>
                    </div>
                </div>
            </div>
        `;

        blockToShow.innerHTML += html;
        price+=value.price * value.quantity;
    }
    priceToShow.innerText=price;

}

function changeProductQuantity(productId, quantity) {
    console.log('change:', productId, quantity)
    const cartItems=JSON.parse(sessionStorage.getItem('cart'))
    const product=cartItems[productId]
    const quantityNew=quantity-product.quantity
    console.log("P I:", productId, "qu:", quantityNew);
    addToCart(productId, quantityNew)
}

function addToCart(productId, quantity=1) {
    console.log('add:', productId)
    const url="http://127.0.0.1:8000/cart"
    fetch(url,{
        method:"POST",
        credentials:'include',
        body: JSON.stringify({product_id:productId, quantity:quantity})
    })
        .then(res => res.json())
        .then(data => {
            // console.log(data)
            const cartItems = data.cart;
            sessionStorage.setItem('cart', JSON.stringify(cartItems));
            showCartItems(cartItems, cartItemsBlock, totalprice);
        })
        .catch(err => {
            console.log("Error remove cart item:", err)
        })
}


function removeCartItem(productId, ) {
    // console.log('remove:',productId)
    const url="http://127.0.0.1:8000/cart"
    fetch(url,{
        method:"DELETE",
        credentials:'include',
        body: JSON.stringify({product_id:productId})
    })
        .then(res => res.json())
        .then(data => {
            // console.log(data)
            const cart_info = data.cart;
            sessionStorage.setItem('cart', JSON.stringify(cart_info));
            showCartItems(cart_info, cartItemsBlock, totalprice);

        })
        .catch(err => {
            console.log("Error remove cart item:", err)
        })
}

function fetchCartItems(){
    const url="http://127.0.0.1:8000/cart"
    return fetch(url,{
        method:"GET",
        credentials:'include',
    })
        // .then(res => res.json())
        // .then(data => {
        //     const cart_info = data.cart;
        //     sessionStorage.setItem('cart', JSON.stringify(cart_info));
        //     showCartItems(cart_info, cartItemsBlock, totalprice);

        // })
        // .catch(err => {
        //     console.log("Error get cart item:", err)
        // })
}


