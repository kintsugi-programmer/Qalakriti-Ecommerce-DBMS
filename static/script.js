function incrementQuantity() {
    var quantityInput = document.querySelector('.quantity-input');
    var currentValue = parseInt(quantityInput.value);
    if (!isNaN(currentValue)) {
        quantityInput.value = currentValue + 1;
    } else {
        quantityInput.value = 1;
    }
}

function decrementQuantity() {
    var quantityInput = document.querySelector('.quantity-input');
    var currentValue = parseInt(quantityInput.value);
    if (!isNaN(currentValue) && currentValue > 0) {
        quantityInput.value = currentValue - 1;
    } else {
        quantityInput.value = 0;
    }
}

function goBack() {
    window.location.href = "prod";
}
