console.log("Sanity check!");

fetch("/config/")
    .then((result) => {
        return result.json();
    })
    .then((data) => {
        // Initialize Stripe.js
        const stripe = Stripe(data.publicKey);

        // Event handler
        document.querySelector("#buy-button").addEventListener("click", () => {
            // Get Checkout Session ID
            fetch("/create-checkout-session/")
                .then((result) => {
                    return result.json();
                })
                .then((data) => {
                    console.log("it's data -", data);
                    // Redirect to Stripe Checkout
                    return stripe.redirectToCheckout({
                        sessionId: data.id
                    })
                })
                .then((res) => {
                    console.log("-----  res  -----");
                    console.log(res);
                });
        });
    });