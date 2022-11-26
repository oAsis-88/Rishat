console.log("Sanity check!");

fetch("/config/").then((result) => {
        return result.json();
    })
        .then((data) => {
            var stripe = Stripe(data.publicKey);
            var buyButton = document.getElementById('buy-button');
            buyButton.addEventListener('click', function () {
                // Create a new Checkout Session using the server-side endpoint
                // Redirect to Stripe Session Checkout
                fetch('/buy/' + buyButton.value, {method: 'GET'})
                    .then((response) => {
                        return response.json()
                    })
                    .then(session => stripe.redirectToCheckout({sessionId: session.id}))
            });

        });