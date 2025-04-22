import { showCartItems } from './cart.js';

const orderItemsBlock = document.querySelector('.order-items');
const orderPrice = document.querySelector('.order-price');

window.addEventListener('DOMContentLoaded', () => {
    const cartItems = JSON.parse(sessionStorage.getItem('cart'));
    showCartItems(cartItems, orderItemsBlock, orderPrice);
});